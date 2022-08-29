#This programs reads the data from an excel file concerning
#the census result in the USA and then counts the total population
#in each county

import openpyxl, pprint
print("Opening workbook...")

#We open the excel workbook and spreadsheet
wb = openpyxl.load_workbook(r".\censuspopdata.xlsx")
sheet = wb["Population by Census Tract"]
countyData = {}

#calculate
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')