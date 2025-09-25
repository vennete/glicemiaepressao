from flask import Flask, request, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

# URL do seu Apps Script (substitua pelo link gerado)
GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbwvABfJ3xW12vV4N9RFktGbqNtT6shGTE7hRuLbxy6EA74tlICV407Vv4_z8wi_5r3A/exec"

@app.route("/")
def home():
    return "API de registro rodando 🚀 — use /registrar?var1=abc&var2=def..."

@app.route("/registrar", methods=["GET"])
def registrar():
    # Captura todos os parâmetros da URL
    params = request.args.to_dict()

    # Captura IP real do usuário (primeiro da lista X-Forwarded-For)
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ip_real = ip.split(",")[0].strip()
    params["ip"] = ip_real

    # Captura hora atual
    hora = datetime.now().isoformat()
    params["hora"] = hora

    # Envia os dados para o Google Apps Script
    try:
        r = requests.get(GOOGLE_SHEET_URL, params=params, timeout=5)
        sheet_response = r.text
    except Exception as e:
        sheet_response = str(e)

    # Log local no Render
    print(f"[{hora}] IP={ip_real}, PARAMS={params}")

    # Retorna JSON
    return jsonify({
        "status": "ok",
        "hora": hora,
        "ip": ip_real,
        "params": params,
        "sheet_response": sheet_response
    })
