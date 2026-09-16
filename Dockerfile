FROM python:3.11-slim

# Evitar archivos .pyc e impresiones en búfer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar Java predeterminado (Default JRE/JDK) y utilidades de sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-jre-headless \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Configurar JAVA_HOME detectando la ruta oficial del sistema
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="$JAVA_HOME/bin:$PATH"

WORKDIR /app

# Instalar librerías de Python
RUN pip install --no-cache-dir \
    pandas \
    pyspark \
    pyodbc \
    sqlalchemy \
    jupyter \
    requests

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]