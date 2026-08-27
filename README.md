# The History of Monkton — Sphinx Documentation Site

A Sphinx documentation site for a village history project, written in
**Markdown** (via [MyST](https://myst-parser.readthedocs.io/)) with
the [Furo](https://pradyunsg.me/furo/) theme. Pre-populated with
sample content for a fictional village ("Monkton") so you can see
how the layout, image captions, and source citations work — replace
the placeholder text and images with your own research.

## Project layout

```
docs-site/
├── requirements.txt      # Python dependencies
├── Makefile / make.bat   # Build commands
└── source/
    ├── conf.py           # Sphinx configuration
    ├── index.md          # Home page
    ├── about.md           # About the project / how to contribute
    ├── history/            # Chronological chapters
    │   ├── index.md
    │   ├── origins.md
    │   ├── the-mill.md
    │   └── twentieth-century.md
    ├── timeline.md         # Quick-reference date table
    ├── people/              # One page per notable person/family
    │   ├── index.md
    │   └── example-resident.md
    ├── places.md            # Landmarks and buildings
    ├── gallery.md           # Photo gallery
    ├── sources.md           # Master bibliography — see below
    ├── faq.md
    ├── _static/images/    # Photos and scans go here (currently grey
    │                       # placeholder JPGs — swap these out)
    ├── _static/custom.css # Site-wide CSS overrides (loaded via html_css_files)
    └── _templates/         # Custom HTML template overrides (optional)
```

## Working with sources and images

- **Every factual claim should cite a source.** Pages use Markdown
  footnotes (`[^label]` ... `[^label]: full citation`) that link back
  to the master list in `sources.md`. See `history/origins.md` for an
  example.
- **`sources.md` is organized by record type** (parish registers,
  census, oral histories, etc.) with anchored headings, so you can
  link straight to a section, e.g. `sources.md#oral-histories`.
- **Images** live in `source/_static/images/`. Keep web-sized copies
  (under ~1MB) in the repo and store full-resolution originals
  elsewhere — note where in `sources.md`. Reference them with the
  `{figure}` directive (adds a numbered caption) as shown throughout
  the `history/` and `people/` pages.

## Setup

1. Create a virtual environment (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Build the site

```bash
make html
```

The built site will be in `build/html/index.html` — open it directly in
a browser, or serve it locally:

```bash
python3 -m http.server -d build/html 8000
```

Then visit `http://localhost:8000`.

## Live-reloading dev server (optional but recommended)

Install `sphinx-autobuild` once:

```bash
pip install sphinx-autobuild
```

Then run:

```bash
make livehtml
```

This opens a local server that automatically rebuilds and refreshes
your browser whenever you save a file — much faster for writing.

## Adding new pages

1. Create a new `.md` file (e.g. `source/guides/new-topic.md`).
2. Add it to the relevant `toctree` — e.g. in `source/guides/index.md`:

   ```markdown
   ```{toctree}
   :maxdepth: 1

   example-guide
   new-topic
   ```
   ```

3. Rebuild (`make html`).

## Useful MyST Markdown syntax

- **Admonitions**: `` ```{note} `` / `{warning}` / `{tip}` blocks
- **Tabs**: `` :::{tab-set} `` + `` :::{tab-item} Label `` (needs `sphinx-design`)
- **Cards/grids**: `` :::{grid-item-card} `` (needs `sphinx-design`)
- **Dropdowns**: `` ```{dropdown} Title ``
- **Cross-references**: plain Markdown links, e.g. `[Getting Started](getting-started.md)`
- **Task lists**: `- [ ] todo` / `- [x] done`

Full syntax reference: https://myst-parser.readthedocs.io/en/latest/syntax/typography.html

## Customizing the theme

Edit `html_theme_options` in `source/conf.py` — colors, adding a GitHub
link ("source_repository"), sidebar behavior, etc. Full option list:
https://pradyunsg.me/furo/customisation/

To add a logo or favicon, drop the image file in `source/_static/` and
uncomment the `html_logo` / `html_favicon` lines in `conf.py`.

For tweaks the theme options don't cover, `source/_static/custom.css`
is loaded on every page via `html_css_files` in `conf.py`. It currently
just left-aligns the sidebar logo (Furo centers it by default) —
add further overrides there rather than editing the theme itself.

## Publishing via GitHub Pages (automatic)

This repo includes `.github/workflows/deploy.yml`, which builds and
publishes the site automatically on every push to `main`.

One-time setup after pushing to GitHub:
1. Go to the repo's **Settings → Pages**.
2. Under "Build and deployment", set **Source** to **GitHub Actions**.
3. Push to `main` (or re-run the workflow from the **Actions** tab) —
   the site will be live at `https://<username>.github.io/<repo-name>/`.

After that, there's no manual deploy step: edit a page, commit, push,
and the live site updates in a minute or two.

## Deploying

Common free options:
- **Read the Docs** — connect your git repo, it builds automatically on push.
- **GitHub Pages** — build with `make html`, then publish `build/html/`
  (e.g. via a GitHub Action or the `gh-pages` branch).
- **Netlify / Vercel** — set the build command to
  `pip install -r requirements.txt && sphinx-build -b html source build/html`
  and the publish directory to `build/html`.
