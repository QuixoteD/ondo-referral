#!/usr/bin/env python3
"""Recompute the Content-Security-Policy in index.html.

Every inline <script> is allowed by its SHA-256 hash, so any script that is
injected later (and any edited script whose hash was not updated) is blocked.
Run after every change to a <script> block:  python3 tools/update_csp.py
"""
import base64, hashlib, pathlib, re, sys

path = pathlib.Path(__file__).resolve().parent.parent / "index.html"
html = path.read_text(encoding="utf-8")
scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
if re.search(r"<script\s+[^>]*>", html):
    sys.exit("Unexpected <script> with attributes; review the policy by hand.")
hashes = " ".join(
    "'sha256-%s'" % base64.b64encode(hashlib.sha256(s.encode("utf-8")).digest()).decode()
    for s in scripts)
policy = ("default-src 'none'; "
          f"script-src {hashes}; "
          "style-src 'unsafe-inline'; "
          "img-src 'self' data:; "
          "connect-src 'self'; "
          "manifest-src 'self'; "
          "worker-src 'self'; "
          "base-uri 'none'; "
          "form-action 'none'; "
          "object-src 'none'")
meta = f'<meta http-equiv="Content-Security-Policy" content="{policy}">'
marker = re.compile(r'<meta http-equiv="Content-Security-Policy" content="[^"]*">')
if marker.search(html):
    html = marker.sub(lambda m: meta, html, count=1)
else:
    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + meta, 1)
html = re.sub(r'<meta name="referrer" content="[^"]*">\n?', "", html)
html = html.replace(meta, meta + '\n<meta name="referrer" content="no-referrer">', 1)
path.write_text(html, encoding="utf-8")
print(f"{len(scripts)} inline scripts hashed")
