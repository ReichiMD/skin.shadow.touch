# Known Issues - Shadow Touch v0.0.1

> **Status:** Alpha Development (Phase 2 incomplete)
> **Last Updated:** 2025-02-14

---

## 🚨 Critical Issues (Blocks Usage)

### 1. No Access to Settings ⚠️ CRITICAL

**Problem:**
- Bottom Navigation Bar has only 4 buttons: Home, Live TV, Library, Search
- **No Settings button** → User cannot access Kodi Settings
- Old side menu (which had Settings) was disabled (`<visible>false</visible>`)
- User is locked out of system configuration

**Impact:**
- Cannot configure skin settings
- Cannot add/remove widgets (if using old Estuary system)
- Cannot access system settings
- Cannot change display settings

**Root Cause:**
- File: `xml/Home.xml` line 1578
- Bottom Nav `id="9200"` only has 4 items
- Side menu `id="9000"` was disabled (line 1118: `<visible>false</visible>`)

**Proposed Solutions:**

#### Option A: Add 5th Button to Bottom Nav (RECOMMENDED)
```xml
<!-- In xml/Home.xml, Bottom Nav content section -->
<item>
    <label>Settings</label>
    <onclick>ActivateWindow(Settings)</onclick>
    <thumb>icons/sidemenu/settings.png</thumb>
    <visible>true</visible>
</item>
```

**Changes needed:**
- Line 1573: Change width from `1200px` to `1500px` (5 buttons)
- Line 1571: Change left from `360px` to `210px` (recenter)
- Each button: 300px × 5 = 1500px total
- Update focusedlayout/itemlayout width (keep at 300px per button)

#### Option B: Long-Press Home Button Opens Settings
```xml
<!-- In Home button item -->
<onlongclick>ActivateWindow(Settings)</onlongclick>
```

**Trade-off:** Less discoverable, requires user to know about long-press

#### Option C: Re-enable Side Menu (PARTIAL)
```xml
<!-- In xml/Home.xml, line 1118 -->
<visible>Control.HasFocus(9200) | Window.IsActive(Settings)</visible>
```

**Trade-off:** Defeats purpose of touch-first design, but provides fallback

---

### 2. Vertical Grid Not Showing

**Problem:**
- Home screen shows old Estuary widgets (horizontal scrolling)
- New vertical poster grid (Group 6000, Panel 6100) is not visible
- User reports "looks like before"

**Impact:**
- Phase 2 (Vertical Grid) appears non-functional
- Touch-optimized poster wall is not usable
- Defeats main design goal

**Root Cause (Suspected):**

#### Possible Cause A: Group 2000 Not Properly Disabled
- File: `xml/Home.xml` line 38
- Group 2000 has `<visible>false</visible>` BUT
- May have conditional visibility that overrides this
- Check line 51: `<visible>String.IsEqual(Container(9000).ListItem.Property(id),movies)</visible>`

#### Possible Cause B: No Default Focus Set
- Grid Panel `id="6100"` exists but is never focused
- Home.xml may not have `<defaultcontrol>6100</defaultcontrol>` set
- Kodi defaults to first visible control (probably old widget system)

#### Possible Cause C: Group 6000 Visibility Condition
- Line 1110: Group 6000 has `<visible>true</visible>` (correct)
- But may be hidden by parent group conditions
- May conflict with old menu focus conditions

**Diagnostic Steps:**

1. Check Kodi debug log:
   ```
   Settings → System → Logging → Enable debug logging
   Restart Kodi
   Check: /sdcard/Android/data/org.xbmc.kodi/files/.kodi/temp/kodi.log
   Search for: "Control 6100" or "Group 6000"
   ```

2. Check if Grid is loaded but hidden:
   - Use Kodi's "Developer Options" → "Show Control IDs"
   - Navigate to Home
   - See if any controls show ID 6100 or 6000

3. Test manual focus:
   - Enable Kodi remote control (Settings → Services → Control)
   - Use JSON-RPC: `{"jsonrpc":"2.0","method":"Input.ExecuteAction","params":{"action":"SetFocus(6100)"},"id":1}`
   - If Grid appears → visibility issue. If not → loading issue.

**Proposed Solutions:**

#### Solution A: Set Default Control (QUICK FIX)
```xml
<!-- In xml/Home.xml, after <window> tag -->
<defaultcontrol always="true">6100</defaultcontrol>
```

Add this at line ~35 (right after `<window>` tag, before first `<control>`)

#### Solution B: Remove Conflicting Visibility Conditions
```xml
<!-- In xml/Home.xml, Group 2000 (line 38) -->
<!-- FIND all nested <visible> tags and ensure they're ALL false -->

<!-- Line 51, Group 5000: -->
<visible>false</visible>  <!-- Force disable, ignore Container conditions -->
```

#### Solution C: Force Grid Visibility
```xml
<!-- In xml/Home.xml, Group 6000 (line 1107) -->
<animation effect="fade" start="100" end="100" condition="true">Conditional</animation>
<visible>true</visible>
<depth>DepthContentPanel</depth>  <!-- Ensure proper rendering layer -->
```

---

### 3. Navigation Locked to Grid

**Problem:**
- If Grid is focused, user can navigate within grid (arrow keys)
- But may not be able to escape to Bottom Nav (Down key)
- Bottom Nav can navigate back to Grid (Up key) BUT
- If Grid is not visible, Bottom Nav has nowhere to go

**Impact:**
- User stuck in one control
- Cannot access other parts of UI

**Root Cause:**
- File: `xml/Home.xml` line 1123
- Grid Panel: `<ondown>9200</ondown>` (correct)
- Bottom Nav: `<onup>6100</onup>` (line 1578, correct)
- BUT: If 6100 is not visible/loaded, navigation breaks

**Proposed Solutions:**

#### Solution A: Fallback Navigation
```xml
<!-- Bottom Nav, line 1578 -->
<onup condition="Control.IsVisible(6100)">6100</onup>
<onup condition="!Control.IsVisible(6100)">SetFocus(2000)</onup>
```

#### Solution B: Always Keep Grid Loaded
```xml
<!-- Grid Group 6000 -->
<visible>true</visible>
<include>visible_fade</include>  <!-- Fade in/out instead of hide -->
```

---

## ⚠️ Medium Issues (Impacts UX)

### 4. No Content in Grid (Empty Library)

**Problem:**
- Grid may be visible but empty if user has no movies in Kodi library
- Content path: `library://video/movies/titles/`
- If library is empty → blank screen

**Proposed Solutions:**

#### Solution A: Show Placeholder
```xml
<!-- Add empty state label -->
<control type="label">
    <visible>String.IsEmpty(Container(6100).NumItems)</visible>
    <label>No movies in library. Add movies via Settings → Media → Videos</label>
</control>
```

#### Solution B: Alternative Content Source
```xml
<!-- Use file browser instead -->
<content target="videos">sources://video/</content>
```

---

### 5. Bottom Nav Hidden When Dialogs Open

**Problem:**
- Line 1555 (Bottom Nav Group): Animation slides down when dialogs open
- `<animation effect="slide" end="0,-90" ... condition="$EXP[infodialog_active]">`
- User loses navigation when info dialogs appear

**Proposed Solutions:**

#### Solution A: Remove Slide Animation
```xml
<!-- Delete or comment out line 1555-1556 -->
<!-- <animation effect="slide" end="0,-90" ... </animation> -->
```

#### Solution B: Keep Partially Visible
```xml
<!-- Change slide to only 50px instead of 90px -->
<animation effect="slide" end="0,-50" ... />
```

---

## 🔧 Minor Issues (Polish)

### 6. Missing Icons for Bottom Nav

**Problem:**
- Bottom Nav references icons like `icons/sidemenu/search.png`
- Some icons may be missing or not optimized for bottom nav

**Solution:**
- Check if all icons exist in `media/icons/sidemenu/`
- Create new icons if needed (80×60px PNG, white fill)

---

### 7. No Long-Press Functionality Yet

**Problem:**
- Grid posters do not have `<onlongclick>` implemented
- Phase 3 (Long-Press Overlay) not started

**Status:**
- Expected behavior - Phase 3 not implemented yet
- Document for next session

---

## 🎯 Workarounds for v0.0.1 Users

### Accessing Settings Without Settings Button:

**Method 1: Kodi Remote Control**
1. Enable: Settings → Services → Control → Allow remote control
2. Use smartphone app (Kore, Yatse) to navigate to Settings

**Method 2: System Back Button**
1. Press Android Back button → Opens Kodi menu
2. Navigate to Settings from there

**Method 3: Re-enable Side Menu Temporarily**
1. Edit `xml/Home.xml`
2. Line 1118: Change `<visible>false</visible>` to `<visible>true</visible>`
3. Restart Kodi
4. Side menu reappears with Settings button

**Method 4: Switch to Different Skin**
1. Install Estuary or Confluence skin
2. Configure settings
3. Switch back to Shadow Touch

---

## 📋 Priority Fix List for v0.0.2

**Must Fix (Blocks Usage):**
1. ✅ Add Settings button to Bottom Nav (5 buttons total)
2. ✅ Set `<defaultcontrol>6100</defaultcontrol>` in Home.xml
3. ✅ Verify Group 2000 visibility is fully disabled

**Should Fix (UX):**
4. ⬜ Add empty state for Grid (when no movies)
5. ⬜ Test navigation flow (Grid ↔ Bottom Nav)
6. ⬜ Remove Bottom Nav slide animation on dialogs

**Nice to Have:**
7. ⬜ Add Settings icon to media/icons/
8. ⬜ Improve Grid focus animations
9. ⬜ Start Phase 3 (Long-Press Overlay)

---

## 🔍 How These Would Be Fixed (Technical Details)

### Fix 1: Add Settings Button (15 minutes)

**File:** `xml/Home.xml`

**Step 1:** Update Bottom Nav container dimensions
```xml
<!-- Line 1571-1573 -->
<left>210</left>          <!-- Was: 360 -->
<width>1500</width>       <!-- Was: 1200 -->
```

**Step 2:** Add Settings item
```xml
<!-- After Search item (around line 1680) -->
<item>
    <label>Settings</label>
    <onclick>ActivateWindow(Settings)</onclick>
    <thumb>icons/sidemenu/settings.png</thumb>
    <visible>true</visible>
</item>
```

**Step 3:** Update button spacing math
```
New layout:
- 5 buttons × 300px = 1500px total width
- Center: (1920 - 1500) / 2 = 210px left offset
- Buttons: Home | Live TV | Library | Search | Settings
```

---

### Fix 2: Set Default Focus (5 minutes)

**File:** `xml/Home.xml`

**Location:** After `<window>` tag (around line 35)

```xml
<window>
    <defaultcontrol always="true">6100</defaultcontrol>

    <!-- Existing content starts here -->
    <animation effect="fade" ...>
```

**Explanation:**
- `always="true"` ensures Grid gets focus even if previously focused control was different
- `6100` is the Panel container ID for Vertical Grid
- This forces Kodi to show the Grid on Home screen load

---

### Fix 3: Nuclear Option - Completely Remove Group 2000 (10 minutes)

Instead of `<visible>false</visible>`, delete entire Group 2000 section.

**File:** `xml/Home.xml`

**Delete lines 36-1104:**
```xml
<!-- DELETE FROM: -->
<control type="group" id="2000">
    ...
    (1068 lines of old widget code)
    ...
</control>
<!-- DELETE TO HERE -->
```

**Benefits:**
- No conflicts with visibility conditions
- Reduces XML file size (87KB → ~50KB)
- Cleaner codebase

**Risks:**
- Cannot revert to old widgets without re-adding code
- May break if other files reference Group 2000

---

## 🧪 Testing Checklist for v0.0.2

After fixes are applied, test:

- [ ] Install from ZIP (no errors)
- [ ] Activate skin (no crashes)
- [ ] Home screen loads showing Grid (not old widgets)
- [ ] Bottom Nav shows 5 buttons including Settings
- [ ] Can navigate: Grid → Down → Bottom Nav
- [ ] Can navigate: Bottom Nav → Up → Grid
- [ ] Can navigate: Bottom Nav → Left/Right between buttons
- [ ] Settings button opens Settings window
- [ ] Grid shows movie posters (if library has movies)
- [ ] Grid scrolling works (vertical)
- [ ] Focus animations work (zoom, border)
- [ ] No XML errors in kodi.log

---

## 📸 Expected vs Actual Behavior

### Expected (Design Intent):
```
┌─────────────────────────────────────┐
│  [Movie Posters - 7×2 Grid]        │  ← SHOULD SEE THIS
│  ┌───┐ ┌───┐ ┌───┐ ┌───┐ ...      │
│  └───┘ └───┘ └───┘ └───┘           │
├─────────────────────────────────────┤
│ [Home] [TV] [Library] [Search] [⚙] │  ← SHOULD HAVE 5 BUTTONS
└─────────────────────────────────────┘
```

### Actual (v0.0.1 Bug):
```
┌─────────────────────────────────────┐
│  [Old Estuary Horizontal Widgets]  │  ← WRONG! OLD SYSTEM
│  ← Movie Widget →                   │
│  ← TV Shows Widget →                │
├─────────────────────────────────────┤
│ [Home] [TV] [Library] [Search]     │  ← MISSING SETTINGS!
└─────────────────────────────────────┘
```

---

**Last Updated:** 2025-02-14
**Version:** 0.0.1-alpha
**Status:** Development (MVP 50% complete)
