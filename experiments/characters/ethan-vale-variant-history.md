# Ethan Vale Variant History

## Purpose

Save Ethan Vale's character-development prompt history before starting Marcus Vale.

This is the working lineage for Ethan's look: what was tried, what direction emerged, and what language should be reused or avoided when developing the next character.

## Core Ethan Direction

- Younger son and junior employee at his father's law firm
- Polished but vulnerable
- Expressive face
- Tailored office clothes, slightly less sharp than senior partners
- Clean-cut expensive look
- Youthful softness
- Old-money grooming
- Natural skin texture, realistic fabric, ordinary lighting
- Avoid glossy AI finish, comic-book styling, perfect face, flawless skin

## Stage 00: Broad Cheap Concepts

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/00/`
- Goal: explore broad first-pass Ethan archetypes

Variants:

- Boyish and underestimated, anxious ambition, trying to look older than he is
- Sharp and privileged but emotionally exposed, polished heir under sudden pressure
- Quietly intense and wounded, intelligent eyes, restrained panic beneath a professional exterior
- Clean-cut rising associate, expensive but slightly imperfect suit, desperate for approval

Useful signals:

- The boyish and underestimated direction worked.
- The sharp and privileged direction also worked.
- The character should feel expensive, but not hardened.

## Stage 01: Boyish Plus Privileged

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/01/`
- Goal: combine the two strongest Stage 00 directions

Variants:

- Boyish face with privileged polish, expensive suit worn slightly too carefully, anxious heir trying to project authority
- Sharp young associate with vulnerable eyes, old-money grooming, emotionally exposed beneath a controlled professional mask
- Underestimated golden son, clean-cut and expensive, youthful softness contrasted with a tense corporate posture
- Privileged but not yet hardened, polished law firm heir with boyish uncertainty and a defensive ambitious stare

Useful signals:

- Best direction: underestimated golden son, clean-cut and expensive, youthful softness contrasted with tense corporate posture.

## Stage 02: Selected Golden Son Direction

- Model: `black-forest-labs/flux-schnell`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/02/`
- Goal: develop the selected Stage 01 direction

Variants:

- Underestimated golden son, clean-cut old-money polish, soft youthful face, tense shoulders, trying to look composed in an expensive law office
- Expensive young heir with gentle features, immaculate suit, nervous corporate posture, privilege undercut by visible uncertainty
- Clean-cut law firm son with youthful softness, polished grooming, tense restrained body language, underestimated but quietly intelligent
- Privileged golden boy associate, soft face and expensive tailoring, anxious ambition beneath a controlled corporate stance

Useful signals:

- Youthful softness matters.
- The expensive look should read as inherited polish, not aggressive power.

## Stage 03: Reference-Guided Refinement

- Model: `black-forest-labs/flux-kontext-dev`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/03/`
- References: `ethan-vale-reference-01.png`, `ethan-vale-reference-02.png`
- Goal: use reference images to improve realism and facial believability

Variants:

- Use the reference images as visual direction for face, grooming, wardrobe polish, and realism; create an original underestimated golden son with clean-cut old-money polish, soft youthful face, tense shoulders, and a composed law office presence
- Use the reference images as visual direction without copying either person exactly; make Ethan an expensive young heir with gentle features, immaculate suit, nervous corporate posture, and realistic natural skin detail
- Blend the reference image direction into an original clean-cut law firm son with youthful softness, polished grooming, restrained body language, quiet intelligence, and cinematic realism
- Use the reference images to guide realism, facial believability, hair, and wardrobe; create a privileged golden boy associate with soft features, expensive tailoring, and anxious ambition under a controlled corporate stance

## Stage 04: Seedream Refinement

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/04/`
- Goal: refine selected reference direction while preserving identity

Variants:

- Edit the reference portrait into a more realistic live-action character portrait while preserving Ethan's identity, clean-cut expensive look, youthful softness, restrained corporate tension, natural skin texture, and believable law office lighting
- Make the reference portrait feel like a real photographed person, reducing any stylized or cartoon-like qualities while keeping the same character, wardrobe polish, facial direction, and tense old-money law firm mood
- Refine the reference portrait toward a polished Ivy League law associate: understated old-money grooming, precise tailoring, realistic facial details, soft youthful features, and controlled corporate posture
- Keep the same character from the reference image but make him slightly more naive and emotionally readable, with naturalistic skin, gentle features, expensive grooming, and subtle anxious ambition

## Stage 05: Plain Photoreal Language

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/05/`
- Goal: reduce AI gloss while preserving Ethan's softer qualities

Variants:

- Same identity as the reference image, keep the clean-cut expensive look and youthful softness; make it less glossy and less comic-book-like, with unretouched natural skin texture, realistic suit fabric, ordinary office lighting, and a believable photographed finish
- Same identity and overall character direction as the reference image, preserve the soft youthful features and polished old-money grooming; reduce AI gloss, avoid a perfect face or flawless skin, use realistic fabric, normal indoor lighting, and subtle natural imperfections

Useful signals:

- More realistic language works better when it avoids `ultra-detailed`, `dramatic lighting`, `masterpiece`, `cinematic`, `perfect face`, `flawless skin`, `8K`, and `hyperreal`.
- Better realism language: same identity, less glossy, unretouched, natural skin texture, realistic fabric, ordinary lighting.

## Stage 06: Story-Use Poses

- Model: `bytedance/seedream-4.5`
- Output: `assets/generated/characters/cheap_concepts/ethan-vale/06/`
- Goal: test whether the selected identity transfers into practical story scenes

Variants:

- Same character and identity as the reference image, natural neutral studio portrait, ordinary soft studio light, realistic skin texture, realistic suit fabric, clean-cut expensive look, youthful softness, less glossy and unretouched
- Same character and identity as the reference image, seated at a conference table in a law firm, ordinary office lighting, realistic fabric and natural skin texture, clean-cut expensive look, youthful softness, less AI gloss
- Same character and identity as the reference image, standing in a law firm hallway, natural indoor light, realistic suit fabric, unretouched skin texture, clean-cut old-money grooming, youthful softness, believable photographed look
- Same character and identity as the reference image, looking shocked while holding a phone, realistic office lighting, natural skin texture, clean-cut expensive look, youthful softness, believable expression without comic-book drama
- Same character and identity as the reference image, angry close-up portrait, vertical 9:16, natural skin texture, realistic fabric, ordinary lighting, clean-cut expensive look, youthful softness preserved, less glossy and less stylized

## Notes For Marcus

Marcus should not inherit Ethan's youthful softness. Use this history mainly as a workflow template.

Useful contrast for Marcus:

- Older brother instead of younger son
- More severe and controlled
- Sharper suit and posture
- Less vulnerable, less boyish
- More composed, colder, more strategic
- Should look like he has already won before Ethan understands the game

Prompt language to adapt for Marcus:

- `same identity`, `less glossy`, `unretouched`, `natural skin texture`, `realistic fabric`, `ordinary lighting`
- Keep the corporate realism lessons, but replace Ethan's softness with severity and control.
