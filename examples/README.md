# Build your own Triki project

This folder is a **reusable experimental starting point** for building independent projects with a physical Żabka Triki BLE figurine.

## Included
- [triki_ble_probe.py](triki_ble_probe.py): standalone Python/Bleak BLE discovery, connection, motion notifications and tentative frame decoding.

## Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install bleak
python examples/triki_ble_probe.py
```

This script was prepared from observed hardware behavior; **this exact example has not yet been tested end-to-end**. It selects the first detected Triki device. The observed motion packet interpretation is provisional. See [protocol notes](../docs/BLE_PROTOCOL.md).

## Create your own projects
You can use the documented protocol and example as a foundation for a custom game, interactive installation, gesture controller, research prototype or educational app. Fork the repository, keep your application logic separate from the BLE transport, and validate on your own hardware.

**Reuse terms:** The source code is released under the [MIT License](../LICENSE), allowing reuse, modification and redistribution provided the copyright and license notice are retained. The Żabka/Triki names and branding belong to their respective owners.
