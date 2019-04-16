#!/usr/bin/env python

import os
import sh

filename='test_file.txt'

try:
    print(sh.ls('-al', filename))
except:
    print(f"{filename} was not found")
    pass

sh.touch(filename)

print(sh.ls('-al', filename))

os.unlink(filename)
