# Product roadmap

## Phase 0 — Repository foundation
- [x] Write product README, architecture, BLE notes and development guide
- [ ] Import the actual working Xcode project and Swift source files
- [ ] Add a .gitignore, license decision and first tagged baseline
**Acceptance:** a fresh clone opens in Xcode and compiles without private credentials.

## Phase 1 — BLE reliability
- [ ] Discover Triki devices by advertised name/service
- [ ] Connect, subscribe to notifications and activate streaming
- [ ] Decode packets and validate frame alignment
- [ ] Handle disconnects, permissions and reconnects
- [ ] Test button semantics and firmware variations
**Acceptance:** stable, timestamped motion data on a physical iPhone.

## Phase 2 — Input engine
- [ ] Calibrate neutral orientation
- [ ] Filter noise, add dead zones and sensitivity settings
- [ ] Convert tilt to 2D movement
- [ ] Detect shake gestures without accidental triggers
- [ ] Support touch fallback
**Acceptance:** predictable controls in repeated device tests.

## Phase 3 — Playable vertical slice
- [ ] One complete level with movement and collision
- [ ] Collectibles, scoring and finish condition
- [ ] Basic enemies and attack feedback
- [ ] Pause/restart and accessibility checks
**Acceptance:** complete 3–5 minute playable loop.

## Phase 4 — Expanded game
- [ ] Three distinct levels and progression
- [ ] Audio, animation and visual polish
- [ ] Save progress locally
- [ ] Performance and battery profiling
**Acceptance:** feature-complete beta build.

## Phase 5 — Release preparation
- [ ] Test across supported iPhones and iOS versions
- [ ] Privacy policy and permissions audit
- [ ] Branding/IP review; do not imply Żabka endorsement
- [ ] Distribution and signing strategy
**Acceptance:** repeatable release build with documented limitations.

## Out of scope (initially)
System-wide iOS mouse control, online accounts, analytics, cloud saves and monetization.
