# BLE protocol — observed hardware notes

**Source:** local macOS experiment with one physical Żabka Triki figurine on 18 October 2026. Not a manufacturer specification; behavior may vary by firmware.

## Observed services
| UUID | Property / role |
| --- | --- |
| `6e400001-b5a3-f393-e0a9-e50e24dcca9e` | Vendor UART-like service |
| `6e400002-b5a3-f393-e0a9-e50e24dcca9e` | Write / write without response |
| `6e400003-b5a3-f393-e0a9-e50e24dcca9e` | Notify |
| `6e400004-b5a3-f393-e0a9-e50e24dcca9e` | Read/write; observed 00 |
| `0000180f-0000-1000-8000-00805f9b34fb` | Battery service |
| `00002a19-0000-1000-8000-00805f9b34fb` | Battery level; observed 0x60 (96%) |
| `00002a26-0000-1000-8000-00805f9b34fb` | Firmware revision; observed 3.2.1-A |

## Motion stream
On this unit, subscribing to notify alone produced no motion frames. The following command sent to the write characteristic activated a stream in a macOS experiment:

```text
20 10 00 D0 07 68 00 03
```

Observed notification payloads were decoded as 14-byte records:
- byte 0: `0x22` framing marker
- byte 1: possible button field (observed zero; button behavior **not verified**)
- bytes 2–13: six little-endian signed 16-bit values interpreted as gyro XYZ then acceleration XYZ

**Caution:** This is a provisional interpretation from a working experiment, not independently validated across devices. Units, sampling rate and frame resynchronization need tests. Do not send undocumented commands or write to configuration characteristics without verifying their purpose.

## Test plan
1. Record stationary baseline in multiple orientations.
2. Tilt each axis separately and validate sign/axis mapping.
3. Press button repeatedly and inspect raw bytes.
4. Shake briefly and measure peak values.
5. Test stream interruption, reconnect and battery behavior.
6. Compare iOS CoreBluetooth results against the macOS reference.

Never publish device serial numbers or stable BLE identifiers.
