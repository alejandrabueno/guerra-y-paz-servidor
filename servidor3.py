from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/enviar_palabra", methods=["POST"])
def recibir_palabra():
    data = request.json
    palabra = data.get("palabra")
    frase = data.get("frase")
    
    if not palabra or not frase:
        return jsonify({"status": "error", "mensaje": "Datos incompletos"}), 400
    
    print(f"Palabra seleccionada: {palabra}")
    print(f"Frase enviada: {frase}")
    
    return jsonify({"status": "ok", "frase": frase})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
