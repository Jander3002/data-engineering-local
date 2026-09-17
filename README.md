# 🚀 Data Engineering & Analytics Portfolio

Este repositorio contiene un entorno de desarrollo en **Ingeniería de Datos y Analítica**, diseñado para el procesamiento local de datos, validación automatizada de calidad y modelado dimensional para Inteligencia de Negocios (BI).

---

## 🛠️ Arquitectura y Tecnologías
* **Lenguaje Principal:** Python 3.11
* **Procesamiento de Datos:** PySpark, Pandas
* **Entorno Containerizado:** Docker & Docker Compose (OpenJDK 17)
* **Modelado & BI:** Power BI Desktop (Star Schema, DAX Avanzado)
* **Control de Versiones:** Git & GitHub

---

## 📂 Estructura del Proyecto

```text
DATA-ENGINEERING-LOCAL/
├── data/                       # Datasets de entrada y salida (.csv, .parquet)
├── scripts/                    # Scripts de Python para ETL y validación de calidad
│   ├── prueba.py               # Test de entorno (Pandas & PySpark)
│   └── validar_datos.py        # Script de reglas de calidad de datos
├── .gitignore                  # Exclusión de archivos temporales y pesados
├── Dockerfile                  # Imagen personalizada de Python + Java/Spark
├── docker-compose.yml          # Orquestación de contenedores locales
└── README.md                   # Documentación del proyecto