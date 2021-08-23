"""
This python script gets country data from 'https://restcountries.eu/rest/v2/all'
then uses data from that to create a db.json file. It also adds fake weather data
to each country in this file, because real weather data requires an api key
"""
import json
import requests
from random import randint, choice

def main():
    fields = "name;capital;population;languages;flag" #only care about these fields from api
    countryData = json.loads(requests.get(f"https://restcountries.eu/rest/v2/all?fields={fields}").text)
    #add random weather data
    for country in countryData:
        country['temp'] = f"{randint(0, 100)}"
        country['wind'] = choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"])
        #country['img'] = f"react/res/{choice(['lightning', 'rain', 'snow', 'sun'])}.png"
    with open("react/db.json", "w+") as db:
        finalDict = dict()
        finalDict["countries"] = countryData #proper formatting to be read by react
        db.seek(0) #overwrite whatever is in the file if it exists
        db.truncate()
        db.write(json.dumps(finalDict, indent=3)) #write to file

main()