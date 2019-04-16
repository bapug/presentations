#!/usr/bin/env python

import sh


filename = 'test_file.txt'

with open(filename, 'w') as fp:
    for x in range(100):
        fp.write(f"Writing line {x} at line {x}")


