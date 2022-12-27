#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_general.py -- module General. All general computations for any chart [D1-D60 charts]
#
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from <YET TO BE DONE>
#
# This file is part of the "jyotiSHYAma" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

import mod_constants as c

nakshatras = [  "Ashwini", "Bharani", "Kritika", 
                "Rohini", "Mrigashira", "Ardra", 
                "Punarvasu", "Pushya", "Ashlesha", 
                "Magha", "Purva Phalguni", "Uttara Phalguni", 
                "Hasta", "Chitra", "Swati", 
                "Vishaka", "Anurada", "Jyeshta", 
                "Mula", "Purva Ashadha", "Uttara Ashadha", 
                "Shravana", "Dhanishta", "Shatabhishak", 
                "Purva Bhadrapada", "Uttara Bhadrapada", "Revati" ]

nakshatra_rulers = [    "Ketu", "Venus", "Sun", 
                        "Moon", "Mars", "Rahu", 
                        "Jupiter", "Saturn", "Mercury", 
                        "Ketu", "Venus", "Sun", 
                        "Moon", "Mars", "Rahu", 
                        "Jupiter", "Saturn", "Mercury", 
                        "Ketu", "Venus", "Sun", 
                        "Moon", "Mars", "Rahu", 
                        "Jupiter", "Saturn", "Mercury", ]

nakshatra_dieties = [   "Ashwini kumaras", "Yama", "Agni", 
                        "Bramha", "Soma", "Rudra", 
                        "Aditi", "Brihaspathi", "Nagas", 
                        "Pitris", "Aryaman", "Bhaga", 
                        "Surya", "Vishwakarma", "Vaayu", 
                        "Indra - Agni", "Mitra", "Indra", 
                        "Niriti", "Apah", "Vishwe Devatas", 
                        "Vishnu", "Ashta Vasu", "Varuna", 
                        "Ajikapada", "Ahir Budhyana", "Pushan" ]

signs = [ "Aries",       "Taurus",    "Gemini",   "Cancer",
          "Leo",         "Virgo",     "Libra",    "Scorpio",
          "Saggitarius", "Capricorn", "Aquarius", "Pisces",
        ]

rashis = ["Mesha",       "Vrushaba",  "Mithuna",  "Karka",
          "Simha",       "Kanya",     "Tula",     "Vruschika",
          "Dhanu",       "Makara",    "Kumbha",   "Meena",
         ]

signlords = [ "Mars",    "Venus",     "Mercury",  "Moon",
              "Sun",     "Mercury",   "Venus",    "Mars",
              "Jupiter", "Saturn",    "Saturn",   "Jupiter",
            ]

signtatvas = [  c.FIRE, c.EARTH, c.AIR, c.WATER,
                c.FIRE, c.EARTH, c.AIR, c.WATER,
                c.FIRE, c.EARTH, c.AIR, c.WATER,
             ]

planets = [ "Sun",      "Moon",     "Mars",
            "Mercury",  "Jupiter",  "Venus",
            "Saturn",   "Rahu",     "Ketu"
          ]

exhaltation_signs = [   "Aries",        "Taurus",       "Capricorn",
                        "Virgo",        "Cancer",       "Pisces",
                        "Libra",        "Taurus",       "Scorpio"
                    ]

debilitation_signs = [  "Libra",        "Scorpio",      "Cancer",
                        "Pisces",       "Capricorn",    "Virgo",
                        "Aries",        "Scorpio",      "Taurus"
                     ]

diety_of_nakshatra = dict(zip(nakshatras, nakshatra_dieties))
ruler_of_nakshatra = dict(zip(nakshatras, nakshatra_rulers))
lord_of_sign       = dict(zip(signs, signlords))
lord_of_rashi      = dict(zip(rashis, signlords))
tatva_of_sign      = dict(zip(signs, signtatvas))
tatva_of_rashi     = dict(zip(rashis, signtatvas))
exhaltationSign_of_planet  = dict(zip(planets, exhaltation_signs))
debilitationSign_of_planet = dict(zip(planets, debilitation_signs))

signnum = lambda signstr: signs.index(signstr) + 1

if __name__ == "__main__":
    print(signnum("Scorpio"))
    #print(debilitationSign_of_planet)