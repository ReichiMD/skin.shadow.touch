# Shadow Touch - Kodi Skin

![Status](https://img.shields.io/badge/status-in%20development-orange)
![Kodi](https://img.shields.io/badge/kodi-21.3%20omega-blue)
![License](https://img.shields.io/badge/license-GPL%20v2-green)

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
- **Enhanced PVR Integration**: Based on EstuaryPVR+ Omega's optimized Live TV features
- **Touch-Friendly EPG**: Larger touch targets, improved channel navigation
- **Now/Next View**: Quick access to current and upcoming programs

### ⚡ Performance
- **Code-First Rendering**: Minimal image assets, maximum performance
- **Lightweight**: Designed for smooth scrolling even on lower-end devices
- **Optimized for 1080p**: Landscape-only (Samsung S9 FE, Nvidia Shield)

---

## 📋 Development Status

**Current Phase:** Foundation (Phase 0)
**Progress:** 60%

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 0 | 🟡 In Progress | Project setup & identity |
| Phase 1 | ⚪ Pending | Bottom navigation bar |
| Phase 2 | ⚪ Pending | Vertical grid layout |
| Phase 3 | ⚪ Pending | Long-press overlay |
| Phase 4 | ⚪ Pending | PVR integration |
| Phase 5+ | ⚪ Pending | Polish & optimization |

See [ROADMAP.md](ROADMAP.md) for detailed development plan.

---

## 🛠️ Technical Foundation

**Based On:** [EstuaryPVR+ Omega](https://github.com/SplitEnz/skin.estuary.pvr.plus.omega) by Dumyat/SplitEnz
**Original Skin:** [Estuary](https://github.com/xbmc/xbmc/tree/master/addons/skin.estuary) by phil65 & Team Kodi
**Kodi Version:** 21.3 Omega (and higher)
**Addon ID:** `skin.shadow.touch`

### Why EstuaryPVR+ as Base?
- Already optimized PVR/Live TV features
- Lightweight and performant
- Well-documented XML structure
- GPL v2 licensed (compatible with modifications)

---

## 📦 Installation (Not Ready Yet!)

**Shadow Touch is currently in development and not ready for installation.**

When ready, installation instructions will be:
1. Download the latest release from [Releases](https://github.com/ReichiMD/Skin-Deep-Black/releases)
2. Copy to Kodi's `addons/` folder
3. Enable in Kodi → Settings → Interface → Skin

---

## 🧩 Project Structure

```
skin.shadow.touch/
├── CLAUDE.md           ← AI session continuity (READ FIRST!)
├── ROADMAP.md          ← Development phases & progress
├── skin-structure.md   ← Kodi skinning reference guide
├── addon.xml           ← Skin metadata
├── xml/                ← UI window definitions
│   ├── Home.xml
│   ├── MyPVR*.xml
│   └── Dialog*.xml
├── media/              ← Icons, textures (minimized!)
├── colors/             ← Color palettes
├── fonts/              ← Font definitions
└── themes/             ← Theme variants
```

### Key Documents

- **[CLAUDE.md](CLAUDE.md)**: Master document for AI development sessions (context, architecture, warnings)
- **[ROADMAP.md](ROADMAP.md)**: Detailed development roadmap with checkboxes
- **[skin-structure.md](skin-structure.md)**: Kodi skinning concepts reference

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
- Icon fonts (Font Awesome or similar)
- Kodi-internal rendering (blur, gradients)

### Performance Goals
- Smooth 60fps scrolling on Samsung S9 FE
- < 100MB memory footprint
- Instant response to touch input

---

## 🤝 Contributing

**Shadow Touch is currently a solo project by ReichiMD.**
Contributions, feedback, and testing are welcome once the MVP (Phase 0-3) is complete.

### Development Setup
1. Clone this repository
2. Read [CLAUDE.md](CLAUDE.md) for project context
3. Check [ROADMAP.md](ROADMAP.md) for current priorities
4. Consult [skin-structure.md](skin-structure.md) for Kodi skinning basics

---

## 📜 License & Attribution

**License:** GNU General Public License v2.0
See [LICENSE.txt](LICENSE.txt) for full text.

### Attribution
- **EstuaryPVR+ Omega** by Dumyat/SplitEnz (base skin)
- **Estuary** by phil65 & Team Kodi (original skin)
- Parental Rating icons by wyrm65 & braz
- Media flags from Aeon Madnox by Mike_Doc & Schimi2k

Shadow Touch is a derivative work licensed under GPL v2, maintaining all original attributions.

---

## 🔗 Links

- **Repository**: [github.com/ReichiMD/Skin-Deep-Black](https://github.com/ReichiMD/Skin-Deep-Black)
- **EstuaryPVR+ Omega**: [github.com/SplitEnz/skin.estuary.pvr.plus.omega](https://github.com/SplitEnz/skin.estuary.pvr.plus.omega)
- **Kodi Skin Dev Docs**: [kodi.wiki/view/Skin_development](https://kodi.wiki/view/Skin_development)
- **Kodi Forum**: [forum.kodi.tv](https://forum.kodi.tv)

---

## 📊 Project Timeline

**Started:** 2025-02-14
**Status:** Foundation Phase (Phase 0)
**Next Milestone:** MVP (Phases 0-3) - Bottom nav + Grid + Long-press overlay

---

## ❓ FAQ

### Why "Shadow Touch"?
Dark theme + Touch-optimized = Shadow Touch. Simple, descriptive, memorable.

### Will it work on phones?
No, Shadow Touch is designed exclusively for landscape 1080p (tablets & TV boxes). Portrait mode is not supported.

### Why not support portrait?
Designing for both orientations doubles complexity. Focusing on landscape allows optimization for the primary use case (media consumption on tablets/TVs).

### When will it be ready?
No ETAs. Check the [ROADMAP.md](ROADMAP.md) for current progress.

### Can I use this on Kodi 20 (Nexus)?
No, Shadow Touch requires Kodi 21 (Omega) or higher due to dependencies.

---

**Last Updated:** 2025-02-14
**Version:** 0.0.1-dev
