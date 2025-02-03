from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Diccionario de palabras y frases
frases = {
    "Amor": ["AMOR Y PAZ", "TODO POR AMOR", "EL AMOR SIEMPRE VENCE"],
    "Paz": ["paz y amor", "la paz está aqui", "la paz siempre vence"],
    "Futuro": ["en el futuro estamos todos", "más allá siempre hay luz", "no es utopía es realidad"],
    "Armonía": ["Armonía en la diversidad.", "Todo es equilibrio y armonía.", "La armonía nace del respeto."],
    "Serenidad": ["Serenidad en medio del caos.", "La serenidad es una decisión.", "Encuentra la serenidad en el ahora."],
    "Equilibrio": ["El equilibrio es la clave de todo.", "Vivir es buscar el equilibrio.", "El arte es equilibrio en movimiento."],
    "Tranquilidad": ["La tranquilidad es un tesoro.", "Respira hondo y encuentra la tranquilidad.", "Solo en la tranquilidad nace la claridad."],
    "Silencio": ["El silencio también habla.", "En el silencio habita la verdad.", "Escucha el silencio, ahí está la respuesta."],
    "Unidad": ["La unidad hace la fuerza.", "Donde hay unidad, hay victoria.", "La unidad es el puente hacia la paz."],
    "Esperanza": ["La esperanza es el sueño del alma. - Aristóteles", "La esperanza es lo último que muere.", "Sin esperanza, no hay futuro."],
    "Fraternidad": ["La fraternidad nos hace humanos.", "Todos somos hermanos en el viaje de la vida.", "En la fraternidad está la solución."],
    "Diálogo": ["El diálogo es el camino.", "Hablando se entiende la gente.", "Sin diálogo, no hay entendimiento."],
    "Calma": ["La calma es poder.", "Respira profundo y encuentra la calma.", "En la calma nace la sabiduría."],
    "Bienestar": ["El bienestar es un estado del alma.", "Busca el bienestar en las pequeñas cosas.", "El verdadero bienestar es el equilibrio interior."],
    "Compasión": ["La compasión nos hace humanos.", "La compasión es el amor en acción.", "Ser compasivo es ser fuerte."],
    "Amistad": ["La amistad duplica las alegrías. - Cicerón", "Un amigo es un tesoro.", "La amistad verdadera es eterna."],
    "Empatía": ["Ponerse en el lugar del otro es un arte.", "La empatía construye puentes.", "Sin empatía, no hay humanidad."],
    "Respeto": ["El respeto es la base de toda relación.", "Respeta y serás respetado.", "Sin respeto, no hay paz."],
    "Tolerancia": ["La tolerancia es la mejor virtud.", "Aceptar la diferencia es crecer.", "Sin tolerancia, no hay convivencia."],
    "Justicia": ["Sin justicia no hay paz.", "La justicia da equilibrio al mundo.", "La justicia es la reina de las virtudes."],
    "Solidaridad": ["La solidaridad es amor en acción.", "Solo juntos podemos avanzar.", "Nadie se salva solo."],
    "Equidad": ["La equidad es justicia en movimiento.", "La equidad es la base de la paz.", "Sin equidad, no hay sociedad."],
    "Bondad": ["La bondad cambia el mundo.", "Sé amable, siempre.", "Haz el bien sin mirar a quién."],
    "Reconciliación": ["La reconciliación es el comienzo de la paz.", "Perdonar es sanar.", "La reconciliación abre caminos nuevos."],
    "Humanidad": ["Ser humano es ser compasivo.", "La humanidad se mide en acciones.", "Nuestra fuerza está en nuestra humanidad."],
    "Convivencia": ["La convivencia pacífica es posible.", "Respetarnos es convivir mejor.", "La convivencia es aprender a escuchar."],
    "Luz": ["Donde hay luz, hay esperanza.", "Sé luz en la oscuridad.", "La luz siempre encuentra su camino."],
    "Dignidad": ["La dignidad es innegociable.", "Todos merecemos vivir con dignidad.", "La dignidad es la esencia del ser."],
    "Plenitud": ["La plenitud está en el presente.", "Vive con plenitud cada instante.", "La plenitud nace de la gratitud."],
    "Felicidad": ["La felicidad es un camino, no un destino.", "La felicidad se comparte.", "Haz lo que amas y serás feliz."],
    "Compromiso": ["El compromiso es la base del cambio.", "Sin compromiso, no hay transformación.", "Compromiso es acción, no palabras."],
    "Esperanza": ["La esperanza es el motor del mundo.", "Siempre hay esperanza.", "No pierdas la esperanza, lo mejor está por venir."]
    
}

frase_actual = ""  # Variable para almacenar la frase seleccionada

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/enviar_palabra', methods=['POST'])
def recibir_palabra():
    global frase_actual
    data = request.json
    palabra = data.get('palabra')
    if palabra in frases:
        frase_actual = random.choice(frases[palabra])
        print(f"Frase seleccionada: {frase_actual}")
        return jsonify({"status": "ok", "frase": frase_actual})
    return jsonify({"status": "error", "mensaje": "Palabra no reconocida"})

@app.route('/obtener_frase', methods=['GET'])
def obtener_frase():
    global frase_actual
    return jsonify({"frase": frase_actual})

if __name__ == "__main__":
    app.run(debug=True)
