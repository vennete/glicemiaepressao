from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "API genérica rodando 🚀 — use /registrar?var1=abc&var2=def..."

@app.route("/registrar", methods=["GET"])
def registrar():
    # pega todos os parâmetros passados na URL
    params = request.args.to_dict()

    # captura IP real do usuário (Render pode usar X-Forwarded-For)
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    # data/hora UTC
    hora = datetime.utcnow().isoformat()

    # adiciona ip e hora ao dicionário
    params["ip"] = ip
    params["hora"] = hora

    # log no console do servidor (aparece nos logs do Render)
    print(f"[{hora}] IP={ip}, PARAMS={params}")

    # retorna JSON
    return params
