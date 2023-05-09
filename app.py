import requests
from flask import Flask, render_template

app = Flask(__name__,template_folder='template')

@app.route("/")
def ping_map():
    url = "https://map.diffusehyperion.me"

    try:
        response = requests.get(url)
        response.raise_for_status()

        status = "Online!"
        status_class = "success"
    except requests.exceptions.HTTPError as err:
        code = int(str(err)[:3])

        status = ""
        if code == 502:
            status = "Offline..."
        else:
            status = "Catastrophically Offline!"
        status_class = "error"

    return render_template("index.html", status_class=status_class, status=status)

if __name__ == "__main__":
    app.run()
