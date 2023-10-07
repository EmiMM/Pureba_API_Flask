# Pureba_API_Flask
Prueba técnica de desarrollo de API REST con Flask para el reconocimiento de entidades nombradas con Python

## Objetivo
Crear una API REST sencilla que reciba una lista de oraciones en español y devuelva una lista de las entidades nombradas identificadas en cada oración.

## Instrucciones de uso

Para utilizar y probar la API, es necesario contar con la aplicación Postman API Platform, ya que facilita la prueba de APIs.

1. Se recomienda iniciar el entorno virtual, donde se instalen las librerías necesarias de Flask y Spacy.
2. De la carpeta Flask API REST, Ejecutar el archivo main.py y observar salida en terminal.
3. Entrar a la URI proporcionada por la terminal, generalmente http://127.0.0.1:5000, donde se encontrará con la página de inicio.
4. Para realizar una petició y realizar la prueba, se deberá utilizar Postman API Platform.
5. Entre en Postman e inicie un nuevo request, indicando que es de tipo POST.
6. Indicar URL. Para enviar una peticion a la API, usa la URL http://localhost:5000/ner o http://127.0.0.1:5000/ner
7. En la sección de Body, seleccionar Raw e indicar que es tipo JSON.
8. Colocar la prueba o ejemplo en formato JSON en el cuerpo de texto.
9. Enviar petición y observar resultados en la parte inferior.

Se muestra una captura para observar el ejemplo.

![captura](https://github.com/EmiMM/Pureba_API_Flask/blob/main/ejemplo_FlaskAPI.png?raw=true)
