from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/registrar", methods=["GET"])
def registrar():
    usuario = request.args.get("usuario")
    tipo = request.args.get("tipo")
    valor = request.args.get("valor")
    ip = request.remote_addr
    hora = datetime.utcnow().isoformat()

    print(f"[{hora}] IP={ip}, Usuario={usuario}, Tipo={tipo}, Valor={valor}")

    # grava num arquivo CSV simples (ou outro)
    with open("registros.csv", "a", encoding="utf-8") as f:
        f.write(f"{hora},{ip},{usuario},{tipo},{valor}\n")

    return {"status": "ok"}

@app.route("/")
def home():
    return "Server está ativo"
