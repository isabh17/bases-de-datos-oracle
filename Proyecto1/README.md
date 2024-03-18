# ProyectosBD1_201800565
 Proyecto 1 de Bases de Datos 1.

# Esquema de base de datos
Este manual técnico describe el esquema de base de datos generado por Oracle SQL Developer Data Modeler para Oracle Database 11g. El esquema incluye varias tablas para gestionar información relacionada con categorías, clientes, detalles de ventas, órdenes de venta, países, productos y vendedores.

## Manual Técnico: Proyecto #1 - Universidad de San Carlos de Guatemala

### Introducción

En este manual técnico se describe el proceso para el desarrollo del Proyecto #1 del Laboratorio Sistemas de Bases de Datos 1 de la Universidad de San Carlos de Guatemala. El proyecto consiste en diseñar y crear una base de datos para un pequeño emprendimiento dedicado al comercio de productos, así como desarrollar una API REST para el consumo de la base de datos.

### Herramientas Utilizadas

1. **Base de Datos:**
   - Motor de base de datos: Oracle, MySQL o SQL Server.
   - Oracle Data Modeler para el modelado lógico y relacional.

2. **Desarrollo de la API:**
   - Lenguajes permitidos: Python, Node.js o Golang.
   - Uso de una API REST para las consultas.

3. **Control de Versiones:**
   - GitHub para alojar el código y los archivos del proyecto.

4. **Otros:**
   - Docker para contenerizar la base de datos.
   - Postman, Thunder u otro asistente de pruebas para realizar peticiones HTTP.

### Proceso de Desarrollo

1. **Modelado de la Base de Datos:**
   - Crear el modelo conceptual, lógico y físico (ER) en Oracle Data Modeler.
   - Utilizar las entidades: productos, clientes, vendedores y órdenes de ventas.

2. **Script de Creación de la Base de Datos:**
   - Crear un script SQL para la creación de las tablas del modelo y las relaciones entre ellas.

3. **Carga de Datos:**
   - Crear una tabla temporal para cargar la información del archivo fuente.
   - Utilizar consultas SQL para llenar el modelo de datos de forma correcta y sin redundancias.

4. **Desarrollo de la API:**
   - Desarrollar una API REST en el lenguaje seleccionado.
   - Implementar los endpoints requeridos para mostrar los reportes y realizar las acciones especificadas.

5. **Reportes:**
   - Desarrollar consultas SQL para generar los reportes solicitados en la sección de "Reportería".

6. **Consumo de la API:**
   - Realizar peticiones HTTP a los endpoints de la API para visualizar los reportes y realizar acciones como eliminar tablas, crear tablas, etc.

## Esquema de la Base de Datos

El esquema de la base de datos incluye las siguientes tablas:

- `categoria`: Contiene información sobre las categorías de los productos.
- `cliente`: Almacena los datos de los clientes, como nombre, dirección y teléfono.
- `detalle`: Guarda los detalles de las ventas, como la cantidad de productos vendidos.
- `orden_de_venta`: Contiene información sobre las órdenes de venta, como la fecha y el cliente.
- `pais`: Almacena los países.
- `producto`: Contiene información sobre los productos, como nombre y precio.
- `vendedor`: Guarda los datos de los vendedores, como nombre y país.

## Tablas

### categoria

- `id_categoria` (INTEGER, NOT NULL): Identificador único de la categoría.
- `nombre_categoria` (VARCHAR2(50), NOT NULL): Nombre de la categoría.

### cliente

- `id_cliente` (INTEGER, NOT NULL): Identificador único del cliente.
- `nombre_cliente` (VARCHAR2(50), NOT NULL): Nombre del cliente.
- `apellido_cliente` (VARCHAR2(50), NOT NULL): Apellido del cliente.
- `direccion` (VARCHAR2(50), NOT NULL): Dirección del cliente.
- `telefono` (VARCHAR2(50), NOT NULL): Teléfono del cliente.
- `targeta_credito` (VARCHAR2(50), NOT NULL): Tarjeta de crédito del cliente.
- `edad` (INTEGER, NOT NULL): Edad del cliente.
- `genero` (VARCHAR2(50)): Género del cliente.
- `salario` (FLOAT): Salario del cliente.
- `pais_id_pais` (INTEGER, NOT NULL): ID del país del cliente (clave externa).

### detalle

- `id_detalle` (INTEGER, NOT NULL): Identificador único del detalle.
- `cantidad` (INTEGER, NOT NULL): Cantidad de productos vendidos.
- `linea_orden` (INTEGER, NOT NULL): Línea de la orden.
- `producto_id_producto` (INTEGER, NOT NULL): ID del producto (clave externa).
- `orden_de_venta_id_orden` (INTEGER, NOT NULL): ID de la orden de venta (clave externa).
- `vendedor_id_vendedor` (INTEGER, NOT NULL): ID del vendedor (clave externa).

### orden_de_venta

- `id_orden` (INTEGER, NOT NULL): Identificador único de la orden de venta.
- `fecha_orden` (DATE, NOT NULL): Fecha de la orden de venta.
- `cliente_id_cliente` (INTEGER, NOT NULL): ID del cliente (clave externa).

### pais

- `id_pais` (INTEGER, NOT NULL): Identificador único del país.
- `nombre_pais` (VARCHAR2(50), NOT NULL): Nombre del país.

### producto

- `id_producto` (INTEGER, NOT NULL): Identificador único del producto.
- `nombre_producto` (VARCHAR2(50), NOT NULL): Nombre del producto.
- `precio` (FLOAT, NOT NULL): Precio del producto.
- `categoria_id_categoria` (INTEGER, NOT NULL): ID de la categoría del producto (clave externa).

### vendedor

- `id_vendedor` (INTEGER, NOT NULL): Identificador único del vendedor.
- `nombre_vendedor` (VARCHAR2(50), NOT NULL): Nombre del vendedor.
- `apellido_vendedor` (VARCHAR2(50), NOT NULL): Apellido del vendedor.
- `pais_id_pais` (INTEGER, NOT NULL): ID del país del vendedor (clave externa).

## Restricciones

- Se han definido varias restricciones de clave primaria (`PRIMARY KEY`) y restricciones de clave externa (`FOREIGN KEY`) para mantener la integridad de los datos y establecer relaciones entre las tablas.

Este manual proporciona una descripción detallada de la estructura de la base de datos, lo que facilita la comprensión y el mantenimiento del sistema.

# Consultas
### Consultas SQL

Se deben desarrollar consultas SQL para generar los siguientes reportes:

1. Cliente que ha realizado la mayor cantidad de compras, mostrando su ID, nombre, apellido, país, monto total gastado y número de compras.
2. Producto más y menos comprado, incluyendo su ID, nombre, categoría, cantidad total comprada y monto total.
3. Vendedor que ha vendido productos por el monto total más alto, mostrando su ID, nombre y monto total vendido.
4. País que ha vendido la mayor y menor cantidad de productos en términos de monto total, mostrando el nombre del país y el monto total vendido.
5. Los cinco países que han realizado las mayores compras en orden ascendente, mostrando el ID del país, nombre y monto total comprado.
6. Mostrar la categoría que más y menos se ha comprado. Debe de mostrar el nombre de la categoría y cantidad de unidades. (Una sola consulta).
7. Mostrar la categoría más comprada por cada país. Se debe de mostrar el nombre del país, nombre de la categoría y cantidad de unidades.
8. Mostrar las ventas por mes de Inglaterra. Debe de mostrar el número del mes y el monto.
9. Mostrar el mes con más y menos ventas. Se debe de mostrar el número de mes y monto. (Una sola consulta).
10. Mostrar las ventas de cada producto de la categoría deportes. Se debe de mostrar el id del producto, nombre y monto

1. **consulta_1**: Obtiene la información del cliente que ha realizado la mayor cantidad de compras, mostrando su ID, nombre, apellido, país, monto total gastado y número de compras.
2. **consulta_2**: Muestra el producto más y menos comprado, incluyendo su ID, nombre, categoría, cantidad total comprada y monto total.
3. **consulta_3**: Retorna al vendedor que ha vendido productos por el monto total más alto, mostrando su ID, nombre y monto total vendido.
4. **consulta_4**: Muestra el país que ha vendido la mayor y menor cantidad de productos en términos de monto total, mostrando el nombre del país y el monto total vendido.
5. **consulta_5**: Obtiene los cinco países que han realizado las mayores compras en orden ascendente, mostrando el ID del país, nombre y monto total comprado.
6. **consulta_6**: Muestra la categoría de producto más y menos comprada, incluyendo el nombre de la categoría y la cantidad total comprada.
7. **consulta_7**: Retorna el país que más ha comprado por categoría, mostrando el nombre del país, la categoría y la cantidad total comprada.
8. **consulta_8**: Obtiene el monto total de ventas por mes para un país específico (id_pais=10).
9. **consulta_9**: Muestra el mes con mayor y menor cantidad total vendida, mostrando el número del mes y el monto total vendido.
10. **consulta_10**: Muestra los productos de una categoría específica (id_categoria=15) con el monto total vendido, mostrando el ID del producto, nombre del producto y monto total.
