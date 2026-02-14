# Shadow Touch - Visual Design Specification

> **CRITICAL**: This document defines the EXACT visual design of Shadow Touch.
> Do NOT deviate from these specifications without explicit user approval!

**Last Updated:** 2025-02-14
**Status:** Phase 1 (Bottom Nav implemented)

---

## 🎨 Design Philosophy

**Target Aesthetic:** Netflix/Apple TV/Disney+ style streaming interface
**Platform:** Touch-first (Samsung S9 FE tablet primary, Nvidia Shield secondary)
**Theme:** Dark, minimal, modern
**Key Principle:** Touch-optimized (large targets, generous spacing)

---

## 📐 Global Specifications

### Screen Resolution
- **Target:** 1920×1080 (landscape orientation)
- **Safe Area:** 20px padding from edges (for overscan)
- **Touch Targets:** Minimum 60px (prefer 80-120px)

### Color Palette
```
Primary Background:  #000000 (pure black)
Secondary BG:        #1A1A1A (dark gray)
Focus/Accent:        button_focus (Estuary blue, ~#0E7AC7)
Text Primary:        #FFFFFF (white)
Text Secondary:      #CCCCCC (light gray)
Text Unfocused:      50-80% opacity white
Overlay Background:  #000000 @ 95% opacity
```

### Typography
- **Nav Labels:** font13 (small, under icons)
- **Headings:** font37 (medium-large)
- **Body Text:** font12-font13
- **Poster Titles:** font12

### Spacing System
```
XS:  10px  (tight gaps)
S:   20px  (standard padding)
M:   40px  (section spacing)
L:   60px  (large gaps)
XL:  120px (major sections)
```

---

## 🧩 Component Specifications

### 1. Bottom Navigation Bar

**IMPLEMENTED ✓ - DO NOT CHANGE THESE VALUES!**

#### Layout
```
Position:     bottom=0 (fixed to screen bottom)
Width:        1920px (full screen width)
Height:       120px
Background:   #000000 @ 95% opacity
Depth:        DepthBars (always on top)
```

#### Button Container
```
Type:         FixedList (horizontal orientation)
Position:     left=360px, bottom=10px
Width:        1200px (contains 4 buttons)
Height:       100px
Spacing:      0px (buttons touch each other)
```

#### Individual Buttons
```
Width:        300px (4 buttons × 300px = 1200px)
Height:       100px
Layout:       Icon (top) + Label (bottom)

Icon Size:    80×60px (centered in button)
Icon Y:       top=10px
Icon Color:
  - Unfocused: #FFFFFF @ 50% opacity
  - Focused:   #FFFFFF @ 100% opacity

Label:
  - Font:      font13
  - Position:  bottom=10px
  - Align:     center
  - Color:
    - Unfocused: #FFFFFF @ 50% opacity
    - Focused:   button_focus (blue)
```

#### Focus Indicator
```
Type:         Image (colored bar)
Position:     bottom=0px, left=50px
Width:        200px (centered under icon)
Height:       4px
Color:        button_focus (Estuary blue)
Animation:    fade in 200ms on focus
```

#### The 4 Buttons (DO NOT CHANGE ORDER!)
```
1. Home
   - Label:  "Home"
   - Icon:   icons/sidemenu/home.png
   - Action: ActivateWindow(Home)

2. Live TV
   - Label:  "Live TV"
   - Icon:   icons/sidemenu/livetv.png
   - Action: ActivateWindow(TVGuide)
   - Visibility: !Skin.HasSetting(HomeMenuNoTVButton)

3. Library
   - Label:  "Library"
   - Icon:   icons/sidemenu/movies.png
   - Action: ActivateWindow(Videos,videodb://movies/titles/,return)

4. Search
   - Label:  "Search"
   - Icon:   icons/sidemenu/search.png
   - Action: ActivateWindow(1103)
```

#### Navigation Behavior
```
onup:    9000 (old menu ID, will change to content area)
ondown:  9200 (wrap to self)
onleft:  Previous button (wrap to last)
onright: Next button (wrap to first)
```

#### Animations
```
Focus Transition:   200ms fade (sine easing)
Window Open:        300ms fade from 0% to 100%
Window Close:       200ms fade from 100% to 0%
Slide (on dialogs): 300ms slide up 90px
```

---

## 🚧 Planned Components (Not Yet Implemented)

### 2. Vertical Poster Grid (Phase 2)

**EXACT SPECS FOR FUTURE IMPLEMENTATION:**

#### Grid Container
```
Type:         Panel (2D container)
Position:     top=140px, left=20px, right=20px
Bottom:       140px (space for bottom nav)
Orientation:  vertical (wraps horizontally)
PageControl:  9500 (for pagination)
```

#### Poster Items
```
Width:        240px (poster width)
Height:       360px (poster 2:3 ratio)
Spacing:      30px horizontal, 40px vertical
Padding:      20% larger than Estuary (anti-misclick)

Unfocused:
  - Poster:   100% opacity
  - Border:   none
  - Shadow:   subtle (2px blur)

Focused:
  - Poster:   100% opacity
  - Border:   4px solid button_focus
  - Shadow:   stronger (8px blur)
  - Scale:    1.05× zoom (subtle)
  - Animation: 250ms elastic easing
```

#### Grid Layout Math
```
Screen Width:     1920px - 40px padding = 1880px usable
Poster + Spacing: 240px + 30px = 270px per column
Columns:          1880 ÷ 270 = 6.9 → 7 columns max
Actual Width:     7 × 240 + 6 × 30 = 1680 + 180 = 1860px
Centering:        (1920 - 1860) ÷ 2 = 30px left offset

Screen Height:    1080px - 140px (top) - 140px (bottom) = 800px
Row Height:       360px + 40px = 400px per row
Rows Visible:     800 ÷ 400 = 2 rows visible
```

#### Long-Press Overlay (OnLongClick)
```
Trigger:      OnLongClick (800ms hold)
Action:       Dialog.Close(all,true) +
              SetProperty(overlay.poster,$INFO[ListItem.Art(poster)])
              + ActivateWindow(DialogVideoInfo)
```

---

### 3. Long-Press Info Overlay (Phase 3)

**EXACT SPECS FOR FUTURE IMPLEMENTATION:**

#### Dialog Window
```
Type:         DialogVideoInfo.xml (custom variant)
Background:   #000000 @ 85% opacity + 20px blur
Position:     Centered modal
Width:        800px
Height:       Auto (content-dependent, max 700px)
```

#### Layout Structure
```
┌─────────────────────────────────────┐
│  [Poster]    [Title]                │
│   300×450    [Year | Rating]        │
│              [Plot text...]         │
│                                     │
│   [+ Watchlist] [✓ Mark Watched]   │
│   [▶ Play]      [× Close]          │
└─────────────────────────────────────┘
```

#### Poster
```
Width:        300px
Height:       450px (2:3 ratio)
Position:     left=40px, top=40px
Border:       2px solid button_focus
Shadow:       10px blur
```

#### Metadata Section
```
Position:     left=380px (after poster), top=40px
Width:        380px

Title:
  - Font:     font37 (large)
  - Color:    #FFFFFF
  - Max Lines: 2

Meta Info:
  - Font:     font13
  - Color:    #CCCCCC
  - Format:   "2024 | ★ 7.8 | 2h 15m"

Plot:
  - Font:     font12
  - Color:    #CCCCCC
  - Max Lines: 8
  - Scroll:   If exceeds 8 lines
```

#### Action Buttons
```
Position:     bottom=40px, centered
Width:        4 buttons × 160px = 640px
Height:       60px per button
Spacing:      20px between buttons

Button Style:
  - Background: #1A1A1A (unfocused)
  - Background: button_focus (focused)
  - Border:     2px solid button_focus
  - Border Radius: 4px
  - Font:       font13
  - Icon:       40×40px (left aligned)
  - Text:       right of icon

Buttons:
  1. "+ Watchlist"   → AddToWatchlist
  2. "✓ Watched"     → ToggleWatched
  3. "▶ Play"        → PlayMedia
  4. "× Close"       → Dialog.Close(all,true)
```

---

## 🎬 Animation Specifications

### Global Animation Rules
```
Default Fade:     200ms (sine easing)
Focus Change:     250ms (elastic easing)
Window Transitions: 300ms
Long-Press Feedback: 100ms scale down to 0.95×
```

### Bottom Nav Animations
```
WindowOpen:
  - Effect: fade
  - Start:  0%
  - End:    100%
  - Time:   300ms

WindowClose:
  - Effect: fade
  - Start:  100%
  - End:    0%
  - Time:   200ms

Focus Indicator:
  - Effect: fade
  - Start:  0%
  - End:    100%
  - Time:   200ms
  - Delay:  0ms
```

### Grid Animations (Future)
```
Poster Focus:
  - Effect: zoom + fade
  - Scale:  1.0 → 1.05
  - Border: 0px → 4px
  - Time:   250ms
  - Easing: elastic

Long-Press:
  - Effect: scale (feedback)
  - Scale:  1.0 → 0.95 → 1.0
  - Time:   100ms down, 100ms up
  - Then:   Trigger overlay
```

---

## 🔧 Technical Constraints

### Image Usage (MINIMIZE!)
```
✓ ALLOWED:
  - focus.png (simple 1×1 white texture)
  - colors/white.png (1×1 white for ColorDiffuse)
  - Icon fonts (Font Awesome, Material Icons)

❌ AVOID:
  - PNG textures (except essential icons)
  - Background images
  - Decorative graphics
  - Gradients (use ColorDiffuse instead)
```

### Performance Rules
```
- Panel max items:    500 (lazy load if more)
- Texture memory:     < 100MB total
- Animation overlap:  Max 3 simultaneous
- Scroll smoothness:  60 FPS target
```

### Touch Optimization
```
Minimum Touch Target: 60×60px
Preferred Target:     80×80px (icons)
Large Targets:        120×120px (primary actions)
Anti-Misclick:        20% extra padding on posters
Long-Press Delay:     800ms (Android standard)
```

---

## 🚫 DONT'S - Critical Design Rules

### ❌ NEVER DO THIS:
1. **Don't use side menus** (only bottom nav!)
2. **Don't use horizontal poster scrolling** (Netflix-style carousels are OUT!)
3. **Don't use small touch targets** (< 60px)
4. **Don't add decorative images** (code-first approach!)
5. **Don't create dialogs without blur background**
6. **Don't use more than 4 bottom nav buttons** (keeps it simple)
7. **Don't change bottom nav button order** (muscle memory!)
8. **Don't make focus indicators subtle** (must be obvious!)
9. **Don't use portrait orientation** (landscape only!)
10. **Don't skip animations** (feels cheap without them!)

### ✅ ALWAYS DO THIS:
1. **Use vertical grids** (thumb-friendly scrolling)
2. **Large touch targets** (80-120px)
3. **Clear focus indicators** (4px borders, underlines)
4. **Smooth animations** (200-300ms)
5. **Dark theme** (OLED-friendly blacks)
6. **Test on tablet first** (Samsung S9 FE is primary)
7. **Keep bottom nav visible** (always accessible)
8. **Use icon fonts over PNGs** (scalable, smaller)

---

## 📏 Reference Measurements

### Bottom Nav Bar (CURRENT IMPLEMENTATION)
```
Full Screen:    1920×1080

Bottom Bar:
├─ Background:  1920×120px @ y=0 (bottom)
├─ Container:   1200×100px @ x=360, y=10
│
└─ Buttons (4):
   ├─ Each:     300×100px
   ├─ Icon:     80×60px @ x=110, y=10
   ├─ Label:    font13 @ y=bottom-10
   └─ Focus:    200×4px @ x=50, y=0 (bottom)
```

### Future Grid Layout (Phase 2)
```
Content Area:   1920×800px (top=140, bottom=140)

Grid:
├─ Columns:     7
├─ Rows:        2 visible
├─ Poster:      240×360px
├─ H-Spacing:   30px
├─ V-Spacing:   40px
└─ Total Width: 1860px (centered with 30px margins)
```

---

## 🎯 Design Validation Checklist

Before implementing ANY new component, verify:

- [ ] Touch target ≥ 60px (prefer 80-120px)
- [ ] Spacing ≥ 20px between interactive elements
- [ ] Focus indicator is clearly visible (4px+ border/underline)
- [ ] Animations are 200-300ms (not instant!)
- [ ] Dark theme colors used (#000000 background)
- [ ] No unnecessary PNG textures
- [ ] Works in landscape 1920×1080
- [ ] Bottom nav bar remains accessible
- [ ] Matches Shadow Touch aesthetic (minimal, modern)

---

## 📸 Visual Reference

### Bottom Nav Bar (Current)
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    [Content Area]                           │
│                                                             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ ████████████████████████████████████████████████████████████│ ← Black bar (120px)
│                                                             │
│     [Home]     [Live TV]    [Library]    [Search]          │ ← 4 buttons (centered)
│       🏠          📺           🎬            🔍              │
│       ════                                                  │ ← Blue underline (focused)
└─────────────────────────────────────────────────────────────┘
```

### Future Grid Layout (Phase 2 - NOT YET IMPLEMENTED)
```
┌─────────────────────────────────────────────────────────────┐
│ [Top Bar - Clock/Weather]                         140px     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐              │
│   │   │ │   │ │   │ │   │ │   │ │   │ │   │    ← Row 1   │
│   └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘              │
│                                                             │
│   ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐              │
│   │   │ │   │ │ ▓ │ │   │ │   │ │   │ │   │    ← Row 2   │
│   └───┘ └───┘ └▓▓┘ └───┘ └───┘ └───┘ └───┘              │
│                 ↑ Focused (blue border)                     │
│                                                     800px   │
├─────────────────────────────────────────────────────────────┤
│ ████████████████████████████████████████████████████████████│
│     [Home]     [Live TV]    [Library]    [Search]  120px   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Update Log

### 2025-02-14 (Session 1)
- Created design specification
- Documented Phase 1 (Bottom Nav Bar) implementation
- Defined exact measurements and colors
- Added future component specs (Grid, Overlay)
- Established design rules and constraints

---

**Last Updated:** 2025-02-14
**Document Version:** 1.0
**Phase:** 1 (Bottom Nav complete)
