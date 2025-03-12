# SIC25-The-Debuggers
# IA para Análisis de Electrocardiogramas (ECG)

Este proyecto tiene como objetivo desarrollar una solución de inteligencia artificial para el análisis de electrocardiogramas utilizando datos de la **MIT-BIH Arrhythmia Database**. El pipeline del proyecto abarca la conversión de señales ECG a imágenes, la creación de un DataFrame con las etiquetas correspondientes, la división de los datos en conjuntos de entrenamiento y validación, y el entrenamiento de una red neuronal convolucional (CNN) creada desde 0 y el reentrenamiento de la CNN VGG16; esto con el fin de la clasificación de latidos.

---

## ⚙️ Requisitos

- Python 3.7 o superior
- [wfdb](https://github.com/MIT-LCP/wfdb-python)
- matplotlib
- numpy
- pandas
- scikit-learn
- tensorflow (o tensorflow-cpu, según tu configuración)
- flask
- PIL
- google.generativeai

---

## 🚀 Cómo Empezar

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/repositoriosHackaton/SIC25-The-Debuggers.git
   ```

2. **Conversión de ECG a Imágenes y Generación del CSV:**

   Ejecuta las celdas del notebook data/script_imagen:

   Este script extrae los segmentos de latidos, los guarda como imágenes organizadas por clase y genera el archivo `data_imagenes.csv`.

3. **Iniciar la página web**

   Ejecuta el script en la carpeta "ecg_project":
   ```bash
   python server.py
   ```
   Esto iniciará el servidor local, una vez en funcionamiento ingresa a través de tu buscador con:
   http://127.0.0.1:8000/

5. **Realizar predicción**

   Entra en la sección "chatbot", luego selecciona el botón para subir una imagen y elige la imagen de
   tu preferencia dentro de "data/imagenes_eg/.."

   ¡Envía la imagen y recibe tu predicción!

---

## 📌 Nota

- Asegúrate de que la estructura de carpetas se mantenga igual para evitar errores en la ejecución de los scripts.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, por favor crea un _pull request_ o abre un _issue_.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).

---

¡Gracias por visitar el proyecto! Si tienes alguna pregunta o necesitas asistencia, no dudes en contactar.

---
