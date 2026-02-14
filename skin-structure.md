# Kodi Skin Structure Reference

**Purpose:** Quick reference for Kodi skinning concepts. Read when working with unfamiliar XML.

---

## 📦 Core File Structure

```
skin.shadow.touch/
├── addon.xml               # Skin metadata, version, dependencies
├── xml/                    # All UI window definitions
│   ├── Home.xml           # Main home screen (window ID 10000)
│   ├── MyVideoNav.xml     # Video library (10025)
│   ├── MyPVRChannels.xml  # Live TV channels (10601)
│   ├── DialogVideoInfo.xml # Info popup
│   └── ...
├── media/                  # Images, icons, textures
├── colors/                 # Color palettes (Defaults.xml, Themes.xml)
├── fonts/                  # Font definitions (Font.xml)
├── sounds/                 # Audio feedback
├── themes/                 # Color theme variants
├── language/               # Translations (English/strings.po)
└── 1080i/ or 1080p/        # Resolution-specific folders (optional)
```

---

## 🪟 Window System

Kodi uses numbered windows. Key IDs:

| Window ID | Name | XML File | Purpose |
|-----------|------|----------|---------|
| 10000 | Home | Home.xml | Main menu |
| 10025 | MyVideoNav | MyVideoNav.xml | Movies/TV library |
| 10500 | Music | MyMusicNav.xml | Music library |
| 10601 | MyPVRChannels | MyPVRChannels.xml | Live TV channels |
| 10602 | MyPVRGuide | MyPVRGuide.xml | EPG guide |
| 12005 | VideoOSD | VideoOSD.xml | Playback controls |

**Activate window:**
```xml
<onclick>ActivateWindow(10025)</onclick>  <!-- Open video library -->
```

[Full list of Window IDs](https://kodi.wiki/view/Window_IDs)

---

## 🧩 Container Types

Containers display lists of items (movies, songs, channels, etc.)

### 1. FixedList
- **Use case:** Horizontal/vertical menu with fixed visible items
- **Example:** Bottom navigation bar
```xml
<control type="fixedlist" id="9000">
    <orientation>horizontal</orientation>
    <focusposition>0</focusposition>  <!-- First item always focused -->
    <movement>3</movement>  <!-- Scroll 3 items at a time -->
</control>
```

### 2. Panel
- **Use case:** 2D grid (posters, thumbnails)
- **Example:** Movie poster wall
```xml
<control type="panel" id="50">
    <orientation>vertical</orientation>  <!-- Fill top-to-bottom, then wrap -->
    <viewtype label="Poster">icon</viewtype>
    <pagecontrol>60</pagecontrol>  <!-- Optional scrollbar ID -->
</control>
```

### 3. List
- **Use case:** Simple vertical list
- **Example:** Settings menu
```xml
<control type="list" id="3">
    <onleft>9000</onleft>  <!-- Navigate to container ID 9000 -->
    <onright>50</onright>
</control>
```

### 4. WrapList
- **Use case:** Infinite scrolling (wraps around)
- **Example:** Horizontal movie carousel

### 5. GroupList
- **Use case:** Dynamic list of grouped items
- **Example:** Settings categories

---

## 🎨 Control Types

Controls are UI elements (buttons, labels, images, etc.)

### Button
```xml
<control type="button" id="10">
    <label>Play</label>
    <onclick>PlayMedia($INFO[ListItem.FileNameAndPath])</onclick>
    <onlongclick>ActivateWindow(DialogVideoInfo)</onlongclick>
</control>
```

### Label
```xml
<control type="label">
    <label>$INFO[ListItem.Title]</label>  <!-- Dynamic text -->
    <font>font14</font>
    <textcolor>white</textcolor>
    <align>center</align>
</control>
```

### Image
```xml
<control type="image">
    <texture>$INFO[ListItem.Art(poster)]</texture>  <!-- Dynamic image -->
    <aspectratio>scale</aspectratio>  <!-- Or 'keep', 'stretch' -->
</control>
```

### Group
Organize multiple controls:
```xml
<control type="group">
    <posx>100</posx>
    <posy>200</posy>
    <!-- Child controls inherit position -->
</control>
```

---

## 🎯 Event Handlers

### Navigation Events
```xml
<onup>50</onup>        <!-- Focus container/control ID 50 when pressing UP -->
<ondown>SetFocus(60)</ondown>
<onleft>Action(Back)</onleft>
<onright>ActivateWindow(Home)</onright>
```

### Action Events
```xml
<onclick>PlayMedia()</onclick>              <!-- Single tap/click -->
<onlongclick>ActivateWindow(DialogVideoInfo)</onlongclick>  <!-- Long-press (500ms) -->
<onfocus>SetProperty(focused,true)</onfocus>
<onunfocus>ClearProperty(focused)</onunfocus>
```

---

## 🔤 Variables & Includes

### Variables.xml
Define reusable values:
```xml
<variables>
    <variable name="PosterWidth">
        <value>200</value>
    </variable>
    <variable name="ColorAccent">
        <value>FF1E90FF</value>  <!-- Format: AARRGGBB (alpha, red, green, blue) -->
    </variable>
</variables>
```

**Use in XML:**
```xml
<width>$VAR[PosterWidth]</width>
<textcolor>$VAR[ColorAccent]</textcolor>
```

### Includes.xml
Reusable XML blocks:
```xml
<includes>
    <include name="BottomNavButton">
        <control type="button" id="$PARAM[id]">
            <label>$PARAM[label]</label>
            <onclick>$PARAM[action]</onclick>
        </control>
    </include>
</includes>
```

**Use in XML:**
```xml
<include content="BottomNavButton">
    <param name="id" value="10"/>
    <param name="label" value="Home"/>
    <param name="action" value="ActivateWindow(Home)"/>
</include>
```

---

## 📊 InfoLabels

Dynamic data from Kodi (current song, movie title, etc.)

### ListItem (Current focused item)
```xml
$INFO[ListItem.Title]          <!-- Movie/song title -->
$INFO[ListItem.Plot]           <!-- Description -->
$INFO[ListItem.Art(poster)]    <!-- Poster image path -->
$INFO[ListItem.Rating]         <!-- IMDB rating -->
$INFO[ListItem.Year]           <!-- Release year -->
```

### Player (Currently playing media)
```xml
$INFO[Player.Title]
$INFO[Player.Time]             <!-- Current playback time -->
$INFO[Player.Duration]
```

### System
```xml
$INFO[System.Date]
$INFO[System.Time]
$INFO[System.CPUTemperature]
```

[Full InfoLabel list](https://kodi.wiki/view/InfoLabels)

---

## 🎨 Color System

### Color Format
`AARRGGBB` (hexadecimal)
- **AA** = Alpha (transparency): `00` = invisible, `FF` = opaque
- **RR** = Red
- **GG** = Green
- **BB** = Blue

**Examples:**
- `FFFFFFFF` = White (opaque)
- `FF000000` = Black (opaque)
- `80FFFFFF` = White (50% transparent)
- `FF1E90FF` = DodgerBlue (opaque)

### ColorDiffuse
Apply color tint to images:
```xml
<control type="image">
    <texture>button-focus.png</texture>
    <colordiffuse>FF1E90FF</colordiffuse>  <!-- Tint blue -->
</control>
```

---

## ⚡ Built-in Functions

Common actions:

### Window Management
```xml
ActivateWindow(10025)          <!-- Open video library -->
Dialog.Close(all,true)         <!-- Close all dialogs -->
Action(Back)                   <!-- Navigate back -->
```

### Playback
```xml
PlayMedia($INFO[ListItem.FileNameAndPath])
PlayerControl(Play)
PlayerControl(Stop)
Seek(-30)                      <!-- Rewind 30 seconds -->
```

### Skin Settings
```xml
Skin.SetBool(ShowWeather)      <!-- Enable boolean setting -->
Skin.ToggleSetting(DarkMode)   <!-- Toggle setting -->
Skin.SetString(HomeFocus,10)   <!-- Store string value -->
```

[Full function list](https://kodi.wiki/view/List_of_built-in_functions)

---

## 🔍 Visibility Conditions

Control when elements appear:

```xml
<visible>Player.HasMedia</visible>  <!-- Show only when media is playing -->
<visible>!String.IsEmpty(ListItem.Plot)</visible>  <!-- Show if plot exists -->
<visible>Skin.HasSetting(ShowFanart) + !Window.IsActive(Home)</visible>  <!-- AND condition -->
<visible>Player.Paused | Player.Playing</visible>  <!-- OR condition -->
```

**Operators:**
- `!` = NOT
- `+` = AND
- `|` = OR

---

## 📐 Layout Tips

### Positioning
```xml
<posx>100</posx>      <!-- X position in pixels -->
<posy>200</posy>      <!-- Y position -->
<width>400</width>
<height>300</height>
```

### Alignment
```xml
<align>left</align>           <!-- or center, right -->
<aligny>center</aligny>       <!-- vertical alignment -->
<aspectratio>keep</aspectratio>  <!-- preserve image ratio -->
```

### Padding
```xml
<textoffsetx>20</textoffsetx>  <!-- Indent text -->
<textoffsety>10</textoffsety>
```

---

## 🎬 Animations

Smooth transitions:

```xml
<animation effect="fade" time="200">WindowOpen</animation>  <!-- Fade in on open -->
<animation effect="slide" end="0,50" time="300">Focus</animation>  <!-- Slide down on focus -->
<animation effect="zoom" start="100" end="110" center="auto" time="200">Focus</animation>  <!-- Scale up -->
```

**Common effects:**
- `fade` (opacity)
- `slide` (position)
- `zoom` (scale)
- `rotate` (angle)

**Triggers:**
- `WindowOpen`, `WindowClose`
- `Focus`, `Unfocus`
- `Visible`, `Hidden`
- `Conditional` (custom condition)

---

## 🧪 Testing & Debugging

### Reload Skin
- Kodi Settings → Interface → Skin → Select different skin → Select Shadow Touch again
- Or use Debug Mode (shows control IDs on screen)

### Debug Mode
Settings → System → Logging → Enable "Enable debug logging"
- Shows control IDs overlaid on UI
- Logs to `kodi.log` file

### Common Issues

**Control not clickable:**
- Check `<visible>` conditions
- Ensure `<posx>/<posy>` are within screen bounds (0-1920, 0-1080 for 1080p)

**Navigation broken:**
- Verify `<onup>/<ondown>/<onleft>/<onright>` link to valid control IDs
- Use `SetFocus(ID)` to force focus

**Images not showing:**
- Check path: `media/icons/home.png` (relative to skin root)
- Verify file exists and is `.png` or `.jpg`

---

## 🔗 Essential Resources

- [Kodi Skin Development](https://kodi.wiki/view/Skin_development)
- [Window IDs](https://kodi.wiki/view/Window_IDs)
- [InfoLabels Reference](https://kodi.wiki/view/InfoLabels)
- [Built-in Functions](https://kodi.wiki/view/List_of_built-in_functions)
- [Kodi Forum - Skinning](https://forum.kodi.tv/forumdisplay.php?fid=12)

---

**Last Updated:** 2025-02-14
