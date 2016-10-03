import requests
import json
import time

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid":        ['CES0000000001','CES1000000001','CES2000000001','CES3000000001','CES4000000001','CES5000000001','CES5500000001','CES6000000001','CES6500000001','CES7000000001','CES8000000001','CES9091000001','CES9092000001','CES9093000001'],"startyear":"2012", "endyear":"2012"})
p = requests.post('http://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
print (p.url)
print (p.content)
json_data = json.loads(p.text)
d_results = json_data['Results']  #Dictionary: seriesID: str, data: list of data by date
l_series = d_results['series']    #List of Dictionaries

timestr = time.strftime("%Y%m%d-%H%M")

makeheader = 'True'
f=open('bls' + '-' + timestr + '.csv','w')
for lst in l_series:
    tmp = lst                   #Dictionary: seriesID: str, data: list of data observation dictionaries
#    type(tmp)
    tmpp = tmp['data']          #List of data observation dictionaries
    if makeheader == 'True':
        for ent in tmp['data']:
            f.write( ',' + ent['year'] + ":" + ent['period'] ),  #create observation marker as YYYY:MM
        makeheader = 'False'
    f.write('\n')
    f.write(tmp['seriesID'] ),
    for ent in tmp['data']:
        f.write(',' + ent['value'] ),
f.close
