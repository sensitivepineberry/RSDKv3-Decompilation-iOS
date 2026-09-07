# RSDKv3 iOS

An iOS port of the RSDKv3 decompilation engine (Sonic CD). This is an **unsigned IPA** — you will need to sign it using AltStore, SideStore, TrollStore, or a similar sideloading tool.

Based on [RSDKModding/RSDKv3-Decompilation](https://github.com/RSDKModding/RSDKv3-Decompilation).

## Features
- Native ARM64 build optimized for iOS 13.0+
- Full touchscreen controls
- Mod support (in progress)
- Landscape orientation support (iPhone & iPad)
- File sharing enabled — manage game files directly from the iOS Files app
- No copyrighted game assets included

## Installation

### Pre-built IPA
1. Download the latest IPA from [Releases](../../releases).
2. Install using **AltStore**, **SideStore**, **TrollStore**, or your preferred sideloading method.
3. Launch the app once — it will create its Documents folder.
4. Open the **Files** app → **On My iPhone** → **RSDKv3**.
5. Copy your own `Data.rsdk` file into this folder.
6. Optionally add a `videos/` folder with `.ogv` video files (Steam version only, lowercase filenames).
7. Launch the app again — it will load your game data and generate a `settings.ini`.

### Getting `Data.rsdk`
You **must** provide your own `Data.rsdk` from a legitimate copy of Sonic CD:
- **iOS:** [App Store](https://apps.apple.com/us/app/sonic-cd-classic/id454316134) — extraction tutorial [here](https://gamebanana.com/tuts/14491)
- **Android:** [Google Play](https://play.google.com/store/apps/details?id=com.sega.soniccd.classic) — extraction tutorial [here](https://gamebanana.com/tuts/14942)
- **Steam:** via [Sonic Origins](https://store.steampowered.com/app/1794960) or the original release

## Configuration
Edit `settings.ini` in the Files app to customize:
- `DataFile` — name of your `.rsdk` file
- `Language` — game language
- `DevMenu` — enable developer menu
- `BGMVolume` / `SFXVolume` — audio levels
- `DisableTouchControls` — toggle touch input
- `txtScripts` - text scripts.

## Okay, that’s cool and all, but how do I use MODS???
First, grab the Scripts folder from [here](https://github.com/RSDKModding/RSDKv3-Script-Decompilation). Put the `Scripts` folder in files along with Data.rsdk. Then create a folder named `mods` and put the mods folders in there. You’ll need to activate devmode to manage mods more easily, but otherwise you’ll be fine. (filenames are case sensitive, so make sure they’re the same as here!)

## Building from Source

### Requirements
- macOS with Xcode 16+ (or GitHub Actions)
- Git

### Clone
```bash
git clone --recursive https://github.com/RadiantDelux/RSDKv3-iOS.git
```

### Build
The project builds automatically via GitHub Actions. Push to the repo and the workflow will:
1. Build all dependencies (libogg, libvorbis, libtheora, SDL2) for iOS arm64
2. Compile the Xcode project
3. Generate an unsigned `.ipa` artifact

To trigger manually: go to **Actions** → **Build iOS IPA** → **Run workflow**.

### Manual Build
If building locally with Xcode:
1. Open `RSDKv3 ios.xcodeproj`
2. Set the scheme to **RSDKv3** and target **iOS Device (arm64)**
3. Build with `Release` configuration

> **Note:** You will need to apply the source patches from `.github/workflows/ios.yml` (the Setup step) before building locally, as they fix platform-specific incompatibilities.

## Disclaimer
This project does not include any copyrighted game assets. You must provide your own `Data.rsdk` file from a legitimate copy of Sonic CD. This is an engine reimplementation only.

## Credits
- [RSDKModding](https://github.com/RSDKModding) — original RSDKv3 decompilation
- [Xeeynamo](https://github.com/Xeeynamo), [Sappharad](https://github.com/Sappharad), [SuperSonic16](https://github.com/TheSuperSonic16), [biscuitball425](https://github.com/biscuitball425) — contributions to the original project
