# Shadow Touch - Kodi Skin

![Status](https://img.shields.io/badge/status-in%20development-orange)
![Kodi](https://img.shields.io/badge/kodi-21%20omega-blue)
![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0%20%2B%20GPL%20v2-green)

**A modern, touch-optimized Kodi skin for tablets and TV devices**

---

## 🎯 Project Vision

Shadow Touch is a touch-first Kodi skin designed for **Samsung S9 FE tablets** and **Nvidia Shield** devices. It combines the sleek aesthetics of modern streaming apps (Netflix, Apple TV) with the technical efficiency of a lightweight skin.

### Target Users
- Tablet users who want a thumb-friendly, touch-optimized interface
- Users transitioning from streaming apps to Kodi
- Anyone seeking a minimal, dark-themed, performant skin
- PVR/Live TV enthusiasts who need enhanced EPG features

---

## ✨ Key Features (Planned)

### 🎨 Design
- **Bottom Navigation Bar**: Optimized for thumb reach on tablets (replaces side menu)
- **Vertical Grid Layout**: Movie/TV posters in a scrollable tile grid
- **Long-Press Overlays**: Tap to play, long-press for info and actions
- **Dark Theme**: Modern, minimalist aesthetic with code-based rendering

### 📺 Live TV (PVR)
- **Full PVR Support**: Comprehensive Live TV integration (EPG, recordings, channels)
- **Touch-Friendly Interface**: Larger touch targets, improved navigation
- **Modern Design**: Adapted to match Shadow Touch's dark, minimal aesthetic

### ⚡ Performance
- **Code-First Rendering**: Minimal image assets, maximum performance
- **Lightweight**: Designed for smooth scrolling even on lower-end devices
- **Optimized for 1080p**: Landscape-only (Samsung S9 FE, Nvidia Shield)

---

## 📋 Development Status

**Current Phase:** Foundation (Phase 0)
**Progress:** Migration to Nimbus base complete!

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 0 | ✅ Complete | Project setup & Nimbus migration |
| Phase 1 | ⚪ Pending | Bottom navigation bar |
| Phase 2 | ⚪ Pending | Vertical grid layout |
| Phase 3 | ⚪ Pending | Long-press overlay |
| Phase 4 | ⚪ Pending | PVR customization |
| Phase 5+ | ⚪ Pending | Polish & optimization |

See [ROADMAP.md](ROADMAP.md) for detailed development plan.

---

## 🛠️ Technical Foundation

**Based On:** [Nimbus](https://github.com/ivarbrandt/skin.nimbus) by Ivar Brandt
**Kodi Version:** 21 Omega (and higher)
**Addon ID:** `skin.shadow.touch`

### Why Nimbus as Base?
- Touch-first, landscape-optimized design (perfect for tablets!)
- Netflix-style interface already built-in
- Full PVR support (15+ PVR XML files)
- Modern, clean code-base
- CC BY-SA 4.0 + GPL v2 licensed (compatible with modifications)

---

## 📦 Installation (Not Ready Yet!)

**Shadow Touch is currently in development and not ready for installation.**

When ready, installation instructions will be:
1. Download the latest release from [Releases](https://github.com/ReichiMD/skin.shadow.touch/releases)
2. Install via Kodi's addon manager or manually copy to `addons/` folder
3. Enable in Kodi → Settings → Interface → Skin

---

## 🧩 Project Structure

```
skin.shadow.touch/
├── CLAUDE.md           ← AI session continuity (READ FIRST!)
├── NIMBUS-STRUCTURE.md ← Nimbus architecture reference
├── DESIGN.md           ← Visual design specification
├── ROADMAP.md          ← Development phases & progress
├── addon.xml           ← Skin metadata
├── xml/                ← UI window definitions (121 files!)
│   ├── Home.xml
│   ├── MyPVR*.xml      (15 PVR files)
│   └── Dialog*.xml
├── media/              ← Icons, textures (minimized!)
├── colors/             ← Color palettes (16 themes!)
├── fonts/              ← Font definitions
└── themes/             ← Theme variants
```

### Key Documents

- **[CLAUDE.md](CLAUDE.md)**: Master document for AI development sessions (context, architecture, warnings)
- **[NIMBUS-STRUCTURE.md](NIMBUS-STRUCTURE.md)**: Nimbus architecture guide (121 XMLs explained!)
- **[DESIGN.md](DESIGN.md)**: Exact visual specifications (measurements, colors, layouts)
- **[ROADMAP.md](ROADMAP.md)**: Detailed development roadmap with checkboxes

---

## 🎨 Design Philosophy

### Touch-First Principles
1. **Thumb-Reachable**: Bottom nav bar for one-handed use on tablets
2. **Generous Spacing**: 20% larger padding to prevent misclicks
3. **Long-Press Actions**: Tap = Play, Long-Press = Info/Options
4. **Big Touch Targets**: Minimum 60px hit-boxes for all interactive elements

### Code-First Rendering
- No PNG textures where avoidable
- Colors/shadows via `Variables.xml` and `ColorDiffuse`
- Icon fonts for symbols
- Kodi-internal rendering (blur, gradients)

### Performance Goals
- Smooth 60fps scrolling on Samsung S9 FE
- Minimal memory footprint
- Instant response to touch input

---

## 🤝 Contributing

**Shadow Touch is currently a solo project by ReichiMD.**
Contributions, feedback, and testing are welcome once the MVP (Phase 0-3) is complete.

### Development Setup
1. Clone this repository
2. Read [CLAUDE.md](CLAUDE.md) for project context
3. Read [NIMBUS-STRUCTURE.md](NIMBUS-STRUCTURE.md) for Nimbus architecture
4. Check [ROADMAP.md](ROADMAP.md) for current priorities

---

## 📜 License & Attribution

**License:** CC BY-SA 4.0 (Artwork) + GNU General Public License v2.0 (Code)
See [LICENSE.txt](LICENSE.txt) for full text.

### Attribution
- **Nimbus** by Ivar Brandt (base skin)
  - Repository: https://github.com/ivarbrandt/skin.nimbus
  - License: CC BY-SA 4.0 + GPL v2
- Shadow Touch is a derivative work maintaining all original attributions

---

## 🔗 Links

- **Repository**: [github.com/ReichiMD/skin.shadow.touch](https://github.com/ReichiMD/skin.shadow.touch)
- **Nimbus (Base Skin)**: [github.com/ivarbrandt/skin.nimbus](https://github.com/ivarbrandt/skin.nimbus)
- **Kodi Skin Dev Docs**: [kodi.wiki/view/Skin_development](https://kodi.wiki/view/Skin_development)
- **Kodi Forum**: [forum.kodi.tv](https://forum.kodi.tv)

---

## 📊 Project Timeline

**Started:** 2025-02-14
**Nimbus Migration:** 2025-02-15
**Status:** Foundation Phase (Phase 0) - Migration Complete!
**Next Milestone:** Phase 1-2 - Bottom nav + Vertical grid

---

## ❓ FAQ

### Why "Shadow Touch"?
Dark theme + Touch-optimized = Shadow Touch. Simple, descriptive, memorable.

### Will it work on phones?
No, Shadow Touch is designed exclusively for landscape 1080p (tablets & TV boxes). Portrait mode is not supported.

### Why switch from EstuaryPVR+ to Nimbus?
Nimbus is already touch-first and Netflix-style, saving ~12 hours of development time. It also has full PVR support, so we get the best of both worlds!

### When will it be ready?
No ETAs. Check the [ROADMAP.md](ROADMAP.md) for current progress.

### Can I use this on Kodi 20 (Nexus)?
No, Shadow Touch requires Kodi 21 (Omega) or higher due to dependencies.

---

**Last Updated:** 2025-02-15
**Version:** 0.0.1-dev

