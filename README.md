# Ondo Referral Pathways - GitHub Pages test build (DRAFT)

Static copy of the app in the Drupal package, for testing on a phone over HTTPS. Same page, same DRAFT watermark.

## Publish

1. Create a repository on GitHub, for example `ondo-referral-pathways`.
2. Upload every file in this folder to the root of the repository (keep the `icons` folder and the `.nojekyll` file).
3. In the repository, open Settings > Pages. Under "Build and deployment", choose "Deploy from a branch", branch `main`, folder `/ (root)`, then Save.
4. After a minute or two the site is at `https://<your-user>.github.io/ondo-referral-pathways/`.

## Test on a phone

- Open the address in Chrome on Android. The map and list load and DRAFT shows across the screen.
- Chrome menu > "Add to home screen" or "Install app". The installed app opens full screen with its own icon.
- Open it once, switch on aeroplane mode, and open it again. It still works.
- On iPhone, use Safari > Share > "Add to Home Screen".

## Note before publishing

A GitHub Pages site is public on the internet, even when the repository is private (unless your organisation has GitHub Enterprise with private Pages). Anyone with the address can see the contact list.

## Pages (v1.1)

The single `index.html` now has four pages, addressed by hash:

- `#home`: start page with links to the three sections and the emergency numbers.
- `#guide`: referral guide taken from NAPTIP's *Guidelines on National Referral Mechanism for Protection and Assistance to Trafficked Persons in Nigeria* (2022).
- `#contacts`: the filterable contact list. "Download PDF of this list" opens the browser's print dialog; choose "Save as PDF". The sheet shows the title, the filters applied, and the filtered contacts (name and type, role, place, phone and email, services capped at 20 words).
- `#map`: the same filters on the map. The map loads only when this page is first opened.

## Decision and data-change log

- 2026-11-10: PDF sheet keeps the DRAFT watermark (contacts not yet confirmed by phone).
- 2026-11-10: PDF Services column = service labels plus concern categories, de-duplicated, capped at 20 words. No new text written.
- 2026-11-10: On the Map page with "List only what is in view" ticked, the PDF prints only the contacts in view and says so in the filter lines. Elsewhere it prints every contact matching the filters.
- 2026-11-10: Record N00-0006 (NAPTIP Ondo State Command): added address, phone 08037869287 and email infoakure@naptip.gov.ng. Source: NAPTIP website, Ondo State Command page (https://naptip.gov.ng/ondo-state-command/), read 10 November 2026. No other records changed.
- 2026-11-10: PDF sheet: 8 pt text; national helplines (with 112) printed at the top of every printout; one phone number per line; DRAFT repeated on every printed page; suggested file name `yymmdd-<filters>`, e.g. `261110-GBV-AkokoSouthWest-Specialist` (concern, place, type of contact, `Search…`, `Hid<n>` for hidden types, `MapView`; `AllOndo` when no place is chosen).
