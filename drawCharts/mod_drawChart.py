#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_drawChart.py -- module to Draw AstroCharts. - It creates the astrology charts in svg images. 
#
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

from drawCharts.mod_chartPlanetPositions import planetPosition_northSquareClassic as ppnsc
from drawCharts.mod_chartPlanetPositions import bhavnames, aspectSymbols

chartCfg = {}   #contains all the configurations for drawing chart. Loaded from chartDraw_cfg.json file


def printconfig():
    print(chartCfg)
    return

def draw_classicNorthChartSkeleton(chartSVG):
    # Chart drawing section - Skeleton part for template - north-square-classic
    chartSVG.write(f'''  <rect width="410" height="410" x="5" y="5" style="fill:{chartCfg["background-colour"]};stroke-width:3;stroke:{chartCfg["outerbox-colour"]}" />\n''')
    chartSVG.write(f'''  <polygon id ="tanbhav" points="210,10 110,110 210,210 310,110" style="fill:{chartCfg["house-colour"]["tanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="dhanbhav" points="10,10 210,10 110,110" style="fill:{chartCfg["house-colour"]["dhanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="anujbhav" points="10,10 10,210 110,110" style="fill:{chartCfg["house-colour"]["anujbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="maatabhav" points="110,110 10,210 110,310 210,210" style="fill:{chartCfg["house-colour"]["maatabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="santanbhav" points="10,210 110,310 10,410" style="fill:{chartCfg["house-colour"]["santanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="rogbhav" points="210,410 110,310 10,410" style="fill:{chartCfg["house-colour"]["rogbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="dampathyabhav" points="210,410 110,310 210,210 310,310" style="fill:{chartCfg["house-colour"]["dampathyabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="aayubhav" points="210,410 310,310 410,410" style="fill:{chartCfg["house-colour"]["aayubhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="bhagyabhav" points="310,310 410,410 410,210" style="fill:{chartCfg["house-colour"]["bhagyabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="karmabhav" points="310,310 410,210 310,110 210,210" style="fill:{chartCfg["house-colour"]["karmabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="laabbhav" points="410,210 310,110 410,10" style="fill:{chartCfg["house-colour"]["laabbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="karchbhav" points="310,110 410,10 210,10" style="fill:{chartCfg["house-colour"]["karchbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    return

def write_signnumOnChart_nsc(division, chartSVG):
    chartSVG.write('\n  <!-- ********** Sign Numbers ********** -->\n')
    chartSVG.write(f'''  <text id ="tan" x="193" y="195" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][0]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="dhan" x="97" y="95" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][1]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="anuj" x="70" y="118" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][2]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="maata" x="170" y="218" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][3]["sign-num"]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="santaan" x="75" y="316" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][4]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="rog" x="97" y="335" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][5]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="dampathya" x="195" y="240" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][6]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="aayu" x="296" y="337" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][7]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="bhagya" x="320" y="318" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][8]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karma" x="220" y="218" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][9]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="laab" x="318" y="118" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][10]["sign-num"]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karch" x="298" y="98" fill="{chartCfg["sign-colour"]}" class="sign-num">{division["houses"][11]["sign-num"]:02}</text>\n''')
    return

def get_planetColour(planetname, classification):
    if(planetname in classification["benefics"]):
        #its a benefic planet for the chart. So make it benefic colour
        planetcolour = chartCfg["benefic-planet-colour"]
    elif(planetname in classification["malefics"]):
        #its a malefic planet for the chart. So make it malefic colour
        planetcolour = chartCfg["malefic-planet-colour"]
    elif(planetname in classification["neutral"]):
        #its a neutral planet for the chart. So make it neutral colour
        planetcolour = chartCfg["neutral-planet-colour"]
    else:
        #its not categorised. Control should not come here. So make it neutral colour
        #print(f'The planet {planetname} is not classified as either benefic or malefic or neutral. Fix it.')
        planetcolour = chartCfg["neutral-planet-colour"]
    return(planetcolour)

def write_planetsAspectsOnChart_nsc(division, chartSVG):
    chartSVG.write('\n  <!-- ********** Planets ********** -->\n')
    for houseIdx in range(0,12):    #for all houses
        chartSVG.write(f'  <!-- Aspects -->\n')
        for planetname in division["houses"][houseIdx]["aspect-planets"]:
            planetIdx = division["houses"][houseIdx]["aspect-planets"].index(planetname)
            #compute index of aspect position as planets present in house occupy first and aspects occupy next positions
            planetposIdx = planetIdx + len(division["houses"][houseIdx]["planets"])
            symbol = aspectSymbols[planetname]
            retro = division["planets"][planetname]["retro"]
            #identify the planet colour to be put in chart
            planetcolour = get_planetColour(planetname, division["classifications"])
            #Get planet position co-ordinates x and y on chart svg
            px = ppnsc[houseIdx][planetposIdx]["x"]
            py = ppnsc[houseIdx][planetposIdx]["y"]
            #Since all needed properties are computed, Now create the svg entry string for planet
            if(retro == True):
                Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="planet">{symbol}</text>\n'''
            else:
                Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="planet">{symbol}</text>\n'''
            #write the planet to SVG chart
            chartSVG.write(Planet_SVGstring)
    return

def write_planetsOnChart_nsc(division, chartSVG):
    chartSVG.write('\n  <!-- ********** Planets ********** -->\n')
    for houseIdx in range(0,12):    #for all houses
        chartSVG.write(f'  <!-- {bhavnames[houseIdx]} -->\n')
        chartSVG.write(f'  <!-- Planet placements -->\n')
        for planetname in division["houses"][houseIdx]["planets"]:
            planetIdx = division["houses"][houseIdx]["planets"].index(planetname)
            symbol = division["planets"][planetname]["symbol"]
            retro = division["planets"][planetname]["retro"]
            #identify the planet colour to be put in chart
            planetcolour = get_planetColour(planetname, division["classifications"])
            #Get planet position co-ordinates x and y on chart svg
            px = ppnsc[houseIdx][planetIdx]["x"]
            py = ppnsc[houseIdx][planetIdx]["y"]
            #Since all needed properties are computed, Now create the svg entry string for planet
            if(retro == True):
                Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="planet">{symbol}</text>\n'''
            else:
                Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="planet">{symbol}</text>\n'''
            #write the planet to SVG chart
            chartSVG.write(Planet_SVGstring)
    return

def create_chartSVG(division):
    ''' Creates SVG image of astrology chart as per the chart draw configuration
        with data in division. The divisional chart is mentioned by division and 
        hence named accordingly'''
    # open or create chart file 
    chartSVGfilename = f'{division["name"]}_chart'
    chartSVG = open(f'drawCharts/chart_images/{chartSVGfilename}.svg', 'w',  encoding='utf-16')

    #Write the content into the file
    #SVG chart open section
    chartSVG.write(f'''<svg id="{chartSVGfilename}" height="500" width="500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 22px sans-serif; }\n')
    chartSVG.write('    .planet { font: bold 20px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    #create chart for given template
    if (chartCfg["template"] == "north-square-classic"):
        draw_classicNorthChartSkeleton(chartSVG)    #Create skeleton
        write_signnumOnChart_nsc(division, chartSVG)    #Update the sign numbers on chart skeleton
        write_planetsOnChart_nsc(division, chartSVG)    #Update the planets on chart for every house
        if(chartCfg["aspect-visibility"] == True):
            write_planetsAspectsOnChart_nsc(division, chartSVG)
    
    #SVG chart End section
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')

    #close the file
    chartSVG.close()
    return