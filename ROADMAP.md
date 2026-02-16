# Shadow Touch - Development Roadmap

**Project:** Touch-optimized Kodi skin for Google Pixel 7 (primary) & Samsung S9 FE Tablet
**Timeline:** Iterative development (MVP → Full Features)
**Last Updated:** 2026-02-16

---

## 📅 Phase 0: Foundation ✅ COMPLETED

**Goal:** Setup project infrastructure and identity

- [x] Clone EstuaryPVR+ Omega base
- [x] Create CLAUDE.md (session continuity)
- [x] Create ROADMAP.md (this file)
- [x] Create skin-structure.md (Kodi concepts reference)
- [x] Rename addon.xml to `skin.shadow.touch`
- [x] Update README.md for Shadow Touch
- [x] Create development branch `claude/fresh-start-019atboB3389YWXj82W62sLt`
- [x] Initial commit & push

**Deliverable:** Clean skeleton with Shadow Touch identity ✅

---

## 📅 Phase 1: Bottom Navigation Bar ✅ COMPLETED

**STATUS:** ✅ **COMPLETED** (2026-02-16)

**Goal:** Replace Nimbus side menu with bottom-fixed navigation

**Decision Made:** Bottom Navigation Bar (touch-first design!)
- Side menu hidden (entire group with visible=false)
- Bottom Nav implemented with 5 static buttons

### Implementation Details:
- [x] Hidden Nimbus side menu (entire group at left=-540)
- [x] Created ShadowTouchBottomNav Include (xml/Includes_ShadowTouch.xml)
- [x] 5 individual buttons (NOT scrollable FixedList!):
  - Home (id=9201) @ 360px → Focus Grid
  - Live TV (id=9202) @ 600px → TVGuide
  - Library (id=9203) @ 840px → Videos Library
  - Search (id=9204) @ 1080px → Search Window
  - Settings (id=9205) @ 1320px → Kodi Settings
- [x] Styling: Text labels, focus feedback (blue background 20% opacity)
- [x] Navigation: Circular onleft/onright, onup to Grid (9300)
- [x] Touch-optimized: 240px width buttons, thumb-reachable
- [x] Tested on Google Pixel 7 → **Works!**
- [x] Cleanup: Side menu background fully removed

**Deliverable:** ✅ Bottom Nav working, 5 buttons, not scrollable, touch-friendly!

---

## 📅 Phase 2: Vertical Poster Grid ✅ COMPLETED

**STATUS:** ✅ **COMPLETED** (2026-02-16)

**Goal:** Replace Nimbus horizontal widgets with vertical poster grid

**Decision Made:** Full replacement with custom Vertical Grid!
- Nimbus widgets hidden (id="2000" - visible=false)
- Custom Panel with TMDB Helper integration

### Implementation Details:
- [x] Hidden Nimbus horizontal widgets (id="2000")
- [x] Created ShadowTouchVerticalGrid Include (xml/Includes_ShadowTouch.xml)
- [x] Panel-Container (id=9300):
  - Vertical orientation (no horizontal scrolling!)
  - Position: 100x100, Size: 1720x850px
  - Touch-optimized spacing: 20px padding
- [x] Poster tiles: 300x450px (portrait 2:3 ratio)
- [x] Item layout: 320x480px (includes spacing)
- [x] TMDB Helper content: `plugin://plugin.video.themoviedb.helper/?info=popular&type=movie`
- [x] Focus effects:
  - Unfocused: Gray border (40% opacity), white text
  - Focused: Blue border (button_focus), blue text, 105% zoom
- [x] Navigation: ondown to Bottom Nav (9201), wraps internally
- [x] Tested on Google Pixel 7 → **Visible & functional!**

**Critical Debugging:**
- Panel hierarchy issue solved (control type 7 error)
- Include registration required in Includes.xml
- Clean hierarchy: Panel at correct level (not nested in complex Groups)

**Deliverable:** ✅ Vertical Grid working, TMDB movies visible, touch-friendly!

### 2.2 Additional Details (Completed):
- [x] Cleanup: Hidden Nimbus horizontal widgets (id=2000)
- [x] Grid has full width (side menu background removed)
- [x] Touch targets tested on Pixel 7 → Confirmed working!
- [x] Custom grid implemented (replaced Nimbus widgets)

### 2.3 IF Custom Grid Needed: Panel Container Setup (ARCHIVED - Already Implemented Above)
- [ ] Replace Nimbus widget containers in Home.xml
- [ ] Create Panel container (vertical scrolling)
- [ ] Set poster size: 240x360px (2:3 ratio, per DESIGN.md)
- [ ] Enable vertical wrap (7 columns, scrolls vertically)
- [ ] Add focus animations (1.05× zoom, 4px border, shadow)
- [ ] Connect navigation (Grid ↔ Navigation)

### 2.3 IF Custom Grid Needed: Content Binding
- [ ] Bind to Movies library (library://video/movies/titles/)
- [ ] Bind to TV Shows library
- [ ] Implement "Recently Added" smart playlist
- [ ] Test scrolling (touch-friendly, no lag)

### 2.4 IF Custom Grid Needed: Poster Visuals
- [ ] Display poster image (`ListItem.Art(poster)`)
- [ ] Add subtle shadow (unfocused: 20%, focused: 40%)
- [ ] Show minimal metadata (title label below poster)
- [ ] Test with 100+ items for performance

**Deliverable:** Optimal grid layout (Nimbus widgets OR custom grid)

---

## 📅 Phase 3: Long-Press Info Overlay (Touch UX)

**Goal:** Modal info dialog triggered by long-press

### 3.1 Custom Dialog Creation
- [ ] Create `DialogVideoInfo_ShadowTouch.xml`
- [ ] Design layout: centered 600x800px modal
- [ ] Add background blur effect
- [ ] Semi-transparent black background (80% opacity)

### 3.2 Content Layout
- [ ] Large poster on left (300x450px)
- [ ] Metadata panel on right:
  - Title
  - Year, Rating, Duration
  - Plot (scrollable text)
  - Genre tags
- [ ] Action buttons at bottom:
  - Play
  - Add to Watchlist
  - Mark as Watched
  - Close

### 3.3 Event Binding
- [ ] Add `<onlongclick>` to Panel items in Home.xml
- [ ] Link to custom dialog: `ActivateWindow(DialogVideoInfo_ShadowTouch)`
- [ ] Pass `ListItem` context to dialog
- [ ] Test on tablet (long-press = 500ms hold)

**Deliverable:** Functional long-press info overlay

---

## 📅 Phase 4: PVR/Live TV Integration

**Goal:** Adapt EstuaryPVR+ screens to Shadow Touch style

### 4.1 Preserve Core PVR Logic
- [ ] Audit PVR XML files (MyPVRChannels.xml, MyPVRGuide.xml, etc.)
- [ ] Document which files contain critical logic (DON'T DELETE!)
- [ ] Map PVR windows to bottom nav "TV" button

### 4.2 Visual Restyling
- [ ] Apply dark theme to PVR screens
- [ ] Enlarge touch targets (channel list items = 80px height)
- [ ] Adapt EPG grid for touch (larger cells)
- [ ] Test Now/Next view (keep EstuaryPVR+ feature)

### 4.3 OSD Customization
- [ ] Modify VideoOSD.xml for live TV
- [ ] Keep "Last Channel" button (EstuaryPVR+ feature)
- [ ] Simplify controls (fewer buttons, bigger size)
- [ ] Test with actual PVR backend

**Deliverable:** Fully functional Live TV with touch-optimized UI

---

## 📅 Phase 5: Additional Windows & Polish

**Goal:** Complete all essential Kodi screens

### 5.1 Settings & System Windows
- [ ] Adapt Settings.xml (touch-friendly lists)
- [ ] Adapt SkinSettings.xml (Shadow Touch options)
- [ ] Adapt FileManager.xml (file browser)

### 5.2 Media Windows
- [ ] MyVideoNav.xml (Movies/TV library)
- [ ] MyMusicNav.xml (Music library)
- [ ] Pictures.xml (Photo gallery)

### 5.3 Dialogs
- [ ] DialogContextMenu.xml (right-click menu)
- [ ] DialogSeekBar.xml (video scrubbing)
- [ ] DialogVolumeBar.xml (volume slider)

**Deliverable:** Complete skin covering all Kodi functions

---

## 📅 Phase 6: Code-First Rendering (Optimization)

**Goal:** Minimize image assets, maximize Variables.xml

### 6.1 Audit Media Folder
- [ ] List all `.png` files in `media/`
- [ ] Identify which are deletable (shadows, backgrounds, gradients)
- [ ] Replace with ColorDiffuse or Variables.xml definitions

### 6.2 Variable Consolidation
- [ ] Create master color palette in Variables.xml
- [ ] Define consistent spacing units (8px grid system)
- [ ] Create reusable dimension variables

### 6.3 Performance Testing
- [ ] Benchmark memory usage (before/after)
- [ ] Test Panel scroll performance with 500+ items
- [ ] Optimize slow areas (lazy-loading if needed)

**Deliverable:** Ultra-lightweight skin with minimal textures

---

## 📅 Phase 7: Testing & Refinement

**Goal:** Real-world testing on target devices

### 7.1 Samsung S9 FE Testing
- [ ] Install on tablet via Kodi
- [ ] Test all touch gestures (tap, long-press, swipe)
- [ ] Verify grid spacing (no accidental taps)
- [ ] Check portrait mode handling (should block or show message)

### 7.2 Nvidia Shield Testing
- [ ] Install via Kodi on Shield
- [ ] Test remote navigation (D-pad)
- [ ] Verify OK button = Play, Menu = Long-press equivalent
- [ ] Check performance (should be faster than tablet)

### 7.3 Bug Fixes & Tweaks
- [ ] Fix layout issues discovered in testing
- [ ] Adjust focus behavior (sometimes D-pad gets lost in Panel)
- [ ] Polish animations (reduce jank)

**Deliverable:** Stable v1.0 release candidate

---

## 📅 Phase 8: Documentation & Release

**Goal:** Prepare for public release (optional)

### 8.1 User Documentation
- [ ] Write comprehensive README.md
- [ ] Create installation guide
- [ ] Screenshot gallery (home, PVR, overlay)
- [ ] Feature comparison (vs Estuary)

### 8.2 Code Documentation
- [ ] Comment complex XML sections
- [ ] Document Variables.xml structure
- [ ] Explain custom dialog architecture

### 8.3 Licensing & Attribution
- [ ] Maintain GPL v2 license
- [ ] Credit EstuaryPVR+ authors
- [ ] Attribute icon fonts (if used)

**Deliverable:** Publicly shareable skin (GitHub release)

---

## 🎯 MVP Milestone (Minimum Viable Product)

**To demonstrate core concept, complete:**
- ✅ Phase 0 (Foundation)
- ✅ Phase 1 (Bottom Nav)
- 🟡 Phase 2 (Vertical Grid) - 85% done, needs testing
- Phase 3 (Long-Press Overlay)

**This proves the touch-first design works!**

---

## 📊 Progress Tracking

**Overall Status:** 30% (Phase 1 + 2 COMPLETE!)

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 0 | 🟢 Complete | 100% |
| Phase 1 | 🟢 Complete | 100% (Bottom Nav with 5 buttons!) |
| Phase 2 | 🟢 Complete | 100% (Vertical Grid with TMDB!) |
| Phase 3 | ⚪ Pending | 0% (Long-Press Overlay - NEXT!) |
| Phase 4 | ⚪ Pending | 0% |
| Phase 5 | ⚪ Pending | 0% |
| Phase 6 | ⚪ Pending | 0% |
| Phase 7 | ⚪ Pending | 0% |
| Phase 8 | ⚪ Pending | 0% |

**Legend:**
- ⚪ Pending
- 🟡 In Progress / Evaluation
- 🟢 Complete
- 🔴 Blocked

---

## 🔄 Update Log

### 2025-02-14 (Session 1 - EstuaryPVR+ Base)
- Created roadmap
- Defined 8 development phases
- Identified MVP scope (Phases 0-3)
- ✅ Phase 0 completed: Foundation established
- ✅ Phase 1 completed: Bottom Navigation Bar (EstuaryPVR+ version)
- 🟡 Phase 2 started: Vertical Poster Grid (EstuaryPVR+ version)
- 🔴 **CRITICAL BUGS DISCOVERED** → Led to decision to switch base skin

### 2025-02-15 (Session 2 - Switch to Nimbus)
- **MAJOR DECISION:** Switched from EstuaryPVR+ to Nimbus
- ✅ Deleted all EstuaryPVR+ files
- ✅ Cloned Nimbus (v0.1.38) as new base
- ✅ Updated addon.xml (ID: skin.shadow.touch)
- ✅ Created NIMBUS-STRUCTURE.md
- **Result:** Clean Nimbus installation, NO Shadow Touch modifications yet

### 2026-02-15 (Session 3 - Installation Fix & Documentation Cleanup)
- ✅ Fixed addon.xml syntax error (missing `>` on line 2)
- ✅ Skin now installs correctly in Kodi
- ✅ Clarified script.nimbus.helper dependency
- ✅ Corrected all documentation to reflect TRUE status:
  - Phase 1 & 2 NOT implemented (were EstuaryPVR+, now deleted)
  - Nimbus is UNMODIFIED base
  - Next step: User testing & evaluation
- **Status:** Nimbus installed & working, ready for testing

### 2026-02-16 (Session 4 - Phase 1 + 2 COMPLETE!)
- ✅ Implemented Bottom Navigation Bar (5 buttons)
- ✅ Implemented Vertical Poster Grid (TMDB integration)
- ✅ Major debugging: Panel hierarchy, Include registration
- ✅ Cleanup: Removed side menu background
- ✅ Added Settings button to Bottom Nav
- ✅ Fixed XML syntax errors (duplicate tags)
- **Status:** Phase 1 + 2 COMPLETE! Ready for Phase 3!

---

**Last Updated:** 2026-02-16
**Status:** Phase 1 + 2 COMPLETE! Bottom Nav (5 buttons) + Vertical Grid working on Pixel 7!
