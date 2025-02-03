from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Diccionario de palabras y frases asociadas
frases_por_palabra = {
    "Amor": ["Amor y paz", "El amor siempre vence", "El amor es la respuesta"],
    "Justicia": ["La justicia trae paz", "Justicia universal", "Justicia y equilibrio"],
    "Paz": ["La paz es un derecho", "Armonía universal", "Felicidad compartida"],
    # Añade más palabras y frases aquí
}

@app.route("/enviar_palabra", methods=["POST"])
def recibir_palabra():
    data = request.json
    palabra = data.get("palabra")
    if palabra in frases_por_palabra:
        frase = random.choice(frases_por_palabra[palabra])  # Selecciona una frase aleatoria
        return jsonify({"frase": frase})
    else:
        return jsonify({"frase": "Palabra no reconocida"}), 400

if __name__ == "__main__":
    app.run(debug=True)
