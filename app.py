import requests

@app.route("/registrar")
def registrar():
    params = request.args.to_dict()
    params["ip"] = request.headers.get("X-Forwarded-For", request.remote_addr)

    url = "https://script.google.com/macros/s/AKfycbwcmuQ8ewoMlM9jl4pUIltGxTN6cLcLcJjYLH3bFef8FMHVaFRGKA_vUDMGLKF6GhOnWA/exec"
    r = requests.get(url, params=params)

    return r.text
