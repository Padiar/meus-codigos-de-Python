from flask import Flask, jsonify, request, send_from_directory
import datetime
import os
import json

app = Flask(__name__)

ARQUIVO = "gas.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"ultima_troca": None, "quantidade_usado": [], "trocas": []}
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

@app.route("/tocar", methods=["POST"])
def trocar_gas():
    dados = carregar_dados()
    hoje = datetime.date.today()

    # Quantidade usada desde a última troca
    quantidade_usada = dados.get("quantidade_usada", 0)

    # Salva essa quantidade na lista de trocas
    if "trocas" not in dados:
        dados["trocas"] = []
    dados["trocas"].append({
        "data": hoje.isoformat(),
        "quantidade_usada": quantidade_usada
    })

    # Reseta a quantidade usada para o próximo ciclo
    dados["quantidade_usada"] = 0
    dados["ultima_troca"] = hoje.isoformat()

    salvar_dados(dados)

    msg = f"Gás trocado em {hoje.isoformat()}. Quantidade usada no ciclo anterior: {quantidade_usada:.2f}"

    return jsonify({"mensagem": msg})

@app.route("/usar", methods=["POST"])
def usar_gas():
    dados = carregar_dados()

    #quantidade usada
    req = request.get_json()
    usada = req.get("quantidade", 0)

    dados["quantidade_usado"] = dados.get("quantidade_usado" + 0) + usada

    salvar_dados(dados)
    return jsonify({"mensagem": f"Quantidade usada atualizada: {dados['quantidade_usada']:.2f}"})

def media_duracao_gas(dados):
    trocas = dados.get("trocas", [])
    if not trocas:
        return 40  # média padrão inicial
    total = sum(t.get("quantidade_usado", 0) for t in trocas)
    return total / len(trocas)

@app.route("/status")
def status():
    dados = carregar_dados()
    return jsonify(dados)

@app.route("/previsao")
def previsao():
    dados = carregar_dados()
    if not dados.get("ultima_troca"):
        return jsonify({"erro": "Nenhuma troca registrada."})

    data_ultima_troca = datetime.datetime.strptime(dados["ultima_troca"], "%Y-%m-%d").date()
    hoje = datetime.date.today()
    dias_passados = (hoje - data_ultima_troca).days
    media = media_duracao_gas(dados)
    dias_restantes = max(0, int(media - dias_passados))

    aviso = None
    if dias_restantes <= 6 and dias_restantes > 0:
        aviso = f"Faltam {dias_restantes} dias para acabar o gás!"
    elif dias_restantes == 0:
        aviso = "Gás deve acabar hoje!"
    elif dias_restantes < 0:
        aviso = "Gás já deve ter acabado! Troque o quanto antes."

    return jsonify({
        "ultima_troca": dados["ultima_troca"],
        "dias_usados": dias_passados,
        "media_duracao": media,
        "dias_restantes": dias_restantes,
        "aviso": aviso
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
