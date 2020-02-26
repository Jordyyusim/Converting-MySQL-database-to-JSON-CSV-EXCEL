import mysql.connector
import json
import csv
import xlsxwriter

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '12345',
    database = 'world'
)

# CITY
x = db.cursor(dictionary=True)
x.execute('select * from city')
city = list(x)
citykey = []
cityval = []
DictCity = []
sum = 0
for i in city:
    for data in i.values():
        cityval.append(str(data))
for k in city:
    for data in k.keys():
        citykey.append(data)

cityID = cityval[::5]
cityName = cityval[1::5]
cityCountryCode = cityval[2::5]
cityDistrict = cityval[3::5]
cityPopulation = cityval[4::5]
dataCity = list(zip(cityID, cityName, cityCountryCode, cityDistrict, cityPopulation))
listCity = []
for i in dataCity:
    listCity.append(list(i))

while sum < (len(citykey)):
    dict_city =  {citykey[sum]:cityval[sum]}
    for i in range(sum+1, sum+5):
        dictup = {citykey[i]:cityval[i]}
        dict_city.update(dictup)
    DictCity.append(dict_city)
    sum += 5

#COUNTRY
y = db.cursor(dictionary=True)
y.execute('select * from country')
country = list(y)

countrykey = []
countryvalue = []
for i in country:
    for data in i.values():
        countryvalue.append(str(data))
for k in country:
    for data in k.keys():
        countrykey.append(data)

countryCode = countryvalue[::15]
countryName = countryvalue[1::15]
countryContinent = countryvalue[2::15]
countryRegion = countryvalue[3::15]
countrySurfaceArea = countryvalue[4::15]
countryIndepYear = countryvalue[5::15]
countryPopulation = countryvalue[6::15]
countryLifeExpectancy = countryvalue[7::15]
countryGNP = countryvalue[8::15]
countryGNPOld = countryvalue[9::15]
countryLocalName = countryvalue[10::15]
countryGovernment = countryvalue[11::15]
countryHeadofState = countryvalue[12::15]
countryCapital = countryvalue[13::15]
countryCode2 = countryvalue[14::15]
dataCountry = list(zip(countryCode, countryName, countryContinent, countryRegion, countrySurfaceArea,
                    countryIndepYear, countryPopulation, countryLifeExpectancy, countryGNP, countryGNPOld,
                    countryLocalName, countryGovernment, countryHeadofState, countryCapital, countryCode2))
listCountry = []
for i in dataCountry:
    listCountry.append(list(i))

Dict_Country = []
counter = 0
while counter < (len(countrykey)):
    Dicti =  {countrykey[counter]:countryvalue[counter]}
    for i in range(counter+1,counter+15):
        dictiup = {countrykey[i]:countryvalue[i]}
        Dicti.update(dictiup)
    Dict_Country.append(Dicti)
    counter += 15
# print(Dict_Country)

#COUNTRY LANGUAGE
z = db.cursor(dictionary=True)
z.execute('select * from countrylanguage')
countrylang = list(z)
countrylangval = []
countrylangkey = []
for i in countrylang:
    for data in i.values():
        countrylangval.append(str(data))
for k in countrylang:
    for data in k.keys():
        countrylangkey.append(data)

countrylangCountryCode = countrylangval[::4]
countrylangLanguage = countrylangval[1::4]
countrylangIsOfficial = countrylangval[2::4]
countrylangPercentage = countrylangval[3::4]
dataCountryLang = list(zip(countrylangCountryCode, countrylangLanguage, countrylangIsOfficial, countrylangPercentage))
listCL = []
for i in dataCountryLang:
    listCL.append(list(i))
# print(listCL)

DictCL = []
sum = 0
while sum < (len(countrylangkey)):
    dicti =  {countrylangkey[sum]:countrylangval[sum]}
    for i in range(sum+1, sum+4):
        dictiup = {countrylangkey[i]:countrylangval[i]}
        dicti.update(dictiup)
    DictCL.append(dicti)
    sum += 4

# CITY TABLE TO JSON
# x = db.cursor(dictionary=True)
# x.execute('select * from city')
# city = list(x)
# with open('city.json', 'w') as myjson:
#    json.dump(city, myjson)

# COUNTRY TABLE TO JSON
# with open('country.json', 'w') as myjson:
#    json.dump(Dict_Country, myjson)

#COUNTRYLANGUAGE TABLE TO JSON
# with open('countrylanguage.json', 'w') as myjson:
#    json.dump(DictCL, myjson)

# CITY TABLE TO CSV
# with open('tablecity.csv', 'w', newline='') as x:
#     writer = csv.DictWriter(x, delimiter = ',',fieldnames=['ID', 'Name', 
#                                                         'CountryCode', 'District', 'Population'])
#     writer.writerows(DictCity)

# COUNTRY TABLE TO CSV
# with open('tablecountry.csv', 'w', newline='') as y:
#     writer = csv.DictWriter(y, delimiter = ',',fieldnames=['Code', 'Name', 
#                                                         'Continent', 'Region', 'SurfaceArea', 'IndepYear'
#                                                         ,'Population', 'LifeExpectancy', 'GNP', 'GNPOld'
#                                                         ,'LocalName', 'GovernmentForm', 'HeadOfState'
#                                                         ,'Capital', 'Code2'])
#     writer.writerows(Dict_Country)

#COUNTRY LANGUAGE TABLE TO CSV
# with open('tablecountrylang.csv', 'w', newline='') as z:
#     writer = csv.DictWriter(z, delimiter = ',',fieldnames=['CountryCode', 'Language', 
#                                                         'IsOfficial', 'Percentage'])
#     writer.writerows(DictCL)


# x = db.cursor
# x.execute('select * from city')
# city = list(x)
# citykey = []
# cityval = []
# DictCity = []
# sum = 0
# for i in city:
#     for data in i.values():
#         cityval.append(str(data))
# for k in city:
#     for data in k.keys():
#         citykey.append(data)
# print(citykey)

#CITY TABLE TO EXCEL
book = xlsxwriter.Workbook('db_world_city.xlsx')
sheet = book.add_worksheet('Sheet 1')
row = 0
for cityID, cityName, cityCountryCode, cityDistrict, cityPopulation in listCity:
    sheet.write(row, 0, 'ID')
    sheet.write(row, 1, 'Name')
    sheet.write(row, 2, 'Country Code')
    sheet.write(row, 3, 'District')
    sheet.write(row, 4, 'Population')
row = 1
for cityID, cityName, cityCountryCode, cityDistrict, cityPopulation in listCity:
    sheet.write(row, 0, cityID)
    sheet.write(row, 1, cityName)
    sheet.write(row, 2, cityCountryCode)
    sheet.write(row, 3, cityDistrict)
    sheet.write(row, 4, cityPopulation)
    row += 1

book.close()

# COUNTRY TABLE TO EXCEL
book = xlsxwriter.Workbook('db_world_country.xlsx')
sheet = book.add_worksheet('Sheet 1')
row = 0
for countryCode, countryName, countryContinent, countryRegion, countrySurfaceArea, countryIndepYear, countryPopulation, countryLifeExpectancy, countryGNP, countryGNPOld,countryLocalName, countryGovernment, countryHeadofState, countryCapital, countryCode2 in listCountry:
    sheet.write(row, 0, 'Code')
    sheet.write(row, 1, 'Name')
    sheet.write(row, 2, 'Continent')
    sheet.write(row, 3, 'Region')
    sheet.write(row, 4, 'Surface Area')
    sheet.write(row, 5, 'Indep Year')
    sheet.write(row, 6, 'Population')
    sheet.write(row, 7, 'Life Expectancy')
    sheet.write(row, 8, 'GNP')
    sheet.write(row, 9, 'GNPOld')
    sheet.write(row, 10, 'Local Name')
    sheet.write(row, 11, 'Government')
    sheet.write(row, 12, 'Head of State')
    sheet.write(row, 13, 'Capital')
    sheet.write(row, 14, 'Code 2')
row = 1
for countryCode, countryName, countryContinent, countryRegion, countrySurfaceArea, countryIndepYear, countryPopulation, countryLifeExpectancy, countryGNP, countryGNPOld, countryLocalName, countryGovernment, countryHeadofState, countryCapital, countryCode2 in listCountry:
    sheet.write(row, 0, countryCode )
    sheet.write(row, 1, countryName)
    sheet.write(row, 2, countryContinent)
    sheet.write(row, 3, countryRegion)
    sheet.write(row, 4, countrySurfaceArea)
    sheet.write(row, 5, countryIndepYear)
    sheet.write(row, 6, countryPopulation)
    sheet.write(row, 7, countryLifeExpectancy)
    sheet.write(row, 8, countryGNP)
    sheet.write(row, 9, countryGNPOld)
    sheet.write(row, 10, countryLocalName)
    sheet.write(row, 11, countryGovernment)
    sheet.write(row, 12, countryHeadofState)
    sheet.write(row, 13, countryCapital)
    sheet.write(row, 14, countryCode2)
    row += 1

book.close()

#COUNTRY LANGUAGE TABLE TO EXCEL
book = xlsxwriter.Workbook('db_world_countryLanguage.xlsx')
sheet = book.add_worksheet('Sheet 1')
row = 0
for countrylangCountryCode, countrylangLanguage, countrylangIsOfficial, countrylangPercentage in listCL:
    sheet.write(row, 0, 'Country Code')
    sheet.write(row, 1, 'Language')
    sheet.write(row, 2, 'IsOfficial')
    sheet.write(row, 3, 'Percentage')
row = 1
for countrylangCountryCode, countrylangLanguage, countrylangIsOfficial, countrylangPercentage in listCL:
    sheet.write(row, 0, countrylangCountryCode)
    sheet.write(row, 1, countrylangLanguage)
    sheet.write(row, 2, countrylangIsOfficial)
    sheet.write(row, 3, countrylangPercentage)
    row += 1

book.close()

    