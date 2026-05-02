# Cheap Character Concepts

## Goal

Generate inexpensive first-pass portrait concepts for Ethan Vale before moving to stronger edit or refinement models.

## Hypothesis

A cheap model is a useful first step for character development because it can quickly explore broad visual directions before spending more time and money refining selected concepts with stronger models.

The workflow should simulate an agent helping craft the character: start with the story description, generate several prompt variants, review what works visually, then use those choices to revise the next round.

## Pipeline

- Code: `src/pipeline/characters/cheap_concepts.py`
- Output: `assets/generated/characters/cheap_concepts/`
- Aspect ratio: `9:16`
- Character: Ethan Vale

## Attempts

### Attempt 00

- Model: `black-forest-labs/flux-schnell`
- Flow: generate multiple Ethan variants from the same base character description, then choose which traits are worth carrying into the next round
- Variant 01: boyish and underestimated, anxious ambition, trying to look older than he is
- Variant 02: sharp and privileged but emotionally exposed, polished heir under sudden pressure
- Variant 03: quietly intense and wounded, intelligent eyes, restrained panic beneath a professional exterior
- Variant 04: clean-cut rising associate, expensive but slightly imperfect suit, desperate for approval
- Result: not run yet

## Run Command

```bash
python -m src.pipeline.characters.cheap_concepts
```

Requires `REPLICATE_API_TOKEN` in the environment or `.env`.

## Outcome

Not run yet.

## Next Steps

- Pick the strongest rough concepts for Ethan.
- Note which prompt variants work best and revise the next round around those traits.
- Move selected outputs into the next refinement experiment.
- Try a stronger edit-capable model with the selected images as references.
