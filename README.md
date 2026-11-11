<p align="center">
  <a href="https://github.com/DTM-Mods"><img src="https://raw.githubusercontent.com/DTM-Mods/.github/main/assets/dtm-header.jpg" alt="DTM Mods by PropaineX & Fennell" width="100%"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/DTM-Mods/.github/main/assets/icons/FS25_ProEdition_BoxTruck.png" alt="Box Truck Pro Edition icon" width="128">
</p>

<h1 align="center">Box Truck Pro Edition</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Farming%20Simulator-25-2E6B4F" alt="Farming Simulator 25">
  <a href="https://github.com/DTM-Mods/FS25_ProEdition_BoxTruck/releases/latest"><img src="https://img.shields.io/github/v/release/DTM-Mods/FS25_ProEdition_BoxTruck?label=version&color=D9A441" alt="Latest version"></a>
  <a href="https://github.com/DTM-Mods"><img src="https://img.shields.io/badge/DTM-Mods-143326" alt="DTM Mods"></a>
</p>

<p align="center">
  <b>A Volvo FH16 8x4 curtain-sider and flatbed for hauling pallets.</b><br>
  <sub>by PropaineX</sub>
</p>

<p align="center">
  <a href="https://github.com/DTM-Mods/FS25_ProEdition_BoxTruck/releases/latest"><img src="https://img.shields.io/badge/Download-latest%20release-D9A441?style=for-the-badge&logo=github&logoColor=143326&labelColor=E9C77A" alt="Download the latest release"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/DTM-Mods/.github/main/assets/features.jpg" alt="Features" width="100%">
</p>

Two trucks in the shop under **PropaineX Pro Edition > Pro Edition Trucks**, both on the game's own Volvo FH16 8x4 Tag cab and chassis, with four engines (FH425 City Hauler, FH515 Regional Hauler, FH585 Long Hauler, FH600 Heavy Hauler, 425 to 600 hp).

**Box Truck**: a curtain-sider for hauling pallets, in the style of the Krone ProfiLiner.

- The curtain gathers at the rear, the side boards fold away and the posts slide back
- Rear barn doors and 9 tension belts across the load floor
- Load space about 6.8 x 2.48 m, 2.55 m inside height
- Curtain designs: plain white, ProEdition, Krone, Farming Simulator League, GIANTS; plain white paint option that matches the body
- Controls: **X** rear doors, **Z** open/close the selected curtain, **U** select the left or right curtain

**Flatbed Truck**: a 6.85 x 2.55 m deck with side walls or sliding stakes (shop choice).

- **X** folds the side boards down, or pairs the stakes on both sides
- Side-wall version: a stainless tailgate on **Left Alt + T**
- Nine tension belts; works with Universal Autoload (2.44 m between the stakes, so euro pallets fit 2 across sideways)

Price $175,000, top speed 90 km/h. Works in multiplayer. All controls can be changed in the controls menu.

See [PATCH_NOTES.md](PATCH_NOTES.md) for the changes in each version.

<p align="center">
  <img src="https://raw.githubusercontent.com/DTM-Mods/.github/main/assets/installation.jpg" alt="Installation" width="100%">
</p>

Download `FS25_BoxTruck_ProEdition.zip` from the [latest release](https://github.com/DTM-Mods/FS25_ProEdition_BoxTruck/releases/latest) and put it in `Documents/My Games/FarmingSimulator2025/mods`, without unzipping or renaming it. In multiplayer, the server and every player need the same version.

<p align="center">
  <img src="https://raw.githubusercontent.com/DTM-Mods/.github/main/assets/license.jpg" alt="License" width="100%">
</p>

MIT, see [LICENSE](LICENSE). It covers only PropaineX's own work: the models, textures and other files that come from or are based on Farming Simulator 25 belong to GIANTS Software GmbH and stay under its terms.

<details>
<summary><b>For developers</b>: files, building and tests</summary>

### Working source: 1.4.0.0 — Flatbed Truck Pro Edition

The flatbed is integrated as a separate shop vehicle beside the Box Truck, under
**PropaineX Pro Edition > Pro Edition Trucks**. This source build is **untested
in game**, and has not been packaged or uploaded.

- Same Volvo FH16 8x4 Tag cab, engine and color options; Aero Parts defaults to None.
- Shop choice: side walls or sliding stakes. **X** folds the side boards outward/down or pairs the alternating stakes on both sides using the native Fliegl-style 0.7-second setup.
- Side-wall version only: 30 cm diamond-pattern stainless tailgate, controlled independently by **Left Alt + T**.
- Nine tension belts, body collisions, rear light controls, centered rear plate mount and the approved striped round underrun tube.
- Optional Universal Autoload retains its own shop menu and **Shift + R** controls. Its fallback area is added only when no saved config exists: 2.44 m clear width between the stakes (same as the Krone ProfiLiner, so euro pallets fit 2 across sideways), 6.70 m length, floor at root y1.625, height2.20 m.
- Tailgate save/network state is implemented; native Foldable handles the side animation state. Existing Box Truck runtime files are preserved.

Source, reference, localization, belt-anchor, tailgate network/save and existing
Box Truck regression checks pass. GIANTS Editor loaded the saved asset and
resolved all 363 flatbed mappings and 13 lamp color channels. Purchase, driving,
real loading/collisions, nighttime lighting and live multiplayer remain untested.
No special milk-pallet spacing override is applied.

Runtime files: `flatbedTruck.xml`, `flatbedTruck.i3d` and `scripts/FlatbedBody.lua`.
Build/check instructions: `source/flatbed_runtime/README.md`; player notes:
`PATCH_NOTES.md`.

### Earlier documented release: 1.3.0.4

October 27, 2026: the curtain, banner, bottom reinforcement band, straps and buckles now move together continuously between shut and the selected gathered shape. All three shapes on both sides use the same reversible transition, with artwork visible throughout. Random selection, networking, saves and loading controls are preserved.

Lua and asset regressions, hardware attachment checks, all 347 node mappings, and package verification pass. GIANTS Editor previews verify closed, intermediate and gathered positions. Full vehicle gameplay and multiplayer rendering remain untested.

Local testing ZIP: `FarmingSimulator2025/Testing_local/FS25_BoxTruck_ProEdition.zip` ? 21 runtime files, 64,537,218 bytes. SHA-256: `d987e511b2e3b7d352ced84261cc2631b47a262d482497be91c33071009b46ee`. The identical ZIP was delivered to remote `/testing` and passed full SHA-256 readback. Delivery is recorded in `chat_history/2026-10-27_1.3.0.4_testing_release.md`.

Finished animated preview: `previews/curtain_straps_motion_v2/curtain_straps_open_close_loop.gif`. Implementation notes: `chat_history/2026-10-27_curtain_shape_motion.md` and `chat_history/2026-10-27_moving_curtain_straps.md`.

### Previous version: 1.3.0.1

Curtain attachment fix: use the mapping record's `nodeId` when linking runtime gathered curtains. Corrected regression checks pass; actual in-game verification remains pending. The new Testing_local ZIP is 50,453,200 bytes, SHA-256 `50693c7c85c8a57772260fdbdc76975cd180bee3334c2263cbdbf24a18cea6c0`. See `chat_history/2026-10-26_1.3.0.1_testing_release.md`; the 1.3.0.0 delivery details below describe the previous build.

Updated October 26, 2026. The current build adds three randomized gathered-curtain shapes on each side, white inner linings, higher-resolution curtain textures, woven fabric detail, and upgraded body hardware. Curtain choices are selected by the server, synchronized to clients and late joiners, and retained in saves. Existing door, board, post, curtain, and loading controls are preserved.

The chassis center of mass is now `0 0.8464 0.6`.

### Latest delivery

- ZIP filename: `FS25_BoxTruck_ProEdition.zip` (20 runtime files; 50,453,180 bytes).
- SHA-256: `85510e3800a3c06b982b34827c4be3a5d6cad974c14f2901a726ca0ca4c24389`.
- Local build: `FarmingSimulator2025/Testing_local/FS25_BoxTruck_ProEdition.zip`.
- This exact build was delivered to SFTP `/testing` and then `/incoming`; both deliveries passed full remote SHA-256 readback verification.
- Build with `python -I source/package_testing.py`. ZIPs and local test dependencies are excluded from Git.

### Validation and remaining testing

All 347 vehicle node mappings resolve. The Lua regression checks pass for random selection, server authority, event serialization, late joining, save/restore, legacy saves, all curtain designs, cleanup, mesh indices, and white linings. Packaging checks verify ZIP CRC, runtime references, and every member against source. GIANTS Editor previously loaded and displayed the integrated asset.

In-game animation/performance and an actual multiplayer session still need testing. Run `python -I source/test_gathered_runtime.py` with Lupa installed in `.local/lua-test-runtime` to repeat the mocked engine/network checks.

See [implementation notes](chat_history/2026-10-26_random_gathered_curtains.md), [testing release](chat_history/2026-10-26_1.3.0.0_testing_release.md), and [incoming delivery](chat_history/2026-10-26_incoming_release.md). These supersede older session status statements.

- Cab, chassis and 8x4 Tag axles: the game's own Volvo FH16.
- Body: our own curtain-sider (curtain sides, rear barn doors), built in Blender.
- Loading: forklift with tension belts, plus an autoload script written from scratch.

### Files

- `source/` - Blender build scripts, texture tools, runtime checks, and ZIP packaging.
- `previews/` - preview renders and the generated .blend.
- `reference_*.md` - measurements taken from other trucks (reference only, nothing copied).
- `chat_history/` - session notes.

Repository: `PropaineX/FS25_ProEdition_BoxTruck`. The truck uses the GIANTS FH16 base-game chassis and cab.

</details>

---

<p align="center">
  <a href="https://github.com/DTM-Mods"><img src="https://raw.githubusercontent.com/DTM-Mods/.github/main/assets/dtm-intro.gif" alt="DTM Mods by PropaineX & Fennell" width="420"></a><br>
  <sub>Part of <a href="https://github.com/DTM-Mods">DTM Mods</a> (Dead To Me) by PropaineX & Fennell</sub>
</p>
