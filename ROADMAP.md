# Shadow Touch - Entwicklungs-Roadmap

**Projekt:** Touch-optimierter Kodi 22 Skin — Google Pixel 7
**Basis:** Eigenes Grundgerüst (keine Fremdskin-Abhängigkeiten)
**Zuletzt aktualisiert:** 2026-02-17 (Session 8)

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

## ✅ Phase 2: Home Screen testen & verfeinern (ABGESCHLOSSEN — 2026-02-17)

### 2a — Erster Test auf Pixel 7
- ✅ Skin auf Pixel 7 installiert
- ✅ TMDB Helper installiert und konfiguriert
- ✅ Home Screen lädt: Grid mit Filmpostern sichtbar
- ✅ Bottom Nav: alle 5 Buttons reagieren auf Tap
- ✅ Tap auf Poster → Kodi Info-Dialog öffnet sich
- ✅ Scrollen im Grid: funktional

### 2b — Layout-Anpassungen
- ✅ Grid: 7 Spalten × 310px = 2170px (zentriert in 2400px, 115px Rand beidseitig)
- ✅ Auflösung: 2400×1080 (20:9, Pixel 7 Format)
- ✅ Abgerundete Cover-Ecken: PNG-Maske in `media/`, Radius 40px
- ✅ NavBar: 150px Höhe, gut erreichbar

### 2c — Touch-Feeling
- ✅ Scroll-Timing: 250ms cubic easing
- ✅ Fokus-Animation: Zoom 104% auf fokussiertem Cover

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
Phase 2: ██████████ 100% — ABGESCHLOSSEN
Phase 3: ░░░░░░░░░░   0% — NÄCHSTES: Info-Dialog
Phase 4: ░░░░░░░░░░   0% — Ausstehend
```
