# Copyright (c) 2016 Stefan Wendler (original work)
# Copyright (c) 2023 by GWENDESIGN. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from machine import Pin, I2C
i2c0 = I2C(0, scl=Pin(12), sda=Pin(11), freq=400000) # M5Dial (internal)
from mfrc522 import MFRC522
rdr = MFRC522(i2c0)
version = rdr.version()
print("Version: %d" % version)
