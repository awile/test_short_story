# Marcus Cheap Concepts

## Goal

Generate inexpensive first-pass portrait concepts for Marcus Vale using Ethan's workflow as a template, but with a clearly colder and more controlled visual direction.

## Hypothesis

Marcus should visually contrast Ethan. Where Ethan is youthful, soft, and vulnerable, Marcus should feel older, sharper, severe, and strategically composed.

The cheap model should be useful for exploring the broad Marcus archetype before moving into reference-guided refinement.

## Pipeline

- Code: `src/pipelines/characters/cheap_concepts.py`
- Output: `assets/generated/characters/cheap_concepts/marcus-vale/`
- Aspect ratio: `9:16`
- Character: Marcus Vale
- Stage folders: `00`, `01`, etc. under each character output directory
- Run behavior: the script currently generates `ACTIVE_CHARACTER`, which is set to Marcus

## Attempts

### Attempt 00

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/marcus-vale/00/`
- Flow: generate broad Marcus variants that explore severity, polish, strategic control, and older-brother resentment; Marcus should read mid-to-late thirties with dark hair, not 50s or father-like
- Variant 01: mid-to-late thirties older brother, dark hair, severe old-money polish, precise grooming, controlled expression, looks like he has already won without looking fifty or father-like
- Variant 02: dark-haired senior associate in his late thirties, sharp and composed, expensive dark suit, restrained ambition, strategic eyes, polished law firm posture
- Variant 03: mid-thirties resentful heir with dark hair and a severe tailored suit, calm surface with quiet hostility underneath, youthful enough to be Ethan's older brother not his father
- Variant 04: dark-haired older brother in his late thirties watching from the edge of a glass law office, immaculate wardrobe, colder posture than Ethan, patient calculating expression
- Result: not run yet

### Attempt 01

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/marcus-vale/01/`
- Flow: stay close to the selected Attempt 00 prompt and only make small controlled changes around age, suit, mood, and subtlety
- Variant 01: mid-thirties resentful heir with dark hair and a severe tailored suit, calm surface with quiet hostility underneath, youthful enough to be Ethan's older brother not his father, slightly younger face
- Variant 02: mid-thirties resentful heir with dark hair and a severe expensive tailored suit, calm surface with quiet hostility underneath, youthful enough to be Ethan's older brother not his father
- Variant 03: mid-thirties resentful heir with dark hair and a severe tailored suit, calm surface with quiet hostility underneath, darker corporate mood, youthful enough to be Ethan's older brother not his father
- Variant 04: mid-thirties resentful heir with dark hair and a severe tailored suit, calm surface with very subtle hostility underneath, youthful enough to be Ethan's older brother not his father
- Result: not run yet

### Attempt 02

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/marcus-vale/02/`
- Flow: develop the selected Attempt 01 direction: mid-thirties resentful heir with dark hair, severe expensive tailored suit, calm surface, and quiet hostility underneath
- Variant 01: mid-thirties resentful heir with dark hair and a severe expensive tailored suit, calm surface with quiet hostility underneath, youthful enough to be Ethan's older brother not his father, natural realistic face
- Variant 02: mid-thirties resentful heir with dark hair and a severe expensive tailored charcoal suit, calm surface with quiet hostility underneath, polished law firm presence, youthful enough to be Ethan's older brother not his father
- Variant 03: late-thirties resentful heir with dark hair and a severe expensive tailored suit, calm surface with quiet hostility underneath, sharp older brother energy without looking father-like
- Variant 04: mid-thirties resentful heir with dark hair and a severe expensive tailored suit, controlled posture, calm surface with quiet hostility underneath, precise but not overly villainous
- Result: not run yet

### Attempt 03

- Model: `black-forest-labs/flux-kontext-dev`
- Output: `assets/generated/characters/cheap_concepts/marcus-vale/03/`
- Reference image: `marcus-vale-reference-01.png`
- Reference behavior: place the selected Marcus image anywhere under `assets/` with this filename; Kontext receives it as `input_image`
- Flow: use the selected Marcus reference image to preserve identity while refining the severe, dark-haired, mid-to-late-thirties resentful-heir direction
- Variant 01: use the reference image as visual direction for Marcus Vale's identity, dark hair, severe expensive tailored suit, calm surface with quiet hostility underneath, mid-to-late thirties, realistic law firm heir, not father-like
- Variant 02: preserve the reference image's face direction and dark-haired older-brother energy; refine Marcus into a severe mid-thirties resentful heir with expensive tailoring, controlled posture, and subtle hostility beneath a calm polished surface
- Variant 03: use the reference image to guide facial believability, grooming, and wardrobe; create Marcus as a sharp dark-haired law firm heir in his late thirties, severe suit, quiet resentment, realistic natural skin texture
- Variant 04: keep the reference image's identity direction while making Marcus colder and more strategic than Ethan, dark hair, severe tailored suit, calm expression, quiet hostility, realistic corporate-noir portrait
- Result: not run yet

### Attempt 04

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/marcus-vale/04/`
- Reference image: `marcus-vale-reference-01.png`
- Reference behavior: place the selected Marcus image anywhere under `assets/` with this filename; Seedream receives it as `image_input`
- Flow: use the realism language that worked for Ethan's second-to-last stage: same identity, less glossy, unretouched, natural skin texture, realistic fabric, ordinary lighting
- Variant 01: same identity as the reference image, keep Marcus as a dark-haired mid-to-late-thirties resentful heir in a severe expensive tailored suit; make it less glossy and less stylized, with unretouched natural skin texture, realistic suit fabric, ordinary office lighting, and a believable photographed finish
- Variant 02: same identity and overall character direction as the reference image, preserve the calm surface with quiet hostility underneath, dark hair, severe tailoring, and older-brother age; reduce AI gloss, avoid a perfect face or flawless skin, use realistic fabric, normal indoor lighting, and subtle natural imperfections
- Result: not run yet

### Attempt 05

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/marcus-vale/05/`
- Reference image: `marcus-vale-reference-01.png`
- Reference behavior: place the selected Marcus image anywhere under `assets/` with this filename; Seedream receives it as `image_input`
- Flow: keep Marcus's identity and reference look while testing practical story-use poses and scenes with plain photoreal language
- Variant 01: same character and identity as the reference image, natural neutral studio portrait, ordinary soft studio light, realistic skin texture, realistic suit fabric, dark hair, severe expensive tailored suit, calm controlled expression, less glossy and unretouched
- Variant 02: same character and identity as the reference image, seated at a conference table in a law firm, composed posture, hands still, dark hair, severe tailored suit, quiet hostility under a calm surface, ordinary office lighting, realistic fabric and skin
- Variant 03: same character and identity as the reference image, standing in a glass law firm hallway, dark hair, severe tailored suit, controlled older-brother posture, strategic watchful expression, natural indoor light, less glossy, believable photographed look
- Variant 04: same character and identity as the reference image, watching from the edge of a conference room doorway, dark hair, severe expensive suit, calm expression with quiet resentment underneath, realistic office lighting, natural skin texture
- Variant 05: same character and identity as the reference image, cold close-up portrait, vertical 9:16, dark hair, severe tailored suit collar visible, restrained anger behind a calm face, realistic fabric, ordinary lighting, less stylized
- Result: not run yet

## Run Command

```bash
python -m src.pipelines.characters.cheap_concepts
```

Requires `REPLICATE_API_TOKEN` in the environment or `.env`.

## Outcome

Not run yet.

## Next Steps

- Pick the strongest broad Marcus direction.
- Compare against Ethan to make sure Marcus reads older, colder, and more controlled.
- Build a second cheap variant stage from the strongest Marcus traits.
