# Cheap Character Concepts

## Goal

Generate inexpensive first-pass portrait concepts for Ethan Vale before moving to stronger edit or refinement models.

## Hypothesis

A cheap model is a useful first step for character development because it can quickly explore broad visual directions before spending more time and money refining selected concepts with stronger models.

The workflow should simulate an agent helping craft the character: start with the story description, generate several prompt variants, review what works visually, then use those choices to revise the next round.

## Pipeline

- Code: `src/pipelines/characters/cheap_concepts.py`
- Output: `assets/generated/characters/cheap_concepts/`
- Aspect ratio: `9:16`
- Character: Ethan Vale
- Stage folders: `00`, `01`, etc. under each character output directory
- Run behavior: the script generates the newest configured stage by default

## Attempts

### Attempt 00

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/00/`
- Flow: generate multiple Ethan variants from the same base character description, then choose which traits are worth carrying into the next stage
- Variant 01: boyish and underestimated, anxious ambition, trying to look older than he is
- Variant 02: sharp and privileged but emotionally exposed, polished heir under sudden pressure
- Variant 03: quietly intense and wounded, intelligent eyes, restrained panic beneath a professional exterior
- Variant 04: clean-cut rising associate, expensive but slightly imperfect suit, desperate for approval
- Result: not run yet

### Attempt 01

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/01/`
- Flow: permute the strongest directions from Attempt 00: boyish and underestimated plus sharp and privileged
- Variant 01: boyish face with privileged polish, expensive suit worn slightly too carefully, anxious heir trying to project authority
- Variant 02: sharp young associate with vulnerable eyes, old-money grooming, emotionally exposed beneath a controlled professional mask
- Variant 03: underestimated golden son, clean-cut and expensive, youthful softness contrasted with a tense corporate posture
- Variant 04: privileged but not yet hardened, polished law firm heir with boyish uncertainty and a defensive ambitious stare
- Result: not run yet

### Attempt 02

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/02/`
- Flow: develop the selected Attempt 01 direction: underestimated golden son, clean-cut and expensive, youthful softness contrasted with tense corporate posture
- Variant 01: underestimated golden son, clean-cut old-money polish, soft youthful face, tense shoulders, trying to look composed in an expensive law office
- Variant 02: expensive young heir with gentle features, immaculate suit, nervous corporate posture, privilege undercut by visible uncertainty
- Variant 03: clean-cut law firm son with youthful softness, polished grooming, tense restrained body language, underestimated but quietly intelligent
- Variant 04: privileged golden boy associate, soft face and expensive tailoring, anxious ambition beneath a controlled corporate stance
- Result: not run yet

### Attempt 03

- Model: `black-forest-labs/flux-kontext-dev`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/03/`
- Reference images: `ethan-vale-reference-01.png`, `ethan-vale-reference-02.png`
- Reference behavior: files can be placed anywhere under `assets/`; the current Kontext model input uses one image per request, so the script passes the first resolved reference image and tracks both as visual direction for the stage
- Flow: use the selected Attempt 02 direction with reference-image guidance to improve realism, grooming, wardrobe polish, and facial believability without copying either reference exactly
- Variant 01: use the reference images as visual direction for face, grooming, wardrobe polish, and realism; create an original underestimated golden son with clean-cut old-money polish, soft youthful face, tense shoulders, and a composed law office presence
- Variant 02: use the reference images as visual direction without copying either person exactly; make Ethan an expensive young heir with gentle features, immaculate suit, nervous corporate posture, and realistic natural skin detail
- Variant 03: blend the reference image direction into an original clean-cut law firm son with youthful softness, polished grooming, restrained body language, quiet intelligence, and cinematic realism
- Variant 04: use the reference images to guide realism, facial believability, hair, and wardrobe; create a privileged golden boy associate with soft features, expensive tailoring, and anxious ambition under a controlled corporate stance
- Result: not run yet

### Attempt 04

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/04/`
- Reference image: `ethan-vale-seedream-reference.png`
- Reference behavior: place the selected Ethan image anywhere under `assets/` with this filename; Seedream receives it as `image_input`
- Flow: use the selected image as the character anchor and make controlled realism-focused edits that reduce stylization while preserving Ethan's identity and corporate-thriller direction
- Variant 01: edit the reference portrait into a more realistic live-action character portrait while preserving Ethan's identity, clean-cut expensive look, youthful softness, restrained corporate tension, natural skin texture, and believable law office lighting
- Variant 02: make the reference portrait feel like a real photographed person, reducing any stylized or cartoon-like qualities while keeping the same character, wardrobe polish, facial direction, and tense old-money law firm mood
- Variant 03: refine the reference portrait toward a polished Ivy League law associate: understated old-money grooming, precise tailoring, realistic facial details, soft youthful features, and controlled corporate posture
- Variant 04: keep the same character from the reference image but make him slightly more naive and emotionally readable, with naturalistic skin, gentle features, expensive grooming, and subtle anxious ambition
- Result: not run yet

### Attempt 05

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/05/`
- Reference image: `ethan-vale-reference-01.png`
- Reference behavior: place the selected Ethan image anywhere under `assets/` with this filename; Seedream receives it as `image_input`
- Flow: use the selected image as the character anchor and make a restrained realism pass using plain photo-real language: same identity, less glossy, unretouched, natural skin texture, realistic fabric, ordinary lighting
- Variant 01: same identity as the reference image, keep the clean-cut expensive look and youthful softness; make it less glossy and less comic-book-like, with unretouched natural skin texture, realistic suit fabric, ordinary office lighting, and a believable photographed finish
- Variant 02: same identity and overall character direction as the reference image, preserve the soft youthful features and polished old-money grooming; reduce AI gloss, avoid a perfect face or flawless skin, use realistic fabric, normal indoor lighting, and subtle natural imperfections
- Result: not run yet

### Attempt 06

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/06/`
- Reference image: `ethan-vale-reference-01.png`
- Reference behavior: place the selected Ethan image anywhere under `assets/` with this filename; Seedream receives it as `image_input`
- Flow: keep Ethan's identity and reference look while testing practical story-use poses and scenes with plain photoreal language
- Variant 01: same character and identity as the reference image, natural neutral studio portrait, ordinary soft studio light, realistic skin texture, realistic suit fabric, clean-cut expensive look, youthful softness, less glossy and unretouched
- Variant 02: same character and identity as the reference image, seated at a conference table in a law firm, ordinary office lighting, realistic fabric and natural skin texture, clean-cut expensive look, youthful softness, less AI gloss
- Variant 03: same character and identity as the reference image, standing in a law firm hallway, natural indoor light, realistic suit fabric, unretouched skin texture, clean-cut old-money grooming, youthful softness, believable photographed look
- Variant 04: same character and identity as the reference image, looking shocked while holding a phone, realistic office lighting, natural skin texture, clean-cut expensive look, youthful softness, believable expression without comic-book drama
- Variant 05: same character and identity as the reference image, angry close-up portrait, vertical 9:16, natural skin texture, realistic fabric, ordinary lighting, clean-cut expensive look, youthful softness preserved, less glossy and less stylized
- Result: not run yet

## Run Command

```bash
python -m src.pipelines.characters.cheap_concepts
```

Requires `REPLICATE_API_TOKEN` in the environment or `.env`.

## Outcome

Not run yet.

## Next Steps

- Pick the strongest rough concepts for Ethan.
- Note which prompt variants work best and revise the next round around those traits.
- Move selected outputs into the next refinement experiment.
- Try a stronger edit-capable model with the selected images as references.
