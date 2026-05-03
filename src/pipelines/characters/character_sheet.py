from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import replicate
import requests
from replicate.exceptions import ReplicateError

from src.config import ASSETS_DIR, GENERATED_DIR, load_environment


MODEL = "google/nano-banana"
CHARACTER_SLUG = "ethan-vale"
OUTPUT_DIR = GENERATED_DIR / "characters" / "character_sheets" / CHARACTER_SLUG / "00"
REFERENCE_DIR = OUTPUT_DIR
REQUEST_DELAY_SECONDS = 11
MAX_THROTTLE_RETRIES = 3

REFERENCE_IMAGES = (
    "ethan-vale-reference-01.png",
    "ethan-vale-reference-02.png",
    "ethan-vale-reference-03.png",
    "ethan-vale-reference-04.png",
)

BASE_CHARACTER_DIRECTION = (
    "same character and identity as the reference images, Ethan Vale, clean-cut expensive look, "
    "youthful softness, polished old-money grooming, realistic law firm wardrobe, natural skin texture, "
    "realistic fabric, ordinary studio lighting, less glossy, unretouched, no comic-book styling"
)


@dataclass(frozen=True)
class SheetVariant:
    slug: str
    prompt: str


SHEET_VARIANTS = (
    SheetVariant(
        slug="technical-turnaround",
        prompt=(
            "Create a professional character reference sheet based strictly on the uploaded reference images. "
            "Use a clean neutral plain background and present it as a technical model turnaround while matching "
            "the realistic visual style of the references. Arrange the composition into two horizontal rows. "
            "Top row: four full-body standing views, front, left profile, right profile, and back. Bottom row: "
            "three close-up portraits, front, left profile, and right profile. Maintain the same identity across "
            "every panel. Keep relaxed A-pose body language, consistent scale and alignment, accurate anatomy, "
            "clear silhouette, and consistent ordinary lighting. Crisp realistic reference sheet, no text labels."
        ),
    ),
    SheetVariant(
        slug="portrait-turnaround",
        prompt=(
            "Create a clean character portrait turnaround sheet using the reference images as the strict identity anchor. "
            "Show seven panels on a plain neutral background: front portrait, left profile portrait, right profile portrait, "
            "three-quarter portrait, neutral expression, worried expression, and angry close-up. Keep the same suit, "
            "hair, youthful softness, old-money grooming, natural skin texture, and ordinary lighting. No text labels."
        ),
    ),
    SheetVariant(
        slug="production-reference",
        prompt=(
            "Create a film production reference sheet based strictly on the same character identity. Include a full-body "
            "front standing view, full-body side view, upper-body portrait, close-up face detail, realistic suit fabric detail, "
            "and phone prop pose. Clean neutral background, consistent scale, ordinary lighting, realistic fabric and skin, "
            "no text labels."
        ),
    ),
    SheetVariant(
        slug="story-use",
        prompt=(
            "Create a practical story-use character sheet from the same identity: neutral studio portrait, seated at a "
            "conference table, standing in a law firm hallway, shocked while holding a phone, and tense close-up. Preserve "
            "the same face, hair, grooming, youthful softness, and clean-cut expensive look across every panel. Use ordinary "
            "realistic lighting and no text labels."
        ),
    ),
)


def resolve_asset_inputs(relative_paths: tuple[str, ...]) -> list[Path]:
    paths = []
    assets_root = ASSETS_DIR.resolve()

    for relative_path in relative_paths:
        path = resolve_asset_input(relative_path)
        if path != assets_root and assets_root not in path.parents:
            raise ValueError(f"Input image must stay inside assets: {relative_path}")
        if path.exists():
            paths.append(path)
        else:
            print(f"Skipping missing reference image: assets/{relative_path}")

    return paths


def resolve_asset_input(relative_path: str) -> Path:
    reference_path = (REFERENCE_DIR / relative_path).resolve()
    if reference_path.exists():
        return reference_path

    path = (ASSETS_DIR / relative_path).resolve()
    if path.exists():
        return path

    matches = sorted(ASSETS_DIR.rglob(relative_path))
    if matches:
        return matches[0].resolve()

    return path


def build_prompt(variant: SheetVariant) -> str:
    return f"{BASE_CHARACTER_DIRECTION}. {variant.prompt}"


def run_character_sheet() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    reference_images = resolve_asset_inputs(REFERENCE_IMAGES)

    if not reference_images:
        raise FileNotFoundError("No character sheet reference images found under assets")

    print(f"Using {len(reference_images)} reference image(s) as image_input from {REFERENCE_DIR.relative_to(ASSETS_DIR.parent)}.")

    for index, variant in enumerate(SHEET_VARIANTS, start=1):
        stem = f"{CHARACTER_SLUG}-sheet-{index:02d}"
        expected_output = OUTPUT_DIR / f"{stem}.jpg"
        if expected_output.exists():
            print(f"Skipping existing {expected_output.relative_to(ASSETS_DIR.parent)}")
            continue

        if index > 1:
            time.sleep(REQUEST_DELAY_SECONDS)

        output = run_prediction(build_prompt(variant), reference_images)
        save_outputs(output, OUTPUT_DIR, stem)


def run_prediction(prompt: str, reference_images: list[Path]) -> Any:
    for attempt in range(1, MAX_THROTTLE_RETRIES + 1):
        model_input = build_model_input(prompt, reference_images)
        try:
            return replicate.run(MODEL, input=model_input)
        except ReplicateError as error:
            if getattr(error, "status", None) != 429 or attempt == MAX_THROTTLE_RETRIES:
                raise
            print(f"Replicate throttled request; waiting {REQUEST_DELAY_SECONDS}s before retry {attempt + 1}.")
            time.sleep(REQUEST_DELAY_SECONDS)
        finally:
            close_model_input_files(model_input)

    raise RuntimeError("Prediction retry loop exited unexpectedly")


def build_model_input(prompt: str, reference_images: list[Path]) -> dict[str, Any]:
    return {
        "prompt": prompt,
        "image_input": [path.open("rb") for path in reference_images],
        "aspect_ratio": "16:9",
        "output_format": "jpg",
    }


def close_model_input_files(model_input: dict[str, Any]) -> None:
    for value in model_input.values():
        close_value(value)


def close_value(value: Any) -> None:
    if isinstance(value, list):
        for item in value:
            close_value(item)
        return

    close = getattr(value, "close", None)
    if close is not None:
        close()


def save_outputs(output: Any, output_dir: Path, stem: str) -> None:
    if not isinstance(output, list):
        output = [output]

    for index, item in enumerate(output, start=1):
        suffix = "" if len(output) == 1 else f"-{index:02d}"
        destination = output_dir / f"{stem}{suffix}.jpg"
        save_output_item(item, destination)
        print(f"Saved {destination.relative_to(ASSETS_DIR.parent)}")


def save_output_item(item: Any, destination: Path) -> None:
    if hasattr(item, "read"):
        data = item.read()
        if isinstance(data, str):
            data = data.encode()
        destination.write_bytes(data)
        return

    value = str(item)
    parsed = urlparse(value)
    if parsed.scheme in {"http", "https"}:
        response = requests.get(value, timeout=120)
        response.raise_for_status()
        destination.write_bytes(response.content)
        return

    source = Path(value)
    if source.exists():
        destination.write_bytes(source.read_bytes())
        return

    raise ValueError(f"Unsupported output from Replicate: {item!r}")


def main() -> None:
    load_environment()
    run_character_sheet()


if __name__ == "__main__":
    main()
