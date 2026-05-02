from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import replicate
import requests

from src.config import ASSETS_DIR, GENERATED_DIR, load_environment


MODEL = "black-forest-labs/flux-schnell"
OUTPUT_DIR = GENERATED_DIR / "characters" / "cheap_concepts" / "ethan" / "00"

BASE_STYLE_PROMPT = (
    "cinematic corporate thriller, prestige television drama, cold glass law office, "
    "muted navy and charcoal color palette, realistic lighting, shallow depth of field, "
    "vertical 9:16, tense restrained performance, expensive corporate-noir atmosphere"
)

NEGATIVE_PROMPT = (
    "cartoon, illustration, anime, fantasy, sci-fi, courtroom, crowded scene, bright sitcom lighting, "
    "text, watermark, logo, deformed hands, distorted face"
)


@dataclass(frozen=True)
class CharacterConcept:
    slug: str
    name: str
    description: str
    variants: tuple[str, ...]
    optional_input_images: tuple[str, ...] = ()


ETHAN = CharacterConcept(
    slug="ethan-vale",
    name="Ethan Vale",
    description=(
        "younger son and junior employee at his father's law firm, polished but vulnerable, "
        "expressive face, tailored office clothes that are slightly less sharp than senior partners"
    ),
    variants=(
        "boyish and underestimated, anxious ambition, trying to look older than he is",
        "sharp and privileged but emotionally exposed, polished heir under sudden pressure",
        "quietly intense and wounded, intelligent eyes, restrained panic beneath a professional exterior",
        "clean-cut rising associate, expensive but slightly imperfect suit, desperate for approval",
    ),
)


def build_prompt(character: CharacterConcept, variant: str) -> str:
    return f"portrait concept of {character.name}, {character.description}, {variant}, {BASE_STYLE_PROMPT}"


def resolve_asset_inputs(relative_paths: tuple[str, ...]) -> list[Path]:
    paths = []
    assets_root = ASSETS_DIR.resolve()

    for relative_path in relative_paths:
        path = (ASSETS_DIR / relative_path).resolve()
        if path != assets_root and assets_root not in path.parents:
            raise ValueError(f"Input image must stay inside assets: {relative_path}")
        if path.exists():
            paths.append(path)
        else:
            print(f"Skipping missing input image: assets/{relative_path}")

    return paths


def run_character(character: CharacterConcept) -> None:
    character_dir = OUTPUT_DIR / character.slug
    character_dir.mkdir(parents=True, exist_ok=True)

    input_images = resolve_asset_inputs(character.optional_input_images)
    if input_images:
        print(f"Resolved {len(input_images)} input images for {character.name}; {MODEL} may ignore them.")

    for index, variant in enumerate(character.variants, start=1):
        output = replicate.run(
            MODEL,
            input={
                "prompt": build_prompt(character, variant),
                "negative_prompt": NEGATIVE_PROMPT,
                "aspect_ratio": "9:16",
                "output_format": "png",
                "num_outputs": 1,
            },
        )
        save_outputs(output, character_dir, f"{character.slug}-{index:02d}")


def save_outputs(output: Any, output_dir: Path, stem: str) -> None:
    if not isinstance(output, list):
        output = [output]

    for index, item in enumerate(output, start=1):
        destination = output_dir / f"{stem}-{index}.png"
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
        shutil.copyfile(source, destination)
        return

    raise ValueError(f"Unsupported output from Replicate: {item!r}")


def main() -> None:
    load_environment()
    run_character(ETHAN)


if __name__ == "__main__":
    main()
