import requests
from flask import Flask, render_template
from mcstatus import JavaServer

app = Flask(__name__)


@app.route("/")
def index():
    map_url = "https://map.diffusehyperion.me"
    server_url = "mc.diffusehyperion.me"

    try:
        response = requests.get(map_url)
        response.raise_for_status()
        map_status = "Online!"
        map_status_class = "success"
    except requests.exceptions.HTTPError as err:
        code = int(str(err)[:3])
        map_status = ""

        if code == 502:
            map_status = "Offline!"
        else:
            map_status = "Catastrophically Offline!!"
        map_status_class = "error"

    try:
        server = JavaServer.lookup(server_url)
        status = server.ping()
        server_status = "Offline!"
        server_status_class = "error"
    except:
        server_status = "Online!"
        server_status_class = "success"

    return render_template("index.html", map_status_class=map_status_class, map_status=map_status, server_status_class=server_status_class, server_status=server_status)


@app.route('/info.html')
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run()
