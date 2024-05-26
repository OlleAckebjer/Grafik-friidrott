from flask_socketio import emit

from .extensions import socketio, session
import csv
from io import StringIO



""" @socketio.on("send_color")
def handle_change_color(color):
    
    emit("change_color", color, broadcast=True)

@socketio.on("send_text")
def handle_change_text(text):
    
    emit("change_text", text, broadcast=True) """

@socketio.on("show_startlista")
def handle_show_startlista(gren):
    
    
    if gren == "Kvinnor Stav A":
        gren_id = 201734 
    elif gren == "Män Stav A":
        gren_id = 201736 
    
    comp_id = 25050 
    url = f"https://api.admin.rosterathletics.com/api/admin/meeting/{comp_id}/export-event/{gren_id}"
    
    
    data_response = session.get(url)
    data_response.encoding = 'utf-8'

    csv_string = (data_response.text)
    
    csv_file = StringIO(csv_string)

    # Use csv.reader to parse the CSV file-like object
    csv_reader = csv.reader(csv_file)

    # Convert the CSV data into a list of lists
    data = list(csv_reader)

    print(data[0])
    print(data[1])
    print(len(data))


    name_index = data[0].index("FullName")
    """ pb_index = data[0].index("PersonalBest")
    sb_index = data[0].index("SeasonBest") """
    klubb_index = data[0].index("ShortClubName")
    status_index = data[0].index("StartStatus")



    event_id_index = data[0].index("EventGroup")
    
    name = []
    """ pb = []
    sb = [] """
    klubb = []
    ordning = []
    x=1    
    for row in data[1:]:
        if row[status_index] != "DNS" and row[event_id_index] == "1":
            name.append(row[name_index])
            """ pb.append(row[pb_index])
            sb.append(row[sb_index]) """
            klubb.append(row[klubb_index])
            ordning.append(x)
            x+=1

    startlista = [ordning, name, klubb]
    

    emit("change_startlista", [startlista, gren], broadcast=True)


@socketio.on("show_results")
def handle_show_results(gren):
    if gren == "Kvinnor Stav A":
        gren_id = 201734 
    elif gren == "Män Stav A":
        gren_id = 201736 
    
    comp_id = 25050 
    url = f"https://api.admin.rosterathletics.com/api/admin/meeting/{comp_id}/export-event/{gren_id}"
    
    
    data_response = session.get(url)
    data_response.encoding = 'utf-8'

    csv_string = (data_response.text)
    
    csv_file = StringIO(csv_string)

    # Use csv.reader to parse the CSV file-like object
    csv_reader = csv.reader(csv_file)

    # Convert the CSV data into a list of lists
    data = list(csv_reader)

    name_index = data[0].index("FullName")
    klubb_index = data[0].index("ShortClubName")
    results_index = data[0].index("Result")
    position_index = data[0].index("PositionHeat")
    event_id_index = data[0].index("EventGroup")

    position = []
    name = []
    results = []
    klubb = []
    
    for row in data[1:]:
        if row[event_id_index] == "1":
            name.append(row[name_index])
            results.append(row[results_index])
            klubb.append(row[klubb_index])
            position.append(row[position_index])

    results_lista = [position, name, klubb, results]

    print(results_lista)

    emit("change_results", [results_lista, gren], broadcast=True)


@socketio.on("show_namnskylt")
def handle_show_namnskylt(gren, aktiv):
    if gren == "Kvinnor Stav A":
        gren_id = 201734 
    elif gren == "Män Stav A":
        gren_id = 201736 
    
    comp_id = 25050 
    url = f"https://api.admin.rosterathletics.com/api/admin/meeting/{comp_id}/export-event/{gren_id}"
    
    
    data_response = session.get(url)
    data_response.encoding = 'utf-8'

    csv_string = (data_response.text)
    
    csv_file = StringIO(csv_string)

    # Use csv.reader to parse the CSV file-like object
    csv_reader = csv.reader(csv_file)

    # Convert the CSV data into a list of lists
    data = list(csv_reader)

    id_index = data[0].index("EntryId")
    name_index = data[0].index("FullName")
    pb_index = data[0].index("PersonalBest")
    sb_index = data[0].index("SeasonBest")
    klubb_index = data[0].index("ShortClubName")




    id_lista = []
    name = []
    pb = []
    sb = []
    klubb = []
    for row in data[1:]:
        name.append(row[name_index])
        pb.append(row[pb_index])
        sb.append(row[sb_index])
        klubb.append(row[klubb_index])
        id_lista.append(row[id_index])

    aktiv_index = id_lista.index(aktiv)
    
    namnskylt = [name[aktiv_index], klubb[aktiv_index], "SB: " + sb[aktiv_index], "PB: " + pb[aktiv_index]]

    print(namnskylt)

    emit("change_namnskylt", namnskylt, broadcast=True)


@socketio.on("show_enskild_resultat")
def handle_show_enskild_resultat(gren, aktiv):
    if gren == "Kvinnor Stav A":
        gren_id = 201734 
    elif gren == "Män Stav A":
        gren_id = 201736 
    
    comp_id = 25050 
    url = f"https://api.admin.rosterathletics.com/api/admin/meeting/{comp_id}/export-event/{gren_id}"
    
    
    data_response = session.get(url)
    data_response.encoding = 'utf-8'

    csv_string = (data_response.text)
    
    csv_file = StringIO(csv_string)

    # Use csv.reader to parse the CSV file-like object
    csv_reader = csv.reader(csv_file)

    # Convert the CSV data into a list of lists
    data = list(csv_reader)

    id_index = data[0].index("EntryId")
    name_index = data[0].index("FullName")
    klubb_index = data[0].index("ShortClubName")
    position_index = data[0].index("PositionHeat")
    resultat_status_1_index = data[0].index("Round1Status")




    resultat_tot = []
    placering = []
    id_lista = []
    name = []
    klubb = []
    for row in data[1:]:
        name.append(row[name_index])
        klubb.append(row[klubb_index])
        id_lista.append(row[id_index])
        placering.append(row[position_index])
        resultat_tot.append(row[resultat_status_1_index:-1])


    aktiv_index = id_lista.index(aktiv)


    resultat_enskild = []
    for x in range(0, len(resultat_tot[aktiv_index]), 7):
        resultat_enskild.append([resultat_tot[aktiv_index][x+5], resultat_tot[aktiv_index][x+4]])
        
        if resultat_tot[aktiv_index][x+4] == "xxx" or resultat_tot[aktiv_index][x+4]=="":
            break
        
    resultatskylt = [placering[aktiv_index], name[aktiv_index], klubb[aktiv_index], resultat_enskild[-6:]] #placering, namn, klubb, resultatlista

    print(resultatskylt)
    
    emit("change_resultatskylt", resultatskylt, broadcast=True)


""" 
@socketio.on("send_results")
def handle_send_results(gren_id):
        comp_id = 24406
        #gren_id = 165626
        gren_id = 165623
        url = f"https://api.admin.rosterathletics.com/api/admin/meeting/{comp_id}/export-event/{gren_id}"

        data_response = session.get(url)
        data_response.encoding = 'utf-8'

        csv_string = (data_response.text)
        
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

        

        for i in range(len(name)):
            print(name[i], pb[i], sb[i], klubb[i], resultat[i], position[i], resultat_status[i])
            print(resultat_full[i])


        results = [name, pb, sb, klubb, resultat, position, resultat_status, resultat_full]

    
        emit("change_results", results, broadcast=True) """

""" import random
import time

@socketio.on("random_color")
def read():
    print("FUNKAR")

    colors = [
            "aliceblue",
            "antiquewhite",
            "aqua",
            "aquamarine",
            "azure",
            "beige",
            "bisque",
            "black",
            "blanchedalmond",
            "blue",
            "blueviolet",
            "brown",
            "burlywood",
            "cadetblue",
            "chartreuse",
            "chocolate",
            "coral",
            "cornflowerblue",
            "cornsilk",
            "crimson",
            "cyan",
            "darkblue",
            "darkcyan",
            "darkgoldenrod",
            "darkgray",
            "darkgreen",
            "darkkhaki",
            "darkmagenta",
            "darkolivegreen",
            "darkorange",
            "darkorchid",
            "darkred",
            "darksalmon",
            "darkseagreen",
            "darkslateblue",
            "darkslategray",
            "darkturquoise",
            "darkviolet",
            "deeppink",
            "deepskyblue",
            "dimgray",
            "dodgerblue",
            "firebrick",
            "floralwhite",
            "forestgreen",
            "fuchsia",
            "gainsboro",
            "ghostwhite",
            "gold",
            "goldenrod",
            "gray",
            "green",
            "greenyellow",
            "honeydew",
            "hotpink",
            "indianred",
            "indigo",
            "ivory",
            "khaki",
            "lavender",
            "lavenderblush",
            "lawngreen",
            "lemonchiffon",
            "lightblue",
            "lightcoral",
            "lightcyan",
            "lightgoldenrodyellow",
            "lightgray",
            "lightgreen",
            "lightpink",
            "lightsalmon",
            "lightseagreen",
            "lightskyblue",
            "lightslategray",
            "lightsteelblue",
            "lightyellow",
            "lime",
            "limegreen",
            "linen",
            "magenta",
            "maroon",
            "mediumaquamarine",
            "mediumblue",
            "mediumorchid",
            "mediumpurple",
            "mediumseagreen",
            "mediumslateblue",
            "mediumspringgreen",
            "mediumturquoise",
            "mediumvioletred",
            "midnightblue",
            "mintcream",
            "mistyrose",
            "moccasin",
            "navajowhite",
            "navy",
            "oldlace",
            "olive",
            "olivedrab",
            "orange",
            "orangered",
            "orchid",
            "palegoldenrod",
            "palegreen",
            "paleturquoise",
            "palevioletred",
            "papayawhip",
            "peachpuff",
            "peru",
            "pink",
            "plum",
            "powderblue",
            "purple",
            "rebeccapurple",
            "red",
            "rosybrown",
            "royalblue",
            "saddlebrown",
            "salmon",
            "sandybrown",
            "seagreen",
            "seashell",
            "sienna",
            "silver",
            "skyblue",
            "slateblue",
            "slategray",
            "snow",
            "springgreen",
            "steelblue",
            "tan",
            "teal",
            "thistle",
            "tomato",
            "turquoise",
            "violet",
            "wheat",
            "white",
            "whitesmoke",
            "yellow",
            "yellowgreen"
        ]

    n = len(colors)
    color = colors[random.randint(0, n)]
    #print(color)

    time.sleep(2)
    emit("change_color", color, broadcast=True) """




''' 
@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None 
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True) '''


