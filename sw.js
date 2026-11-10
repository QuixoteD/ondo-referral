/* Ondo Referral Pathways service worker (static hosting). Paths resolve against the folder the site is served from. */
const CACHE = 'orp-gh-1.0.0-draft';
const SCOPE = new URL(self.registration.scope).pathname;
const PRECACHE = ['./', 'manifest.webmanifest', 'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png']
  .map((p) => new URL(p, self.registration.scope).pathname);

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(PRECACHE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(caches.keys()
    .then((keys) => Promise.all(keys.filter((k) => k.startsWith('orp-') && k !== CACHE).map((k) => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  const isApp = req.mode === 'navigate' || url.pathname === SCOPE || url.pathname === SCOPE + 'index.html';
  if (isApp) {
    event.respondWith(fetch(req)
      .then((res) => { if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(SCOPE, copy)); } return res; })
      .catch(() => caches.match(SCOPE)));
    return;
  }
  if (PRECACHE.includes(url.pathname)) {
    event.respondWith(caches.match(url.pathname).then((hit) => hit || fetch(req)));
  }
});
