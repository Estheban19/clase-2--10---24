import sqlite3

# Conectar (o crear) una base de datos
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL   
)
''') 

# Insertar algunos datos   
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Bob', 25)")
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Charlie', 35)")

# Guardar (commit) los cambios
conn.commit()

# Cerrar la conexión    
conn.close()

print("Base de datos y tabla creadas exitosamente.")
        

