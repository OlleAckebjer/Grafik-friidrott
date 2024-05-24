from flask import Blueprint, render_template, jsonify, request
from .extensions import session

main = Blueprint("main", __name__)
import csv
from io import StringIO

@main.route("/admin")
def index():
    

    return render_template("index.html")

@main.route("/get_aktiva", methods=["POST"])
def get_aktiva():
    data = request.get_json()
    print(data)
    if data == "Kvinnor Stav A":
        gren_id = 165623
    elif data == "Män Stav A":
        gren_id = 165626
    
    comp_id = 24406

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
    id_index = data[0].index("EntryId")

    aktiva = []
    aktiva_id = []
    for row in data[1:]:
        aktiva.append(row[name_index])
        aktiva_id.append(row[id_index])

    return jsonify(aktiva, aktiva_id)

@main.route("/display")
def display():
    return render_template("display.html")  


""" @main.route("/send_data")
def send_data():
    data = "Hello, frontend!"  # The data you want to send
    sse.publish(data, type="data_event")  # Publish the data to SSE clients
    return "Data sent to SSE clients" """