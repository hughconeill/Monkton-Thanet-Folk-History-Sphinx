# Project Brief

*This file is the first thing a new contributor or maintainer should
read. Keep it short and current — update it when key decisions change.*

## What this project is

A documentation website recording the history of [village name],
built with Sphinx and hosted on GitHub Pages. Content is written in
Markdown and lives in the `source/` folder.

## Scope

- **Geographic area covered:** [define the boundary — parish,
  village, hamlet included/excluded]
- **Time period:** [earliest date] to [present / a cutoff date]
- **What's included:** history, notable people, places, photographs
- **What's out of scope:** [e.g. living persons' current addresses,
  unverified family trees without a source]

## Editorial standards

- **Citations:** every factual claim gets a footnote citing a source
  listed in `source/sources.md`. See that file's bottom section for
  the exact syntax.
- **Placeholders:** unresearched sections should stay clearly marked
  as placeholders (see the admonition style used in `index.md`) rather
  than left silently blank or invented.
- **Disputed facts:** where sources disagree, say so on the page —
  don't quietly pick one version.

## Images

- Store web-sized copies (under ~1MB) in `source/_static/images/`.
- Keep full-resolution originals outside the repo (external drive,
  family archive, etc.) — note where in `sources.md`.
- Every image needs a caption with source/date/contributor, even if
  approximate.

## How the site is built and published

- Source files: Markdown in `source/`, built with Sphinx
  (MyST parser + Furo theme).
- On every push to `main`, a GitHub Actions workflow
  (`.github/workflows/deploy.yml`) automatically builds the site and
  publishes it to GitHub Pages. No manual deploy step.
- To preview changes locally before pushing, see `README.md` for
  setup and `make html` / `make livehtml` instructions.

## Handover notes

*Fill this in as the project matures — who to contact, where original
documents/photos are physically stored, any accounts (GitHub, domain
name if used) and who holds the credentials.*

- Repository: [GitHub URL]
- Original documents/photos held by: [name/organization]
- Contact for questions: [name/email]
