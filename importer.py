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
#print(json.dumps(scenarios, indent=True))

INVESTMENT_REQUIRED ='''2020	2025	2030	2035	2040	2045	2050
NDC2_BAU	83992	103047	111385	96121	155247	132229	147831
NDC2_S2F	89986	136656	160867	108513	133090	130179	150143
NDC2_S2G	89128	134300	156169	111315	149803	133607	136431
NDC2_S2S	90473	133986	155739	113350	150206	132857	136589
NDC2_REF	90764	129677	142663	169349	119091	137765	144642
UGD_NewPolicy	89762	135903	147028	122585	145610	144995	171642
NDC2_S2C	90753	134741	158101	116281	170683	135211	156851
NDC2_S2D	90476	135166	157064	116081	166278	147165	173839
NDC2_Opt_BAU	84445	128265	124923	120650	178299	175764	205299
NDC2_Opt_REF	85486	147959	161693	245111	125257	177681	197496
NDC2_S3F	90164	135163	158623	141488	130172	176294	426142
NDC2_S3G	89265	133984	155747	143744	147271	180578	413429
NDC2_S3E	90564	134410	158035	150786	143583	169585	419109
NDC2_CNE	90358	134502	157354	142606	148813	178399	417710
NDC2_Opt_CNE	84913	150773	176680	217505	157585	236607	1663268'''

scenarios = {}
for l in INVESTMENT_REQUIRED.split('\n')[1:]:
    scenario = l.split('\t')
    scenarios[scenario[0]] = list(int(x[:-1]) for x in scenario[1:])

print(json.dumps(scenarios, indent=True))