import pandas as pd

def validar_calidad():
    path = "data/ventas_logistica_plano.csv"
    print(f"=== Leyendo archivo: {path} ===")
    
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo CSV en la ruta especificada.")
        return

    print(f"Total de registros a validar: {len(df)}\n")

    # Regla 1: Validar nulos en campos clave
    campos_clave = ['ID_Despacho', 'Fecha_Despacho', 'Monto_Venta_USD']
    nulos = df[campos_clave].isnull().sum()
    print("1. Validación de Nulos:")
    print(nulos)
    
    # Regla 2: Validar valores negativos o ceros en Ventas
    ventas_invalidas = df[df['Monto_Venta_USD'] <= 0]
    print(f"\n2. Registros con monto de venta inválido (<= 0): {len(ventas_invalidas)}")

    # Regla 3: Validar duplicados en ID_Despacho
    duplicados = df.duplicated(subset=['ID_Despacho']).sum()
    print(f"3. Registros duplicados por ID_Despacho: {duplicados}")

    print("\n✅ ¡Validación de calidad completada!")

if __name__ == "__main__":
    validar_calidad()