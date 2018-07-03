#!/usr/bin/env python2.7
import houndify
import sys
sys.path.append('.')
from pprint import pprint
import json
import csv

#CSV input file given from the user
TESTCSV = sys.argv[1]

# Client ID and Client Key are fixed for this user.
# Note: Hard coded here for ease of use.
CLIENT_ID = "9y_3gUuFUrAZu5w9XOKTOA=="
CLIENT_KEY = "OPBiPm_ceOBCGX9-2VQXniIKm259iCVhn68s3VUa_DX5ny3HMdelLMMR8ysunObHplLdhKMuWi02dTieM-aFjQ=="

requestInfo = {
  # Pretend we're at SoundHound HQ.  Set other fields as appropriate
  'Latitude': 37.388309, 
  'Longitude': -121.973968
}

# Create a client based on the client ID and Client KEY
client = houndify.TextHoundClient(CLIENT_ID, CLIENT_KEY, "test_user", requestInfo)

# open the csv file for input and output checking
with open(TESTCSV, 'r') as csvfile:
    errcount = 0
    readCSV = csv.reader(csvfile, delimiter=',')
    for num, row in enumerate(readCSV):
        if (num > 1):
            # Ensure no empty requests are sent
            if row[0] != "":
                print "Sending this Query: ", row[0]
                response = client.query(row[0])
                # Only proceed further when the status is OK
                if(response["Status"] == "OK"):
                    try:
                        # printing the query results
                        pprint(response["AllResults"][0]["WrittenResponseLong"])
                        pprint(response["AllResults"][0]["CommandKind"])
                        pprint(response["AllResults"][0]["InformationNuggets"][0]["NuggetKind"])
                        pprint(response["AllResults"][0]["InformationNuggets"][0]["WeatherNuggetKind"])

                        #checking against the csv expected output
                        if(str(response["AllResults"][0]["CommandKind"]) != str(row[1])):
                            pprint("Error: CommandKind is incorrect")
                            errcount += 1

                        if(str(response["AllResults"][0]["InformationNuggets"][0]["NuggetKind"]) != str(row[2])):
                            pprint("Error: NuggetKind is incorrect")
                            errcount += 1

                        if(str(response["AllResults"][0]["InformationNuggets"][0]["WeatherNuggetKind"]) != str(row[3])):
                            pprint("Error: WeatherNuggetKind is incorrect")
                            errcount += 1
                    except:
                        pass
                else:
                    pprint("Status error!")
                pprint("**************************************************")

    if(errcount > 0):
        pprint("ERROR: Test failed!")
    else:
        pprint("SUCCESS: Test passed!")
