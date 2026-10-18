# Development guide

## Local prerequisites
- Mac with a working compatible Xcode installation
- iPhone with Developer Mode enabled
- Apple Account selected under Xcode Signing & Capabilities
- Physical Żabka Triki for BLE tests

## Import source from the Mac
The current prototype was created locally in Xcode as `tricki-game-01`. The three Swift source files discussed during development were `AdventureView.swift`, `TrikiAdventureApp.swift` and `TrikiBLE.swift`. These **must be imported from the actual local project**; this repository does not yet contain their source.

Commit the `.xcodeproj`, source files, assets and tests. Exclude `DerivedData/`, `.build/`, `*.xcuserstate`, `xcuserdata/`, certificates, private keys and provisioning profiles.

## Build
1. Open the `.xcodeproj` in Xcode.
2. Select the app target and confirm Swift files are in Target Membership / Compile Sources.
3. Set `Generate Info.plist File = Yes`, `Mach-O Type = Executable`, `Skip Install = No`.
4. Add Bluetooth usage description (`NSBluetoothAlwaysUsageDescription`).
5. Choose a unique bundle ID and your own Personal Team.
6. Select the physical iPhone, then Product → Build and Run.

## Known history
- First local build succeeded but produced an app bundle without an executable because Compile Sources was empty.
- After adding Swift sources to the target, Xcode reported Build Succeeded.
- Installation reached an iPhone trust prompt; on-device BLE gameplay is not yet verified.
- Two deprecation warnings for SwiftUI `onChange(of:perform:)` were reported.

## Troubleshooting
- No device in Xcode: check Finder, USB data connection and Developer Mode.
- Missing executable: inspect Compile Sources, build phases and generated app bundle.
- BLE scan fails: check iOS Bluetooth permission and device power.
- Device connects but no motion: verify notify subscription and the documented stream command.
- No game response: inspect decoded samples, calibration and input mapping.

## Next task
Import and audit the real Swift/Xcode sources before refactoring.
