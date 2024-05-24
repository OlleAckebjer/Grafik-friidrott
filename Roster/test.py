email = "olle.ackebjer@gmail.com"
psw = "Friidrott18"

import requests
import csv
from io import StringIO


login_url = f"https://api.admin.rosterathletics.com/api/login"

# Skapa ett Session-objekt för att hantera cookies
session = requests.Session()


# Utför Curl-anropet för att logga in och spara cookies
login_data = {
    'username': email,
    "password": psw
}


session.post(login_url, data=login_data)

comp_id = 24406
#gren_id = 165626
gren_id = 165623
url = f"https://api.admin.rosterathletics.com/api/admin/meeting/{comp_id}/export-event/{gren_id}"

data_response = session.get(url)
data_response.encoding = 'utf-8'
csv_string = (data_response.text)
""" print(results)
print(len(results))
print(results[0]) """

csv_file = StringIO(csv_string)

# Use csv.reader to parse the CSV file-like object
csv_reader = csv.reader(csv_file)

# Convert the CSV data into a list of lists
data = list(csv_reader)

name_index = data[0].index("FullName")
pb_index = data[0].index("PersonalBest")
sb_index = data[0].index("SeasonBest")
klubb_index = data[0].index("ShortClubName")
resultat_index = data[0].index("Result")
position_index = data[0].index("PositionHeat")
resultat_status_index = data[0].index("StartStatus")
resultat_status_1_index = data[0].index("Round1Status")




print(data[0])
name = []
pb = []
sb = []
klubb = []
resultat = []
position = []
resultat_tot = []
resultat_status = []

for row in data[1:]:
    name.append(row[name_index])
    pb.append(row[pb_index])
    sb.append(row[sb_index])
    klubb.append(row[klubb_index])
    resultat.append(row[resultat_index])
    position.append(row[position_index])

    resultat_tot.append(row[resultat_status_1_index:-1])
    resultat_status.append(row[resultat_status_index])






resultat_full = []
for i in resultat_tot:
    resultat_per_aktiv = []
    for x in range(0, len(i), 7):
        if i[x+4] == "xxx" or i[x+4]=="":
            break
        
        resultat_per_aktiv.append([i[x+4], i[x+5]])

    resultat_full.append(resultat_per_aktiv)

""" print(name)
print(pb)
print(sb)
print(klubb)
print(resultat_full) """

for i in range(len(name)):
    print(name[i], pb[i], sb[i], klubb[i], resultat[i], position[i], resultat_status[i])
    print(resultat_full[i])


['Result', 'PositionHeat', 'HeatName', 'Round1Status', 'Round1Record', 'Round1Records', 'Round1Result', 'Round1Attempts', 'Round1TargetHeight', 'Round1Wind', 'Round2Status', 'Round2Record', 'Round2Records', 'Round2Result', 'Round2Attempts', 'Round2TargetHeight', 'Round2Wind', 'Round3Status', 'Round3Record', 'Round3Records', 'Round3Result', 'Round3Attempts', 'Round3TargetHeight', 'Round3Wind', 'Round4Status', 'Round4Record', 'Round4Records', 'Round4Result', 'Round4Attempts', 'Round4TargetHeight', 'Round4Wind', 'Round5Status', 'Round5Record', 'Round5Records', 'Round5Result', 'Round5Attempts', 'Round5TargetHeight', 'Round5Wind', 'Round6Status', 'Round6Record', 'Round6Records', 'Round6Result', 'Round6Attempts', 'Round6TargetHeight', 'Round6Wind', 'Round7Status', 'Round7Record', 'Round7Records', 'Round7Result', 'Round7Attempts', 'Round7TargetHeight', 'Round7Wind', 'Round8Status', 'Round8Record', 'Round8Records', 'Round8Result', 'Round8Attempts', 'Round8TargetHeight', 'Round8Wind', 'Round9Status', 'Round9Record', 'Round9Records', 'Round9Result', 'Round9Attempts', 'Round9TargetHeight', 'Round9Wind', 'Round10Status', 'Round10Record', 'Round10Records', 'Round10Result', 'Round10Attempts', 'Round10TargetHeight', 'Round10Wind', 'Round11Status', 'Round11Record', 'Round11Records', 'Round11Result', 'Round11Attempts', 'Round11TargetHeight', 'Round11Wind', 'Round12Status', 'Round12Record', 'Round12Records', 'Round12Result', 'Round12Attempts', 'Round12TargetHeight', 'Round12Wind', 'Round13Status', 'Round13Record', 'Round13Records', 'Round13Result', 'Round13Attempts', 'Round13TargetHeight', 'Round13Wind', 'Round14Status', 'Round14Record', 'Round14Records', 'Round14Result', 'Round14Attempts', 'Round14TargetHeight', 'Round14Wind', 'Round15Status', 'Round15Record', 'Round15Records', 'Round15Result', 'Round15Attempts', 'Round15TargetHeight', 'Round15Wind', 'Round16Status', 'Round16Record', 'Round16Records', 'Round16Result', 'Round16Attempts', 'Round16TargetHeight', 'Round16Wind']



'ResultRounded', 'ResultNET', 'ReactionTime', 'SplitTime', 'LapTime', 'CombinedPoints', 'WindReading', 'PositionHeat', 'HeatName',
['5.20', '1', '0', 'ok', '', '', '', 's', '4.30', '', 'ok', '', '', '', 's', '4.45', '', 'ok', '', '', '', 's', '4.60', '', 'ok', '', '', '', 's', '4.75', '', 'ok', '', '', '', 's', '4.90', '', 'ok', '', '', '5.00', 'o', '5.00', '', 'ok', '', '', '', 's', '5.10', '', 'ok', 'SB', 'SB', '5.20', 'xxo', '5.20', '', 'ok', '', '', '', '', '5.25', '', 'ok', '', '', '', '', '5.30', '', 'ok', '', '', '', '', '5.35', '', 'ok', '', '', '', '', '5.40', '', 'ok', '', '', '', '', '5.45', '', 'ok', '', '', '', '', '5.50', '', 'ok', '', '', '', '', '5.55', '', 'ok', '', '', '', '', '5.60', '']
