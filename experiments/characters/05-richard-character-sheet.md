# Richard Character Sheet

## Goal

Create a reusable production-style character sheet for Richard Vale from selected final generated images.

## Hypothesis

Nano Banana should be a strong first option because it supports multiple image references and is designed for maintaining character consistency across generated imagery.

Richard's sheet should preserve his silver hair, sixties age, conservative senior-partner wardrobe, authoritative patriarch presence, polished camera-ready face, and emotionally contained expression.

## Pipeline

- Code: `src/pipelines/characters/character_sheet.py`
- Output: `assets/generated/characters/character_sheets/richard-vale/00/`
- Model: `google/nano-banana`
- Reference images: `richard-vale-reference-01.png`, `richard-vale-reference-02.png`, `richard-vale-reference-03.png`, `richard-vale-reference-04.png`, `richard-vale-reference-05.png`
- Reference behavior: the script looks in the output directory first, then anywhere under `assets/`; all resolved references are passed as `image_input`
- Aspect ratio: `16:9`
- Output format: `jpg`

## Attempts

### Attempt 00

- Flow: explore character-sheet layouts using the selected Richard references
- Variant 01: technical model turnaround with two horizontal rows: full-body front, left profile, right profile, back; close-up front, left profile, right profile
- Variant 02: portrait turnaround with front, profiles, three-quarter view, neutral expression, stern expression, and privately shaken close-up
- Variant 03: film-production sheet with full-body views, upper-body portrait, face detail, suit fabric detail, and phone prop pose
- Variant 04: story-use sheet with neutral portrait, conference table, senior partner office, bad-news phone shot, and authoritative close-up
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
