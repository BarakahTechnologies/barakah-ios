#!/usr/bin/env python3
"""Generate the Barakah website: index / privacy / support in en, ar, es, fr, tr.

Shared boilerplate (head/meta/nav/footer/hreflang) lives here in ONE place, parameterized by
the UI dict below - this is what used to be copy-pasted across all 15 HTML files and drift out
of sync (e.g. the copyright-holder text needing a fix in 16 separate places). Per-language
substantive content (marketing copy, privacy policy text, support FAQ) can't be generated from
a template - only translated by hand - so it stays as verbatim fragments in content/*.html,
extracted once from the previously hand-authored pages.

Run from anywhere: `python3 build/generate.py`. Writes index.html, index.ar.html, ...,
support.tr.html into the repo root (15 files), overwriting what's there.
"""
import os

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(BUILD_DIR)
CONTENT_DIR = os.path.join(BUILD_DIR, "content")
CSS_DIR = os.path.join(BUILD_DIR, "css")

BASE = "https://barakah.barakahtechnologies.net"
LANGS = ["en", "ar", "es", "fr", "tr"]
RTL = {"ar"}
BRAND = "Barakah"
CONTACT_EMAIL = "support@barakahtechnologies.net"

# ---- per-language UI strings (shared across all three page types) --------------------------
UI = {
    "en": dict(
        native="English", dir="ltr",
        brand_aria="Barakah — home", brand_icon_alt="Barakah app icon",
        nav_aria="Primary navigation",
        nav_features="Features", nav_privacy="Privacy", nav_support="Support", nav_policy="Policy",
        lang_switch_aria="Change language",
        footer_privacy="Privacy Policy", footer_support="Support", footer_contact="Contact",
        copyright_suffix="All rights reserved.",
    ),
    "ar": dict(
        native="العربية", dir="rtl",
        brand_aria="بَرَكَة — الصفحة الرئيسية", brand_icon_alt="أيقونة تطبيق بركة",
        nav_aria="التنقل الرئيسي",
        nav_features="المزايا", nav_privacy="الخصوصية", nav_support="الدعم", nav_policy="السياسة",
        lang_switch_aria="تغيير اللغة",
        footer_privacy="سياسة الخصوصية", footer_support="الدعم", footer_contact="تواصل معنا",
        copyright_suffix="جميع الحقوق محفوظة.",
    ),
    "es": dict(
        native="Español", dir="ltr",
        brand_aria="Barakah — inicio", brand_icon_alt="Icono de la app Barakah",
        nav_aria="Navegación principal",
        nav_features="Funciones", nav_privacy="Privacidad", nav_support="Soporte", nav_policy="Política",
        lang_switch_aria="Cambiar idioma",
        footer_privacy="Política de privacidad", footer_support="Soporte", footer_contact="Contacto",
        copyright_suffix="Todos los derechos reservados.",
    ),
    "fr": dict(
        native="Français", dir="ltr",
        brand_aria="Barakah — accueil", brand_icon_alt="Icône de l'application Barakah",
        nav_aria="Navigation principale",
        nav_features="Fonctionnalités", nav_privacy="Confidentialité", nav_support="Assistance", nav_policy="Politique",
        lang_switch_aria="Changer de langue",
        footer_privacy="Politique de confidentialité", footer_support="Assistance", footer_contact="Contact",
        copyright_suffix="Tous droits réservés.",
    ),
    "tr": dict(
        native="Türkçe", dir="ltr",
        brand_aria="Barakah — ana sayfa", brand_icon_alt="Barakah uygulama simgesi",
        nav_aria="Birincil gezinme",
        nav_features="Özellikler", nav_privacy="Gizlilik", nav_support="Destek", nav_policy="Politika",
        lang_switch_aria="Dili değiştir",
        footer_privacy="Gizlilik Politikası", footer_support="Destek", footer_contact="İletişim",
        copyright_suffix="Tüm hakları saklıdır.",
    ),
}

# ---- per-page, per-language <title>/<meta description> - these can't be shared -------------
PAGE_META = {
    "index": {
        "en": ("Barakah — Private Baby Tracker",
               "Barakah is a private baby tracking app for feedings, sleep, diapers, growth, temperature, medications, milestones, and caregiver sharing."),
        "ar": ("Barakah — تطبيق خصوصي لتتبع طفلك",
               "Barakah تطبيق خاص لتتبع الرضاعة والنوم وتغيير الحفاضات والنمو ودرجة الحرارة والأدوية ومراحل التطور، مع إمكانية المشاركة مع مقدمي الرعاية."),
        "es": ("Barakah — Seguimiento privado del bebé",
               "Barakah es una app privada de seguimiento del bebé para tomas, sueño, pañales, crecimiento, temperatura, medicamentos, hitos y colaboración entre cuidadores."),
        "fr": ("Barakah — Suivi de bébé privé",
               "Barakah est une application privée de suivi de bébé pour les tétées, le sommeil, les couches, la croissance, la température, les médicaments, les étapes clés et le partage avec les proches aidants."),
        "tr": ("Barakah — Özel Bebek Takip Uygulaması",
               "Barakah; beslenme, uyku, bez değişimi, büyüme, sıcaklık, ilaçlar, gelişim aşamaları ve bakıcı paylaşımı için özel bir bebek takip uygulamasıdır."),
    },
    "privacy": {
        "en": ("Privacy Policy — Barakah",
               "Barakah privacy policy. Your data stays on your device and your private iCloud account. No third-party servers, no tracking."),
        "ar": ("سياسة الخصوصية — Barakah",
               "سياسة خصوصية Barakah. تبقى بياناتك على جهازك وفي حساب iCloud الخاص بك. بدون خوادم من جهات خارجية، وبدون تتبع."),
        "es": ("Política de privacidad — Barakah",
               "Política de privacidad de Barakah. Tus datos permanecen en tu dispositivo y en tu cuenta privada de iCloud. Sin servidores de terceros, sin rastreo."),
        "fr": ("Politique de confidentialité — Barakah",
               "Politique de confidentialité de Barakah. Vos données restent sur votre appareil et votre compte iCloud privé. Aucun serveur tiers, aucun suivi."),
        "tr": ("Gizlilik Politikası — Barakah",
               "Barakah gizlilik politikası. Verileriniz cihazınızda ve kendi özel iCloud hesabınızda kalır. Üçüncü taraf sunucu yok, takip yok."),
    },
    "support": {
        "en": ("Support — Barakah", "Get help with Barakah. FAQs, setup guides, and contact information."),
        "ar": ("الدعم — Barakah", "احصل على المساعدة بخصوص Barakah. الأسئلة الشائعة، وأدلة الإعداد، ومعلومات التواصل."),
        "es": ("Soporte — Barakah", "Obtén ayuda con Barakah. Preguntas frecuentes, guías de configuración e información de contacto."),
        "fr": ("Assistance — Barakah", "Obtenez de l'aide pour Barakah. FAQ, guides de configuration et informations de contact."),
        "tr": ("Destek — Barakah", "Barakah ile ilgili yardım alın. Sıkça sorulan sorular, kurulum rehberleri ve iletişim bilgileri."),
    },
}


def fname(page, lang):
    return f"{page}.html" if lang == "en" else f"{page}.{lang}.html"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read().rstrip("\n")


def hreflang_block(page, indent="  "):
    lines = [f'{indent}<link rel="alternate" hreflang="{l}" href="{BASE}/{fname(page, l)}" />' for l in LANGS]
    lines.append(f'{indent}<link rel="alternate" hreflang="x-default" href="{BASE}/{fname(page, "en")}" />')
    return "\n".join(lines)


def lang_menu(page, lang, indent=""):
    items = []
    for l in LANGS:
        current = ' aria-current="page"' if l == lang else ""
        items.append(f'{indent}<a href="{fname(page, l)}" lang="{l}"{current}>{UI[l]["native"]}</a>')
    return items


# ================================================================================ index.html
def render_index(lang):
    u = UI[lang]
    title, desc = PAGE_META["index"][lang]
    html_attrs = f'lang="{lang}" dir="rtl"' if lang in RTL else f'lang="{lang}"'
    lang_menu_html = "".join(lang_menu("index", lang))
    nav = (
        f'<div class="wrap nav-inner">'
        f'<a class="brand" href="{fname("index", lang)}" aria-label="{u["brand_aria"]}"> '
        f'<img class="brand-mark" src="images/icon.png" alt="{u["brand_icon_alt"]}" width="38" height="38"> '
        f'<span>{BRAND}</span> </a>'
        f'<nav class="nav-links" aria-label="{u["nav_aria"]}">'
        f'<a href="#features">{u["nav_features"]}</a> '
        f'<a href="#privacy">{u["nav_privacy"]}</a> '
        f'<a href="{fname("support", lang)}">{u["nav_support"]}</a> '
        f'<a href="{fname("privacy", lang)}">{u["nav_policy"]}</a> '
        f'<details class="lang-switch"><summary aria-label="{u["lang_switch_aria"]}">🌐 {u["native"]}</summary>'
        f'<div class="lang-menu">{lang_menu_html}</div></details></nav></div>'
    )
    content = read(os.path.join(CONTENT_DIR, f"index.{lang}.html"))
    css = read(os.path.join(CSS_DIR, "index.css"))
    return f"""<!DOCTYPE html>
<html {html_attrs}>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#45B8AC" />

  <title>{title}</title>

  <link rel="icon" type="image/png" href="images/icon.png" />
  <link rel="apple-touch-icon" href="images/icon.png" />
  <link rel="canonical" href="{BASE}/{fname("index", lang)}" />

{hreflang_block("index")}

  <style>
{css}
  </style>
</head>
<body>
<header class="nav">
{nav}
</header><main>
{content}
</main><footer>
<div class="wrap footer-inner">
<p>&copy; 2026 BARAKAH TECHNOLOGIES, INC. {u["copyright_suffix"]}</p>
<div class="footer-links"><a href="{fname("privacy", lang)}">{u["footer_privacy"]}</a> <a href="{fname("support", lang)}">{u["footer_support"]}</a> <a href="mailto:{CONTACT_EMAIL}">{u["footer_contact"]}</a></div>
</div>
</footer>
</body>
</html>"""


# ========================================================================== privacy / support
def render_inner_page(page, lang):
    """privacy.html and support.html share the same pretty-printed nav/footer shape,
    distinct from index.html's minified nav/footer - preserved as originally authored."""
    u = UI[lang]
    title, desc = PAGE_META[page][lang]
    html_attrs = f'lang="{lang}" dir="rtl"' if lang in RTL else f'lang="{lang}"'
    lang_menu_html = "\n".join(lang_menu(page, lang, indent="        "))
    support_current = ' aria-current="page"' if page == "support" else ""
    policy_current = ' aria-current="page"' if page == "privacy" else ""
    content = read(os.path.join(CONTENT_DIR, f"{page}.{lang}.html"))
    css = read(os.path.join(CSS_DIR, f"{page}.css"))
    return f"""<!DOCTYPE html>
<html {html_attrs}>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" type="image/png" href="images/icon.png">
  <link rel="apple-touch-icon" href="images/icon.png">
  <link rel="canonical" href="{BASE}/{fname(page, lang)}">

{hreflang_block(page)}
  <style>
{css}
  </style>
</head>
<body>

<header class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="{fname("index", lang)}" aria-label="{u["brand_aria"]}">
      <img class="brand-mark" src="images/icon.png" alt="{u["brand_icon_alt"]}" width="38" height="38">
      <span>{BRAND}</span>
    </a>
    <nav class="nav-links" aria-label="{u["nav_aria"]}">
      <a href="{fname("index", lang)}#features">{u["nav_features"]}</a>
      <a href="{fname("index", lang)}#privacy">{u["nav_privacy"]}</a>
      <a href="{fname("support", lang)}"{support_current}>{u["nav_support"]}</a>
      <a href="{fname("privacy", lang)}"{policy_current}>{u["nav_policy"]}</a>
      <details class="lang-switch">
        <summary aria-label="{u["lang_switch_aria"]}">🌐 {u["native"]}</summary>
        <div class="lang-menu">
{lang_menu_html}
        </div>
        </details>
    </nav>
  </div>
</header>
{content}

<footer>
  <div>
    <a href="{fname("privacy", lang)}">{u["footer_privacy"]}</a>
    <a href="{fname("support", lang)}">{u["footer_support"]}</a>
    <a href="mailto:{CONTACT_EMAIL}">{u["footer_contact"]}</a>
  </div>
  <p class="copyright">© 2026 BARAKAH TECHNOLOGIES, INC. {u["copyright_suffix"]}</p>
</footer>

</body>
</html>"""


def main():
    written = []
    for lang in LANGS:
        pages = {
            "index": render_index(lang),
            "privacy": render_inner_page("privacy", lang),
            "support": render_inner_page("support", lang),
        }
        for page, html in pages.items():
            out_path = os.path.join(SITE_DIR, fname(page, lang))
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html + "\n")
            written.append(out_path)
    print(f"wrote {len(written)} files")


if __name__ == "__main__":
    main()
