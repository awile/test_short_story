# Marcus Character Sheet

## Goal

Create a reusable production-style character sheet for Marcus Vale from selected final generated images.

## Hypothesis

Nano Banana should be a strong first option because it supports multiple image references and is designed for maintaining character consistency across generated imagery.

Marcus's sheet should preserve his dark hair, mid-to-late-thirties age, severe expensive tailoring, controlled posture, clean-shaven face, and calm hostility while avoiding Ethan's youthful softness.

## Pipeline

- Code: `src/pipelines/characters/character_sheet.py`
- Output: `assets/generated/characters/character_sheets/marcus-vale/00/`
- Model: `google/nano-banana`
- Reference images: `marcus-vale-reference-01.png`, `marcus-vale-reference-02.png`, `marcus-vale-reference-03.png`, `marcus-vale-reference-04.png`, `marcus-vale-reference-05.png`, `marcus-vale-reference-06.png`
- Reference behavior: the script looks in the output directory first, then anywhere under `assets/`; all resolved references are passed as `image_input`
- Aspect ratio: `16:9`
- Output format: `jpg`

## Attempts

### Attempt 00

- Flow: explore character-sheet layouts using the selected Marcus references
- Variant 01: technical model turnaround with two horizontal rows: full-body front, left profile, right profile, back; close-up front, left profile, right profile
- Variant 02: portrait turnaround with front, profiles, three-quarter view, neutral expression, watchful expression, and cold angry close-up
- Variant 03: film-production sheet with full-body views, upper-body portrait, face detail, suit fabric detail, and phone prop pose
- Variant 04: story-use sheet with neutral portrait, conference table, law firm hallway, doorway watch, and cold tense close-up
- Result: not run yet

## Run Command

```bash
python -m src.pipelines.characters.character_sheet
```

Requires `REPLICATE_API_TOKEN` in the environment or `.env`.

## Outcome

Not run yet.

## Next Steps

- Pick the strongest sheet layout.
- If identity drifts, reduce the number of panels or use fewer, stronger references.
- If layout quality is weak, try `bytedance/seedream-4.5` for a second character-sheet pass.
