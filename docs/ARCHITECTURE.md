# Architecture (target design)

```text
Triki physical device
        |
        | BLE notifications
        v
CoreBluetooth adapter (scan/connect/reconnect)
        |
        v
Triki protocol decoder (framing, signed IMU values, button)
        |
        v
Input engine (calibration, filtering, gestures)
        |
        v
Game state (player, collisions, enemies, levels, scoring)
        |
        v
SwiftUI presentation + on-screen fallback controls
```

## Proposed modules
- `App/` — app entry point and permissions
- `Bluetooth/` — BLE central, connection state and characteristic subscriptions
- `Protocol/` — packet framing, decoding and protocol tests
- `Input/` — normalized controller events, filtering and calibration
- `Game/` — deterministic gameplay rules and level data
- `UI/` — SwiftUI screens and overlays
- `Tests/` — decoder, calibration and game-state unit tests

These are **proposed folders**, not a claim that they exist in the current source.

## Interfaces
`MotionSample`: timestamp, gyro XYZ, acceleration XYZ, optional button state.

`ControllerEvent`: move(dx,dy), attack, action, disconnect, reconnect.

The game layer must not know BLE UUIDs or raw packet layouts.

## Reliability and privacy
Handle BLE permission denial, device power-off, packet loss and reconnection. Avoid logging device IDs in public issues. All gameplay should work offline. Do not request unrelated iOS permissions.
