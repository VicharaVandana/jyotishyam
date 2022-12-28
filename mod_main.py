#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_main.py -- main module. All chart, vimshottari and bala calculations 
# are triggered from here
#
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

import generic.mod_constants as c
import chart_calc.mod_lagna as mod_lagna
import mod_astrodata as data
import mod_json as js

if __name__ == "__main__":
    #print(data.lagna_ascendant)
    #data.birthdata = js.get_birthdata("Shyam-Self")
    mod_lagna.compute_lagnaChart()
    #print("Updated lagna")
    #print(data.lagna_ascendant)
    print("START")
    #print(data.lagna_planets["Sun"])
    #print(data.D1["houses"])
    js.dump_astrodata_injson()
    #js.load_birthdatas()
    #print(js.add_birthdata2DB(data.birthdata, "Shyam-Self"))
    #print(data.birthdatas)
    #js.dump_birthdatas_injson()
    print("END")
    

