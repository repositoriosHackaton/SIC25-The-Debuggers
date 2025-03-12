import os
import io
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template, send_from_directory
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import google.generativeai as genai

# Configura la API Key de Gemini
genai.configure(api_key="AIzaSyCbHZNITIK6E449OSjWndYQDjGVEANSPoY")

# Cargar los modelos
model_from_scratch = tf.keras.models.load_model("ecg_cnn.keras")
pretrained_model = tf.keras.models.load_model("modelo_pre_entrenado_ecg.keras")

app = Flask(__name__, static_folder='static', template_folder='.')

anomaly_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0)]

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Diccionario de clases
class_labels = {
    0.0: "El paciente está sano",
    1.0: "El paciente tiene latido prematuro supraventricular",
    2.0: "El paciente tiene Contracción ventricular prematura",
    3.0: "El paciente tiene Fusión ventricular"
}

def preprocess_image_grayscale(image):
    image = image.convert("L")  
    image = image.resize((224, 224)) 
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0)
    image = np.expand_dims(image, axis=-1)
    return image

def preprocess_image_rgb(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def get_gemini_description(class_name):
    try:
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        response = model.generate_content(f"Explica detenidamente que es: {class_name}")
        return response.text if response else "No se pudo obtener la descripción."
    except Exception as e:
        return f"Error al obtener descripción: {str(e)}"

def get_gemini_text_response(text):
    try:
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        response = model.generate_content(text)
        return response.text if response else "No se pudo obtener respuesta."
    except Exception as e:
        return f"Error al obtener respuesta: {str(e)}"

def calculate_confidence(prediction):
    confidence = np.max(prediction) * 100
    return round(confidence, 2)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No se envió ninguna imagen'}), 400
        
        image_file = request.files['image']
        
        if image_file and allowed_file(image_file.filename):
            image = Image.open(io.BytesIO(image_file.read()))
        else:
            return jsonify({'error': 'Formato de imagen no permitido'}), 400

        processed_image_1 = preprocess_image_grayscale(image)
        processed_image_2 = preprocess_image_rgb(image)

        prediction_1 = model_from_scratch.predict(processed_image_1)
        prediction_2 = pretrained_model.predict(processed_image_2)

        label_1 = np.argmax(prediction_1)
        label_2 = np.argmax(prediction_2)

        class_name_1 = class_labels.get(label_1, "Desconocido")
        class_name_2 = class_labels.get(label_2, "Desconocido")

        description_1 = get_gemini_description(class_name_1)
        description_2 = get_gemini_description(class_name_2)

        # Convertir la confianza a float para ser serializable
        confidence_1 = float(calculate_confidence(prediction_1))
        confidence_2 = float(calculate_confidence(prediction_2))
        
        # Si las predicciones son iguales, combinar los resultados
        if label_1 == label_2:
            return jsonify({
                'prediction': int(label_1),
                'class_name': class_name_1,
                'description': description_1,
                'confidence': float((confidence_1 + confidence_2) / 2),
            })

        # Si las predicciones son diferentes, devolver las respuestas separadas
        return jsonify({
            'prediction_model_1': int(label_1),
            'class_name_model_1': class_name_1,
            'description_model_1': description_1,
            'confidence_model_1': confidence_1,
            'prediction_model_2': int(label_2),
            'class_name_model_2': class_name_2,
            'description_model_2': description_2,
            'confidence_model_2': confidence_2,
        })
    
    except Exception as e:
        return jsonify({'error': f'Ha ocurrido un error: {str(e)}'}), 500


@app.route('/chatbot', methods=['POST'])
def chatbot_text():
    try:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({'error': 'No se envió texto'}), 400
        
        user_text = data['text']
        response = get_gemini_text_response(user_text)

        return jsonify({
            'user_text': user_text,
            'gemini_response': response
        })
    except Exception as e:
        return jsonify({'error': f'Ha ocurrido un error: {str(e)}'}), 500

# Rutas principales
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)