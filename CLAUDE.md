# CLAUDE.md - Shadow Touch Skin for Kodi

> **CRITICAL**: Read this file FIRST in every new session!
> This document contains all essential context for developing Shadow Touch.

---

## 🎯 Project Identity

**Name:** Shadow Touch
**Addon ID:** `skin.shadow.touch`
**Based On:** EstuaryPVR+ Omega (Kodi 21.3)
**Target Devices:**
- Samsung S9 FE Tablet (Touch, Landscape 1080p)
- Nvidia Shield (Remote, Landscape 1080p)

**Design Philosophy:**
- Touch-first interface (Netflix/Apple TV style)
- Minimal/No static images (code-based rendering)
- Dark theme, modern streaming app aesthetic
- Lightweight & performant

---

## 🗂️ Project Structure

```
Skin-Deep-Black/
├── CLAUDE.md           ← YOU ARE HERE (session context)
├── ROADMAP.md          ← Development phases & checkboxes
├── DESIGN.md           ← VISUAL DESIGN SPEC (exact measurements!)
├── skin-structure.md   ← Kodi skin concepts reference
├── addon.xml           ← Skin metadata & dependencies
├── xml/                ← All UI definitions
│   ├── Home.xml        ← Main home screen
│   ├── MyPVR*.xml      ← Live TV screens
│   ├── DialogVideo*.xml ← Info overlays
│   └── ...
├── media/              ← Icons, textures (minimize usage!)
├── colors/             ← Color definitions
├── fonts/              ← Font definitions
├── themes/             ← Color themes
└── language/           ← Translations
```

---

## 🎨 Core Design Requirements

### 1. Bottom Navigation Bar
- **Location:** Fixed at bottom (not side menu)
- **Purpose:** Thumb-reachable on tablets
- **Implementation:** FixedList with horizontal orientation
- **Icons:** Font-based (Font Awesome or similar)

### 2. Vertical Grid Layout (Home)
- **Replace:** Horizontal widgets
- **Use:** Panel-Container with vertical wrapping
- **Padding:** 20% larger than default (anti-misclick)
- **Content:** Movie/TV posters in tile grid

### 3. Long-Press Overlay
- **Trigger:** OnLongClick event on poster items
- **Visual:** Centered modal dialog with blur background
- **Content:** Larger poster + metadata (plot, rating) + actions (watchlist, mark watched)
- **Implementation:** Custom DialogVideoInfo.xml variant

### 4. PVR/Live TV
- **Keep:** EstuaryPVR+ logic (already optimized)
- **Adapt:** Visual styling to dark/minimal theme
- **Retain:** Now/Next, EPG, recordings features

---

## 🛠️ Technical Constraints

### Code-First Approach
- **No PNG textures** where avoidable
- **Use:**
  - `Variables.xml` for colors/dimensions
  - `ColorDiffuse` for dynamic coloring
  - Icon fonts for symbols
  - Kodi-internal rendering (blur, shadows via XML)

### Touch Optimization
- Enlarge invisible focus containers (hit-boxes)
- Minimum 60px touch targets
- Generous spacing between interactive elements
- OnClick → Immediate action
- OnLongClick → Context menu

### Performance
- Panel-Container can lag with >500 items
- Lazy-loading for large libraries
- Minimal texture memory usage

---

## 📚 Key Kodi Concepts (Quick Reference)

See **skin-structure.md** for detailed explanations.

### Essential XML Containers
- **FixedList**: Bottom nav bar (fixed position, scrolling items)
- **Panel**: Grid layout (2D container, wrapping)
- **GroupList**: Vertical/horizontal groups
- **Group**: Visual grouping container

### Event Handlers
- `<onleft>`, `<onright>`, `<onup>`, `<ondown>`: Navigation
- `<onclick>`: Tap/Enter action
- `<onlongclick>`: Long-press action (key for touch UI!)
- `<onfocus>`: When element gets focus

### Built-in Functions
- `ActivateWindow(WindowName)`: Open window
- `Dialog.Close(all,true)`: Close dialogs
- `Skin.SetBool(VariableName)`: Set skin setting
- `Action(Back)`: Navigate back

### Variables & Includes
- `Variables.xml`: Define reusable values (colors, sizes)
- `Includes.xml`: Define reusable XML blocks
- Use `$VAR[VariableName]` and `<include>IncludeName</include>`

---

## 🚧 Current Development Phase

**Check ROADMAP.md for detailed status!**

**Last Session:** Initial setup (EstuaryPVR+ cloned, docs created)

**Next Priority:**
1. Rename addon.xml to `skin.shadow.touch`
2. Clean up EstuaryPVR+ README (create Shadow Touch specific)
3. Start Phase 1 - Bottom Nav Bar prototype

---

## ⚠️ Critical Warnings

### DO NOT:
- Delete PVR-related XML files (we need that logic!)
- Remove EstuaryPVR+ attribution (GPL license!)
- Commit without testing on target device
- Use `ActivateWindow()` without checking window IDs in code

### ALWAYS:
- Test on Samsung S9 FE (primary device)
- Maintain GPL v2 license
- Document major XML structure changes
- Keep Variables.xml organized (comment sections!)

---

## 🔗 Important Links

**Base Skin:**
- [EstuaryPVR+ Omega GitHub](https://github.com/SplitEnz/skin.estuary.pvr.plus.omega)

**Kodi Documentation:**
- [Skin Development Docs](https://kodi.wiki/view/Skin_development)
- [Window IDs](https://kodi.wiki/view/Window_IDs)
- [Built-in Functions](https://kodi.wiki/view/List_of_built-in_functions)
- [InfoLabels](https://kodi.wiki/view/InfoLabels)

**Touch Events:**
- Long-press requires `<onlongclick>` in control definition
- Test thoroughly - behavior varies by Android version

---

## 🧠 Session Checklist for New AI

When starting a new session, DO THIS:

1. ✅ Read this file (CLAUDE.md)
2. ✅ Read ROADMAP.md to see current phase
3. ✅ **Read DESIGN.md** - EXACT visual specs (measurements, colors, layouts)
4. ✅ Check last commit message for context
5. ✅ Review skin-structure.md if working with unfamiliar XML
6. ✅ Ask user for device testing availability before major changes

**CRITICAL:** DESIGN.md contains EXACT measurements and specs. Do NOT deviate!

---

## 📝 Notes for Future Sessions

### Session 1 (2025-02-14):
- Cloned EstuaryPVR+ Omega as base
- Created documentation structure (CLAUDE.md, ROADMAP.md, skin-structure.md, DESIGN.md)
- Chose name: Shadow Touch (`skin.shadow.touch`)
- Base skin has extensive PVR features already (good!)

**Phase 1 COMPLETE:** Bottom Navigation Bar
  - 4 buttons: Home, Live TV, Library, Search
  - Fixed horizontal bar at bottom (120px height)
  - Touch-optimized (300×100px buttons)
  - Old side menu disabled (visible=false)

**Phase 2 PARTIAL:** Vertical Poster Grid
  - Panel container created (ID 6100, 7×2 layout)
  - Poster items: 240×360px with focus animations
  - Content binding: library://video/movies/titles/
  - Navigation: Grid ↔ Bottom Nav connected

**Documentation Created:**
  - DESIGN.md: Complete visual specification (colors, measurements, layouts)
  - KNOWN_ISSUES.md: Critical bugs and solutions for v0.0.2
  - .github/workflows/release.yml: GitHub Actions for ZIP releases
  - .gitignore: Exclude ZIP packages from git

**CRITICAL ISSUES DISCOVERED (User Testing):**
  1. ❌ No Settings button in Bottom Nav → User locked out of settings!
  2. ❌ Vertical Grid not showing → Home screen shows old widgets
  3. ⚠️ Side menu disabled but no alternative navigation

**Root Causes Identified:**
  - Missing 5th button (Settings) in Bottom Nav (only 4 buttons)
  - No `<defaultcontrol>` set in Home.xml → Grid never gets focus
  - Group 2000 (old widgets) may have conflicting visibility conditions
  - User cannot access Kodi settings without side menu or Settings button

**Solutions Documented in KNOWN_ISSUES.md:**
  - Fix 1: Add Settings button (5th button, 1500px width, 210px left offset)
  - Fix 2: Set `<defaultcontrol always="true">6100</defaultcontrol>`
  - Fix 3: Completely remove Group 2000 instead of just hiding it
  - Workarounds: Use Kodi remote app, Android back button, or switch skins temporarily

**Installation Issues Resolved:**
  - GitHub repo ZIP has wrong folder name (Skin-Deep-Black-claude-...)
  - Created proper Kodi addon ZIP with correct structure (skin.shadow.touch/)
  - Added GitHub Actions workflow for automatic release ZIPs (triggered by tags)
  - User successfully installed on Pixel 7 (Kodi 21.2)

**Testing Platform:** Google Pixel 7 (Android, Kodi 21.2 Omega)

**Status:** v0.0.1-alpha released, critical bugs prevent usage, fixes ready for v0.0.2

### Session N (add date):
- [Future sessions add notes here]

---

**Last Updated:** 2025-02-14
**Project Status:** Initial Setup Phase
