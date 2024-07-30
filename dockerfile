FROM python:3.10.14-bullseye

# Establece el directorio de trabajo
WORKDIR /app/apiv01

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . .

# Establece la variable de entorno FLASK_APP
ENV FLASK_APP=app.py

# Expone el puerto 5000 para la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
