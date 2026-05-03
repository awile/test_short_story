# Ethan Character Sheet

## Goal

Create a reusable production-style character sheet for Ethan Vale from selected final generated images.

## Hypothesis

A separate character-sheet pipeline is better than another character variant stage because this output is a structured deliverable, not another identity-discovery pass.

Nano Banana should be a strong first option because it supports multi-image references and is designed for maintaining character consistency across generated imagery.

## Pipeline

- Code: `src/pipelines/characters/character_sheet.py`
- Output: `assets/generated/characters/character_sheets/ethan-vale/00/`
- Model: `google/nano-banana`
- Reference images: `ethan-vale-reference-01.png`, `ethan-vale-reference-02.png`, `ethan-vale-reference-03.png`, `ethan-vale-reference-04.png`
- Reference behavior: the script looks in the output directory first, then anywhere under `assets/`; all resolved references are passed as `image_input`
- Aspect ratio: `16:9`
- Output format: `jpg`

## Attempts

### Attempt 00

- Flow: explore character-sheet layouts using the same selected Ethan references
- Variant 01: technical model turnaround with two horizontal rows: full-body front, left profile, right profile, back; close-up front, left profile, right profile
- Variant 02: portrait turnaround with front, profiles, three-quarter view, neutral expression, worried expression, and angry close-up
- Variant 03: film-production sheet with full-body views, upper-body portrait, face detail, suit fabric detail, and phone prop pose
- Variant 04: story-use sheet with neutral portrait, conference table, law firm hallway, shocked phone shot, and tense close-up
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
- If identity drifts, reduce the sheet to fewer panels or use a stronger selected reference image.
- If layout quality is weak, try `bytedance/seedream-4.5` for a second character-sheet pass.
