from flask import Flask, jsonify, request, send_from_directory
import datetime
import os
import json

app = Flask(__name__)

ARQUIVO = "gas.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"ultima_troca": None, "dias_uso": []}
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

@app.route("/trocar", methods=["POST"])
def trocar_gas():
    dados = carregar_dados()
    hoje = datetime.date.today().isoformat()
    dados["ultima_troca"] = hoje
    dados["dias_uso"] = []
    salvar_dados(dados)
    return jsonify({"mensagem": f"Gás trocado em {hoje}."})

@app.route("/usar", methods=["POST"])
def usar_gas():
    dados = carregar_dados()
    agora = datetime.datetime.now().isoformat() # data e hora no formato iso 8601
    if agora not in dados["dias_uso"]:
        dados["dias_uso"].append(agora)
    salvar_dados(dados)
    return jsonify({"mensagem": f"Uso registrado para {agora}."})

@app.route("/status")
def status():
    dados = carregar_dados()
    return jsonify(dados)

@app.route("/previsao")
def previsao():
    dados = carregar_dados()
    if not dados["ultima_troca"]:
        return jsonify({"erro": "Nenhuma troca registrada."})
    media_dias = 40  # ajuste conforme seu uso médio real
    dias_usados = len(dados["dias_uso"])
    restante = max(0, media_dias - dias_usados)
    return jsonify({
        "ultima_troca": dados["ultima_troca"],
        "dias_usados": dias_usados,
        "estimativa_restante": restante
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
