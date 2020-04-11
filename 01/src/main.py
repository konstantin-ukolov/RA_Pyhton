#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def do_something():
    print("Do...")
    time.sleep(2)
    print("Done")


def do_something_else():
    print("Do smt else...")
    time.sleep(3)
    print("Done")


if __name__ == '__main__':
    for x in range(3):
        do_something()
        do_something_else()






