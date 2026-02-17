# Kodi 22 (Piers) - Skin Developer Cheatsheet
> Dieses Dokument wächst mit dem Projekt. Nur relevante, verifizierte Infos.
> Letzte Aktualisierung: 2026-02-17

---

## ⚡ Kritisches: Kodi 21 → 22 Migration

### addon.xml Versionssprung
```xml
<!-- Kodi 21 Omega -->
<import addon="xbmc.gui" version="5.17.0" />

<!-- Kodi 22 Piers ← WICHTIG! -->
<import addon="xbmc.gui" version="5.18.0" />
```

### Versionsübersicht
| Kodi | Codename | xbmc.gui |
|------|----------|----------|
| 20   | Nexus    | 5.15.0   |
| 21   | Omega    | 5.17.0   |
| **22**   | **Piers**    | **5.18.0**   |

---

## 📦 TMDB Helper Integration

### Widget-Pfade (Content für Panel/List Container)
```xml
<!-- Populäre Filme (gecacht, kein API-Key nötig!) -->
<content target="videos">
  plugin://plugin.video.themoviedb.helper/?info=popular&amp;type=movie&amp;widget=True
</content>

<!-- Weitere Content-Pfade -->
plugin://plugin.video.themoviedb.helper/?info=top_rated&amp;type=movie&amp;widget=True
plugin://plugin.video.themoviedb.helper/?info=trending_day&amp;type=movie&amp;widget=True
plugin://plugin.video.themoviedb.helper/?info=trending_week&amp;type=movie&amp;widget=True
plugin://plugin.video.themoviedb.helper/?info=popular&amp;type=tv&amp;widget=True
plugin://plugin.video.themoviedb.helper/?info=airing_today&amp;type=tv&amp;widget=True
```

> **Wichtig:** `&` in XML = `&amp;` | `widget=True` = gecacht, performanter

### Service Monitor aktivieren
```xml
<!-- Skin-Setting setzen (z.B. in SkinSettings.xml oder per Button) -->
<onclick>Skin.SetBool(TMDbHelper.Service)</onclick>
```
Dann im XML auf Fenster-Properties zugreifen:
```xml
$INFO[Window(Home).Property(TMDbHelper.ListItem.Title)]
$INFO[Window(Home).Property(TMDbHelper.ListItem.Plot)]
$INFO[Window(Home).Property(TMDbHelper.ListItem.Rating)]
$INFO[Window(Home).Property(TMDbHelper.ListItem.clearlogo)]
```

### Blur-Hintergrund für Dialoge
```xml
SetProperty(TMDbHelper.Blur.SourceImage,Art(poster)|Art(fanart),Home)
<!-- Zugriff: -->
$INFO[Window(Home).Property(TMDbHelper.ListItem.BlurImage)]
```

---

## 🖐️ Touch auf Android (Pixel 7)

### Was Kodi per XML kann
```xml
<onclick>...</onclick>          <!-- Tap -->
<onlongclick>...</onlongclick>  <!-- Long-Press (ACHTUNG: auf Panel-Items mit Plugin-Content
                                     überschreibt Kodi dies mit eigenem Kontextmenü!) -->
```

### Was NICHT skin-konfigurierbar ist
- **Inertial Scrolling** → Hardcoded in C++ (`GUIBaseContainer.cpp`)
- **Touch-Deadzone** → Android-Systemebene, nicht per Skin
- **`ListItem.IsScrolling`** → EXISTIERT NICHT in Kodi 22
- **`Control.IsTouching`** → EXISTIERT NICHT in Kodi 22

### Scroll-Timing konfigurieren (das Einzige was geht)
```xml
<scrolltime tween="cubic" easing="out">250</scrolltime>
```
Tween-Optionen: `linear`, `quadratic`, `cubic`, `sine`, `back`, `circle`, `bounce`
Easing-Optionen: `in`, `out`, `inout`

### Touch-Target Mindestgröße
- **Minimum:** 60px (Android-Standard)
- **Empfohlen:** 80-100px für sichere Touch-Bedienung auf Phones
- **Shadow Touch NavBar:** 130px Höhe für Thumb-Bedienung

### Long-Press Problem
Long-press auf Panel-Items mit Plugin-Content → Kodi öffnet Standard-Kontextmenü, kein `<onlongclick>`
→ **Lösung:** `<onclick>Action(Info)</onclick>` am Panel (Tap = Info, long-press = Kontextmenü)

---

## 🎨 Farb-System (ARGB Format)

```
FF = volle Deckkraft    80 = 50%     40 = 25%     1A = 10%
```

Beispiele:
```xml
<color name="ST_BG">FF0A0A0F</color>        <!-- Fast schwarz -->
<color name="ST_ACCENT">FF4A9FFF</color>    <!-- Blau -->
<color name="ST_TEXT">FFFAFAFA</color>      <!-- Fast weiß -->
<color name="ST_TEXT_DIM">80FAFAFA</color>  <!-- 50% transparent weiß -->
```

---

## 📐 Layout: Pixel 7 (1920×1080 virtuell)

```
Bildschirm:  1920 × 1080px (virtuell, 16:9)
Echter Screen: 2400 × 1080px (20:9) → Kodi nutzt 1920 default res

NavBar:     1920 × 150px (unten)
Grid-Area:  1920 × 930px (0 bis 930)
Item-Grid:  4 Spalten × 480px = 1920px (mit Padding)
```

---

## 🧱 Wichtige Control-Typen

### Panel (Grid)
```xml
<control type="panel" id="9300">
  <orientation>vertical</orientation>
  <scrolltime tween="cubic" easing="out">250</scrolltime>
  <preloaditems>3</preloaditems>
  <itemlayout width="480" height="340">...</itemlayout>
  <focusedlayout width="480" height="340">...</focusedlayout>
  <content target="videos">plugin://...</content>
</control>
```
> **WARNUNG:** Panel NICHT in Groups mit komplexen Animationen nesten!
> Kodi wirft "unsupported control type 7" → Panel direkt unter `<controls>`

### Button (Nav)
```xml
<control type="button" id="9201">
  <texturefocus colordiffuse="ST_NAV_FOCUS">colors/white.png</texturefocus>
  <texturenofocus>-</texturenofocus>
  <textcolor>ST_TEXT_DIM</textcolor>
  <focusedcolor>ST_ACCENT</focusedcolor>
</control>
```

---

## 🪄 Animationen

```xml
<!-- Fade beim Fokus -->
<animation effect="fade" start="0" end="100" time="150">Focus</animation>
<animation effect="fade" start="100" end="0" time="150">UnFocus</animation>

<!-- Zoom beim Fokus (Poster Scale-up) -->
<animation effect="zoom" start="100" end="104" time="150" tween="sine" easing="out">Focus</animation>
<animation effect="zoom" start="104" end="100" time="150" tween="sine" easing="out">UnFocus</animation>

<!-- Fenster-Animationen -->
<animation effect="fade" start="0" end="100" time="300">WindowOpen</animation>
<animation effect="fade" start="100" end="0" time="200">WindowClose</animation>
```

---

## 🔧 Nützliche Built-in Funktionen

```xml
Action(Info)                                    <!-- Info-Dialog für fokussiertes Item -->
SetFocus(9300)                                  <!-- Fokus auf Control setzen -->
ActivateWindow(Settings)                        <!-- Kodi Einstellungen -->
ActivateWindow(TVGuide)                         <!-- Live TV Guide -->
ActivateWindow(Search)                          <!-- Suche -->
ActivateWindow(Videos,videodb://movies/titles/) <!-- Filmsbibliothek -->
Skin.SetBool(SettingName)                       <!-- Skin-Einstellung aktivieren -->
Skin.ToggleSetting(SettingName)                 <!-- Skin-Einstellung umschalten -->
```

---

## 📋 Neue InfoLabels in Kodi 22 (relevant für uns)

```xml
$INFO[ListItem.ChannelLogo]         <!-- PVR Kanal-Logo Pfad -->
$INFO[VideoPlayer.ChannelLogo]      <!-- Aktuell spielender Kanal Logo -->
$INFO[ListItem.ParentalRatingIcon]  <!-- Altersfreigabe Icon -->
```

**Audio Codec neue Werte** (für spätere Badge-Anzeige):
- `dtshd_ma_x` (DTS:X)
- `eac3_ddp_atmos` (Dolby Atmos)
- `truehd_atmos`

---

## 🖼️ Textur-Pfade in Kodi Skins (KRITISCH!)

**Kodi löst Textur-Pfade relativ zum `media/` Ordner auf, NICHT zum Skin-Root!**

```xml
<!-- XML-Referenz:   colors/white.png          -->
<!-- Physischer Pfad: skin.shadow.touch/media/colors/white.png  -->

<!-- XML-Referenz:   poster_rounded_mask.png   -->
<!-- Physischer Pfad: skin.shadow.touch/media/poster_rounded_mask.png -->
```

**Regel:** Alle Skin-Bilder (PNG, etc.) gehören in `media/` oder einen Unterordner davon.
- `media/colors/white.png` → XML: `colors/white.png` ✓
- `media/poster_rounded_mask.png` → XML: `poster_rounded_mask.png` ✓
- `resources/poster_rounded_mask.png` → XML: `resources/poster_rounded_mask.png` ✗ (Kodi findet es nicht!)

### Abgerundete Ecken (Poster/Cover in Panel itemlayout)

Technik: PNG-Maske über dem Poster (transparent = Poster sichtbar, opak = Ecke abschneiden)

```xml
<itemlayout width="310" height="450">
    <!-- 1. Poster -->
    <control type="image">
        <texture background="true">$INFO[ListItem.Art(poster)]</texture>
    </control>
    <!-- 2. Ecken-Maske (MUSS in media/ liegen!) -->
    <control type="image">
        <texture>poster_rounded_mask.png</texture>  <!-- liegt in media/ -->
        <aspectratio>stretch</aspectratio>
    </control>
</itemlayout>
```

PNG-Maske erzeugen (Python, nur stdlib):
- Transparent (0,0,0,0) im gerundeten Rechteck-Bereich → Poster scheint durch
- Opak (R,G,B,255) in den Ecken → Hintergrundfarbe überdeckt Ecken
- Radius 40px empfohlen (= ~18px echte Pixel auf Pixel 7)

---

## 📁 Minimale Skin-Dateistruktur (Kodi 22)

Absolut nötig für funktionierenden Skin:
```
addon.xml                   ← xbmc.gui 5.18.0
xml/
  Font.xml                  ← Pflicht
  Defaults.xml              ← Pflicht
  Includes.xml              ← Pflicht (kann weitere includen)
  Variables.xml             ← Pflicht (darf leer sein)
  Home.xml                  ← Window 10000
  DialogBusy.xml            ← Pflicht (Kodi hängt sonst)
  DialogConfirm.xml         ← Pflicht
  DialogKeyboard.xml        ← Pflicht (Suche, Eingaben)
  DialogNotification.xml    ← Pflicht
  DialogSelect.xml          ← Pflicht
  DialogNumeric.xml         ← Pflicht
  Settings.xml              ← Pflicht
  VideoFullScreen.xml       ← Pflicht (Videoplayer)
  VideoOSD.xml              ← Pflicht (Videoplayer OSD)
  FileBrowser.xml           ← Pflicht
colors/
  defaults.xml              ← Farbdefinitionen
fonts/
  *.ttf                     ← Schriftdateien
```

---

## 📱 Spezielle Touch-Optimierungen (Kodi 22 Fokus)

### 1. Präzision & Treffsicherheit
- **Hitbox-Erweiterung (`<hitrect>`):** Nutze dieses Tag, um die klickbare Fläche über die sichtbare Grafik hinaus zu vergrößern. Besonders wichtig für kleine Icons.
  ```xml
  <control type="button">
      <width>60</width>
      <height>60</height>
      <hitrect x="-20" y="-20" width="100" height="100" /> </control>

  Adaptive Scrollbars: Verbreitere Scrollbalken automatisch, wenn ein Touch-Gerät erkannt wird.

  <width condition="System.HasInput(touch)">40</width>
<width condition="!System.HasInput(touch)">10</width>

Gestik & Interaktion
Long-Press Support: Nutze das neue Kodi 22 Tag für Kontextmenüs oder Zusatzinfos per langem Fingerdruck.

<onlongclick>ActivateWindow(ContextMenu)</onlongclick>

Haptisches Feedback (Visuell): Minimale Latenz-Kompensation durch extrem kurze Animationen (Sofort-Reaktion bei Berührung).

<animation effect="zoom" start="100" end="95" time="50" condition="Control.HasFocus(ID)">Conditional</animation>

Neue Bedingungen (Conditions)
System.HasInput(touch): Prüft, ob ein Touchscreen aktiv ist.
ListItem.IsScrolling: Erlaubt es, visuelle Effekte während des Wischens auszublenden, um die Performance zu erhöhen.

Ergänzung der Dateistruktur
Zusätzlich zu den Standard-Dateien sollte für Touch-Skins folgendes vorhanden sein:
xml/Pointer.xml: Definiert das Aussehen des Cursors/Touch-Indikators (verhindert Grafikfehler auf Android).
xml/Touchscreen.xml: (Optional) Mappt globale Gesten (wie 2-Finger-Tap für "Back").

---

## 🔗 Referenzen

- [Kodi 22 Skinning Changes](https://kodi.wiki/view/Changes_To_The_Skinning_Engine)
- [Kodi Skin Development Docs](https://kodi.wiki/view/Skin_development)
- [Window IDs](https://kodi.wiki/view/Window_IDs)
- [InfoLabels](https://kodi.wiki/view/InfoLabels)
- [Built-in Functions](https://kodi.wiki/view/List_of_built-in_functions)
- [TMDB Helper Wiki](https://github.com/jurialmunkey/plugin.video.themoviedb.helper/wiki/)
- [TMDB Helper Skinners Forum](https://forum.kodi.tv/showthread.php?tid=345847)
