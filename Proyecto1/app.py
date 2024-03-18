import os
import csv
import cx_Oracle
from flask import Flask, jsonify
from flask import Flask, render_template

# Configuración de la base de datos Oracle
def conectar_base_de_datos():
    username = os.environ.get('DB_USERNAME', 'C##SILVERISA17')
    password = os.environ.get('DB_PASSWORD', 'NALA')
    database_url = os.environ.get('DB_URL', 'localhost:1521/free')

    connection = cx_Oracle.connect(username, password, database_url)
    return connection

def ejecutar_consulta():
    connection = conectar_base_de_datos()
    try:
        cursor = connection.cursor()

        # Ejemplo: consulta SELECT
        cursor.execute('SELECT * FROM tu_tabla')
        resultados = cursor.fetchall()

        return resultados
    finally:
        cursor.close()
        connection.close()

def proyecto1Bases():
    pass

def crear_tabla_categoria():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the 'categoria' table
        sql_script = '''
        CREATE TABLE categoria (
            id_categoria     INTEGER NOT NULL,
            nombre_categoria VARCHAR2(50) NOT NULL
        )
        '''
        # Execute the script to create the table
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Tabla 'categoria' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_pk_categoria():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the primary key constraint for the 'categoria' table
        sql_script = '''
        ALTER TABLE categoria ADD CONSTRAINT categoria_pk PRIMARY KEY (id_categoria)
        '''
        # Execute the script to create the primary key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave 'categoria_pk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_tabla_cliente():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the 'cliente' table
        sql_script = '''
        CREATE TABLE cliente (
            id_cliente       INTEGER NOT NULL,
            nombre_cliente   VARCHAR2(50) NOT NULL,
            apellido_cliente VARCHAR2(50) NOT NULL,
            direccion        VARCHAR2(50) NOT NULL,
            telefono         VARCHAR2(50) NOT NULL,
            targeta_credito  VARCHAR2(50) NOT NULL,
            edad             INTEGER NOT NULL,
            genero           VARCHAR2(50),
            salario          FLOAT,
            pais_id_pais     INTEGER NOT NULL
        )
        '''
        # Execute the script to create the table
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Tabla 'cliente' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_pk_cliente():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the primary key constraint for the 'cliente' table
        sql_script = '''
        ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY (id_cliente)
        '''
        # Execute the script to create the primary key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave 'cliente_pk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_tabla_cliente():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the 'cliente' table
        sql_script = '''
        CREATE TABLE cliente (
            id_cliente       INTEGER NOT NULL,
            nombre_cliente   VARCHAR2(50) NOT NULL,
            apellido_cliente VARCHAR2(50) NOT NULL,
            direccion        VARCHAR2(50) NOT NULL,
            telefono         VARCHAR2(50) NOT NULL,
            targeta_credito  VARCHAR2(50) NOT NULL,
            edad             INTEGER NOT NULL,
            genero           VARCHAR2(50),
            salario          FLOAT,
            pais_id_pais     INTEGER NOT NULL
        )
        '''
        # Execute the script to create the table
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Tabla 'cliente' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_pk_cliente():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the primary key constraint for the 'cliente' table
        sql_script = '''
        ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY (id_cliente)
        '''
        # Execute the script to create the primary key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave 'cliente_pk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_tabla_detalle():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the 'detalle' table
        sql_script = '''
        CREATE TABLE detalle (
            id_detalle              INTEGER NOT NULL,
            cantidad                INTEGER NOT NULL,
            linea_orden             INTEGER NOT NULL,
            producto_id_producto    INTEGER NOT NULL,
            orden_de_venta_id_orden INTEGER NOT NULL,
            vendedor_id_vendedor    INTEGER NOT NULL
        )
        '''
        # Execute the script to create the table
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Tabla 'detalle' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_pk_detalle():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the primary key constraint for the 'detalle' table
        sql_script = '''
        ALTER TABLE detalle ADD CONSTRAINT detalle_pk PRIMARY KEY (id_detalle)
        '''
        # Execute the script to create the primary key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave 'detalle_pk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_tabla_orden_de_venta():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the 'orden_de_venta' table
        sql_script = '''
        CREATE TABLE orden_de_venta (
            id_orden           INTEGER NOT NULL,
            fecha_orden        DATE NOT NULL,
            cliente_id_cliente INTEGER NOT NULL
        )
        '''
        # Execute the script to create the table
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Tabla 'orden_de_venta' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_pk_orden_de_venta():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the primary key constraint for the 'orden_de_venta' table
        sql_script = '''
        ALTER TABLE orden_de_venta ADD CONSTRAINT orden_de_venta_pk PRIMARY KEY (id_orden)
        '''
        # Execute the script to create the primary key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave 'orden_de_venta_pk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_tabla_pais():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the 'pais' table
        sql_script = '''
        CREATE TABLE pais (
            id_pais     INTEGER NOT NULL,
            nombre_pais VARCHAR2(50) NOT NULL
        )
        '''
        # Execute the script to create the table
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Tabla 'pais' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_pk_pais():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the primary key constraint for the 'pais' table
        sql_script = '''
        ALTER TABLE pais ADD CONSTRAINT pais_pk PRIMARY KEY (id_pais)
        '''
        # Execute the script to create the primary key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave 'pais_pk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_tabla_producto():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the 'producto' table
        sql_script = '''
        CREATE TABLE producto (
            id_producto            INTEGER NOT NULL,
            nombre_producto        VARCHAR2(50) NOT NULL,
            precio                 FLOAT NOT NULL,
            categoria_id_categoria INTEGER NOT NULL
        )
        '''
        # Execute the script to create the table
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Tabla 'producto' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_pk_producto():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the primary key constraint for the 'producto' table
        sql_script = '''
        ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY (id_producto)
        '''
        # Execute the script to create the primary key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave 'producto_pk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_tabla_vendedor():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the 'vendedor' table
        sql_script = '''
        CREATE TABLE vendedor (
            id_vendedor       INTEGER NOT NULL,
            nombre_vendedor   VARCHAR2(50) NOT NULL,
            apellido_vendedor VARCHAR2(50) NOT NULL,
            pais_id_pais      INTEGER NOT NULL
        )
        '''
        # Execute the script to create the table
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Tabla 'vendedor' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_pk_vendedor():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the primary key constraint for the 'vendedor' table
        sql_script = '''
        ALTER TABLE vendedor ADD CONSTRAINT vendedor_pk PRIMARY KEY (id_vendedor)
        '''
        # Execute the script to create the primary key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave 'vendedor_pk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_fk_cliente_pais():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the foreign key constraint for the 'cliente' table
        sql_script = '''
        ALTER TABLE cliente
        ADD CONSTRAINT cliente_pais_fk FOREIGN KEY ( pais_id_pais )
        REFERENCES pais ( id_pais )
        '''
        # Execute the script to create the foreign key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave foranea 'cliente_pais_fk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
def crear_fk_detalle_orden_venta():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the foreign key constraint for the 'detalle' table
        sql_script = '''
        ALTER TABLE detalle
        ADD CONSTRAINT detalle_orden_de_venta_fk FOREIGN KEY ( orden_de_venta_id_orden )
        REFERENCES orden_de_venta ( id_orden )
        '''
        # Execute the script to create the foreign key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave foranea 'detalle_orden_de_venta_fk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_fk_detalle_producto():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the foreign key constraint for the 'detalle' table
        sql_script = '''
        ALTER TABLE detalle
        ADD CONSTRAINT detalle_producto_fk FOREIGN KEY ( producto_id_producto )
        REFERENCES producto ( id_producto )
        '''
        # Execute the script to create the foreign key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave foranea 'detalle_producto_fk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_fk_detalle_vendedor():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the foreign key constraint for the 'detalle' table
        sql_script = '''
        ALTER TABLE detalle
        ADD CONSTRAINT detalle_vendedor_fk FOREIGN KEY ( vendedor_id_vendedor )
        REFERENCES vendedor ( id_vendedor )
        '''
        # Execute the script to create the foreign key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave foranea 'detalle_vendedor_fk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
def crear_fk_orden_venta_cliente():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the foreign key constraint for the 'orden_de_venta' table
        sql_script = '''
        ALTER TABLE orden_de_venta
        ADD CONSTRAINT orden_de_venta_cliente_fk FOREIGN KEY ( cliente_id_cliente )
        REFERENCES cliente ( id_cliente )
        '''
        # Execute the script to create the foreign key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave foranea 'orden_de_venta_cliente_fk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def crear_fk_producto_categoria():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the foreign key constraint for the 'producto' table
        sql_script = '''
        ALTER TABLE producto
        ADD CONSTRAINT producto_categoria_fk FOREIGN KEY ( categoria_id_categoria )
        REFERENCES categoria ( id_categoria )
        '''
        # Execute the script to create the foreign key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave foranea 'producto_categoria_fk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
def crear_fk_vendedor_pais():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # SQL script to create the foreign key constraint for the 'vendedor' table
        sql_script = '''
        ALTER TABLE vendedor
        ADD CONSTRAINT vendedor_pais_fk FOREIGN KEY ( pais_id_pais )
        REFERENCES pais ( id_pais )
        '''
        # Execute the script to create the foreign key constraint
        cursor.execute(sql_script)

        # Commit the changes
        connection.commit()

        return "Llave foranea 'vendedor_pais_fk' creada exitosamente."
    
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        return f"Error de base de datos: {error.message}"
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
def cargar_categoria():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        ruta_archivo = 'C:\\Users\\silve\\OneDrive\\Documentos\\GitHub\\ProyectosBD1_201800565\\Proyecto1\\archivosCarga\\Categorias.csv'
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')  # El delimitador es una tabulación en este caso
            for row in reader:
                id_categoria = int(row['id_categoria'])
                nombre_categoria = row['nombre']
                cursor.execute("SELECT COUNT(id_categoria) FROM CATEGORIA WHERE id_categoria = :id_categoria", {'id_categoria': id_categoria})
                resultado = cursor.fetchone()
                if resultado[0] == 0:  # Si no existe, insertar el nuevo registro
                    cursor.execute("INSERT INTO CATEGORIA (id_categoria, nombre_categoria) VALUES (:id_categoria, :nombre_categoria)", {'id_categoria': id_categoria, 'nombre_categoria': nombre_categoria})

        connection.commit()  # Confirmar los cambios en la base de datos
        print("Categorías insertadas exitosamente en la tabla categorias.")
        return "Categorias insertadas exitosamente en la tabla categorias."

    except Exception as e:
        print("Error al insertar categorías en la tabla categorias:", str(e))

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
        
def cargar_pais():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        ruta_archivo = 'C:\\Users\\silve\\OneDrive\\Documentos\\GitHub\\ProyectosBD1_201800565\\Proyecto1\\archivosCarga\\paises.csv'
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';') # El delimitador es una tabulación en este caso
            for row in reader:
                id_pais = int(row['id_pais'])
                nombre_pais = row['nombre']
                cursor.execute("SELECT COUNT(id_pais) FROM PAIS WHERE id_pais = :id_pais", {'id_pais': id_pais})
                resultado = cursor.fetchone()
                if resultado[0] == 0:  # Si no existe, insertar el nuevo registro
                    cursor.execute("INSERT INTO PAIS (id_pais, nombre_pais) VALUES (:id_pais, :nombre_pais)", {'id_pais': id_pais, 'nombre_pais': nombre_pais})

        connection.commit()  # Confirmar los cambios en la base de datos
        print("Países insertados exitosamente en la tabla paises.")
        return "Paises insertados exitosamente en la tabla paises."
        
    except Exception as e:
        print("Error al insertar paises en la tabla paises:", str(e))

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def cargar_productos():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        ruta_archivo = 'C:\\Users\\silve\\OneDrive\\Documentos\\GitHub\\ProyectosBD1_201800565\\Proyecto1\\archivosCarga\\productos.csv'
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')  # El delimitador es punto y coma en este caso
            for row in reader:
                id_producto = int(row['id_producto'])
                nombre_producto = row['Nombre']
                precio = float(row['Precio'])
                id_categoria = int(row['id_categoria'])
                cursor.execute("SELECT COUNT(id_producto) FROM PRODUCTO WHERE id_producto = :id_producto", {'id_producto': id_producto})
                resultado = cursor.fetchone()
                if resultado[0] == 0:  # Si no existe, insertar el nuevo registro
                    cursor.execute("INSERT INTO PRODUCTO (id_producto, nombre_producto, precio,  categoria_id_categoria) VALUES (:id_producto, :nombre_producto, :precio, :id_categoria)",
                                   {'id_producto': id_producto, 'nombre_producto': nombre_producto, 'precio': precio, 'id_categoria': id_categoria})

        connection.commit()  # Confirmar los cambios en la base de datos
        print("Productos insertados exitosamente en la tabla productos.")
        return "Productos insertados exitosamente en la tabla productos."
        
    except Exception as e:
        print("Error al insertar productos en la tabla productos:", str(e))

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
        
def cargar_cliente():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        ruta_archivo = 'C:\\Users\\silve\\OneDrive\\Documentos\\GitHub\\ProyectosBD1_201800565\\Proyecto1\\archivosCarga\\clientes.csv'
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')  # El delimitador es punto y coma en este caso
            for row in reader:
                id_cliente = int(row['id_cliente'])
                nombre_cliente = row['Nombre']
                apellido_cliente = row['Apellido']
                direccion = row['Direccion']
                telefono = row['Telefono']  # Truncar el número de teléfono a los primeros 8 caracteres
                tarjeta_credito = row['Tarjeta']
                edad = int(row['Edad'])
                salario = float(row['Salario'])
                genero = row['Genero']
                id_pais = int(row['id_pais'])
                
                cursor.execute("SELECT COUNT(id_cliente) FROM cliente WHERE id_cliente = :id_cliente", {'id_cliente': id_cliente})
                resultado = cursor.fetchone()
                if resultado[0] == 0:  # Si no existe, insertar el nuevo registro
                    cursor.execute("INSERT INTO cliente (id_cliente, nombre_cliente, apellido_cliente, direccion, telefono, targeta_credito, edad, salario, genero, pais_id_pais) VALUES (:id_cliente, :nombre_cliente, :apellido_cliente, :direccion, :telefono, :targeta_credito, :edad, :salario, :genero, :pais_id_pais)",
                                   {'id_cliente': id_cliente, 'nombre_cliente': nombre_cliente, 'apellido_cliente': apellido_cliente, 'direccion': direccion, 'telefono': telefono, 'targeta_credito': tarjeta_credito, 'edad': edad, 'salario': salario, 'genero': genero, 'pais_id_pais': id_pais})

        connection.commit()  # Confirmar los cambios en la base de datos
        print("Clientes insertados exitosamente en la tabla cliente.")
        return "Clientes insertados exitosamente en la tabla cliente."
        
    except Exception as e:
        print("Error al insertar clientes en la tabla cliente:", str(e))

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def verificar_ids_repetidos_cliente():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT id_cliente, COUNT(id_cliente) FROM cliente GROUP BY id_cliente HAVING COUNT(id_cliente) > 1")
        resultados = cursor.fetchall()
        
        if resultados:
            print("Se encontraron IDs de cliente repetidos:")
            for row in resultados:
                print(f"ID de cliente: {row[0]}, Cantidad de repeticiones: {row[1]}")
            return "Se encontraron IDs de cliente repetidos. Revisa la consola para más detalles."
        else:
            print("No se encontraron IDs de cliente repetidos.")
            return "No se encontraron IDs de cliente repetidos."

    except Exception as e:
        print("Error al verificar IDs de cliente repetidos:", str(e))
        return "Hubo un error al verificar IDs de cliente repetidos. Revisa la consola para más detalles."

    finally:
        cursor.close()
        connection.close()
        
def cargar_vendedores():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        ruta_archivo = 'C:\\Users\\silve\\OneDrive\\Documentos\\GitHub\\ProyectosBD1_201800565\\Proyecto1\\archivosCarga\\vendedores.csv'
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')  # El delimitador es punto y coma en este caso
            for row in reader:
                id_vendedor = int(row['id_vendedor'])
                nombre = row['nombre'].split(" ")
                nombre_vendedor = nombre[0]
                apellido_vendedor = nombre[1]
                # Apellido del vendedor se ignora
                id_pais = int(row['id_pais'])
                
                cursor.execute("SELECT COUNT(id_vendedor) FROM vendedor WHERE id_vendedor = :id_vendedor", {'id_vendedor': id_vendedor})
                resultado = cursor.fetchone()
                if resultado[0] == 0:  # Si no existe, insertar el nuevo registro
                    cursor.execute("INSERT INTO vendedor (id_vendedor, nombre_vendedor, apellido_vendedor, pais_id_pais) VALUES (:id_vendedor, :nombre_vendedor, :apellido_vendedor, :pais_id_pais)",
                                   {'id_vendedor': id_vendedor, 'nombre_vendedor': nombre_vendedor,'apellido_vendedor' :apellido_vendedor, 'pais_id_pais': id_pais})

        connection.commit()  # Confirmar los cambios en la base de datos
        print("Vendedores insertados exitosamente en la tabla vendedor.")
        return "Vendedores insertados exitosamente en la tabla vendedor."

    except Exception as e:
        print("Error al insertar vendedores en la tabla vendedor:", str(e))

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def cargar_orden_de_venta():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        ruta_archivo = 'C:\\Users\\silve\\OneDrive\\Documentos\\GitHub\\ProyectosBD1_201800565\\Proyecto1\\archivosCarga\\ordenes.csv'
        cursor.execute("SELECT MAX(id_detalle) + 1 from detalle")
        countDetalle = cursor.fetchone()
        id_detalle = 1 if countDetalle[0] is None else int(countDetalle[0])
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as file:  # Usamos 'utf-8-sig' para manejar caracteres especiales al principio del archivo
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                id_orden = int(row['id_orden'])  # Accedemos a la columna 'id_orden' sin los caracteres especiales al principio
                fecha_orden = row['fecha_orden']
                cliente_id_cliente = int(row['id_cliente'])
                cantidad = int(row['cantidad'])
                linea_orden = int(row['linea_orden'])
                producto_id = int(row['id_producto'])
                orden_id = int(row['id_orden'])
                vendedor_id = int(row['id_vendedor'])
                try:
                    cursor.execute("SELECT COUNT(*) FROM orden_de_venta where id_orden=:id_orden", {'id_orden': id_orden})
                except Exception as e:
                        raise Exception("Error en encabezado OrdenVenta" + str(e) + " id_orden " + str(id_orden) + " linea_orden " + str(linea_orden))
                resultado = cursor.fetchone()
                if resultado[0] == 0:  # Si no existe, insertar el nuevo registro
                    try:
                        cursor.execute("INSERT INTO orden_de_venta (id_orden, fecha_orden, cliente_id_cliente) VALUES (:id_orden, TO_DATE(:fecha_orden, 'DD/MM/YYYY'), :cliente_id_cliente)",
                                    {'id_orden': id_orden, 'fecha_orden': fecha_orden, 'cliente_id_cliente': cliente_id_cliente})
                    except Exception as e:
                        raise Exception("Error en encabezado" + str(e) + " id_orden " + str(id_orden) + " linea_orden " + str(linea_orden))
                try:
                    cursor.execute("SELECT COUNT(*) FROM detalle where orden_de_venta_id_orden=:id_orden and linea_orden=:linea_orden", {'id_orden': id_orden, 'linea_orden':linea_orden})
                except Exception as e:
                        raise Exception("Error en Consultadetalle" + str(e) + " id_orden " + str(id_orden) + " linea_orden " + str(linea_orden))
                resultado = cursor.fetchone()       
                if resultado[0] == 0:  # Si no existe, insertar el nuevo registro
                    try:
                        cursor.execute("INSERT INTO detalle (id_detalle, cantidad, linea_orden, producto_id_producto, orden_de_venta_id_orden, vendedor_id_vendedor) VALUES (:id_detalle, :cantidad, :linea_orden, :producto_id, :orden_de_venta_id, :vendedor_id)",
                        {'id_detalle': id_detalle, 'cantidad': cantidad, 'linea_orden': linea_orden, 'producto_id': producto_id, 'orden_de_venta_id': orden_id, 'vendedor_id': vendedor_id})
                        id_detalle +=1
                    except Exception as e:
                        raise Exception("Error en detalle" + str(e) + " id_orden " + str(id_orden) + " linea_orden " + str(linea_orden))
        connection.commit()  # Confirmar los cambios en la base de datos
        print("Datos de orden de venta insertados exitosamente en la tabla orden_de_venta.")
        return "Datos de orden de venta insertados exitosamente en la tabla orden_de_venta."

    except Exception as e:
        print("Error al insertar datos de orden de venta en la tabla orden_de_venta:", str(e))

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def delete_tables():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # Lista de tablas a eliminar
        tablas = ['CATEGORIA', 'PAIS', 'PRODUCTO', 'CLIENTE', 'VENDEDOR', 'ORDEN_DE_VENTA', 'DETALLE']

        for tabla in tablas:
            cursor.execute(f"DROP TABLE {tabla} CASCADE CONSTRAINTS")

        connection.commit()  # Confirmar los cambios en la base de datos
        mensaje = "Tablas eliminadas exitosamente."

    except Exception as e:
        mensaje = f"Error al eliminar las tablas: {str(e)}"

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
        
    return mensaje

def delete_tables_info():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        # Lista de tablas a limpiar
        tablas = ['DETALLE', 'ORDEN_DE_VENTA', 'VENDEDOR', 'CLIENTE', 'PRODUCTO', 'PAIS', 'CATEGORIA']

        for tabla in tablas:
            cursor.execute(f"DELETE FROM {tabla}")

        connection.commit()  # Confirmar los cambios en la base de datos
        mensaje = "Informacion de las tablas eliminada exitosamente."

    except Exception as e:
        mensaje = f"Error al eliminar la informacion de las tablas: {str(e)}"

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

    return mensaje

def consulta_1():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            WITH TotalCompras AS (
                SELECT
                    CLIENTE_ID_CLIENTE,
                    COUNT(*) AS NUM_COMPRAS,
                    SUM(DETALLE.CANTIDAD * PRODUCTO.PRECIO) AS MONTO_TOTAL_COMPRAS
                FROM
                    ORDEN_DE_VENTA
                    INNER JOIN DETALLE ON ORDEN_DE_VENTA.ID_ORDEN = DETALLE.ORDEN_DE_VENTA_ID_ORDEN
                    INNER JOIN PRODUCTO ON DETALLE.PRODUCTO_ID_PRODUCTO = PRODUCTO.ID_PRODUCTO
                GROUP BY
                    CLIENTE_ID_CLIENTE
            ),
            ClienteMasCompras AS (
                SELECT
                    CLIENTE.ID_CLIENTE,
                    CLIENTE.NOMBRE_CLIENTE,
                    CLIENTE.APELLIDO_CLIENTE,
                    PAIS.NOMBRE_PAIS,
                    TC.MONTO_TOTAL_COMPRAS,
                    TC.NUM_COMPRAS,
                    RANK() OVER (ORDER BY TC.MONTO_TOTAL_COMPRAS DESC) AS RANKING
                FROM
                    CLIENTE
                    INNER JOIN PAIS ON CLIENTE.PAIS_ID_PAIS = PAIS.ID_PAIS
                    INNER JOIN TotalCompras TC ON CLIENTE.ID_CLIENTE = TC.CLIENTE_ID_CLIENTE
            )
            SELECT
                ID_CLIENTE,
                NOMBRE_CLIENTE,
                APELLIDO_CLIENTE,
                NOMBRE_PAIS,
                MONTO_TOTAL_COMPRAS,
                NUM_COMPRAS
            FROM
                ClienteMasCompras
            WHERE
                RANKING = 1
        """)
        resultado = cursor.fetchone()

        if resultado:
            id_cliente, nombre_cliente, apellido_cliente, nombre_pais, monto_total, num_compras = resultado
            response = {
                "id_cliente": id_cliente,
                "nombre_cliente": nombre_cliente,
                "apellido_cliente": apellido_cliente,
                "nombre_pais": nombre_pais,
                "monto_total": monto_total,
                "num_compras": num_compras
            }
            return response
        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return "Error al ejecutar la consulta."

    finally:
        cursor.close()
        connection.close()

def consulta_2():
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            WITH ProductosComprados AS (
                SELECT
                    DETALLE.PRODUCTO_ID_PRODUCTO,
                    PRODUCTO.NOMBRE_PRODUCTO,
                    CATEGORIA.NOMBRE_CATEGORIA,
                    SUM(DETALLE.CANTIDAD) AS CANTIDAD_TOTAL,
                    SUM(DETALLE.CANTIDAD * PRODUCTO.PRECIO) AS MONTO_TOTAL
                FROM
                    DETALLE
                    INNER JOIN PRODUCTO ON DETALLE.PRODUCTO_ID_PRODUCTO = PRODUCTO.ID_PRODUCTO
                    INNER JOIN CATEGORIA ON PRODUCTO.CATEGORIA_ID_CATEGORIA = CATEGORIA.ID_CATEGORIA
                GROUP BY
                    DETALLE.PRODUCTO_ID_PRODUCTO, PRODUCTO.NOMBRE_PRODUCTO, CATEGORIA.NOMBRE_CATEGORIA
            ),
            ProductosRanking AS (
                SELECT
                    PC.*,
                    RANK() OVER (ORDER BY PC.CANTIDAD_TOTAL DESC) AS RANK_MAS,
                    RANK() OVER (ORDER BY PC.CANTIDAD_TOTAL ASC) AS RANK_MENOS
                FROM
                    ProductosComprados PC
            ),
            MasComprado AS (
                SELECT
                    PRODUCTO_ID_PRODUCTO AS ID_PRODUCTO_MAS,
                    NOMBRE_PRODUCTO AS NOMBRE_PRODUCTO_MAS,
                    NOMBRE_CATEGORIA AS NOMBRE_CATEGORIA_MAS,
                    CANTIDAD_TOTAL AS CANTIDAD_TOTAL_MAS,
                    MONTO_TOTAL AS MONTO_TOTAL_MAS
                FROM
                    ProductosRanking
                WHERE
                    RANK_MAS = 1
                FETCH FIRST ROW ONLY
            ),
            MenosComprado AS (
                SELECT
                    PRODUCTO_ID_PRODUCTO AS ID_PRODUCTO_MENOS,
                    NOMBRE_PRODUCTO AS NOMBRE_PRODUCTO_MENOS,
                    NOMBRE_CATEGORIA AS NOMBRE_CATEGORIA_MENOS,
                    CANTIDAD_TOTAL AS CANTIDAD_TOTAL_MENOS,
                    MONTO_TOTAL AS MONTO_TOTAL_MENOS
                FROM
                    ProductosRanking
                WHERE
                    RANK_MENOS = 1
                FETCH FIRST ROW ONLY
            )
            SELECT
                'Mas comprado' AS TIPO_MAS,
                ID_PRODUCTO_MAS,
                NOMBRE_PRODUCTO_MAS,
                NOMBRE_CATEGORIA_MAS,
                CANTIDAD_TOTAL_MAS AS CANTIDAD_PRODUCTO_MAS,
                MONTO_TOTAL_MAS
            FROM
                MasComprado

            UNION ALL

            SELECT
                'Menos comprado' AS TIPO_MENOS,
                ID_PRODUCTO_MENOS,
                NOMBRE_PRODUCTO_MENOS,
                NOMBRE_CATEGORIA_MENOS,
                CANTIDAD_TOTAL_MENOS AS CANTIDAD_PRODUCTO_MENOS,
                MONTO_TOTAL_MENOS
            FROM
                MenosComprado
        """)
        resultados = cursor.fetchall()

        if resultados:
            response = []
            for resultado in resultados:
                tipo, id_producto, nombre_producto, nombre_categoria, cantidad_total, monto_total = resultado
                response.append({
                    "tipo": tipo,
                    "id_producto": id_producto,
                    "nombre_producto": nombre_producto,
                    "nombre_categoria": nombre_categoria,
                    "cantidad_total": cantidad_total,
                    "monto_total": monto_total
                })
            return response  # Devuelve los resultados directamente

        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return {"error": "Error al ejecutar la consulta."}

    finally:
        cursor.close()
        connection.close()

def consulta_3():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                VENDEDOR.ID_VENDEDOR,
                VENDEDOR.NOMBRE_VENDEDOR,
                SUM(PRODUCTO.PRECIO * DETALLE.CANTIDAD) AS MONTO_TOTAL_VENDIDO
            FROM
                VENDEDOR
                INNER JOIN DETALLE ON DETALLE.VENDEDOR_ID_VENDEDOR = VENDEDOR.ID_VENDEDOR
                INNER JOIN PRODUCTO ON DETALLE.PRODUCTO_ID_PRODUCTO = PRODUCTO.ID_PRODUCTO
            GROUP BY
                VENDEDOR.ID_VENDEDOR,
                VENDEDOR.NOMBRE_VENDEDOR
            ORDER BY
                MONTO_TOTAL_VENDIDO DESC
            FETCH FIRST 1 ROW ONLY
        """)
        resultado = cursor.fetchone()

        if resultado:
            id_vendedor, nombre_vendedor, monto_total_vendido = resultado
            response = {
                "id_vendedor": id_vendedor,
                "nombre_vendedor": nombre_vendedor,
                "monto_total_vendido": monto_total_vendido
            }
            return response
        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return "Error al ejecutar la consulta."

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def consulta_4():
# Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                nombre_pais,
                monto_total
                FROM (
                SELECT
                    pais.nombre_pais,
                    SUM(detalle.cantidad * producto.precio) AS monto_total,
                    RANK() OVER (ORDER BY SUM(detalle.cantidad) DESC) AS rango_desc,
                    RANK() OVER (ORDER BY SUM(detalle.cantidad) ASC) AS rango_asc
                FROM
                vendedor
                INNER JOIN pais ON vendedor.pais_id_pais = pais.id_pais
                INNER JOIN detalle ON vendedor.id_vendedor = detalle.vendedor_id_vendedor
                INNER JOIN producto ON detalle.producto_id_producto = producto.id_producto
                GROUP BY
                    pais.nombre_pais
                )
                WHERE
                rango_desc = 1 OR rango_asc = 1
        """)
        resultados = cursor.fetchall()

        if resultados:
            pais_mas_vendido = None
            pais_menos_vendido = None
            for resultado in resultados:
                nombre_pais, monto_total = resultado
                if pais_mas_vendido is None:
                    pais_mas_vendido = {"nombre_pais": nombre_pais, "monto_total": monto_total}
                else:
                    pais_menos_vendido = {"nombre_pais": nombre_pais, "monto_total": monto_total}
            return {
                "pais_mas_vendido": pais_mas_vendido,
                "pais_menos_vendido": pais_menos_vendido
            }
        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return "Error al ejecutar la consulta."

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def consulta_5():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""SELECT
                id_pais,
                nombre_pais,
                monto_total
            FROM (
                SELECT
                    pais.id_pais,
                    pais.nombre_pais,
                    SUM(detalle.cantidad * precio) AS monto_total,
                    RANK() OVER (ORDER BY SUM(detalle.cantidad) DESC) AS rango
                FROM
                    cliente
                    INNER JOIN pais ON cliente.pais_id_pais = pais.id_pais
                    INNER JOIN orden_de_venta ON cliente.id_cliente = orden_de_venta.cliente_id_cliente
                    INNER JOIN detalle ON orden_de_venta.id_orden = detalle.orden_de_venta_id_orden
                    INNER JOIN producto ON detalle.producto_id_producto = producto.id_producto
                GROUP BY
                    pais.id_pais,
                    pais.nombre_pais
            )
            WHERE
                rango <= 5
            ORDER BY
            monto_total ASC
        """)
        resultados = cursor.fetchall()

        if resultados:
            response = []
            for resultado in resultados:
                id_pais, nombre_pais, monto_total = resultado
                response.append({
                    "id_pais": id_pais,
                    "nombre_pais": nombre_pais,
                    "monto_total": monto_total
                })
            return response
        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return "Error al ejecutar la consulta."

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def consulta_6():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            WITH ComprasPorCategoria AS (
                SELECT
                    c.nombre_categoria,
                    SUM(d.cantidad) AS cantidad_total
                FROM
                    detalle d
                    INNER JOIN producto p ON d.producto_id_producto = p.id_producto
                    INNER JOIN categoria c ON p.categoria_id_categoria = c.id_categoria
                GROUP BY
                    c.nombre_categoria
            )
            SELECT
                'Mas comprada' AS tipo,
                nombre_categoria,
                cantidad_total
            FROM
                ComprasPorCategoria
            WHERE
                cantidad_total = (SELECT MAX(cantidad_total) FROM ComprasPorCategoria)

            UNION ALL

            SELECT
                'Menos comprada' AS tipo,
                nombre_categoria,
                cantidad_total
            FROM
                ComprasPorCategoria
            WHERE
                cantidad_total = (SELECT MIN(cantidad_total) FROM ComprasPorCategoria)
        """)
        resultados = cursor.fetchall()

        if resultados:
            response = []
            for resultado in resultados:
                tipo, nombre_categoria, cantidad_total = resultado
                response.append({
                    "tipo": tipo,
                    "nombre_categoria": nombre_categoria,
                    "cantidad_total": cantidad_total
                })
            return response
        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return "Error al ejecutar la consulta."

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def consulta_7():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            WITH ComprasPorPaisYCategoria AS (
                SELECT
                    pa.nombre_pais,
                    ca.nombre_categoria,
                    SUM(de.cantidad) AS cantidad_total,
                    ROW_NUMBER() OVER(PARTITION BY pa.id_pais ORDER BY SUM(de.cantidad) DESC) AS rn
                FROM
                    detalle de
                    INNER JOIN orden_de_venta ov ON de.orden_de_venta_id_orden = ov.id_orden
                    INNER JOIN cliente cl ON ov.cliente_id_cliente = cl.id_cliente
                    INNER JOIN pais pa ON cl.pais_id_pais = pa.id_pais
                    INNER JOIN producto pr ON de.producto_id_producto = pr.id_producto
                    INNER JOIN categoria ca ON pr.categoria_id_categoria = ca.id_categoria
                GROUP BY
                    pa.id_pais,
                    pa.nombre_pais,
                    ca.nombre_categoria
            )
            SELECT
                nombre_pais,
                nombre_categoria,
                cantidad_total
            FROM
                ComprasPorPaisYCategoria
            WHERE
                rn = 1
        """)
        resultados = cursor.fetchall()

        if resultados:
            response = []
            for resultado in resultados:
                nombre_pais, nombre_categoria, cantidad_total = resultado
                response.append({
                    "nombre_pais": nombre_pais,
                    "nombre_categoria": nombre_categoria,
                    "cantidad_total": cantidad_total
                })
            return response
        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return "Error al ejecutar la consulta."

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def consulta_8():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                extract(year from orden_de_venta.fecha_orden),
                SUM(detalle.cantidad * producto.precio) AS monto_total,
                extract(month from orden_de_venta.fecha_orden)
            FROM
            vendedor
            INNER JOIN pais ON vendedor.pais_id_pais = pais.id_pais
            INNER JOIN detalle ON vendedor.id_vendedor = detalle.vendedor_id_vendedor
            INNER JOIN producto ON detalle.producto_id_producto = producto.id_producto
            INNER JOIN orden_de_venta ON orden_de_venta.id_orden = detalle.orden_de_venta_id_orden
            where pais.id_pais=10
            GROUP BY
                extract(year from orden_de_venta.fecha_orden),
                extract(month from orden_de_venta.fecha_orden)
        """)
        resultados = cursor.fetchall()

        if resultados:
            response = []
            for resultado in resultados:
                year, monto_total, month= resultado
                response.append({
                    "monto_total": monto_total,
                    "No. mes": month
                })
            return response
        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return "Error al ejecutar la consulta."

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def consulta_9():
            # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                mes,
                monto_total
                FROM
                (SELECT
                    SUM(detalle.cantidad * producto.precio) AS monto_total,
                    extract(month from orden_de_venta.fecha_orden) AS mes,
                    RANK() OVER (ORDER BY SUM(detalle.cantidad) DESC) AS rango_desc,
                    RANK() OVER (ORDER BY SUM(detalle.cantidad) ASC) AS rango_asc
                FROM
                vendedor
                INNER JOIN pais ON vendedor.pais_id_pais = pais.id_pais
                INNER JOIN detalle ON vendedor.id_vendedor = detalle.vendedor_id_vendedor
                INNER JOIN producto ON detalle.producto_id_producto = producto.id_producto
                INNER JOIN orden_de_venta ON orden_de_venta.id_orden = detalle.orden_de_venta_id_orden
                GROUP BY
                    extract(month from orden_de_venta.fecha_orden)
                )WHERE
                rango_desc = 1 OR rango_asc = 1
        """)
        resultados = cursor.fetchall()

        if resultados:
            response = []
            for resultado in resultados:
                month, monto_total= resultado
                response.append({
                    "No. mes": month,
                    "monto_total": monto_total
                })
            return response
        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return "Error al ejecutar la consulta."

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

def consulta_10():
    # Conexión a la base de datos Oracle
    connection = conectar_base_de_datos()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        SELECT
            producto.id_producto AS id_producto,
            producto.nombre_producto AS nombre_producto,
            SUM(detalle.cantidad * producto.precio) AS monto_total
        FROM
            producto
            INNER JOIN detalle ON producto.id_producto = detalle.producto_id_producto
            INNER JOIN categoria ON producto.categoria_id_categoria = categoria.id_categoria
        WHERE
            categoria.id_categoria = 15
        GROUP BY
            producto.id_producto, producto.nombre_producto
        """)
        resultados = cursor.fetchall()

        if resultados:
            response = []
            for resultado in resultados:
                id_producto, nombre_producto, monto_total= resultado
                response.append({
                    "id_producto": id_producto,
                    "nombre_producto": nombre_producto,
                    "monto_total": monto_total
                })
            return response
        else:
            return "No se encontraron resultados."

    except Exception as e:
        print("Error al ejecutar la consulta:", str(e))
        return "Error al ejecutar la consulta."

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

# Configuración de la aplicación Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Datos para mostrar en la página
    laboratorio = 'LABORATORIO DE BASES DE DATOS'
    proyecto = 'PROYECTO NO. #1'
    nombre = 'NOMBRE: MARIA ISABEL MASAYA CÓRDOVA'
    carnet = 'CARNET: 201800565'

    # Renderizar la plantilla con los datos
    return render_template('index.html', laboratorio=laboratorio, proyecto=proyecto, nombre=nombre, carnet=carnet)

@app.route('/crearmodelo', methods=['GET'])
def crear_modelo():
    resultados1 = crear_tabla_categoria()
    resultados2 = crear_pk_categoria()
    resultados3 = crear_tabla_cliente()
    resultados4 = crear_pk_cliente()
    resultados5 = crear_tabla_detalle()
    resultados6 = crear_pk_detalle()
    resultados7 = crear_tabla_orden_de_venta()
    resultados8 = crear_pk_orden_de_venta()
    resultados9 = crear_tabla_pais()
    resultados10 = crear_pk_pais()
    resultados11 = crear_tabla_producto()
    resultados12 = crear_pk_producto()
    resultados13 = crear_tabla_vendedor()
    resultados14 = crear_pk_vendedor()
    resultados15 = crear_fk_cliente_pais()
    resultados16 = crear_fk_detalle_orden_venta()
    resultados17 = crear_fk_detalle_producto()
    resultados18 = crear_fk_detalle_vendedor()
    resultados19 = crear_fk_orden_venta_cliente()
    resultados20 = crear_fk_producto_categoria()
    resultados21 =  crear_fk_vendedor_pais()
    mensaje = "Las tablas fueron creadas"
    return jsonify({"resultados1": resultados1, 
                    "resultados2": resultados2, 
                    "resultados3": resultados3, 
                    "resultados4": resultados4, 
                    "resultados5": resultados5, 
                    "resultados6": resultados6, 
                    "resultados7": resultados7, 
                    "resultados8": resultados8, 
                    "resultados9": resultados9, 
                    "resultados10": resultados10, 
                    "resultados11": resultados11, 
                    "resultados12": resultados12,
                    "resultados13": resultados13, 
                    "resultados14": resultados14,
                    "resultados15": resultados15,
                    "resultados16": resultados16,
                    "resultados17": resultados17,
                    "resultados18": resultados18,
                    "resultados19": resultados19,
                    "resultados20": resultados20,
                    "resultados21": resultados21,
                    "mensaje": mensaje})

@app.route('/cargarmodelo', methods=['GET'])
def cargar_modelo():
    resultados = cargar_categoria()
    resultados2 = cargar_pais()
    resultados3 = cargar_productos()
    resultados4 = cargar_cliente()
    resultados5 = verificar_ids_repetidos_cliente()
    resultados6 = cargar_vendedores()
    resultados7 = cargar_orden_de_venta()
    mensaje = "Todos los datos fueron cargados"

    return jsonify({"resultados": resultados, 
                    "resultados2": resultados2, 
                    "resultados3": resultados3, 
                    "resultados4": resultados4, 
                    "resultados5": resultados5, 
                    "resultados6": resultados6,
                    "resultados7": resultados7, 
                    "mensaje": mensaje})

@app.route('/borrarinfodb', methods=['GET'])
def borrar_info_tablas():
    resultados = delete_tables_info()
    return jsonify({"resultados": resultados})

@app.route('/eliminarmodelo', methods=['GET'])
def borrar_tablas():
    resultados = delete_tables()
    return jsonify({"resultados": resultados})

@app.route('/consulta1', methods=['GET'])
def consulta1():
    resultados = consulta_1()
    return jsonify({"resultados": resultados})

@app.route('/consulta2', methods=['GET'])
def consulta2():
    resultados = consulta_2()
    return jsonify({"resultados": resultados})

@app.route('/consulta3', methods=['GET'])
def consulta3():
    resultados = consulta_3()
    return jsonify({"resultados": resultados})

@app.route('/consulta4', methods=['GET'])
def consulta4():
    resultados = consulta_4()
    return jsonify({"resultados": resultados})

@app.route('/consulta5', methods=['GET'])
def consulta5():
    resultados = consulta_5()
    return jsonify({"resultados": resultados})

@app.route('/consulta6', methods=['GET'])
def consulta6():
    resultados = consulta_6()
    return jsonify({"resultados": resultados})

@app.route('/consulta7', methods=['GET'])
def consulta7():
    resultados = consulta_7()
    return jsonify({"resultados": resultados})

@app.route('/consulta8', methods=['GET'])
def consulta8():
    resultados = consulta_8()
    return jsonify({"resultados": resultados})

@app.route('/consulta9', methods=['GET'])
def consulta9():
    resultados = consulta_9()
    return jsonify({"resultados": resultados})

@app.route('/consulta10', methods=['GET'])
def consulta10():
    resultados = consulta_10()
    return jsonify({"resultados": resultados})

if __name__ == '__main__':
    app.run(debug=True)
    
    