# Shadow Touch - Development Roadmap

**Project:** Touch-optimized Kodi skin for Samsung S9 FE & Nvidia Shield
**Timeline:** Iterative development (MVP → Full Features)

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

## 📅 Phase 1: Bottom Navigation Bar (MVP Core)

**STATUS:** ⚠️ UNDER EVALUATION
**Current Nimbus:** Has vertical side menu (Netflix-style) on LEFT side

**Goal:** Decide if we replace side menu with bottom-fixed navigation

**IMPORTANT:** Nimbus already has a working touch-optimized side menu!
- Test it first before deciding to replace it
- Bottom nav might not be necessary if side menu works well

### 1.1 FIRST: Evaluate Nimbus Side Menu
- [ ] Test Nimbus side menu on Samsung S9 FE tablet
- [ ] Check if it's thumb-reachable in landscape
- [ ] Evaluate touch responsiveness
- [ ] Compare with bottom nav design goals
- [ ] **DECIDE:** Keep side menu OR implement bottom nav?

### 1.2 IF Bottom Nav Needed: Home.xml Modification
- [ ] Remove Nimbus side menu (vertical FixedList id="9000")
- [ ] Create bottom FixedList (horizontal, y=1020)
- [ ] Define 4 main buttons: Home, TV, Library, Search
- [ ] Style buttons: icon + label (minimalist)
- [ ] Test navigation (left/right works, onclick activates)

### 1.3 IF Bottom Nav Needed: Icon Integration
- [ ] Research icon font options (Font Awesome / Material Icons)
- [ ] Add icon font to `fonts/` directory
- [ ] Define font in `Font.xml`
- [ ] Map icons to labels in `Variables.xml`

### 1.4 IF Bottom Nav Needed: Focus & Animation
- [ ] Create focus texture (subtle glow or underline)
- [ ] Add smooth transitions (FadeTime=200)
- [ ] Test touch response (tap switches focus → activates)

**Deliverable:** Working navigation (bottom OR keep Nimbus side menu)

---

## 📅 Phase 2: Grid Layout (Home Content)

**STATUS:** ⚠️ UNDER EVALUATION
**Current Nimbus:** Has landscape + portrait widgets (Netflix-style)

**Goal:** Decide if Nimbus widget layout needs modification

**IMPORTANT:** Nimbus already has poster grids!
- Landscape widgets (horizontal posters, 16:9)
- Portrait widgets (vertical posters, 2:3)
- Test them first before rebuilding!

### 2.1 FIRST: Evaluate Nimbus Widgets
- [ ] Test Nimbus widget layouts on Samsung S9 FE
- [ ] Check if widgets scroll vertically or horizontally
- [ ] Measure poster sizes and spacing
- [ ] Test touch targets (too small? accidental taps?)
- [ ] **DECIDE:** Keep Nimbus widgets OR create custom grid?

### 2.2 IF Custom Grid Needed: Panel Container Setup
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

**Overall Status:** 10% (Nimbus installed, ready for evaluation!)

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 0 | 🟢 Complete | 100% |
| Phase 1 | 🟡 Evaluation | 10% (Nimbus has side menu - testing needed) |
| Phase 2 | 🟡 Evaluation | 10% (Nimbus has widgets - testing needed) |
| Phase 3 | ⚪ Pending | 0% |
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

---

**Last Updated:** 2026-02-15
**Status:** Nimbus 0.1.38 base installed - Ready for user testing to evaluate what needs modification
