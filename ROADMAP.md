# Shadow Touch - Entwicklungs-Roadmap

**Projekt:** Touch-optimierter Kodi 22 Skin — Google Pixel 7
**Basis:** Eigenes Grundgerüst (keine Fremdskin-Abhängigkeiten)
**Zuletzt aktualisiert:** 2026-02-17

---

## ✅ Phase 0: Fundament (ABGESCHLOSSEN)
- ✅ Projektname: `skin.shadow.touch`
- ✅ Design-Philosophie definiert (Touch-FIRST, Netflix-Style)
- ✅ Testgerät: Google Pixel 7
- ✅ Kodi 22 Piers Alpha 2 auf Pixel 7

---

## ✅ Phase 1: Kodi 22 Grundgerüst (ABGESCHLOSSEN — 2026-02-17)
- ✅ `addon.xml` für Kodi 22: `xbmc.gui 5.18.0`
- ✅ Nimbus-Abhängigkeiten entfernt (helper, requests, Python)
- ✅ `Home.xml` — clean slate, nur unsere Includes
- ✅ `Includes_ShadowTouch.xml` — Grid + Bottom Nav
- ✅ ST_* Farb-System in `colors/defaults.xml`
- ✅ `KODI22-CHEATSHEET.md` als Spickzettel angelegt

---

## 📋 Phase 2: Home Screen testen & verfeinern (AKTUELL)

### 2a — Erster Test auf Pixel 7
- [ ] Skin als ZIP installieren auf Pixel 7
- [ ] TMDB Helper installiert und konfiguriert
- [ ] Home Screen lädt: Grid mit Filmpostern sichtbar
- [ ] Bottom Nav: alle 5 Buttons reagieren auf Tap
- [ ] Tap auf Poster → Kodi Info-Dialog öffnet sich
- [ ] Scrollen im Grid: flüssig, keine Ruckler

### 2b — Layout-Anpassungen (nach Test)
- [ ] Grid-Item-Größe prüfen: 480×340px — passt das auf Pixel 7?
- [ ] Spacing zwischen Items anpassen falls nötig
- [ ] NavBar-Größe prüfen: 150px — gut mit Daumen erreichbar?
- [ ] Poster-Aspect-Ratio: scale vs. stretch prüfen

### 2c — Touch-Feeling
- [ ] Scroll-Geschwindigkeit prüfen (scrolltime: 250ms)
- [ ] Fokus-Animationen (zoom 104%): zu viel? zu wenig?
- [ ] NavBar-Focus-Indikator sichtbar genug?

---

## 📋 Phase 3: Info-Dialog (als nächstes)

- [ ] Kodi Standard-Dialog (`Action(Info)`) bewerten:
  → Reicht der aus? Oder brauchen wir eigenen?
- [ ] Eigener Info-Dialog (falls nötig):
  - Poster + Titel + Jahr + Rating + Plot
  - TMDB Helper Service Monitor nutzen (kein API-Key!)
  - Deutsch
- [ ] Alternativer Ansatz: TMDB Helper eigene Detail-Seite aufrufen

---

## 📋 Phase 4: Weitere Bereiche (spätere Phasen)

### Navigation erweitern
- [ ] Live TV (TVGuide) — touch-optimiert
- [ ] Bibliothek (MyVideoNav) — touch-optimiert
- [ ] Suche — touch-optimiert

### Home Screen erweitern
- [ ] Mehrere Content-Reihen (Popular, Trending, etc.)
- [ ] Section-Header zwischen Reihen
- [ ] TV-Shows-Tab in Bottom Nav?

### Design verfeinern
- [ ] Remixicon Icons in NavBar (statt Text-Labels)
- [ ] Fanart als Grid-Hintergrund (dynamisch)
- [ ] Loading-Indikator während TMDB lädt

### Optionales (viel später)
- [ ] Deutsche Übersetzungen (language/)
- [ ] TV/Remote Kompatibilität
- [ ] Skin-Einstellungen (Akzentfarbe wählen)

---

## 📊 Aktueller Status

```
Phase 0: ██████████ 100% — ABGESCHLOSSEN
Phase 1: ██████████ 100% — ABGESCHLOSSEN
Phase 2: ░░░░░░░░░░   0% — NÄCHSTES: Pixel 7 Test
Phase 3: ░░░░░░░░░░   0% — Ausstehend
Phase 4: ░░░░░░░░░░   0% — Ausstehend
```
