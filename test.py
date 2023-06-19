import usb.core
import usb.util

# Find the USB device

vendor_id=1532
product_id="005C"

#\VID_1532&PID_005C&MI_00\7&79a61ef&0&0000


def read_data():
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)

    # Check if the device is found
    if device is None:
        raise ValueError("USB device not found.")

    # Set the active configuration of the USB device
    device.set_configuration()

    # Find the input endpoint (assuming it's the first endpoint)
    endpoint = device[0][(0, 0)][0]

    # Read data from the USB device
    data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)

    # Process the data as needed
    print(data)

def find_usb_data():
    for device in usb.core.find(find_all=True):
        # Get the VID and PID
        vid = hex(device.idVendor)
        pid = hex(device.idProduct)

        # Print the VID and PID
        print(f"Device: VID={vid}, PID={pid}")

read_data()