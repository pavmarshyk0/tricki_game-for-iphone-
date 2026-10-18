# Triki Adventure

**Experimental iOS adventure game controlled by a physical Żabka Triki Bluetooth figurine.**

> Status: early prototype. Independent hobby project; not affiliated with Żabka.

## Goal
Use a physical Triki BLE toy as a motion controller for a native iPhone game. Planned interactions: tilt to move, shake to attack, button for actions, with on-screen controls as fallback.

## Verified progress (18 October 2026)
| Component | Status |
| --- | --- |
| BLE discovery and connection on Mac | Verified |
| Motion streaming (gyroscope / accelerometer) on Mac | Verified |
| iOS SwiftUI project compilation in Xcode | Verified locally |
| Installation on iPhone 14 Pro | Verified locally (developer trust prompt) |
| iPhone BLE gameplay | **Not yet verified** |

## Stack
Swift, SwiftUI, CoreBluetooth, Xcode. Hardware experiments use Python and Bleak on macOS.

## Documentation
- [Step-by-step roadmap](docs/ROADMAP.md)
- [Proposed architecture](docs/ARCHITECTURE.md)
- [Observed BLE protocol](docs/BLE_PROTOCOL.md)
- [Build and development guide](docs/DEVELOPMENT.md)

## Getting started
**The real Xcode project and Swift files have not yet been uploaded to this repository.** Import the local `tricki-game-01` Xcode project, `AdventureView.swift`, `TrikiAdventureApp.swift`, `TrikiBLE.swift`, assets and tests from the Mac first.

After import, open the Xcode project, select a development team, add `NSBluetoothAlwaysUsageDescription`, select an iPhone with Developer Mode enabled, then Build and Run.

## Roadmap summary
1. Import and reproduce the working Xcode build.
2. Stabilize iOS BLE connection and decode motion packets.
3. Calibrate tilt, gestures and touch fallback.
4. Deliver one polished playable level.
5. Add three levels, enemies, scoring and progress.
6. Test, document privacy and prepare a release.

## Project principles
Separate BLE code from game rules, verify physical-device behavior, support reconnection, and avoid undocumented writes to hardware. Do not commit signing credentials or device identifiers.

## License
No license selected yet; all rights reserved until the owner decides.
