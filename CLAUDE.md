# CLAUDE.md - Shadow Touch Skin for Kodi

> **CRITICAL**: Read this file FIRST in every new session!
> This document contains all essential context for developing Shadow Touch.

---

## 🎯 Project Identity

**Name:** Shadow Touch
**Addon ID:** `skin.shadow.touch`
**Based On:** Nimbus (Kodi 21 Omega)
**Target Devices:**
- Google Pixel 7 (Primary testing device)
- Samsung S9 FE Tablet (Secondary, when needed)

**Design Philosophy:**
- **Touch-FIRST** (100% focus, no TV compromises!)
- Netflix/Apple TV/Disney+ style interface
- Bottom Navigation Bar (thumb-reachable)
- Vertical Poster Grid (no horizontal scrolling!)
- Long-Press Overlay for quick actions
- Dark theme, minimal, modern
- Lightweight & performant

**Design Reference:** See DESIGN.md for exact specifications!
**Visual Target:** [Image from Session 3] - Bottom Nav + Grid + Long-Press Overlay

**Later (Optional):** TV/Remote compatibility (but NOT primary focus!)

---

## 🗂️ Project Structure

```
Skin-Deep-Black/
├── CLAUDE.md           ← YOU ARE HERE (session context)
├── ROADMAP.md          ← Development phases & checkboxes
├── DESIGN.md           ← VISUAL DESIGN SPEC (exact measurements!)
├── NIMBUS-STRUCTURE.md ← Nimbus architecture reference (READ THIS!)
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
- **Keep:** Nimbus PVR features (already implemented)
- **Adapt:** Visual styling to match our dark/minimal theme
- **Retain:** EPG, recordings, channels features

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

**Current Status:** Nimbus 0.1.38 installed as base - UNMODIFIED
**Base Skin:** Pure Nimbus (no Shadow Touch modifications yet!)

**DESIGN DECISION (Session 3):** ✅ CONFIRMED
- **Option B: Full Touch Focus** (no TV/Remote optimization)
- Design from image: Bottom Nav + Vertical Grid + Long-Press Overlay
- Later optional: TV compatibility (but not primary goal)

**IMPORTANT:** Nimbus already has:
- ✅ Touch-first Netflix-style interface
- ✅ Landscape/Portrait widgets
- ✅ Full PVR support
- ✅ Modern dark theme

**What we WILL change:**
1. ✅ Replace side menu with **Bottom Navigation Bar**
2. ✅ Implement **Vertical Poster Grid** (no horizontal scrolling)
3. ✅ Add **Long-Press Overlay** (quick actions on posters)
4. ✅ Complete **German translation** (3 strings missing)
5. ✅ Touch-optimize spacing & targets (60-120px)

**What we KEEP from Nimbus:**
- ✅ PVR features (Live TV, EPG, Recordings)
- ✅ Dark theme & modern aesthetic
- ✅ Helper script (script.nimbus.helper)

**Testing Order:**
1. **Primary:** Google Pixel 7 (first test on every change)
2. **Secondary:** Samsung S9 FE Tablet (when needed)

**For Design Questions:** Always check DESIGN.md first!

---

## ⚠️ Critical Warnings

### DO NOT:
- Delete PVR-related XML files (we need that logic!)
- Remove Nimbus attribution (CC BY-SA 4.0 license!)
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
- [Nimbus Skin GitHub](https://github.com/ivarbrandt/skin.nimbus)

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
2. ✅ Read NIMBUS-STRUCTURE.md - Nimbus architecture & XML guide
3. ✅ Read ROADMAP.md to see current phase
4. ✅ **Read DESIGN.md** - EXACT visual specs (measurements, colors, layouts)
5. ✅ Check last commit message for context
6. ✅ Ask user for device testing availability before major changes

**CRITICAL:** DESIGN.md contains EXACT measurements and specs. Do NOT deviate!

---

## 📝 Notes for Future Sessions

### Session 1 (2025-02-14):
- Started with EstuaryPVR+ Omega as base
- Created full documentation structure (CLAUDE.md, ROADMAP.md, DESIGN.md, KNOWN_ISSUES.md)
- Chose name: Shadow Touch (`skin.shadow.touch`)
- Implemented Phase 1 & 2 prototype (Bottom Nav + Grid)
- Discovered critical issues during user testing
- Realized EstuaryPVR+ not optimal for Netflix-style touch UI

### Session 2 (2025-02-15):
**MAJOR DECISION:** Switched base skin from EstuaryPVR+ to Nimbus

**Reasoning:**
- Nimbus is touch-first, landscape-optimized (perfect for tablets!)
- Netflix-style design already built-in (saves ~12h work)
- Still has full PVR support (15+ PVR files like EstuaryPVR+)
- Modern code-base, less legacy cleanup needed
- Only lost ~15 minutes of code work (Phase 1+2 incomplete anyway)

**Migration Process:**
1. ✅ Backed up all documentation (CLAUDE.md, DESIGN.md, ROADMAP.md, KNOWN_ISSUES.md)
2. ✅ Deleted all EstuaryPVR+ files
3. ✅ Cloned Nimbus (v0.1.38) as new base
4. ✅ Restored documentation with updates
5. ✅ Changed addon.xml (ID: skin.shadow.touch, version: 0.0.1)
6. ✅ Created NIMBUS-STRUCTURE.md (architecture reference)

**What We Kept:**
- All documentation (updated for Nimbus)
- Design philosophy and goals
- Target devices and requirements
- GitHub workflows (.github/workflows/release.yml)

**What Changed:**
- Base skin: Nimbus instead of EstuaryPVR+
- License: CC BY-SA 4.0 (Nimbus) + GPL v2 (code parts)
- Starting fresh with better foundation!

**Status:** Nimbus installed as-is, NO modifications yet

### Session 3 (2026-02-15):
**Tasks completed:**
1. ✅ Fixed addon.xml syntax error preventing Kodi installation
   - Missing closing `>` on `<addon>` tag line 2
   - Skin now installs correctly via ZIP or manual copy
2. ✅ Clarified script.nimbus.helper dependency
   - Handles widget management, API keys, menu customization
   - Keeping it for now (provides important functionality)
3. ✅ Updated documentation to reflect TRUE current status
   - Corrected CLAUDE.md, DESIGN.md, ROADMAP.md
   - Removed misleading "IMPLEMENTED" claims
   - Clarified: Nimbus is UNMODIFIED base

**MAJOR DESIGN DECISIONS:**
4. ✅ **DECISION: Option B - Full Touch Focus!**
   - No TV/Remote optimization (that's optional later)
   - 100% focus on touch-first experience
   - Design from user-provided image confirmed as target
5. ✅ **Testing Strategy Defined:**
   - Primary: Google Pixel 7 (test first!)
   - Secondary: Samsung S9 FE Tablet (when needed)
6. ✅ **Language: German**
   - Complete all UI strings in German
   - Fix 3 missing strings in language/resource.language.de_de/strings.po
   - All skin settings menu in German

**Next Priority:**
1. Complete German translation (3 missing strings)
2. Implement Bottom Navigation Bar (replace Nimbus side menu)
3. Implement Vertical Poster Grid
4. Add Long-Press Overlay for quick actions

### Session N (add date):
- [Future sessions add notes here]

---

**Last Updated:** 2026-02-15
**Project Status:** Nimbus installed & working - Ready for user testing & evaluation
