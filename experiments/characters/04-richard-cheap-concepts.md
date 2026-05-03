# Richard Cheap Concepts

## Goal

Generate inexpensive first-pass portrait concepts for Richard Vale using the same staged workflow as Ethan and Marcus.

## Hypothesis

Richard should read as the family patriarch and law firm founder: older, more authoritative, more conservative, and more image-conscious than either son.

The cheap model should help establish the broad senior-partner archetype before moving into reference-guided refinement.

## Pipeline

- Code: `src/pipelines/characters/cheap_concepts.py`
- Output: `assets/generated/characters/cheap_concepts/richard-vale/`
- Aspect ratio: `9:16`
- Character: Richard Vale
- Stage folders: `00`, `01`, etc. under each character output directory
- Run behavior: the script currently generates `ACTIVE_CHARACTER`, which is set to Richard

## Attempts

### Attempt 00

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/richard-vale/00/`
- Flow: explore Richard as powerful father, law firm founder, conservative senior partner, and image-conscious patriarch under pressure
- Variant 01: powerful law firm founder in his sixties, conservative immaculate senior partner suit, authoritative expensive presence, emotionally contained, treats family pain like a business decision
- Variant 02: wealthy managing partner and father, late sixties, silver hair, conservative dark suit, commanding posture, image-conscious and visibly burdened by the firm's crisis
- Variant 03: old-money law firm patriarch, polished silver-haired founder, immaculate senior partner wardrobe, clipped restrained expression, powerful but privately shaken
- Variant 04: authoritative father in an expensive law office, conservative suit, controlled face, visibly under pressure, chooses the family name and firm before emotion
- Result: not run yet

### Attempt 01

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/richard-vale/01/`
- Flow: develop the selected Attempt 00 direction while making Richard a soap-opera patriarch: old and powerful, but less deeply wrinkled and more polished on camera
- Variant 01: powerful law firm founder in his sixties, conservative immaculate senior partner suit, authoritative expensive presence, emotionally contained, soap opera patriarch polish, older but not deeply wrinkled
- Variant 02: powerful law firm founder in his early sixties, smooth well-kept face for his age, conservative immaculate senior partner suit, controlled expression, expensive soap opera family patriarch energy
- Variant 03: wealthy senior partner and father in his sixties, silver hair, polished camera-ready face with fewer wrinkles, conservative dark suit, commanding presence, emotionally contained
- Variant 04: old-money law firm founder in his sixties, handsome aging patriarch, lightly lined face, immaculate senior partner suit, restrained expression, treats family pain like a business decision
- Result: not run yet

### Attempt 02

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/richard-vale/02/`
- Flow: develop the selected Attempt 01 third image direction: wealthy senior partner and father, silver hair, polished camera-ready face, conservative dark suit, commanding but emotionally contained
- Variant 01: wealthy senior partner and father in his sixties, silver hair, polished camera-ready face with fewer wrinkles, conservative dark suit, commanding presence, emotionally contained, soap opera patriarch realism
- Variant 02: wealthy senior partner and father in his sixties, silver hair, polished well-kept face, conservative dark senior partner suit, calm commanding presence, emotionally contained under pressure
- Variant 03: wealthy law firm founder and father in his sixties, silver hair, camera-ready face with light age lines, conservative immaculate dark suit, powerful contained presence, image-conscious patriarch
- Variant 04: wealthy senior partner and father, early sixties, silver hair, polished face without deep wrinkles, conservative dark suit, restrained expression, commanding but privately shaken
- Result: not run yet

### Attempt 03

- Model: `black-forest-labs/flux-kontext-dev`
- Output: `assets/generated/characters/cheap_concepts/richard-vale/03/`
- Reference image: `richard-vale-reference-01.png`
- Reference behavior: place the selected Richard image anywhere under `assets/` with this filename; Kontext receives it as `input_image`
- Flow: use the selected Richard reference image to preserve identity while refining the silver-haired, polished senior-partner patriarch direction
- Variant 01: use the reference image as visual direction for Richard Vale's identity, silver hair, polished camera-ready face with fewer wrinkles, conservative dark senior partner suit, commanding presence, emotionally contained, realistic law firm founder
- Variant 02: preserve the reference image's face direction and wealthy patriarch energy; refine Richard into a powerful silver-haired law firm founder in his sixties, conservative immaculate suit, controlled expression, soap opera realism
- Variant 03: use the reference image to guide facial believability, grooming, and wardrobe; create Richard as an image-conscious senior partner and father, polished face with light age lines, conservative dark suit, calm authority under pressure
- Variant 04: keep the reference image's identity direction while making Richard authoritative and expensive, silver hair, conservative senior partner suit, emotionally restrained expression, realistic corporate-noir portrait
- Result: not run yet

### Attempt 04

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/richard-vale/04/`
- Reference image: `richard-vale-reference-01.png`
- Reference behavior: place the selected Richard image anywhere under `assets/` with this filename; Seedream receives it as `image_input`
- Flow: use the realism language that worked for Ethan and Marcus: same identity, less glossy, unretouched, natural skin texture, realistic fabric, ordinary lighting
- Variant 01: same identity as the reference image, keep Richard as a silver-haired law firm founder in his sixties with a conservative dark senior partner suit; make it less glossy and less stylized, with unretouched natural skin texture, realistic suit fabric, ordinary office lighting, and a believable photographed finish
- Variant 02: same identity and overall character direction as the reference image, preserve Richard's polished patriarch presence, silver hair, conservative tailoring, and emotionally contained authority; reduce AI gloss, avoid a perfect face or flawless skin, use realistic fabric, normal indoor lighting, and subtle natural age lines
- Result: not run yet

### Attempt 05

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/richard-vale/05/`
- Reference image: `richard-vale-reference-01.png`
- Reference behavior: place the selected Richard image anywhere under `assets/` with this filename; Seedream receives it as `image_input`
- Flow: keep Richard's identity and reference look while testing practical story-use poses and scenes with plain photoreal language
- Variant 01: same character and identity as the reference image, natural neutral studio portrait, ordinary soft studio light, realistic skin texture, realistic suit fabric, silver hair, conservative dark senior partner suit, emotionally contained authority, less glossy and unretouched
- Variant 02: same character and identity as the reference image, seated at the head of a law firm conference table, commanding posture, silver hair, conservative dark suit, calm patriarch presence, ordinary office lighting, realistic fabric and skin
- Variant 03: same character and identity as the reference image, standing in a private senior partner office with glass walls, silver hair, conservative tailored suit, controlled expression, image-conscious law firm founder, natural indoor light, believable photographed look
- Variant 04: same character and identity as the reference image, holding a phone while receiving bad news, emotionally restrained face, silver hair, conservative dark suit, ordinary office lighting, natural skin texture, powerful but privately shaken
- Variant 05: same character and identity as the reference image, authoritative close-up portrait, vertical 9:16, silver hair, conservative senior partner suit collar visible, clipped restrained expression, realistic fabric, ordinary lighting, less stylized
- Result: not run yet

## Run Command

```bash
python -m src.pipelines.characters.cheap_concepts
```

Requires `REPLICATE_API_TOKEN` in the environment or `.env`.

## Outcome

Not run yet.

## Next Steps

- Pick the strongest broad Richard direction.
- Make sure he reads older and more authoritative than Marcus.
- Build a second cheap variant stage from the strongest patriarch traits.
