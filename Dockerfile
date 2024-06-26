# Utiliza la imagen base de Python 3.11.0 con Debian Bullseye (Slim)
FROM python:3.11.0-slim-bullseye

# Actualiza el sistema y instala dependencias requeridas
RUN apt-get update && apt-get upgrade -y

# Instala los paquetes necesarios
RUN apt-get install -y \
    apache2 \
    libmariadb-dev \
    libapache2-mod-wsgi-py3 \
    pkg-config \
    gcc                           # Instala el compilador de C

# Configura la zona horaria
ENV TZ=America/Mexico_City
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos del proyecto al directorio de trabajo del contenedor
COPY ./requirements.txt /app/requirements.txt

# Instala las dependencias del proyecto
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

# Expone el puerto 80 para el tráfico HTTP
EXPOSE 80

# Define el comando predeterminado para ejecutar el contenedor
CMD ["apachectl", "-DFOREGROUND"]

