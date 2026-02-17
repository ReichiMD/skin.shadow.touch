# CLAUDE.md - Shadow Touch Skin für Kodi 22

> **KRITISCH:** Diese Datei als ERSTES in jeder neuen Session lesen!

---

## 🤖 Für die KI: Rolle & Arbeitsregeln

**Du bist ein professioneller Kodi-Skin-Entwickler.**
Wir entwickeln gemeinsam den Skin `skin.shadow.touch` für **Kodi 22 (Piers)**.

**Wichtige Arbeitsregeln:**

1. **Spickzettel zuerst lesen** — `KODI22-CHEATSHEET.md` enthält verifizierte Kodi 22
   Infos. Immer dort nachschauen bevor du etwas annimmst.

2. **Dein Wissensstand ist Kodi 21** — Du kennst die Kodi 22 API nicht vollständig
   aus deinem Training. Verlasse dich nicht auf Annahmen über neue Features.

3. **Internet-Recherche: erst fragen!** — Wenn du etwas nachschlagen musst das nicht
   im Spickzettel steht, den User **vorher informieren** und Erlaubnis einholen.
   Recherche kostet viele Tokens → so sparsam wie möglich einsetzen.

4. **Neue Erkenntnisse dokumentieren** — Was du recherchierst oder herausfindest,
   direkt in `KODI22-CHEATSHEET.md` eintragen. Kein Wissen verlieren.

---

## 🎯 Projekt-Identität

**Name:** Shadow Touch
**Addon ID:** `skin.shadow.touch`
**Kodi Version:** **22 (Piers)** — `xbmc.gui 5.18.0`
**Design-Basis:** Eigenes Grundgerüst (kein Nimbus mehr!)
**Testgerät:** Google Pixel 7 (primär)

**Design-Philosophie:**
- Touch-FIRST (100% Fokus, kein TV-Kompromiss)
- Netflix/Apple TV Style
- Bottom Navigation Bar (daumenreichbar)
- Vertikales Poster-Grid
- Dunkles, minimales, modernes Design

---

## 🗂️ Projektstruktur

```
skin.shadow.touch/
├── CLAUDE.md               ← DU BIST HIER
├── KODI22-CHEATSHEET.md    ← Spickzettel: Kodi 22 Referenz
├── DESIGN.md               ← Visuelle Spezifikation
├── ROADMAP.md              ← Entwicklungsphasen
├── addon.xml               ← Kodi 22 (xbmc.gui 5.18.0)
├── xml/
│   ├── Home.xml            ← Haupt-Homescreen (CLEAN!)
│   ├── Includes.xml        ← Alle Includes registrieren
│   ├── Includes_ShadowTouch.xml  ← Grid + Bottom Nav
│   ├── Variables.xml       ← Kodi-Variablen
│   ├── Font.xml            ← Inter + remixicon
│   ├── Defaults.xml        ← Standard-Control-Stile
│   └── Dialog*.xml         ← Kodi Standard-Dialoge (Nimbus-Basis, temporär)
├── colors/
│   └── defaults.xml        ← Alle Farben (ST_* Prefix = Shadow Touch)
├── fonts/
│   ├── Inter-*.ttf         ← Schriften
│   └── remixicon.ttf       ← Icon-Font (für spätere Icons in NavBar)
└── resources/
    ├── rating_images/      ← Bewertungs-Icons (für später)
    ├── icon.png            ← Skin-Icon
    ├── fanart.png          ← Skin-Fanart
    └── settings.xml        ← Skin-Einstellungen
```

---

## 🏗️ Aktueller Aufbau (Home Screen)

```
Home.xml (Window 10000)
├── Hintergrund (id=9100)         → Einfarbig ST_BG
├── ShadowTouchVerticalGrid (id=9300)  → TMDB Helper Panel
│   └── content: popular movies (widget=True, gecacht)
│   └── onclick: Action(Info) → Kodi Standard-Info-Dialog
└── ShadowTouchBottomNav (id=9200)
    ├── Home         (id=9201) → SetFocus(9300)
    ├── Live TV      (id=9202) → ActivateWindow(TVGuide)
    ├── Bibliothek   (id=9203) → ActivateWindow(Videos,...)
    ├── Suchen       (id=9204) → ActivateWindow(Search)
    └── Einstellungen(id=9205) → ActivateWindow(Settings)
```

---

## 🎨 Farb-System (ST_ Prefix = Shadow Touch)

Alle Farben in `colors/defaults.xml` definiert.

```
ST_BG           FF0A0A0F  → Fast schwarz (Hintergrund)
ST_NAV_BG       E6060608  → Nav-Bar Hintergrund (90% schwarz)
ST_ACCENT       FF4A9FFF  → Akzentfarbe (Blau, Fokus-Highlight)
ST_TEXT         FFFAFAFA  → Primärtext (fast weiß)
ST_TEXT_DIM     80FAFAFA  → Sekundärtext (50% weiß)
ST_BORDER_FOCUS CC4A9FFF  → Poster-Rahmen fokussiert
ST_GLOW         334A9FFF  → Glow-Effekt beim Fokus
ST_NAV_FOCUS    264A9FFF  → Nav-Button Fokus-Hintergrund
ST_SEPARATOR    1AFFFFFF  → Trennlinien (10% weiß)
```

---

## ⚙️ Technische Details

### TMDB Helper (kein API-Key nötig!)
```xml
<content target="videos">
  plugin://plugin.video.themoviedb.helper/?info=popular&amp;type=movie&amp;widget=True
</content>
```
- `widget=True` = gecacht, TMDB Helper verwaltet API-Key selbst
- Kein Python-Backend nötig

### Panel Grid (id=9300)
- Item-Größe: 480×340px → 4 Spalten bei 1920px
- Poster: 460×290px
- `scrolltime tween="cubic" easing="out">250`
- `onclick`: `Action(Info)` → Kodi Standard-Info-Dialog

### Bottom Nav (id=9200)
- Höhe: 150px (groß genug für Daumen!)
- Buttons: 240×130px Touch-Target
- Fixiert am unteren Bildschirmrand

### Pixel 7 Layout (virtuell 1920×1080)
- Grid-Bereich: top=0, height=920
- NavBar: height=150, bottom=0

---

## 📚 Kodi 22 Wichtiges

→ **KODI22-CHEATSHEET.md** für alle Details!

Key Facts:
- `xbmc.gui 5.18.0` für Kodi 22 Piers
- `ListItem.IsScrolling` → existiert nicht
- `Control.IsTouching` → existiert nicht
- Inertial Scrolling → nicht per XML konfigurierbar
- Panel NICHT in Groups mit komplexen Animationen nesten!

---

## 🔗 Abhängigkeiten

| Addon | Status | Wozu |
|-------|--------|------|
| `xbmc.gui 5.18.0` | **Pflicht** | Kodi 22 API |
| TMDB Helper | User-installiert | Poster-Content |
| script.nimbus.helper | **Entfernt** | — |
| script.module.requests | **Entfernt** | — |

---

## ⚠️ Warnungen

**NICHT TUN:**
- Nimbus-Abhängigkeiten wieder hinzufügen
- `script-nimbus-*.xml` Includes in `Includes.xml` (existieren nicht!)
- Python-Backend für TMDB nutzen
- Panel in Group mit Animationen nesten

**IMMER:**
- Auf Pixel 7 testen
- `ST_` Prefix für Shadow Touch Farben
- Neues in `KODI22-CHEATSHEET.md` dokumentieren

---

## 📅 Session-Log

### Sessions 1–6 (2025–2026-02-16): Kodi 21 / Nimbus-Basis
- Gestartet mit EstuaryPVR+, dann zu Nimbus gewechselt
- Bottom Nav + Grid + Tap-Info-Dialog implementiert (Kodi 21)
- Python-Backend für TMDB API gebaut
- Getestet auf Pixel 7, MVP funktionierte

### Session 7 (2026-02-17): NEUSTART für Kodi 22 Piers
**Kontext:** Pixel 7 läuft Kodi 22 Alpha 2 → brauchen `xbmc.gui 5.18.0`

**Durchgeführt:**
- Nimbus-Abhängigkeiten entfernt (nimbus.helper, requests)
- Python-Backend entfernt (resources/lib/, default.py)
- Obsolete Docs entfernt (KNOWN_ISSUES, NIMBUS-STRUCTURE, DEVELOPMENT_NOTES)
- Nimbus Custom XMLs entfernt (Custom_110*.xml)
- Nimbus Farbthemen entfernt (18 Paletten + themes/)
- `addon.xml`: `xbmc.gui 5.18.0`
- `Home.xml`: Komplett neu, clean (nur unsere Includes)
- `Includes_ShadowTouch.xml` verbessert:
  - `widget=True` in TMDB-Pfad → gecacht, kein API-Key
  - ST_* Farben überall eingesetzt
  - 130px Nav-Button Höhe
  - `Action(Info)` statt Python-Backend
- `colors/defaults.xml`: ST_* Farb-System hinzugefügt
- `Includes.xml`: nicht-existierende script-nimbus Refs entfernt
- `KODI22-CHEATSHEET.md` erstellt
- `CLAUDE.md` komplett neu (dieses Dokument)
- `ROADMAP.md` zurückgesetzt

**Stand nach Session 7:**
- ✅ Kodi 22 kompatibel
- ✅ Home Screen: Grid + Bottom Nav (clean, kein Nimbus)
- ✅ TMDB Helper: widget=True, gecacht
- ✅ Nimbus Dialog-XMLs: bleiben als funktionierende Basis
- 📋 Nächstes: Auf Pixel 7 testen → Feedback → Anpassungen

### Session 8 (2026-02-17): Home Screen auf Pixel 7 getestet & verfeinert

**Durchgeführt:**
- Grid zentriert: 7 Spalten × 310px = 2170px, `left=115` → gleicher Rand links & rechts
- Auflösung auf 2400×1080 (20:9, echtes Pixel 7 Format) umgestellt
- Abgerundete Ecken implementiert:
  - Technik: PNG-Maske (`poster_rounded_mask.png`) über Poster gelegt
  - Transparent im Zentrum → Poster sichtbar; opak (#0A0A0F) in Ecken → abgeschnitten
  - Radius 40px (= ~18px echte Pixel auf Pixel 7)
  - **Kritische Erkenntnis:** PNG muss in `media/` liegen, nicht in `resources/`!
    Kodi löst Textur-Pfade relativ zum `media/` Ordner auf.
- `KODI22-CHEATSHEET.md` aktualisiert: Textur-Pfade + Ecken-Technik dokumentiert

**Stand nach Session 8:**
- ✅ Grid: 7 Spalten, zentriert, kein schwarzer Rand rechts
- ✅ Abgerundete Cover-Ecken (40px Radius)
- ✅ Bottom Nav: 5 Buttons, funktional
- ✅ TMDB Helper: Poster laden korrekt
- 📋 Nächstes: Info-Dialog bewerten / eigenen bauen

### Session 9 (2026-02-17): Cover-Touch in letzter Reihe gefixt

**Problem:** Tap auf Cover in der letzten Grid-Reihe funktionierte nicht.
**Ursache:** `<ondown>9201</ondown>` am Panel (id=9300) schickte den Fokus zur NavBar,
wenn am Scroll-Ende eine minimale Abwärtsbewegung des Fingers erkannt wurde.
Das Panel verlor den Fokus → Tap wurde nicht als `onclick` verarbeitet.

**Fix:** `<ondown>9300</ondown>` (Selbstreferenz, wie bereits `onup`).
NavBar bleibt per direktem Finger-Tap erreichbar.

**Durchgeführt:**
- `Includes_ShadowTouch.xml`: `ondown` von `9201` auf `9300` geändert
- `KODI22-CHEATSHEET.md`: Panel-ondown-Problem dokumentiert
- `CLAUDE.md`: Session 9 dokumentiert

**Stand nach Session 9:**
- ✅ Alle Cover-Reihen per Tap erreichbar
- ✅ NavBar weiterhin per Finger-Tap bedienbar
- 📋 Nächstes: Info-Dialog bewerten / eigenen bauen

---

### Session 10 (2026-02-17): Floating Glassmorphism NavBar

**Aufgabe:** Navigationsleiste komplett neu gestalten nach UI/UX-Spezifikation.

**Spezifikation:**
- Floating Glassmorphism Pill-Shape Tab Bar
- 4 Icons: Home, Live TV, Video-Library, Search (kein Settings mehr)
- Frosted Glass Effekt: semi-transparent dark pill + Layers
- Remixicon White-Line-Icons (Outline-Stil)
- Fokus: subtiler Glow + Alpha-Wechsel (dim → bright)

**Durchgeführt:**
- `remixicon.ttf` per Python-Stdlib inspiziert: Font v4.3, 2819 Glyphen, Codepoints ab U+EA01
- TTF-Cmap ausgelesen, Codepoints verifiziert:
  - home-line=U+EDF3, tv-line=U+F1A3, film-line=U+ECFC, search-line=U+F05C
- `media/nav_pill.png` generiert: 280×26px, radius=13 → skaliert ×5 auf 1400×130 ohne Verzerrung
- `media/nav_btn_glow.png` generiert: 80×64px, radius=32 (Button-Glow BG)
- `colors/defaults.xml`: 4 neue Pill-Farben (ST_PILL_BG, ST_PILL_SHADOW, ST_PILL_BORDER, ST_PILL_TOP)
- `xml/Font.xml`: NavIcon Font (remixicon, 46px, symbol) für Default + Arial Fontsets
- `xml/Includes_ShadowTouch.xml`: ShadowTouchBottomNav komplett neu:
  - Floating Pill 1400×130px | left=500 | bottom=40 | horizontal zentriert in 2400px
  - 4-Layer Glassmorphism: Shadow → Glass BG → Outline → Top-Highlight
  - 4 Buttons (9201-9204): icon-only per NavIcon-Font, dim/bright + Glow
  - Settings-Button (9205) entfernt
- `KODI22-CHEATSHEET.md`: Pill-Technik, Glassmorphism-Layer + Remixicon-Codepoints dokumentiert

**Wichtige Erkenntnisse:**
- Kein echter Blur in Kodi → Glassmorphism via Layer-Technik simulieren
- Pill-PNG ohne Verzerrung: gleiche Scale-Faktoren in X und Y (280×26 → ×5 → 1400×130)
- Remixicon v4.3 Codepoints via Python-Stdlib TTF-Cmap auslesbar (kein Pillow nötig!)
- `&#xXXXX;` XML-Charakter-Referenzen funktionieren in Kodi `<label>` Tags

**Stand nach Session 10:**
- ✅ Floating Glassmorphism Pill NavBar implementiert
- ✅ 4 Remixicon White-Line-Icons (home-line, tv-line, film-line, search-line)
- ✅ Glow-Fokus-Feedback: dim → bright + blauer Glow-Hintergrund
- ✅ Pill: 1400×130px, zentriert in 2400px, 40px schwebend über Rand
- 📋 Nächstes: Auf Pixel 7 testen → Icon-Größe & Pill-Radius ggf. anpassen

---

**Zuletzt aktualisiert:** 2026-02-17
**Status:** Floating Glassmorphism NavBar implementiert ✅
