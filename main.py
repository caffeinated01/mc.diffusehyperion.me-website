import requests
from flask import Flask, render_template

app = Flask(__name__,template_folder='template')

@app.route("/")
def ping_map():
    url = "https://map.diffusehyperion.me"

    try:
        response = requests.get(url)
        response.raise_for_status()
        message = "DiffuseHyperion did not screw up his server map"
        status_class = "success"
    except requests.exceptions.HTTPError as err:
        message = f"DiffuseHyperion has ran into a skill issue, {err}"
        status_class = "error"

    return render_template("index.html", message=message, status_class=status_class)

if __name__ == "__main__":
    app.run()
