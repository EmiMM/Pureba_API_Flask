""" 
Prueba tecnica - Kosmos
Autor: Emilio Martínez Miranda

Desarrollo de API REST 
 recibir lista de oraciones en español
 devolver lista de entidades nombradas identificadas en cada oracion

Uso de Flask y Spacy
API debe aceptar peticion POST que contenga JSON con lista de oraciones en español

Instrucciones de ejecucion al final del archivo
"""

# Importacion de Librerias
from flask import Flask, request, jsonify, make_response
import spacy

# Carga de modelo Spacy en español
ner_model = spacy.load('es_core_news_sm')

# Aplicacion Flask
app = Flask(__name__)

# Ruta y metodo de API para pagina de inicio
@app.route('/')
def index():
    # Crear una variable con el contenido HTML que quieres mostrar
    html_content = """
    <html>
    <head>
      <title>API REST de NER</title>
    </head>
    <body>
      <h1>Bienvenido a la API REST de NER</h1>
      <p>Esta es una API REST sencilla que recibe una lista de oraciones en español y devuelve una lista de las entidades nombradas identificadas en cada oracion.</p>
      <p>Para usar la API, sigue las siguientes instrucciones:</p>
      <ul>
        <li>La API acepta una peticion POST que contenga un JSON con una lista de oraciones en español (key: oraciones, texto: cualquier cantidad de oraciones).</li>
        <li>La API devuelve un JSON que contenga una lista de las entidades identificadas en cada oracion, junto con el tipo de cada entidad.</li>
        <li>Para enviar una peticion a la API, usa la URL http://localhost:5000/ner o http://127.0.0.1:5000/ner.</li>
      </ul>
    </body>
    </html>
    """
    # Crear una respuesta con el contenido HTML
    response = make_response(html_content)
    # Cambiar el encabezado Content-Type por text/html
    response.headers["Content-Type"] = "text/html"
    # Devolver la respuesta
    return response


# Ruta y metodo de API para NER
@app.route('/ner', methods=['POST'])

def ner():
    # Obtener peticion en JSON
    data = request.get_json()

    # Verificar lista de oraciones
    if 'oraciones' in data and isinstance(data['oraciones'], list):

        # Lista para almacenar entidades nombradas
        entities = []

        # Iterar en oraciones
        for sentence in data['oraciones']:

            # Aplicacion de modelo NER
            model = ner_model(sentence)

            # Diccionario de entidades de oracion
            sentence_entities = {}
            sentence_entities['oración'] = sentence

            # Lista para guardar entidades y su tipo
            sentence_entities['entidades'] = {}

            # Iterar por entidad en oracion 
            for ent in model.ents:

                # Agregar texto y tipo a lista
                sentence_entities['entidades'][ent.text] = ent.label_

            # Agregar diccionario a lista de entidades nombradas
            entities.append(sentence_entities)

        # Diccionario de resultados
        resultados = {}
        resultados['resultado'] = entities
        
        # Devolver JSON con lista de entidades
        return jsonify(resultados)
    
    else:
        # Mensaje de error 
        return 'Formato de JSON no valido'

# Ejecucion principal
if __name__ == '__main__':
    app.run(debug=True)

"""
Instrucciones de ejecucion:

1. [recomendado] Iniciar entorno virtual
2. Instalar paquetes flask, spacy y el modelo NER
3. Ejecutar el archivo
4. En la terminal se mostrará la URL, http://127.0.0.1:5000
5. Al acceder a ella se in
"""