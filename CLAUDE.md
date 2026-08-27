# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Sphinx documentation site recording the history of Monkton (Thanet, Kent) — led by
Stuart Horsburgh — currently focused on St Mary Magdalene church: its architecture,
clergy back to 1291, bells, war memorial, and a full churchyard survey. Content is
Markdown via MyST, rendered with the Furo theme, and deployed to GitHub Pages.

## Commands

```bash
source .venv/bin/activate          # venv already exists at .venv/
pip install -r requirements.txt    # install/update deps

make html                          # build to build/html/
make clean                         # remove build/
make livehtml                      # live-reload dev server (needs sphinx-autobuild,
                                    #   not currently in requirements.txt — pip install it first)
python3 -m http.server -d build/html 8000   # serve a built site locally
```

There is no test suite or linter configured — "correctness" here means the site builds
without Sphinx warnings/errors and renders as expected.

## Architecture

- `source/conf.py` — Sphinx config: MyST + `sphinx_copybutton` + `sphinx_design`
  extensions, Furo theme, brand colors, logo/favicon. Also loads
  `source/_static/custom.css` (via `html_css_files`) for style tweaks the
  theme's `html_theme_options` can't express — currently just left-aligning
  the sidebar logo, which Furo centers by default.
- `source/index.md` — home page. Its `toctree` is the actual site nav; only pages
  listed there (directly or via a nested `toctree`) are reachable/built into the
  visible site. **When adding a new page, it must be added to a `toctree` or it
  won't appear in the sidebar.**
- **Live content**: `source/church/` is the only section currently linked from
  `index.md`. `source/church/index.md` has its own `toctree` fanning out to
  `short-guide.md`, `clergy.md`, `bells.md`, `richard-culmer.md`, `war-memorial.md`,
  `memorials-inside.md`, and `churchyard/index.md` (which itself fans out to
  `names-alphabetical.md`, `numbered-stones.md`, `survey-by-location.md`,
  `register-appendix.md` — the churchyard survey data).
- **Scaffold/placeholder content, not yet linked into the site**: `source/history/`,
  `source/people/`, `source/places.md`, `source/faq.md`, `source/timeline.md`,
  `source/sources.md`. These still contain bracketed placeholders (e.g. `[Manor Name]`,
  `[Record Office reference]`) and template guidance text left over from the initial
  scaffold. Don't treat their presence as evidence a topic is "done" — check whether
  they're wired into a `toctree` and whether the bracketed placeholders have been
  replaced with real content/citations.
- Images referenced from `history/`/`people/`/church pages sometimes point at
  `_static/images/placeholder-*.jpg` (literal grey placeholders) — replace with real
  scans before treating a page as finished. Some newer pages (e.g. `index.md`,
  `church/index.md`) instead reference images hosted externally on Cloudinary
  (`res.cloudinary.com/monkton/...`).

## Editorial conventions (from `README.md` / `PROJECT-BRIEF.md`)

- **Citations**: every factual claim gets a Markdown footnote (`[^label]` ...
  `[^label]: full citation`) linking back to `source/sources.md`, which is organized
  by record type with anchored headings (e.g. `sources.md#manorial-records`). See
  `source/history/origins.md` for the pattern, even though that page itself is
  still placeholder content.
- **Disputed facts**: where sources disagree, say so on the page (see the
  `{admonition}` "Conflicting evidence" pattern) rather than silently picking one.
- **Placeholders**: unresearched sections should stay clearly marked as placeholders
  rather than left blank or invented.
- **Images**: web-sized copies (under ~1MB) go in `source/_static/images/`;
  full-resolution originals are kept outside the repo, noted in `sources.md`. Use the
  `{figure}` directive for numbered captions.

## MyST syntax in use

- `{admonition}` (note/warning/tip), `{figure}`, `{toctree}` — core Sphinx/MyST
- `{grid}` / `{grid-item-card}` (from `sphinx_design`) — the card layouts used on
  `index.md` and section index pages like `church/index.md`
- `{dropdown}`, `:::` colon-fence directives, `{{ }}` substitutions, `- [ ]` task
  lists — enabled via `myst_enable_extensions` in `conf.py`

## Deployment

`.github/workflows/deploy.yml.example` is a template GitHub Pages workflow (build with
`sphinx-build -b html source build/html`, then `actions/deploy-pages`). It is **not**
active yet — rename/copy it to `.github/workflows/deploy.yml` to enable auto-deploy on
push to `main`. README.md and PROJECT-BRIEF.md both describe it as already active, which
is currently inaccurate.
