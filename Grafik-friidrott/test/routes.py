from flask import Blueprint, render_template
from .extensions import sse

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/display")
def display():
    return render_template("display.html")  


@main.route("/send_data")
def send_data():
    data = "Hello, frontend!"  # The data you want to send
    sse.publish(data, type="data_event")  # Publish the data to SSE clients
    return "Data sent to SSE clients"