# Untitled - By: kutenai - Wed Aug 10 2016

import sensor

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames()

while(True):
    img = sensor.snapshot()


