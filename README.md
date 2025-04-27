# Gestor_de_clientes
https://github.com/ardillaCHIKI/Gestor_de_clientes.git

# Gestor de Clientes

Gestor de Clientes es una aplicación desarrollada en Python para la gestión de clientes mediante un archivo CSV como base de datos. Proporciona dos interfaces principales: una **interfaz de terminal** y una **interfaz web** basada en Gradio.

## 🛠️ Características

- **Gestión completa de clientes:**  
  Operaciones CRUD (crear, consultar, modificar y borrar) con persistencia en un archivo CSV.

- **Interfaz de usuario:**  
  - **Modo Terminal:** Menú interactivo para administrar clientes desde la línea de comandos.  
  - **Modo Web:** Interfaz gráfica amigable y fácil de usar con Gradio.

- **Pruebas automatizadas:**  
  Validación del correcto funcionamiento mediante `unittest`.

## 📦 Instalación

1. **Clonar el repositorio:**
   git clone https://github.com/tu_usuario/Gestor_de_clientes.git
   cd Gestor_de_clientes

2. **Instalar dependencias**
pip install -r requirements.txt

## 🚀 Uso

- **Modo Terminal**
Ejecuta el menú interactivo desde la línea de comandos:

python -m gestor.run -m

- **Modo Web**
Ejecuta la interfaz gráfica de Gradio:

python -m gestor.run

## ✅ Pruebas

Ejecuta las pruebas unitarias con:

- **unittest:**
python -m unittest discover
pytest:

## 📋 Consideraciones

- **Archivo CSV:** Se utiliza newline='' para evitar problemas de formato al trabajar con la base de datos.

- **Separación de entornos:** En el entorno de pruebas se utiliza un archivo temporal (clientes_test.csv) para evitar modificar la base de datos de producción.

- **Importaciones:** Ejecuta la aplicación desde el directorio raíz del proyecto para evitar problemas con las importaciones relativas:

python -m gestor.run -m

