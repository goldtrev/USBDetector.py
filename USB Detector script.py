import os
import subprocess

# define the target USB device
target_usb = "sda1"

while True:
    # get the list of currently connected USB devices
    output = subprocess.run(["lsblk", "-o", "name,mountpoint"], capture_output=True).stdout.decode()
    connected_devices = [line.split()[0] for line in output.split("\n") if target_usb in line]

    if not connected_devices:
        # target USB device is not connected
        subprocess.run(["yad", "--title=Device Unplugged", "--text=The target USB device has been unplugged."])
    else:
        # target USB device is connected
        pass