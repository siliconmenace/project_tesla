# -*- coding: utf-8 -*-
import usb.core
import usb.util
import sys

# find our device
dev = usb.core.find(idVendor=0x1bad, idProduct=0x0003)

# was it found?
if dev is None:
    raise ValueError('Device not Found')

dev.set_configuration()
cfg = dev.get_active_configuration()
interface_number = cfg[(0,0)].bInterfaceNumber


intf = usb.util.find.descriptor(
    cfg, bInterfaceNumber = interface_number,
    bAlternateSetting = 0
    )

##for cfg in dev:
##    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
##    for intf in cfg:
##        sys.stdout.write('\t' + str(intf.bInterfaceNumber)
