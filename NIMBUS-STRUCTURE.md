# NIMBUS-STRUCTURE.md - Nimbus Skin Architecture Reference

> **Purpose:** Quick reference for understanding Nimbus structure when developing Shadow Touch.
> **Read this** when modifying XML files or implementing new features!

---

## 📁 File Overview (121 XML Files Total)

### **Critical Files (READ FIRST!):**

| File | Lines | Purpose |
|------|-------|---------|
| `xml/Home.xml` | 1266 | Main home screen (widgets, menu, navigation) |
| `xml/Includes.xml` | 2068 | Reusable XML blocks (most important!) |
| `xml/Variables.xml` | 759 | Color/dimension/string variables |
| `xml/Defaults.xml` | ? | Default control definitions |

### **Window Files (Main Screens):**

| File | Purpose | Touch-Relevant? |
|------|---------|-----------------|
| `MyVideoNav.xml` | Video library browser | ✅ YES (poster grid!) |
| `MyMusicNav.xml` | Music library browser | ⚠️ Low priority |
| `MyPVR*.xml` | Live TV screens (15 files) | ✅ YES (keep as-is!) |
| `Custom_1100_AddonLauncher.xml` | Addon launcher window | ⚠️ Maybe |
| `Custom_1107_SearchDialog.xml` | Search window | ✅ YES (touch!) |
| `Custom_1121_SearchResults.xml` | Search results | ✅ YES |

### **Dialog Files (Overlays):**

| File | Purpose | Touch-Relevant? |
|------|---------|-----------------|
| `DialogVideoInfo.xml` | Movie/TV show info dialog | ✅ YES (long-press!) |
| `DialogPVR*.xml` | PVR dialogs (9 files) | ✅ YES (keep as-is!) |
| `DialogContextMenu.xml` | Context menu | ✅ YES (touch menus) |
| `DialogButtonMenu.xml` | Button menu | ✅ YES |

---

## 🏗️ Nimbus Architecture

### **Widget System (Home Screen):**

Nimbus uses a **complex widget system** with:
- **Landscape widgets:** Horizontal posters (16:9)
- **Portrait widgets:** Vertical posters (2:3)
- **Square widgets:** Square tiles (1:1)
- **PVR widgets:** Live TV widgets

**Widget Types:**
```xml
<!-- Home.xml structure (simplified) -->
<window id="10000">
  <controls>
    <!-- Top bar overlay (logo, clock, etc.) -->
    <include>TopBarOverlay</include>

    <!-- Main menu (vertical side menu) -->
    <control type="fixedlist" id="9000">
      <!-- Menu items: Home, Movies, TV, Music, etc. -->
    </control>

    <!-- Widget containers (one per menu item) -->
    <control type="group" id="10000">
      <!-- Home widgets -->
    </control>
    <control type="group" id="10001">
      <!-- Movies widgets -->
    </control>
    <!-- ... etc -->
  </controls>
</window>
```

**Important:** Widgets are **dynamically loaded** via `script.nimbus.helper`!

---

## 🎨 Variables & Theming

### **Key Variables (Variables.xml):**

| Variable | Purpose | Example Value |
|----------|---------|---------------|
| `ColorHighlight` | Accent color | Theme-dependent |
| `ColorText` | Primary text color | `FFFFFFFF` (white) |
| `ColorTextDim` | Secondary text | `99FFFFFF` (dim white) |
| `SideMenuWidth` | Side menu width | `540` (pixels) |
| `WidgetPosterHeight` | Poster widget height | `360` |
| `WidgetLandscapeHeight` | Landscape widget height | `240` |

**Color Themes:** 16 themes in `colors/` directory (e.g., "Altitude Blue", "Shock Pink")

---

## 🧩 Includes System

### **Key Includes (Includes.xml):**

| Include Name | Purpose |
|--------------|---------|
| `TopBarOverlay` | Top bar with logo, clock, weather |
| `WidgetLandscape` | Landscape widget layout |
| `WidgetPortrait` | Portrait widget layout |
| `WidgetSquare` | Square widget layout |
| `PVRWidget` | Live TV widget layout |
| `ButtonCommon` | Common button style |
| `FocusAnimation` | Focus animation effect |

**Usage:**
```xml
<include>TopBarOverlay</include>
<include content="WidgetLandscape">
  <param name="id" value="6000"/>
</include>
```

---

## 📺 PVR Integration

### **PVR Files (DO NOT DELETE!):**

Nimbus has **15 PVR-related XML files** (same as EstuaryPVR+):
- `DialogPVRChannelGuide.xml`
- `DialogPVRChannelManager.xml`
- `DialogPVRChannelsOSD.xml`
- `DialogPVRGroupManager.xml`
- `DialogPVRGuideControls.xml`
- `DialogPVRGuideSearch.xml`
- `DialogPVRInfo.xml`
- `DialogPVRRadioRDSInfo.xml`
- `Includes_PVR.xml`
- `MyPVRChannels.xml`
- `MyPVRGuide.xml`
- `MyPVRRecordings.xml`
- `MyPVRSearch.xml`
- `MyPVRTimers.xml`
- `VideoOSD.xml` (also used for PVR playback)

**DO NOT MODIFY** these unless absolutely necessary!

---

## 🔧 Helper Script Dependency

### **script.nimbus.helper (v0.0.50):**

Nimbus **requires** this helper script for:
- Widget management (loading content)
- Ratings integration (IMDb, TMDb, Trakt, etc.)
- Search functionality
- Addon launcher features

**Important:**
- This is in `addon.xml` dependencies
- **Keep it** unless we remove widget features
- Later we can fork it or remove it

---

## 🎯 Key Differences from EstuaryPVR+

| Feature | EstuaryPVR+ | Nimbus |
|---------|-------------|--------|
| **Design** | Kodi Standard | Netflix-style |
| **Touch** | Not optimized | Touch-first |
| **Widgets** | Horizontal | Landscape + Portrait |
| **Side Menu** | Left side | Left side (same) |
| **PVR** | PVR-first | PVR-included |
| **Helper Script** | None | script.nimbus.helper |
| **Complexity** | Medium | High (121 XMLs!) |

---

## 🚧 Modification Strategy for Shadow Touch

### **What to KEEP (Don't touch!):**
- ✅ All PVR files (`DialogPVR*.xml`, `MyPVR*.xml`)
- ✅ Helper script dependency (for now)
- ✅ Includes_PVR.xml (PVR logic)
- ✅ VideoOSD.xml (playback controls)

### **What to MODIFY:**
- 🔧 `Home.xml` - Change navigation to bottom nav
- 🔧 `MyVideoNav.xml` - Adjust poster grid layout
- 🔧 `DialogVideoInfo.xml` - Add long-press support
- 🔧 `Variables.xml` - Add Shadow Touch colors/sizes

### **What to ADD:**
- ➕ Bottom navigation container (in Home.xml)
- ➕ Vertical poster grid (in Home.xml or MyVideoNav.xml)
- ➕ Long-press overlay (custom dialog or modify DialogVideoInfo.xml)

---

## 📖 Recommended Reading Order for New Sessions

1. ✅ Read CLAUDE.md (project context)
2. ✅ Read DESIGN.md (exact visual specs)
3. ✅ Read this file (NIMBUS-STRUCTURE.md)
4. ✅ Read ROADMAP.md (current phase)
5. ✅ Check last commit message

**This saves ~500 tokens per session!**

---

## 🔍 Quick XML Location Guide

**Need to modify...** | **Edit this file:**
---------------------|-------------------
Bottom navigation | `Home.xml`
Poster grid | `Home.xml` or `MyVideoNav.xml`
Long-press overlay | `DialogVideoInfo.xml`
Colors/themes | `Variables.xml`, `colors/defaults.xml`
Button styles | `Includes.xml` (search for `ButtonCommon`)
PVR/Live TV | **DON'T TOUCH!** (unless user requests)
Settings menu | `Custom_1101_SettingsList.xml`

---

## 💡 Token-Saving Tips

**Instead of reading entire files:**
1. Use `grep` to search for specific controls (e.g., `grep -n "id=\"9000\"" xml/Home.xml`)
2. Read specific line ranges (e.g., `sed -n '100,200p' xml/Home.xml`)
3. Refer to this document for structure overview

**Common Control IDs:**
- `9000` = Main menu (side menu)
- `6000-6999` = Widget containers
- `10000+` = Window groups

---

**Last Updated:** 2025-02-15
**Nimbus Version:** 0.1.38
**Shadow Touch Version:** 0.0.1
