#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_main.py -- main module. All chart, vimshottari and bala calculations 
# are triggered from here
#
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from <YET TO BE DONE>
#
# This file is part of the "jyotiSHYAma" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

import mod_constants as c
import mod_lagna
import mod_astrodata as data

if __name__ == "__main__":
    #print(data.lagna_ascendant)
    mod_lagna.compute_lagnaChart()
    print("Updated lagna")
    print(data.lagna_ascendant)
    print("planetary data")
    print(data.lagna_planets)