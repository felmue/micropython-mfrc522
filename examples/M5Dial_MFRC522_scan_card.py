from machine import Pin, I2C
i2c0 = I2C(0, scl=Pin(12), sda=Pin(11), freq=400000) # M5Dial (internal)
from mfrc522 import MFRC522
rdr = MFRC522(i2c0)
version = rdr.version()
print("Version: %d" % version)

while True:
  (stat, tag_type) = rdr.request(rdr.REQIDL)
  if stat == rdr.OK:
    (stat, raw_uid) = rdr.anticoll()
    if stat == rdr.OK:
      print("New card detected")
      print("  - tag type: 0x%02x" % tag_type)
      print("  - uid: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
      print("")
