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


OUTPUT_DIR = GENERATED_DIR / "characters" / "cheap_concepts"
REQUEST_DELAY_SECONDS = 11
MAX_THROTTLE_RETRIES = 3
RUN_STAGE_INDEX: int | None = None

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
class VariantStage:
    model: str
    variants: tuple[str, ...]
    reference_images: tuple[str, ...] = ()
    reference_input_name: str = "input_image"
    reference_input_many: bool = False
    include_negative_prompt: bool = True
    include_num_outputs: bool = True
    aspect_ratio: str = "9:16"
    output_format: str | None = "png"
    model_inputs: dict[str, Any] | None = None


@dataclass(frozen=True)
class CharacterConcept:
    slug: str
    name: str
    description: str
    variant_stages: tuple[VariantStage, ...]
    optional_input_images: tuple[str, ...] = ()


ETHAN = CharacterConcept(
    slug="ethan-vale",
    name="Ethan Vale",
    description=(
        "younger son and junior employee at his father's law firm, polished but vulnerable, "
        "expressive face, tailored office clothes that are slightly less sharp than senior partners"
    ),
    variant_stages=(
        VariantStage(
            model="black-forest-labs/flux-schnell",
            variants=(
                "boyish and underestimated, anxious ambition, trying to look older than he is",
                "sharp and privileged but emotionally exposed, polished heir under sudden pressure",
                "quietly intense and wounded, intelligent eyes, restrained panic beneath a professional exterior",
                "clean-cut rising associate, expensive but slightly imperfect suit, desperate for approval",
            ),
        ),
        VariantStage(
            model="black-forest-labs/flux-schnell",
            variants=(
                "boyish face with privileged polish, expensive suit worn slightly too carefully, anxious heir trying to project authority",
                "sharp young associate with vulnerable eyes, old-money grooming, emotionally exposed beneath a controlled professional mask",
                "underestimated golden son, clean-cut and expensive, youthful softness contrasted with a tense corporate posture",
                "privileged but not yet hardened, polished law firm heir with boyish uncertainty and a defensive ambitious stare",
            ),
        ),
        VariantStage(
            model="black-forest-labs/flux-schnell",
            variants=(
                "underestimated golden son, clean-cut old-money polish, soft youthful face, tense shoulders, trying to look composed in an expensive law office",
                "expensive young heir with gentle features, immaculate suit, nervous corporate posture, privilege undercut by visible uncertainty",
                "clean-cut law firm son with youthful softness, polished grooming, tense restrained body language, underestimated but quietly intelligent",
                "privileged golden boy associate, soft face and expensive tailoring, anxious ambition beneath a controlled corporate stance",
            ),
        ),
        VariantStage(
            model="black-forest-labs/flux-kontext-dev",
            reference_images=(
                "ethan-vale-reference-01.png",
                "ethan-vale-reference-02.png",
            ),
            include_negative_prompt=False,
            include_num_outputs=False,
            variants=(
                "use the reference images as visual direction for face, grooming, wardrobe polish, and realism; create an original underestimated golden son with clean-cut old-money polish, soft youthful face, tense shoulders, and a composed law office presence",
                "use the reference images as visual direction without copying either person exactly; make Ethan an expensive young heir with gentle features, immaculate suit, nervous corporate posture, and realistic natural skin detail",
                "blend the reference image direction into an original clean-cut law firm son with youthful softness, polished grooming, restrained body language, quiet intelligence, and cinematic realism",
                "use the reference images to guide realism, facial believability, hair, and wardrobe; create a privileged golden boy associate with soft features, expensive tailoring, and anxious ambition under a controlled corporate stance",
            ),
        ),
        VariantStage(
            model="bytedance/seedream-4",
            reference_images=("ethan-vale-reference-01.png","ethan-vale-reference-02.png",),
            reference_input_name="image_input",
            reference_input_many=True,
            include_negative_prompt=False,
            include_num_outputs=False,
            aspect_ratio="match_input_image",
            output_format=None,
            model_inputs={
                "size": "2K",
                "max_images": 1,
                "enhance_prompt": True,
                "sequential_image_generation": "disabled",
            },
            variants=(
                "edit the reference portrait into a more realistic live-action character portrait while preserving Ethan's identity, clean-cut expensive look, youthful softness, restrained corporate tension, natural skin texture, and believable law office lighting",
                "make the reference portrait feel like a real photographed person, reducing any stylized or cartoon-like qualities while keeping the same character, wardrobe polish, facial direction, and tense old-money law firm mood",
                "refine the reference portrait toward a polished Ivy League law associate: understated old-money grooming, precise tailoring, realistic facial details, soft youthful features, and controlled corporate posture",
                "keep the same character from the reference image but make him slightly more naive and emotionally readable, with naturalistic skin, gentle features, expensive grooming, and subtle anxious ambition",
            ),
        ),
        VariantStage(
            model="bytedance/seedream-4.5",
            reference_images=("ethan-vale-reference-01.png",),
            reference_input_name="image_input",
            reference_input_many=True,
            include_negative_prompt=False,
            include_num_outputs=False,
            aspect_ratio="match_input_image",
            output_format=None,
            model_inputs={
                "size": "2K",
                "max_images": 1,
                "sequential_image_generation": "disabled",
            },
            variants=(
                "same identity as the reference image, keep the clean-cut expensive look and youthful softness; make it less glossy and less comic-book-like, with unretouched natural skin texture, realistic suit fabric, ordinary office lighting, and a believable photographed finish",
                "same identity and overall character direction as the reference image, preserve the soft youthful features and polished old-money grooming; reduce AI gloss, avoid a perfect face or flawless skin, use realistic fabric, normal indoor lighting, and subtle natural imperfections",
            ),
        ),
        VariantStage(
            model="bytedance/seedream-4.5",
            reference_images=("ethan-vale-reference-01.png","ethan-vale-reference-02.png",),
            reference_input_name="image_input",
            reference_input_many=True,
            include_negative_prompt=False,
            include_num_outputs=False,
            aspect_ratio="match_input_image",
            output_format=None,
            model_inputs={
                "size": "2K",
                "max_images": 1,
                "sequential_image_generation": "disabled",
            },
            variants=(
                "same character and identity as the reference image, natural neutral studio portrait, ordinary soft studio light, realistic skin texture, realistic suit fabric, clean-cut expensive look, youthful softness, less glossy and unretouched",
                "same character and identity as the reference image, seated at a conference table in a law firm, ordinary office lighting, realistic fabric and natural skin texture, clean-cut expensive look, youthful softness, less AI gloss",
                "same character and identity as the reference image, standing in a law firm hallway, natural indoor light, realistic suit fabric, unretouched skin texture, clean-cut old-money grooming, youthful softness, believable photographed look",
                "same character and identity as the reference image, looking shocked while holding a phone, realistic office lighting, natural skin texture, clean-cut expensive look, youthful softness, believable expression without comic-book drama",
                "same character and identity as the reference image, angry close-up portrait, vertical 9:16, natural skin texture, realistic fabric, ordinary lighting, clean-cut expensive look, youthful softness preserved, less glossy and less stylized",
            ),
        ),
    ),
)

MARCUS = CharacterConcept(
    slug="marcus-vale",
    name="Marcus Vale",
    description=(
        "older brother and senior law firm presence, composed and strategic, colder and sharper than Ethan, "
        "severe expensive suit, controlled posture, always watching from the edge of the room"
    ),
    variant_stages=(
        VariantStage(
            model="black-forest-labs/flux-schnell",
            variants=(
                "mid-to-late thirties older brother, dark hair, severe old-money polish, precise grooming, controlled expression, looks like he has already won without looking fifty or father-like",
                "dark-haired senior associate in his late thirties, sharp and composed, expensive dark suit, restrained ambition, strategic eyes, polished law firm posture",
                "mid-thirties resentful heir with dark hair and a severe tailored suit, calm surface with quiet hostility underneath, youthful enough to be Ethan's older brother not his father",
                "dark-haired older brother in his late thirties watching from the edge of a glass law office, immaculate wardrobe, colder posture than Ethan, patient calculating expression",
            ),
        ),
        VariantStage(
            model="black-forest-labs/flux-schnell",
            variants=(
                "mid-thirties resentful heir with dark hair and a severe tailored suit, calm surface with quiet hostility underneath, youthful enough to be Ethan's older brother not his father, slightly younger face",
                "mid-thirties resentful heir with dark hair and a severe expensive tailored suit, calm surface with quiet hostility underneath, youthful enough to be Ethan's older brother not his father",
                "mid-thirties resentful heir with dark hair and a severe tailored suit, calm surface with quiet hostility underneath, darker corporate mood, youthful enough to be Ethan's older brother not his father",
                "mid-thirties resentful heir with dark hair and a severe tailored suit, calm surface with very subtle hostility underneath, youthful enough to be Ethan's older brother not his father",
            ),
        ),
        VariantStage(
            model="black-forest-labs/flux-schnell",
            variants=(
                "mid-thirties resentful heir with dark hair and a severe expensive tailored suit, calm surface with quiet hostility underneath, youthful enough to be Ethan's older brother not his father, natural realistic face",
                "mid-thirties resentful heir with dark hair and a severe expensive tailored charcoal suit, calm surface with quiet hostility underneath, polished law firm presence, youthful enough to be Ethan's older brother not his father",
                "late-thirties resentful heir with dark hair and a severe expensive tailored suit, calm surface with quiet hostility underneath, sharp older brother energy without looking father-like",
                "mid-thirties resentful heir with dark hair and a severe expensive tailored suit, controlled posture, calm surface with quiet hostility underneath, precise but not overly villainous",
            ),
        ),
        VariantStage(
            model="black-forest-labs/flux-kontext-dev",
            reference_images=("marcus-vale-reference-01.png",),
            include_negative_prompt=False,
            include_num_outputs=False,
            variants=(
                "use the reference image as visual direction for Marcus Vale's identity, dark hair, severe expensive tailored suit, calm surface with quiet hostility underneath, mid-to-late thirties, realistic law firm heir, not father-like",
                "preserve the reference image's face direction and dark-haired older-brother energy; refine Marcus into a severe mid-thirties resentful heir with expensive tailoring, controlled posture, and subtle hostility beneath a calm polished surface",
                "use the reference image to guide facial believability, grooming, and wardrobe; create Marcus as a sharp dark-haired law firm heir in his late thirties, severe suit, quiet resentment, realistic natural skin texture",
                "keep the reference image's identity direction while making Marcus colder and more strategic than Ethan, dark hair, severe tailored suit, calm expression, quiet hostility, realistic corporate-noir portrait",
            ),
        ),
        VariantStage(
            model="bytedance/seedream-4.5",
            reference_images=("marcus-vale-reference-01.png",),
            reference_input_name="image_input",
            reference_input_many=True,
            include_negative_prompt=False,
            include_num_outputs=False,
            aspect_ratio="match_input_image",
            output_format=None,
            model_inputs={
                "size": "2K",
                "max_images": 1,
                "sequential_image_generation": "disabled",
            },
            variants=(
                "same identity as the reference image, keep Marcus as a dark-haired mid-to-late-thirties resentful heir in a severe expensive tailored suit; make it less glossy and less stylized, with unretouched natural skin texture, realistic suit fabric, ordinary office lighting, and a believable photographed finish",
                "same identity and overall character direction as the reference image, preserve the calm surface with quiet hostility underneath, dark hair, severe tailoring, and older-brother age; reduce AI gloss, avoid a perfect face or flawless skin, use realistic fabric, normal indoor lighting, and subtle natural imperfections",
            ),
        ),
        VariantStage(
            model="bytedance/seedream-4.5",
            reference_images=("marcus-vale-reference-01.png",),
            reference_input_name="image_input",
            reference_input_many=True,
            include_negative_prompt=False,
            include_num_outputs=False,
            aspect_ratio="match_input_image",
            output_format=None,
            model_inputs={
                "size": "2K",
                "max_images": 1,
                "sequential_image_generation": "disabled",
            },
            variants=(
                "same character and identity as the reference image, natural neutral studio portrait, ordinary soft studio light, realistic skin texture, realistic suit fabric, dark hair, severe expensive tailored suit, calm controlled expression, less glossy and unretouched",
                "same character and identity as the reference image, seated at a conference table in a law firm, composed posture, hands still, dark hair, severe tailored suit, quiet hostility under a calm surface, ordinary office lighting, realistic fabric and skin",
                "same character and identity as the reference image, standing in a glass law firm hallway, dark hair, severe tailored suit, controlled older-brother posture, strategic watchful expression, natural indoor light, less glossy, believable photographed look",
                "same character and identity as the reference image, watching from the edge of a conference room doorway, dark hair, severe expensive suit, calm expression with quiet resentment underneath, realistic office lighting, natural skin texture",
                "same character and identity as the reference image, cold close-up portrait, vertical 9:16, dark hair, severe tailored suit collar visible, restrained anger behind a calm face, realistic fabric, ordinary lighting, less stylized",
            ),
        ),
    ),
)

RICHARD = CharacterConcept(
    slug="richard-vale",
    name="Richard Vale",
    description=(
        "father of Ethan and Marcus, founder and managing partner of Vale and Rowe, powerful and image-conscious, "
        "authoritative expensive presence, emotionally contained, conservative immaculate senior partner suit"
    ),
    variant_stages=(
        VariantStage(
            model="black-forest-labs/flux-schnell",
            variants=(
                "powerful law firm founder in his sixties, conservative immaculate senior partner suit, authoritative expensive presence, emotionally contained, treats family pain like a business decision",
                "wealthy managing partner and father, late sixties, silver hair, conservative dark suit, commanding posture, image-conscious and visibly burdened by the firm's crisis",
                "old-money law firm patriarch, polished silver-haired founder, immaculate senior partner wardrobe, clipped restrained expression, powerful but privately shaken",
                "authoritative father in an expensive law office, conservative suit, controlled face, visibly under pressure, chooses the family name and firm before emotion",
            ),
        ),
        VariantStage(
            model="black-forest-labs/flux-schnell",
            variants=(
                "powerful law firm founder in his sixties, conservative immaculate senior partner suit, authoritative expensive presence, emotionally contained, soap opera patriarch polish, older but not deeply wrinkled",
                "powerful law firm founder in his early sixties, smooth well-kept face for his age, conservative immaculate senior partner suit, controlled expression, expensive soap opera family patriarch energy",
                "wealthy senior partner and father in his sixties, silver hair, polished camera-ready face with fewer wrinkles, conservative dark suit, commanding presence, emotionally contained",
                "old-money law firm founder in his sixties, handsome aging patriarch, lightly lined face, immaculate senior partner suit, restrained expression, treats family pain like a business decision",
            ),
        ),
        VariantStage(
            model="black-forest-labs/flux-schnell",
            variants=(
                "wealthy senior partner and father in his sixties, silver hair, polished camera-ready face with fewer wrinkles, conservative dark suit, commanding presence, emotionally contained, soap opera patriarch realism",
                "wealthy senior partner and father in his sixties, silver hair, polished well-kept face, conservative dark senior partner suit, calm commanding presence, emotionally contained under pressure",
                "wealthy law firm founder and father in his sixties, silver hair, camera-ready face with light age lines, conservative immaculate dark suit, powerful contained presence, image-conscious patriarch",
                "wealthy senior partner and father, early sixties, silver hair, polished face without deep wrinkles, conservative dark suit, restrained expression, commanding but privately shaken",
            ),
        ),
        VariantStage(
            model="black-forest-labs/flux-kontext-dev",
            reference_images=("richard-vale-reference-01.png",),
            include_negative_prompt=False,
            include_num_outputs=False,
            variants=(
                "use the reference image as visual direction for Richard Vale's identity, silver hair, polished camera-ready face with fewer wrinkles, conservative dark senior partner suit, commanding presence, emotionally contained, realistic law firm founder",
                "preserve the reference image's face direction and wealthy patriarch energy; refine Richard into a powerful silver-haired law firm founder in his sixties, conservative immaculate suit, controlled expression, soap opera realism",
                "use the reference image to guide facial believability, grooming, and wardrobe; create Richard as an image-conscious senior partner and father, polished face with light age lines, conservative dark suit, calm authority under pressure",
                "keep the reference image's identity direction while making Richard authoritative and expensive, silver hair, conservative senior partner suit, emotionally restrained expression, realistic corporate-noir portrait",
            ),
        ),
        VariantStage(
            model="bytedance/seedream-4.5",
            reference_images=("richard-vale-reference-01.png",),
            reference_input_name="image_input",
            reference_input_many=True,
            include_negative_prompt=False,
            include_num_outputs=False,
            aspect_ratio="match_input_image",
            output_format=None,
            model_inputs={
                "size": "2K",
                "max_images": 1,
                "sequential_image_generation": "disabled",
            },
            variants=(
                "same identity as the reference image, keep Richard as a silver-haired law firm founder in his sixties with a conservative dark senior partner suit; make it less glossy and less stylized, with unretouched natural skin texture, realistic suit fabric, ordinary office lighting, and a believable photographed finish",
                "same identity and overall character direction as the reference image, preserve Richard's polished patriarch presence, silver hair, conservative tailoring, and emotionally contained authority; reduce AI gloss, avoid a perfect face or flawless skin, use realistic fabric, normal indoor lighting, and subtle natural age lines",
            ),
        ),
        VariantStage(
            model="bytedance/seedream-4.5",
            reference_images=("richard-vale-reference-01.png",),
            reference_input_name="image_input",
            reference_input_many=True,
            include_negative_prompt=False,
            include_num_outputs=False,
            aspect_ratio="match_input_image",
            output_format=None,
            model_inputs={
                "size": "2K",
                "max_images": 1,
                "sequential_image_generation": "disabled",
            },
            variants=(
                "same character and identity as the reference image, natural neutral studio portrait, ordinary soft studio light, realistic skin texture, realistic suit fabric, silver hair, conservative dark senior partner suit, emotionally contained authority, less glossy and unretouched",
                "same character and identity as the reference image, seated at the head of a law firm conference table, commanding posture, silver hair, conservative dark suit, calm patriarch presence, ordinary office lighting, realistic fabric and skin",
                "same character and identity as the reference image, standing in a private senior partner office with glass walls, silver hair, conservative tailored suit, controlled expression, image-conscious law firm founder, natural indoor light, believable photographed look",
                "same character and identity as the reference image, holding a phone while receiving bad news, emotionally restrained face, silver hair, conservative dark suit, ordinary office lighting, natural skin texture, powerful but privately shaken",
                "same character and identity as the reference image, authoritative close-up portrait, vertical 9:16, silver hair, conservative senior partner suit collar visible, clipped restrained expression, realistic fabric, ordinary lighting, less stylized",
            ),
        ),
    ),
)

ACTIVE_CHARACTER = RICHARD


def build_prompt(character: CharacterConcept, variant: str) -> str:
    return f"portrait concept of {character.name}, {character.description}, {variant}, {BASE_STYLE_PROMPT}"


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
            print(f"Skipping missing input image: assets/{relative_path}")

    return paths


def resolve_asset_input(relative_path: str) -> Path:
    path = (ASSETS_DIR / relative_path).resolve()
    if path.exists():
        return path

    matches = sorted(ASSETS_DIR.rglob(relative_path))
    if matches:
        return matches[0].resolve()

    return path


def run_character(character: CharacterConcept) -> None:
    input_images = resolve_asset_inputs(character.optional_input_images)
    if input_images:
        print(f"Resolved {len(input_images)} input images for {character.name}; current models may ignore them.")

    stage_index = RUN_STAGE_INDEX if RUN_STAGE_INDEX is not None else len(character.variant_stages) - 1
    stage = character.variant_stages[stage_index]
    run_variant_stage(character, stage, stage_index)


def run_variant_stage(character: CharacterConcept, stage: VariantStage, stage_index: int) -> None:
    stage_dir = OUTPUT_DIR / character.slug / f"{stage_index:02d}"
    stage_dir.mkdir(parents=True, exist_ok=True)
    reference_images = resolve_asset_inputs(stage.reference_images)

    if stage.reference_images and not reference_images:
        raise FileNotFoundError(f"No reference images found for stage {stage_index:02d}")

    if reference_images:
        if stage.reference_input_many:
            print(f"Using {len(reference_images)} reference image(s) as {stage.reference_input_name}.")
        elif len(reference_images) > 1:
            print(f"Using {reference_images[0].relative_to(ASSETS_DIR)} as {stage.reference_input_name}; this model accepts one input image.")

    for variant_index, variant in enumerate(stage.variants, start=1):
        stem = output_stem(character, stage_index, variant_index)
        expected_output = stage_dir / f"{stem}.png"
        if expected_output.exists():
            print(f"Skipping existing {expected_output.relative_to(ASSETS_DIR.parent)}")
            continue

        if variant_index > 1:
            time.sleep(REQUEST_DELAY_SECONDS)

        output = run_prediction(stage, build_prompt(character, variant), reference_images)
        save_outputs(output, stage_dir, stem)


def output_stem(character: CharacterConcept, stage_index: int, variant_index: int) -> str:
    return f"{character.slug}-{variant_index:02d}"


def run_prediction(stage: VariantStage, prompt: str, reference_images: list[Path]) -> Any:
    for attempt in range(1, MAX_THROTTLE_RETRIES + 1):
        model_input = build_model_input(stage, prompt, reference_images)
        try:
            return replicate.run(
                stage.model,
                input=model_input,
            )
        except ReplicateError as error:
            if getattr(error, "status", None) != 429 or attempt == MAX_THROTTLE_RETRIES:
                raise
            print(f"Replicate throttled request; waiting {REQUEST_DELAY_SECONDS}s before retry {attempt + 1}.")
            time.sleep(REQUEST_DELAY_SECONDS)
        finally:
            close_model_input_files(model_input)

    raise RuntimeError("Prediction retry loop exited unexpectedly")


def build_model_input(stage: VariantStage, prompt: str, reference_images: list[Path]) -> dict[str, Any]:
    model_input: dict[str, Any] = {
        "prompt": prompt,
        "aspect_ratio": stage.aspect_ratio,
    }

    if stage.output_format is not None:
        model_input["output_format"] = stage.output_format

    if stage.model_inputs:
        model_input.update(stage.model_inputs)

    if stage.include_negative_prompt:
        model_input["negative_prompt"] = NEGATIVE_PROMPT

    if stage.include_num_outputs:
        model_input["num_outputs"] = 1

    if reference_images:
        if stage.reference_input_many:
            model_input[stage.reference_input_name] = [path.open("rb") for path in reference_images]
        else:
            model_input[stage.reference_input_name] = reference_images[0].open("rb")

    return model_input


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
        destination = output_dir / f"{stem}{suffix}.png"
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
    run_character(ACTIVE_CHARACTER)


if __name__ == "__main__":
    main()
