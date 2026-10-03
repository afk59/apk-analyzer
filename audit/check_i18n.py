"""Audit script 3 -- i18n key consistency.

Every key the page asks for (data-i18n / data-i18n-ph in index.html, t('...')
in the JS) must exist in all three languages, and every language must carry the
same key set. Also flags values identical to English in tr/zh (untranslated) and
placeholders ({n}) that do not survive translation.
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "app" / "web"
OUT = ROOT / "audit" / "out"

# Evaluate STRINGS with node if present, else a regex parse of the object literal.
src = (WEB / "js" / "i18n.js").read_text(encoding="utf-8")
strings = None
try:
    js = src + "\nconsole.log(JSON.stringify(STRINGS));"
    r = subprocess.run(["node", "-e", js.replace("document.", "({addEventListener(){}}).")
                        .replace("localStorage", "({getItem(){},setItem(){}})")
                        .replace("navigator.language", "'en'")],
                       capture_output=True, text=True, encoding="utf-8", timeout=30)
    if r.returncode == 0 and r.stdout.strip():
        strings = json.loads(r.stdout.strip().splitlines()[-1])
except Exception:
    pass
if strings is None:
    strings = {}
    for lang in ("en", "tr", "zh"):
        m = re.search(rf"\n  {lang}: \{{(.*?)\n  \}}", src, re.S)
        body = m.group(1) if m else ""
        strings[lang] = dict(re.findall(r"'([\w.]+)':\s*'((?:[^'\\]|\\.)*)'", body))

used = set()
html = (WEB / "index.html").read_text(encoding="utf-8")
used |= set(re.findall(r'data-i18n(?:-ph)?="([\w.]+)"', html))
for js in (WEB / "js").glob("*.js"):
    t = js.read_text(encoding="utf-8")
    used |= set(re.findall(r"\bt\(\s*'([\w.]+)'", t))
    # dynamic keys: t('stage.' + key), t('dl.' + key), t('theme.' + mode)
    for pfx in re.findall(r"\bt\(\s*'([\w.]+\.)'\s*\+", t):
        used.add(pfx + "*")

report = {"languages": {k: len(v) for k, v in strings.items()}, "missing": {}, "extra": {},
          "dynamic_prefixes": sorted(k for k in used if k.endswith("*")),
          "untranslated_same_as_en": {}, "placeholder_mismatch": []}
en = strings.get("en", {})
for lang, table in strings.items():
    miss = sorted(k for k in used if not k.endswith("*") and k not in table)
    if miss:
        report["missing"][lang] = miss
    if lang != "en":
        report["extra"][lang + "_vs_en_missing"] = sorted(set(en) - set(table))
        report["extra"][lang + "_not_in_en"] = sorted(set(table) - set(en))
        same = sorted(k for k in table if k in en and table[k] == en[k] and re.search("[A-Za-z]{4,}", en[k]))
        report["untranslated_same_as_en"][lang] = same
        for k in table:
            if k in en and set(re.findall(r"\{\w+\}", en[k])) != set(re.findall(r"\{\w+\}", table[k])):
                report["placeholder_mismatch"].append((lang, k))
# dynamic prefixes: every concrete key under the prefix used by code
code_dyn = {"stage.": ["loading", "dex", "scan", "imports", "kits", "api", "render"],
            "dl.": ["queued", "downloading", "ready", "analysing", "analysed", "failed"],
            "theme.": ["system", "light", "dark"]}
for pfx, keys in code_dyn.items():
    for lang, table in strings.items():
        for k in keys:
            if pfx + k not in table:
                report["missing"].setdefault(lang, []).append(pfx + k + " (dynamic)")
report["unused_keys_in_en"] = sorted(k for k in en if k not in used
                                     and not any(k.startswith(p[:-1]) for p in report["dynamic_prefixes"]))
(OUT / "i18n_check.json").write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps(report, indent=1, ensure_ascii=False))
