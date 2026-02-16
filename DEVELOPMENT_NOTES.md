# Development Notes - Critical Learnings for Future Sessions

**Purpose:** This document contains CRITICAL technical insights from debugging sessions.
**Target Audience:** Future AI agents working on this project.
**Priority:** **READ THIS BEFORE MAKING XML CHANGES!**

---

## 🚨 CRITICAL KODI SKIN DEVELOPMENT RULES

### **1. Panel Container Hierarchy (MOST IMPORTANT!)**

**Problem:** Kodi throws `"Trying to add unsupported control type 7"` error

**Control Type 7 = Panel Container**

#### ❌ WRONG - Panel nested in complex Groups:
```xml
<control type="group">  <!-- Group 1 with animations -->
  <control type="group">  <!-- Group 2 with more animations -->
    <include>SomeAnimationInclude</include>
    <control type="panel" id="9300">  ← FAILS TO LOAD!
      <!-- Panel content -->
    </control>
  </control>
</control>
```

**Error in log:**
```
warning: Trying to add unsupported control type 7
```

#### ✅ CORRECT - Panel at clean hierarchy level:
```xml
<controls>
  <include>MyPanelInclude</include>  ← Panel inside clean Include
</controls>
```

**Solution:**
- Place Panel controls at **clean hierarchy level**
- Avoid nesting Panel inside Groups with complex animations
- Use **Includes** to keep Panel definitions clean
- Test loading in Kodi log - check for "control type 7" warning

---

### **2. Include Registration (MANDATORY!)**

**Problem:** `"Skin has invalid include: YourIncludeName"`

**Cause:** Custom Include files are NOT automatically loaded by Kodi!

#### ✅ CORRECT - Register in Includes.xml:

1. Create your Include file:
```xml
<!-- xml/Includes_ShadowTouch.xml -->
<includes>
  <include name="MyCustomInclude">
    <!-- Your content -->
  </include>
</includes>
```

2. **REGISTER in xml/Includes.xml:**
```xml
<includes>
  <include file="Includes_ShadowTouch.xml" />  ← ADD THIS!
  <include file="Defaults.xml" />
</includes>
```

3. Now you can use it:
```xml
<include>MyCustomInclude</include>  ← Works!
```

---

### **3. Tab/Whitespace Sensitivity in Edit Tool**

**Problem:** `Edit` tool fails with "String not found"

**Cause:** Kodi XML uses **TABS**, not spaces!

**Solutions:**
1. Use `cat -A` to see exact whitespace:
```bash
cat -A xml/Home.xml | grep "pattern"
```

2. Use `Write` tool instead of `Edit` for complex changes

3. Use `sed` for line-based operations:
```bash
sed -i '100,200d' xml/Home.xml  # Delete lines 100-200
```

---

### **4. Testing on Real Hardware (MANDATORY!)**

**Problem:** Changes work in theory but fail on device

**Cause:** Emulators don't match real Kodi behavior

**Solution:**
- ALWAYS test on **Google Pixel 7** (primary device)
- Check Kodi log for errors/warnings
- Screenshot + log snippet very helpful for debugging!

**How to get log:**
```
Settings → System → Logging → Enable debugging
View log at: /storage/emulated/0/KodiData/.kodi/kodi.log
```

---

### **5. Visibility Conditions Matter!**

**Problem:** Control exists but is invisible

**Common causes:**
```xml
<visible>$EXP[isContent]</visible>  ← Nimbus variable, may be false!
<visible>String.IsEmpty(Something)</visible>  ← Condition not met
```

**Solution:**
- Use `<visible>true</visible>` for testing
- Check log for visibility issues
- Test by setting temporarily to `true`

---

## 📁 Project File Structure (Important!)

```
skin.shadow.touch/
├── xml/
│   ├── Home.xml                    ← Main home screen
│   ├── Includes.xml                ← REGISTER custom Includes HERE!
│   ├── Includes_ShadowTouch.xml    ← Our custom Includes
│   └── ...
├── CLAUDE.md                       ← READ FIRST in new session!
├── ROADMAP.md                      ← Current phase status
├── DESIGN.md                       ← Visual specs
└── DEVELOPMENT_NOTES.md            ← This file (technical learnings)
```

---

## 🔧 Shadow Touch Implementation Details

### Current Status (2026-02-16):
- ✅ Phase 1: Bottom Navigation Bar (DONE)
- ✅ Phase 2: Vertical Poster Grid (DONE)
- 📋 Phase 3: Long-Press Overlay (NEXT)

### Key Files Modified:
1. **xml/Includes_ShadowTouch.xml** - Our custom Includes:
   - `ShadowTouchVerticalGrid` - Panel (id=9300)
   - `ShadowTouchBottomNav` - 4 buttons (id=9201-9204)

2. **xml/Includes.xml** - Registered our Include file

3. **xml/Home.xml**:
   - Added `<include>ShadowTouchVerticalGrid</include>`
   - Added `<include>ShadowTouchBottomNav</include>`
   - Hidden Nimbus widgets (id=2000, visible=false)
   - Hidden Nimbus side menu (id=9000, visible=false)

### Control IDs Used:
- **9200** - Bottom Nav Group
- **9201** - Home Button
- **9202** - Live TV Button
- **9203** - Library Button
- **9204** - Search Button
- **9205** - Settings Button
- **9300** - Vertical Poster Grid (Panel)

### Content Source:
```xml
<content target="videos">plugin://plugin.video.themoviedb.helper/?info=popular&amp;type=movie</content>
```

---

## 🚨 CRITICAL: XML Editing Best Practices

### **6. Avoid `sed` for Complex XML Changes**

**Problem:** Duplicate tags or missing closing tags

**Cause:** `sed` doesn't understand XML structure!

#### ❌ WRONG - Using sed for complex changes:
```bash
sed -i 's/<onleft>9204<\/onleft>/<onleft>9205<\/onleft>/' file.xml
# Risk: Creates duplicate tags if pattern repeats!
```

#### ✅ CORRECT - Use Write tool for complete rewrites:
```
Use Write tool to rewrite entire file with proper structure
- Guarantees valid XML
- No duplicate tags
- Proper indentation
- All closing tags present
```

**Real Example from Session 4:**
- Used `sed` to add Settings button navigation
- Created duplicate `<onleft>` and `<onright>` tags
- Settings button defined but INVISIBLE (no error!)
- Solution: Complete rewrite with Write tool

**Rule of Thumb:**
- Simple line deletions → `sed` OK
- Complex XML modifications → Use `Write` tool!

---

## 💡 Debugging Tips for Future Sessions

### 1. Check Kodi Log First!
```bash
# Get last 50 lines of log
tail -50 /storage/emulated/0/KodiData/.kodi/kodi.log
```

Look for:
- `warning: Trying to add unsupported control type 7` → Panel hierarchy issue
- `warning: Skin has invalid include:` → Include not registered
- `error:` → Syntax errors in XML

### 2. Verify Include Loading:
```bash
# Check if Include is registered
grep "Includes_ShadowTouch" xml/Includes.xml
```

### 3. Test Changes Incrementally:
- Make ONE change at a time
- Test on device after each change
- Don't batch multiple risky changes!

### 4. Use Screenshots + Logs:
- Screenshot shows visual state
- Log shows technical errors
- Combine both for effective debugging

---

## ⚠️ Known Issues (Non-Critical)

1. **Log Warning:** `"Trying to add unsupported control type 7"`
   - **Cause:** Nimbus Panel (id=14100) still in Home.xml
   - **Impact:** None (our Panel works fine!)
   - **Fix:** Can be cleaned up later (low priority)

2. **Nimbus Code Bloat:**
   - Many Nimbus files still present
   - Not affecting functionality
   - Can be cleaned up in future phases

3. **Invisible Controls Due to Duplicate Tags:**
   - **Problem:** Control defined but not visible (no error in log)
   - **Cause:** Duplicate navigation tags (`<onleft>`, `<onright>`)
   - **Detection:** Hard to spot! Check XML manually or use validator
   - **Prevention:** Use `Write` tool for complex XML changes

---

## 🎯 Strategy for Next Session

1. **ALWAYS READ FIRST:**
   - CLAUDE.md (project context)
   - This file (DEVELOPMENT_NOTES.md)
   - ROADMAP.md (current phase)

2. **Before Making Changes:**
   - Check existing code structure
   - Verify Panel hierarchy rules
   - Plan Include strategy

3. **Testing Protocol:**
   - Test on Google Pixel 7
   - Check Kodi log
   - Get screenshot + log snippet if issues

4. **Commit Strategy:**
   - Clear, descriptive commit messages
   - Reference session URL
   - Explain WHY, not just WHAT

---

**Last Updated:** 2026-02-16
**Session:** 4 (+ Cleanup)
**Status:** Phase 1 + 2 Complete + Cleanup Done! 🎉
**Next:** Phase 3 - Long-Press Overlay
