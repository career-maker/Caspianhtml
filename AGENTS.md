# Caspian & Sun Food Trading LLC — AI Agent Rules

These rules are **mandatory** for every AI agent that creates, edits, or reviews
pages in this project. They must be applied without exception before any work is
committed.

---

## Rule 1 — Reusable Heading Component

### What to do
- Every section title **must** carry the class `section-heading` (defined in
  `css/style.css`).
- Use modifier classes for visual variants:
  - `section-heading--upper` — uppercase editorial headings (About page style)
  - `section-heading--display` — hero-scale display headings
  - `section-heading--on-dark` — headings on dark/teal backgrounds
  - `section-heading--center` — centred alignment

### What NOT to do
- Never write CSS rules that target a bare heading tag to style a section
  title, e.g.:
  ```css
  /* BAD */
  h2 { font-family: ...; }
  .some-section h2 { font-size: ...; }
  ```
- Never create one-off heading classes that duplicate `.section-heading`
  styles (e.g., `.who-heading`, `.process-title`, `.cta-title`).

### Why
Styling that depends on the tag breaks the moment the semantic level changes
(h2 to h3). The class decouples visual design from document structure.

### Checklist — Before committing any new page or section
- [ ] Every section title element has `class="section-heading"` (plus any needed
      modifier).
- [ ] No bare `h2 { }` or `h3 { }` rules exist in the page style block
      or in `css/style.css` for section-level styling.
- [ ] No duplicate heading classes were invented instead of reusing
      `.section-heading`.

---

## Rule 2 — Natural Section Height

### What to do
- Sections must **grow with their content**. Use `padding` (ideally `clamp()`)
  to control vertical breathing room.
- `min-height` is **only** permitted for these two cases:
  1. **True full-screen heroes** — sections whose entire purpose is to fill the
     viewport (e.g., `.hero { min-height: 560px }`).
  2. **Full-bleed image/video backdrops** — sections where a background photo
     or video must remain visually prominent regardless of text length.
  - Always add a comment explaining why `min-height` is needed.

### What NOT to do
- Never add `min-height: 100vh` (or any fixed pixel value) to a content
  section just to make it look full screen:
  ```css
  /* BAD */
  .contact-section { min-height: 100vh; }
  .blog-section    { min-height: 100vh; }
  .article-wrap    { min-height: 100vh; }
  section          { min-height: 100vh; }
  ```
- Never apply a blanket `section { min-height: ... }` rule.

### Checklist — Before committing any new page or section
- [ ] No content section has `min-height` unless it is a full-screen hero or
      full-bleed backdrop.
- [ ] A comment exists on every permitted `min-height` explaining the design
      rationale.
- [ ] Sections still look correct at different text lengths without fixed heights.

---

## Quick Reference — Approved Patterns

HTML:
```html
<!-- Section heading — standard -->
<h2 class="section-heading">Our Products</h2>

<!-- Section heading — uppercase editorial -->
<h2 class="section-heading section-heading--upper">Who We Are</h2>

<!-- Section heading — on dark background -->
<h2 class="section-heading section-heading--on-dark">Why Choose Us</h2>

<!-- Section — natural height (correct) -->
<section class="sec about">
  <div class="wrap"> ... </div>
</section>

<!-- Hero — min-height permitted (correct, with comment) -->
<!-- min-height: 560px — true full-screen hero -->
<section class="hero"> ... </section>
```

CSS:
```css
/* Heading override for a section context (correct) */
.cats .section-heading { color: #fff; }

/* Section padding — correct approach */
.contact-section {
  padding: clamp(3rem, 5vw, 4.5rem) clamp(1.5rem, 5vw, 3rem);
  background: #fff;
  /* no min-height — content drives height */
}
```
