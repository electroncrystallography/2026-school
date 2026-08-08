# Electron Crystallography School 2026

[![DOI](https://zenodo.org/badge/1328109677.svg)](https://doi.org/10.5281/zenodo.21854947)

Companion website for the **2026 Electron Crystallography School**, an IUCr
satellite school held 8–10 August 2026 at the BMO Centre in Calgary, Canada,
immediately before the 27th Congress and General Assembly of the IUCr.

Organizers: Sergi Plana Ruiz (Universitat Autònoma de Barcelona), Andrew
Stewart (University College London).

## Building the site

The site is built with [MyST Markdown](https://mystmd.org/):

```bash
npm install -g mystmd   # or: pip install mystmd
myst start              # local dev server with live reload
myst build --html       # static site in _build/html
```

The book-theme template is patched after download to replace the modal search
with a flat top-bar input and to add the organizing-body logos to the sidebar:

```bash
python3 scripts/patch_theme.py
```

Run it after any `myst build`/`myst start` that re-downloads the template (that
is, whenever `_build/` has been cleared). The deploy workflow does this
automatically.

## Deployment

Pushes to `main` trigger the GitHub Actions workflow in
`.github/workflows/deploy.yml`, which builds the site and publishes it to
GitHub Pages. One-time setup on GitHub: repository **Settings → Pages →
Source → GitHub Actions**.

## Layout

- `index.md` — landing page: what the school covered and where to start
- `agenda.md` — the three-day programme
- `instructors.md` — organizers, scientific committee, speakers
- `day1/`, `day2/`, `day3/` — one page per programme block
- `software.md` — install instructions and datasets for the practical session
- `sponsors.md` — sponsors and organizing bodies
- `assets/` — school and sponsor logos, banner artwork, instructor photos
- `style.css` — theme overrides for the MyST book-theme
- `scripts/patch_theme.py` — post-download theme patches
- `LICENSE` / `NOTICE` — CC BY 4.0, plus the third-party carve-out
- `.zenodo.json` / `CITATION.cff` — archive and citation metadata

## Adding block content

Each page in `day1/`, `day2/`, `day3/` is currently a stub carrying the block
title, time, and speaker. The plan is to convert the speakers' PPTX decks to
MyST Markdown one block at a time, watermarking the figures and carrying over
all references and citations.

## License

Text and code created for this site are licensed [CC BY 4.0](LICENSE).

Logos, sponsor marks, the banner artwork, and photographs of individuals are
**third-party material and are not covered by that license** — see [NOTICE](NOTICE)
for the full list and the terms under which each is included.

## Citing this site

Each GitHub release is archived on Zenodo. Cite the **concept DOI**, which always
resolves to the most recent version:

> Plana Ruiz, S., & Stewart, A. (2026).
> *IUCr Electron Crystallography School 2026 — companion website*. Zenodo.
> https://doi.org/10.5281/zenodo.21854947

Do **not** cite `10.5281/zenodo.21854948` — that is the version DOI pinned to
`v0.1.0` and will not follow later releases.

The two organizers are the record's **creators**; the scientific committee and
the other speakers are listed as **contributors**, so they are credited on the
Zenodo record without appearing on the citation line.

Author list and metadata for the archive live in `.zenodo.json`; `CITATION.cff`
drives GitHub's "Cite this repository" button. Both must be updated together.
