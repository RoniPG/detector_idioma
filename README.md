# 🌍 Detector de Idioma

Proyecto que identifica el idioma de un texto ingresado por el usuario utilizando la librería **langdetect**.
Incluye una versión por consola (CLI) y una interfaz gráfica sencilla (GUI) con  **tkinter**.

---

## 🎯 Objetivo
Detectar automáticamente el idioma de un texto y mostrar su código de idioma correspondiente (por ejemplo: `en`, `es`, `fr`).

---

## 🛠️ Tecnologías utilizadas
- **Python 3.11+**
- **langdetect**
- **tkinter** para (GUI)

---

## 📂 Estructura del proyecto

```
detector_idioma/
│
├── src/                 
│   └── main.py
│   └── gui.py
│
├── .gitignore
├── README.md
```

---

## ⚙️ Instalación

#### 1. Asegúrate de tener **Python 3.11 o superior** instalado.

1. 1  (Opcional) Crear un entorno virtual con conda

   ```
    conda create -n detector_idioma_env python=3.11
    conda activate detector_idioma_env
   ```

#### 2. Clona el repositorio:

   ```
   git clone https://github.com/RoniPG/detector_idioma.git
   ```

#### 3. Accede al directorio del proyecto:

   ```
    cd detector_idioma
   ```

---

## :rocket: Uso

**(Para la version en consola)** desde la raíz del proyecto, ejecuta:
   ```
    python src/main.py
   ```

**(Para la interfaz gráfica)** desde la raíz del proyecto, ejecuta:
```
   python src/gui.py
```
