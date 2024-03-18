-- Consulta 1
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
    RANKING = 1;

-- Consulta 2
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
    MenosComprado;

-- Consulta 3
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
FETCH FIRST 1 ROW ONLY;

-- Consulta 4
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
    rango_desc = 1 OR rango_asc = 1;

-- Consulta 5
SELECT
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
    monto_total ASC;

-- Consulta 6
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
    cantidad_total = (
        SELECT
            MAX(cantidad_total)
        FROM
            ComprasPorCategoria
)

UNION ALL

SELECT
    'Menos comprada' AS tipo,
    nombre_categoria,
    cantidad_total
FROM
    ComprasPorCategoria
WHERE
    cantidad_total = (
        SELECT
            MIN(cantidad_total)
        FROM
            ComprasPorCategoria
);

-- Consulta 7
SELECT
    producto.nombre_producto,
    SUM(detalle.cantidad) AS total_compras
FROM
    producto
    INNER JOIN detalle ON producto.id_producto = detalle.producto_id_producto
GROUP BY
    producto.nombre_producto
ORDER BY
    total_compras DESC
FETCH FIRST 10 ROWS ONLY;

-- Consulta 8
WITH VentasPorMes AS (
    SELECT
        TO_CHAR(orden_de_venta.fecha_venta, 'MM-YYYY') AS mes,
        SUM(detalle.cantidad * producto.precio) AS monto_total
    FROM
        orden_de_venta
        INNER JOIN detalle ON orden_de_venta.id_orden = detalle.orden_de_venta_id_orden
        INNER JOIN producto ON detalle.producto_id_producto = producto.id_producto
    GROUP BY
        TO_CHAR(orden_de_venta.fecha_venta, 'MM-YYYY')
)
SELECT
    mes,
    monto_total
FROM
    VentasPorMes
ORDER BY
    mes;

-- Consulta 9
WITH VentasPorMes AS (
    SELECT
        TO_CHAR(orden_de_venta.fecha_venta, 'MM-YYYY') AS mes,
        SUM(detalle.cantidad * producto.precio) AS monto_total
    FROM
        orden_de_venta
        INNER JOIN detalle ON orden_de_venta.id_orden = detalle.orden_de_venta_id_orden
        INNER JOIN producto ON detalle.producto_id_producto = producto.id_producto
    GROUP BY
        TO_CHAR(orden_de_venta.fecha_venta, 'MM-YYYY')
)
SELECT
    mes,
    monto_total
FROM
    VentasPorMes
ORDER BY
    mes DESC
FETCH FIRST 3 ROWS ONLY;

-- Consulta 10
SELECT
    pais.nombre_pais,
    SUM(detalle.cantidad * producto.precio) AS monto_total
FROM
    cliente
    INNER JOIN pais ON cliente.pais_id_pais = pais.id_pais
    INNER JOIN orden_de_venta ON cliente.id_cliente = orden_de_venta.cliente_id_cliente
    INNER JOIN detalle ON orden_de_venta.id_orden = detalle.orden_de_venta_id_orden
    INNER JOIN producto ON detalle.producto_id_producto = producto.id_producto
GROUP BY
    pais.nombre_pais
ORDER BY
    monto_total DESC
FETCH FIRST 5 ROWS ONLY;
