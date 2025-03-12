# SIC25-The-Debuggers
# IA para Análisis de Electrocardiogramas (ECG)
![Python](https://img.shields.io/badge/Code-Python-blue.svg)
![Jupyter Notebook](https://img.shields.io/badge/Tool-Jupyter%20Notebook-orange.svg)
![Machine Learning](https://img.shields.io/badge/Technology-Machine%20Learning-yellow.svg)
![Artificial Intelligence](https://img.shields.io/badge/Field-Artificial%20Intelligence-brightgreen.svg)
![Data Analysis](https://img.shields.io/badge/Focus-Data%20Analysis-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-ffbb00.svg)

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
## Precisión
![Precisión de nuestro modelo](img/precisión_cnn_ecg.png)

![Precisión de modelo preentrenado](img/precisión_cnn_preentrenado.png)
s
---
## Equipo

<!-- markdownlint-disable MD033 -->
<table>
   <thead>
      <tr>
         <th></th>
         <th><strong>Nombre</strong></th>
         <th><strong>GitHub</strong></th>
         <th><strong>Rol del equipo</strong></th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>
            <img src="https://avatars.githubusercontent.com/u/125231044?v=4/"
                 alt="Adrian Sanchez" width="65">
         </td>
         <td>Adrian Sanchez</td>
         <td><a href="https://github.com/asm2202">asm2202</a></td>
         <td>Desarrollador</td>
      </tr>
      <tr>
         <td>
            <img src="https://avatars.githubusercontent.com/u/115899276?v=4"
                 alt="Hector Colmenares" width="65">
         </td>
         <td>Hector Colmenares</td>
         <td><a href="https://github.com/hectordacb">hectordacb</a></td>
         <td>Desarrollador</td>
      </tr>
      <tr>
         <td>
            <img src="https://avatars.githubusercontent.com/u/140109596?v=4"
                 alt="Jorge Morales" width="65">
         </td>
         <td>Jorge Morales</td>
         <td><a href="https://github.com/mordacay">mordacay</a></td>
         <td>Desarrollador</td>
      </tr>
      <tr>
         <td>
            <img src="https://avatars.githubusercontent.com/u/125399105?v=4"
                 alt="Maeva Puente" width="65">
         </td>
         <td>Maeva Puente</td>
         <td><a href="https://github.com/msathiu">msathiu</a></td>
         <td>Desarrollador</td>
      </tr>
      <tr>
         <td>
            <img src="https://avatars.githubusercontent.com/u/125196247?v=4"
                 alt="Manuel Maldonado" width="65">
         </td>
         <td>Manuel Maldonado</td>
         <td><a href="https://github.com/manumaldonado">manumaldonado</a></td>
         <td>Desarrollador</td>
      </tr>
   </tbody>
</table>
<!-- markdownlint-enable MD033 -->

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
