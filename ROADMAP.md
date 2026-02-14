# Shadow Touch - Development Roadmap

**Project:** Touch-optimized Kodi skin for Samsung S9 FE & Nvidia Shield
**Timeline:** Iterative development (MVP → Full Features)

---

## 📅 Phase 0: Foundation ✅ IN PROGRESS

**Goal:** Setup project infrastructure and identity

- [x] Clone EstuaryPVR+ Omega base
- [x] Create CLAUDE.md (session continuity)
- [x] Create ROADMAP.md (this file)
- [ ] Create skin-structure.md (Kodi concepts reference)
- [ ] Rename addon.xml to `skin.shadow.touch`
- [ ] Update README.md for Shadow Touch
- [ ] Create development branch `claude/kodi-skin-assessment-mG29G`
- [ ] Initial commit & push

**Deliverable:** Clean skeleton with Shadow Touch identity

---

## 📅 Phase 1: Bottom Navigation Bar (MVP Core)

**Goal:** Replace side menu with bottom-fixed navigation

### 1.1 Home.xml Modification
- [ ] Remove default side menu (vertical FixedList)
- [ ] Create bottom FixedList (horizontal, y=1020)
- [ ] Define 4 main buttons: Home, TV, Library, Search
- [ ] Style buttons: icon + label (minimalist)
- [ ] Test navigation (left/right works, onclick activates)

### 1.2 Icon Integration
- [ ] Research icon font options (Font Awesome / Material Icons)
- [ ] Add icon font to `fonts/` directory
- [ ] Define font in `Font.xml`
- [ ] Map icons to labels in `Variables.xml`

### 1.3 Focus & Animation
- [ ] Create focus texture (subtle glow or underline)
- [ ] Add smooth transitions (FadeTime=200)
- [ ] Test touch response (tap switches focus → activates)

**Deliverable:** Working bottom nav bar with 4 functional buttons

---

## 📅 Phase 2: Vertical Grid Layout (Home Content)

**Goal:** Replace horizontal widgets with vertical tile grid

### 2.1 Panel Container Setup
- [ ] Replace default widget containers in Home.xml
- [ ] Create Panel container (vertical orientation)
- [ ] Set poster size: 200x300px (with 20% padding = ~240px spacing)
- [ ] Enable vertical wrap (fill screen top-to-bottom, then right)

### 2.2 Content Binding
- [ ] Bind to Movies library (`Container.Content`)
- [ ] Bind to TV Shows library
- [ ] Implement "Recently Added" smart playlist
- [ ] Test scrolling (touch-friendly, no lag)

### 2.3 Poster Visuals
- [ ] Display poster image (`ListItem.Art(poster)`)
- [ ] Add subtle shadow (ColorDiffuse or overlay texture)
- [ ] Show minimal metadata (title overlay on focus)
- [ ] Test with 100+ items for performance

**Deliverable:** Home screen with scrollable poster grid

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
- Phase 1 (Bottom Nav)
- Phase 2 (Vertical Grid)
- Phase 3 (Long-Press Overlay)

**This proves the touch-first design works!**

---

## 📊 Progress Tracking

**Overall Status:** 5% (Foundation underway)

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 0 | 🟡 In Progress | 60% |
| Phase 1 | ⚪ Pending | 0% |
| Phase 2 | ⚪ Pending | 0% |
| Phase 3 | ⚪ Pending | 0% |
| Phase 4 | ⚪ Pending | 0% |
| Phase 5 | ⚪ Pending | 0% |
| Phase 6 | ⚪ Pending | 0% |
| Phase 7 | ⚪ Pending | 0% |
| Phase 8 | ⚪ Pending | 0% |

**Legend:**
- ⚪ Pending
- 🟡 In Progress
- 🟢 Complete
- 🔴 Blocked

---

## 🔄 Update Log

### 2025-02-14 (Session 1)
- Created roadmap
- Defined 8 development phases
- Identified MVP scope (Phases 0-3)

---

**Last Updated:** 2025-02-14
