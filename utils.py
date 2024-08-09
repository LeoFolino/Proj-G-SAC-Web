import pandas as pd
import sqlite3
from datetime import datetime
import os

def filtrar_transacciones(codigo_tienda, tid, tarjeta, monto_desde, monto_hasta, fecha_desde, fecha_hasta):
    query = "SELECT * FROM transacciones_sitef WHERE 1=1"
    if codigo_tienda:
        codigo_busqueda = f'GI{codigo_tienda.zfill(6)}'
        query += f" AND CODIGO_TIENDA = '{codigo_busqueda}'"
    if tid:
        query += f" AND TID = '{tid.zfill(8)}'"
    if tarjeta:
        query += f" AND SUBSTRING(TARJETA, 1, 6) = '{tarjeta[:6]}'"
    if monto_desde:
        query += f" AND MONTO_FORMATEADO >= {monto_desde}"
    if monto_hasta:
        query += f" AND MONTO_FORMATEADO <= {monto_hasta}"
    if fecha_desde:
        fecha_desde_obj = datetime.strptime(fecha_desde, '%d/%m/%Y')
        query += f" AND substr(FECHA, 7, 4) || '-' || substr(FECHA, 4, 2) || '-' || substr(FECHA, 1, 2) >= '{fecha_desde_obj.strftime('%Y-%m-%d')}'"
    if fecha_hasta:
        fecha_hasta_obj = datetime.strptime(fecha_hasta, '%d/%m/%Y')
        query += f" AND substr(FECHA, 7, 4) || '-' || substr(FECHA, 4, 2) || '-' || substr(FECHA, 1, 2) <= '{fecha_hasta_obj.strftime('%Y-%m-%d')}'"

    # Ajustar la ruta a la base de datos
    db_path = os.path.join(os.path.dirname(__file__), 'datos/db/FISERV.db')
    conn = sqlite3.connect(db_path)
    df_filtrado = pd.read_sql_query(query, conn)
    conn.close()
    return df_filtrado

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
