import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Consultar las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Mostrar las tablas
tables = cursor.fetchall()
print("Tablas en la base de datos:")
for table in tables:
    print(table[0])

# Cerrar la conexión
conn.close()
