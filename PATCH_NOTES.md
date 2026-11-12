<p align="center">
  <img src="https://raw.githubusercontent.com/DTM-Mods/.github/main/assets/patch-notes.jpg" alt="Patch notes" width="100%">
</p>

# Patch notes

## 1.5.4.0
- Both trucks: with Universal Autoload, the zone they pick pallets up from beside the truck is now the same size as the Krone ProfiLiner's (14.6 m long, centred on the load area), so pulling up to a row of pallets reaches the same ones a ProfiLiner would. Each truck still holds only what fits on it.
- Flatbed: the black frame bar under the side walls no longer flickers with the grey deck-edge rail; it now shows cleanly all the way round.

## 1.5.3.0
- Flatbed: milk pallets and other euro pallets load across the deck again (two side by side) instead of long side front to back. The truck now always gives Universal Autoload its correct loading area, even when an older saved setting exists.

## 1.5.2.0
- Flatbed deck widened to 2.44 m, the same load width as the Krone ProfiLiner, so two euro pallets fit side by side. Belts, stakes and collisions moved to match.

## 1.5.1.0
- The "Pro Edition Trucks" shop tile now sits next to the other Pro Edition vehicle tiles.
- Flatbed: new weathered wooden deck.
- Flatbed: 10 off-road tyre options in the shop (445/65 and 500/60 singles on the drive axles), plus the stock tyres.

## 1.5.0.0
- Both trucks now show up in their own "Pro Edition Trucks" section in the shop.
- Flatbed: off-road single tyre options added.

## 1.4.0.1
- Flatbed: the tailgate no longer has its own key. It opens and closes together with the side walls on X.

## 1.4.0.0 - 2026-11-06 - Flatbed Truck Pro Edition

Status: **Source build complete. Untested in game. Not packaged or uploaded.**

- Added Flatbed Truck Pro Edition as a separate shop vehicle beside the existing Box Truck, under PropaineX Pro Edition > Pro Edition Trucks.
- Uses the same Volvo FH16 8x4 Tag cab, engines, colors and cab options, with a 6.85 m by 2.55 m deck. Aero Parts defaults to None; the other choices remain available.
- Choose Side walls or Sliding stakes in the shop. X folds all six side boards outward and down, or slides stakes 1, 3 and 5 forward into pairs on both sides. The divider posts stay upright.
- The stakes use the Fliegl Timber Runner's native 0.7-second folding setup, adapted to our own nodes and travel distances.
- The side-wall version has a 30 cm diamond-pattern stainless tailgate. Left Alt + T opens and closes it independently. The stake version keeps an open rear.
- Added nine tension belts, body collision shapes, rear lamp controls, and a centered rear plate mount.
- Retained the round underrun tube with full-length red-and-white stripes rising outward from the bottom center. The stripes use the game's reflector shader; nighttime appearance still needs testing.
- Supports Universal Autoload when installed, with its own shop controls and Shift + R loading. Supplies a default loading area only when no saved configuration exists; existing custom settings and opt-outs are preserved.
- Added tailgate save/load and network state handling. The side animations use the game's native folding save/network support.
- Source, node, Lua, network-state and regression checks pass. Driving, actual loading, collision behavior, lighting and live multiplayer still need in-game testing. The 20-pallet milk layout remains a preview; no special pallet stacking override was added.
- Existing Box Truck XML, model, shapes and body script are unchanged by this build.
