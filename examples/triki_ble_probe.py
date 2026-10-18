"""Minimal experimental Triki BLE probe for macOS/Linux/Windows.

Requires: pip install bleak
Run: python examples/triki_ble_probe.py
Use only with a device you own. UUIDs and packet decoding are experimental.
"""
import asyncio
import struct
from bleak import BleakClient, BleakScanner

UART_NOTIFY = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
UART_WRITE = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
START_STREAM = bytes.fromhex("20 10 00 D0 07 68 00 03")


def decode(payload: bytearray) -> None:
    data = bytes(payload)
    if len(data) != 14 or data[0] != 0x22:
        print("Raw notification:", data.hex(" "))
        return
    button = data[1]  # Interpretation not yet validated.
    gyro_x, gyro_y, gyro_z, acc_x, acc_y, acc_z = struct.unpack("<6h", data[2:])
    print(f"button?={button} gyro=({gyro_x}, {gyro_y}, {gyro_z}) "
          f"acc=({acc_x}, {acc_y}, {acc_z})")


async def main() -> None:
    print("Searching for Triki...")
    devices = await BleakScanner.discover(timeout=8.0)
    matches = [device for device in devices if "triki" in (device.name or "").lower()]
    if not matches:
        print("No Triki device found. Wake it up and retry.")
        return
    for index, device in enumerate(matches):
        print(f"{index}: {device.name}")
    selected = matches[0]
    print(f"Connecting to {selected.name} (first match)...")
    async with BleakClient(selected) as client:
        await client.start_notify(UART_NOTIFY, lambda _, data: decode(data))
        await client.write_gatt_char(UART_WRITE, START_STREAM, response=False)
        print("Listening for 20 seconds. Move the figurine.")
        await asyncio.sleep(20)
        await client.stop_notify(UART_NOTIFY)


if __name__ == "__main__":
    asyncio.run(main())
