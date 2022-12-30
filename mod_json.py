import generic.mod_constants as c
import mod_astrodata as data
import drawCharts.mod_drawChart as dc
import json

def dump_astrodata_injson():
    with open('./database/astrodata.json', 'w') as json_astrodatafile:
        json.dump(dict(data.charts), json_astrodatafile, indent=4)
    return

def load_birthdatas():
    with open('./database/birthdatas.json', 'r') as json_birthfile:        
        data.birthdatas = json.loads(json_birthfile.read()) 
    return

def load_drawChartConfig():
    with open('./drawCharts/chartDraw_cfg.json', 'r') as json_birthfile:        
        dc.chartCfg = json.loads(json_birthfile.read()) 
    return

def get_birthdata(id):
    load_birthdatas()
    needed_birthdata = data.birthdatas.get(id, "NOT_FOUND")
    #check if the element with ID exists
    if ("NOT_FOUND" == needed_birthdata):
        #Element cannot be fetched
        print(f'Given ID {id} doesnt exist. So can not be fetched')
    return needed_birthdata
    
def dump_birthdatas_injson():
    with open('./database/birthdatas.json', 'w') as json_birthfile:
        json.dump(dict(data.birthdatas), json_birthfile, indent=4)
    return

def add_birthdata2DB(birthdata, id):
    #check if the element with ID already exists
    if ("NOT_FOUND" == data.birthdatas.get(id, "NOT_FOUND")):
        #New element -can be added
        data.birthdatas[id] = birthdata
        return True
    else:   #element already exist and so not possible to add
        print(f'Given ID {id} already exists. So can not be added')
        return False

