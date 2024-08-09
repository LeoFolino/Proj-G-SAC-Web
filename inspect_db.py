import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('datos/db/FISERV.db')
cursor = conn.cursor()

# Obtener las columnas de la tabla
cursor.execute("PRAGMA table_info(transacciones_sitef)")
columns = cursor.fetchall()

# Mostrar las columnas
for column in columns:
    print(column)

# Cerrar la conexión
conn.close()
