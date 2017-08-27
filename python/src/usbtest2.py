import usb.core

dev = usb.core.find(idVendor=0x1bad, idProduct=0x0003)

if dev is None :
	raise ValueError('device not found')

dev.set_configuration()

ep = usb.util.find_descriptor(
	dev.get_interface_altsetting(),
	custom_match = \
		lambda e: \
			usb.util.endpoint_direction(e.bEndpointAddress) == \
			usb.util.ENDPOINT_OUT)
assert ep is not None

print ep
