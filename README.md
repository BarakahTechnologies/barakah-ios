# Barakah — Public Website

This repository hosts the Apple-platform public website for **Barakah**, a private baby and family care tracking app for iPhone and iPad.

The public site is deployed from this private repository at:
**https://barakah.barakahtechnologies.net/**

## Pages

| File | URL | Purpose |
|------|-----|---------|
| `index.html` | `/` | Landing page |
| `privacy.html` | `/privacy.html` | Privacy Policy |
| `support.html` | `/support.html` | Support & FAQ |

Each page also ships in `ar`/`es`/`fr`/`tr` (e.g. `index.ar.html`), linked via `hreflang` tags.

## Editing

The checked-in `.html` files are **generated** — don't hand-edit them directly, edits will be
overwritten. Shared boilerplate (head/meta/nav/footer/hreflang, per-language nav/footer strings)
lives in `build/generate.py`; translated page copy lives in `build/content/{page}.{lang}.html`.
Each page type's CSS lives once in `build/css/{page}.css` (identical across all 5 languages of
that page).

- **Change shared UI text** (nav labels, footer/copyright, lang-switcher) → edit the `UI` dict in
  `build/generate.py`.
- **Change a page's title/meta description** → edit `PAGE_META` in `build/generate.py`.
- **Change a page's actual content** for one language → edit `build/content/{page}.{lang}.html`.
- **Change styling** for a page type → edit `build/css/{page}.css`.

Then regenerate and commit the output:

```sh
python3 build/generate.py
```

## Repository and deployment privacy

Keep this GitHub repository **private**. The deployed product website is public, but visitors do
not need access to the source repository.

GitHub Pages on the organization's current plan requires a public repository, so this site should
be deployed with **Cloudflare Pages**, not GitHub Pages. Do not enable GitHub Pages for this
repository.

In **Cloudflare Dashboard → Workers & Pages**:

1. Create a Pages application and choose **Import an existing Git repository**.
2. Authorize Cloudflare for the private `BarakahTechnologies/barakah-ios` repository only.
3. Use project name `barakah-ios` and production branch `main`.
4. Select no framework preset.
5. Set the build command to `python3 build/generate.py`.
6. Set the build output directory to `.` because the generated HTML and `index.html` are in the
   repository root.
7. Deploy and confirm that the generated `*.pages.dev` address works.
8. Under **Custom domains**, add `barakah.barakahtechnologies.net`.

Add the custom domain from the Pages project and let Cloudflare create or replace its DNS record.
Remove the old record that points `barakah` to GitHub Pages.

There is intentionally no repository `CNAME` file. That file is used by branch-based GitHub Pages;
Cloudflare Pages stores custom-domain configuration in the Cloudflare project.

After the Cloudflare Pages deployment and custom domain both work, change this repository from
public to private. Doing this earlier will take the existing GitHub Pages deployment offline before
its replacement is ready.

## About Barakah

Barakah helps parents log feedings, sleep, diapers, growth measurements, medications, and milestones. Data syncs privately through iCloud — no account required, no third-party servers.

**Contact:** barakah-app@proton.me  
**© 2026 BARAKAH TECHNOLOGIES, INC.**
