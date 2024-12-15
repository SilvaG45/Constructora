import sqlite3

# Conectar a la base de datos (esto crea la base de datos si no existe)
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

# Ejecutar las consultas del archivo SQL
with open('migrations/create_tables.sql', 'r') as file:
    sql_script = file.read()

cursor.executescript(sql_script)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Tablas creadas exitosamente")
