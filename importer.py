import csv
import json
import copy
from itertools import groupby

data = []
years = list(str(y) for y in [2012]+list(range(2015,2051,5)))
with open('data/ghg_emissions_scenarios.csv') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        data.extend(
            list(
                {'scenario':row['Scenario'],
                 'sector':row['CommoditySetDesc\\Period'],
                 'year': year,
                 'value': row[year]
                 } for year in years)
        )

grouper = lambda r: (r['year'])
scenario_grouper = lambda r: (r['scenario'])
sector_grouper = lambda r: (r['sector'])

data.sort(key=scenario_grouper)
scenarios = {}
for d in data:
    scenario = d['scenario']
    sector = d['sector'][:-10]
    year = d['year']
    value = d['value']
    if scenario not in scenarios:
        scenarios[scenario] = {}
    if sector not in scenarios[scenario]:
        scenarios[scenario][sector] = years.copy()
    scenarios[scenario][sector][years.index(year)] = int(value)

percent = copy.deepcopy(scenarios)

for scenario in percent:
    totals = [0]*len(years)
    for sector in percent[scenario]:
        for year in range(0, len(years)):
            totals[year] += percent[scenario][sector][year]
    #print('tot ',totals)
    for sector in percent[scenario]:
        percent[scenario][sector] = list(v[0]/v[1]*100 for v in zip(percent[scenario][sector],totals))
        #print(sector, '\t', percent[scenario][sector])

#print(percent)

#print(json.dumps({'values': scenarios, 'percent': percent}))

#print(json.dumps(all, indent=True))

RENEWABLES_SHARE ='''2012	2015	2020	2025	2030	2035	2040	2045	2050
NDC2_BAU	6%	6%	11%	13%	17%	18%	22%	21%	24%
NDC2_CNE	6%	6%	15%	25%	34%	37%	47%	51%	56%
NDC2_Opt_BAU	6%	6%	11%	12%	16%	19%	23%	23%	25%
NDC2_Opt_CNE	6%	6%	13%	25%	36%	43%	57%	60%	64%
NDC2_Opt_REF	6%	6%	14%	20%	31%	43%	50%	55%	58%
NDC2_REF	6%	6%	14%	21%	30%	41%	47%	47%	45%
NDC2_S2C	6%	6%	14%	24%	35%	38%	51%	52%	55%
NDC2_S2D	6%	6%	15%	25%	35%	37%	49%	50%	56%
NDC2_S2F	6%	6%	14%	25%	36%	38%	45%	51%	62%
NDC2_S2G	6%	6%	14%	25%	36%	40%	45%	52%	56%
NDC2_S2S	6%	6%	14%	25%	35%	38%	44%	50%	54%
NDC2_S3E	6%	6%	15%	25%	35%	44%	68%	79%	82%
NDC2_S3F	6%	6%	14%	25%	36%	40%	53%	65%	78%
NDC2_S3G	6%	6%	14%	25%	35%	40%	48%	52%	62%
UGD_NewPolicy	6%	6%	15%	26%	31%	36%	51%	63%	73%'''

scenarios = {}
for l in RENEWABLES_SHARE.split('\n')[1:]:
    scenario = l.split('\t')
    scenarios[scenario[0]] = list(int(x[:-1]) for x in scenario[1:])
print(json.dumps(scenarios, indent=True))
