# Vertical Short Story Lab

This project is a small workspace for planning and testing a vertical short-form video story pipeline.

The goal is to make one short story manually first, then turn the lessons into reusable tools for story planning, image generation, video generation, voice, and assembly.

## Structure

```text
story/              Creative planning: premise, characters, script, shots
assets/references/  Reference images, mood boards, sketches, examples
assets/generated/   Generated images, audio, and intermediate media
assets/exports/     Final rendered videos or shareable outputs
experiments/        One-off tests for tools, models, prompts, and pipelines
src/                Reusable Python code and runnable tool modules
```

## Working Format

- Aspect ratio: 9:16 vertical
- Target resolution: 1080x1920
- Initial target duration: 30-60 seconds
- Suggested frame rate: 24 or 30 fps

## Suggested Workflow

1. Write the premise in `story/premise.md`.
2. Define repeatable character details in `story/characters.md`.
3. Draft narration and dialogue in `story/script.md`.
4. Break the story into shots in `story/shot-list.md`.
5. Test prompts and tools in `experiments/image-gen/`.
6. Move reusable code into `src/` once an experiment proves useful.
7. Save generated assets under `assets/generated/` and final videos under `assets/exports/`.

## Code

All code lives under `src/`.

Future runnable modules can be invoked with Python's module syntax, for example:

```bash
python -m src.tools.generate_image
```

## Environment

Copy `.env.example` to `.env` and fill in API keys locally. Do not commit `.env`.
