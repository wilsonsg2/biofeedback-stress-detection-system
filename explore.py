import asyncio
from bleak import BleakClient

DEVICE_ADDRESS = "PASTE_ADDRESS_HERE"

async def explore():
    async with BleakClient(DEVICE_ADDRESS) as client:
        print("Connected:", client.is_connected)
        for service in client.services:
            print("\nService:", service.uuid)
            for char in service.characteristics:
                print("  Characteristic:", char.uuid)
                print("    Properties:", char.properties)

asyncio.run(explore())