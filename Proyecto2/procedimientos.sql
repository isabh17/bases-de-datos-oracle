-- Registro de tipo de cliente
CREATE OR REPLACE PROCEDURE registrarTipoCliente (
    p_IdTipo IN INTEGER,
    p_Nombre IN VARCHAR2,
    p_Descripcion IN VARCHAR2
) AS
    v_IdTipo INTEGER;
BEGIN
    -- Validar que ninguno de los campos esté vacío o contenga solo espacios en blanco
    IF p_Nombre IS NULL OR TRIM(p_Nombre) = '' THEN
        RAISE_APPLICATION_ERROR(-20002, 'El campo Nombre es requerido.');
    END IF;

    IF p_Descripcion IS NULL OR TRIM(p_Descripcion) = '' THEN
        RAISE_APPLICATION_ERROR(-20002, 'El campo Descripción es requerido.');
    END IF;

    IF p_IdTipo <= 0 THEN
        -- Autoincrementar el IdTipo empezando en 1
        SELECT NVL(MAX(id_tipo), 0) + 1 INTO v_IdTipo FROM tipo_cliente;
    ELSE
        v_IdTipo := p_IdTipo;
    END IF;

    -- Validar que la descripción solo contenga letras, espacios en blanco.
    IF NOT REGEXP_LIKE(p_Descripcion, '^[[:alpha:][:space:]]+$') THEN
        RAISE_APPLICATION_ERROR(-20001, 'La descripción debe contener solo letras.');
    END IF;

    -- Insertar el tipo de cliente en la tabla
    INSERT INTO tipo_cliente (id_tipo, nombre, descripcion)
    VALUES (v_IdTipo, p_Nombre, p_Descripcion);

    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Tipo de cliente registrado exitosamente.');
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error al registrar el tipo de cliente: ' || SQLERRM);
END;
/
SET SERVEROUTPUT ON;

-- Registro de clientes
CREATE OR REPLACE PROCEDURE registrarCliente (
    p_IdCliente IN INTEGER,
    p_Nombre IN VARCHAR2,
    p_Apellidos IN VARCHAR2,
    p_Telefono IN VARCHAR2,
    p_Correos IN VARCHAR2,
    p_Usuario IN VARCHAR2,
    p_Clave IN VARCHAR2,
    p_TipoCliente IN INTEGER
) AS
    v_IdCliente INTEGER;
    v_ExistenciaTipoCliente INTEGER;
    v_ExistenciaUsuario INTEGER;
    v_ExistenciaTelefono INTEGER;
    v_ExistenciaCorreo INTEGER;
    v_TelefonoTruncado VARCHAR2(8);
BEGIN
    -- Validar que ningún campo esté vacío
    IF p_IdCliente IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo IdCliente es requerido.');
    END IF;

    IF p_Nombre IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo Nombre es requerido.');
    END IF;

    IF p_Apellidos IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo Apellidos es requerido.');
    END IF;

    IF p_Telefono IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo Telefono es requerido.');
    END IF;

    IF p_Correos IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo Correos es requerido.');
    END IF;

    IF p_Usuario IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo Usuario es requerido.');
    END IF;

    IF p_Clave IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo Contraseña es requerido.');
    END IF;

    IF p_TipoCliente IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo TipoCliente es requerido.');
    END IF;

    -- Validar que los campos no estén compuestos solo por espacios en blanco
    IF TRIM(p_Nombre) = '' THEN
        RAISE_APPLICATION_ERROR(-20007, 'El campo Nombre no puede consistir solo de espacios en blanco.');
    END IF;

    IF TRIM(p_Apellidos) = '' THEN
        RAISE_APPLICATION_ERROR(-20007, 'El campo Apellidos no puede consistir solo de espacios en blanco.');
    END IF;

    IF TRIM(p_Telefono) = '' THEN
        RAISE_APPLICATION_ERROR(-20007, 'El campo Telefono no puede consistir solo de espacios en blanco.');
    END IF;

    IF TRIM(p_Correos) = '' THEN
        RAISE_APPLICATION_ERROR(-20007, 'El campo Correos no puede consistir solo de espacios en blanco.');
    END IF;

    IF TRIM(p_Usuario) = '' THEN
        RAISE_APPLICATION_ERROR(-20007, 'El campo Usuario no puede consistir solo de espacios en blanco.');
    END IF;

    IF TRIM(p_Clave) = '' THEN
        RAISE_APPLICATION_ERROR(-20007, 'El campo Contraseña no puede consistir solo de espacios en blanco.');
    END IF;

    -- Validar que el nombre solo contenga letras y espacios en blanco
    IF NOT REGEXP_LIKE(p_Nombre, '^[[:alpha:][:space:]]+$') THEN
        RAISE_APPLICATION_ERROR(-20001, 'El nombre debe contener solo letras y espacios en blanco.');
    END IF;

    -- Validar que los apellidos solo contengan letras y espacios en blanco
    IF NOT REGEXP_LIKE(p_Apellidos, '^[[:alpha:][:space:]]+$') THEN
        RAISE_APPLICATION_ERROR(-20002, 'Los apellidos deben contener solo letras y espacios en blanco.');
    END IF;

    -- Validar el formato del correo electrónico
    FOR v_correo IN (SELECT * FROM TABLE(split_string(p_Correos, '|'))) LOOP
        IF NOT REGEXP_LIKE(v_correo.COLUMN_VALUE, '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') THEN
            RAISE_APPLICATION_ERROR(-20003, 'El formato del correo electrónico no es válido: ' || v_correo.COLUMN_VALUE);
        END IF;
    END LOOP;

    -- Verificar la disponibilidad del usuario
    SELECT COUNT(*)
    INTO v_ExistenciaUsuario
    FROM cliente
    WHERE usuario = p_Usuario;

    IF v_ExistenciaUsuario > 0 THEN
        RAISE_APPLICATION_ERROR(-20004, 'El usuario ya está en uso.');
    END IF;

    -- Verificar la existencia del tipo de cliente
    SELECT COUNT(*)
    INTO v_ExistenciaTipoCliente
    FROM tipo_cliente
    WHERE id_tipo = p_TipoCliente;

    IF v_ExistenciaTipoCliente = 0 THEN
        RAISE_APPLICATION_ERROR(-20005, 'El tipo de cliente especificado no existe.');
    END IF;

    -- Verificar la disponibilidad del cliente
    SELECT COUNT(*)
    INTO v_IdCliente
    FROM cliente
    WHERE id_cliente = p_IdCliente;

    IF v_IdCliente = 0 THEN
         -- Insertar el nuevo cliente en la tabla, incluyendo la hora actual
        INSERT INTO cliente (id_cliente, nombre, apellidos, usuario, clave, tipo_cliente_id_tipo, fecha_c)
        VALUES (p_IdCliente, p_Nombre, p_Apellidos, p_Usuario, p_Clave, p_TipoCliente, CURRENT_TIMESTAMP);

        -- Iterar sobre los correos electrónicos divididos
        FOR v_correo IN (SELECT * FROM TABLE(split_string(p_Correos, '|'))) LOOP
            -- Verificar la disponibilidad del correo
            SELECT COUNT(*)
            INTO v_ExistenciaCorreo
            FROM correo
            WHERE cliente_id_cliente = p_IdCliente AND correo = v_correo.COLUMN_VALUE;

            IF v_ExistenciaCorreo = 0 THEN
                -- Insertar el nuevo correo en la tabla correo
                INSERT INTO correo (correo, cliente_id_cliente)
                VALUES (v_correo.COLUMN_VALUE, p_IdCliente);
            END IF;
        END LOOP;

        -- Iterar sobre los teléfonos divididos
        FOR v_telefono IN (SELECT * FROM TABLE(split_string(p_Telefono, '-'))) LOOP
            -- Verificar la longitud del número de teléfono
            IF LENGTH(v_telefono.COLUMN_VALUE) > 8 THEN
                -- Truncar el número de teléfono si tiene más de 8 dígitos
                v_TelefonoTruncado := SUBSTR(v_telefono.COLUMN_VALUE, -8);
            ELSE
                -- Dejar el número de teléfono sin truncar si tiene 8 dígitos o menos
                v_TelefonoTruncado := v_telefono.COLUMN_VALUE;
            END IF;

            -- Verificar la disponibilidad del telefono
            SELECT COUNT(*)
            INTO v_ExistenciaTelefono
            FROM telefono
            WHERE cliente_id_cliente = p_IdCliente AND telefono = v_TelefonoTruncado;

            IF v_ExistenciaTelefono = 0 THEN
                -- Insertar el nuevo telefono en la tabla telefono
                INSERT INTO telefono (telefono, cliente_id_cliente)
                VALUES (v_TelefonoTruncado, p_IdCliente);
            END IF;
        END LOOP;

        COMMIT;
        DBMS_OUTPUT.PUT_LINE('Cliente registrado exitosamente el ' || TO_CHAR(SYSDATE, 'DD/MM/YYYY HH24:MI:SS'));
    END IF;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error al registrar el cliente: ' || SQLERRM);
END;
/
SET SERVEROUTPUT ON;

-- Tipo de cuenta
CREATE OR REPLACE PROCEDURE registrarTipoCuenta (
    p_IdTipoCuenta IN INTEGER,
    p_Nombre IN VARCHAR2,
    p_Descripcion IN VARCHAR2
) AS
    v_IdTipoCuenta INTEGER;
BEGIN
    -- Validar que ninguno de los campos esté vacío o contenga solo espacios en blanco
    IF p_Nombre IS NULL OR TRIM(p_Nombre) = '' THEN
        RAISE_APPLICATION_ERROR(-20001, 'El campo Nombre es requerido.');
    END IF;

    IF p_Descripcion IS NULL OR TRIM(p_Descripcion) = '' THEN
        RAISE_APPLICATION_ERROR(-20002, 'El campo Descripcion es requerido.');
    END IF;

    IF p_IdTipoCuenta <= 0 THEN
        -- Autoincrementar el IdTipoCuenta empezando en 1
        SELECT NVL(MAX(id_tipo_cuenta), 0) + 1 INTO v_IdTipoCuenta FROM tipo_cuenta;
    ELSE
        v_IdTipoCuenta := p_IdTipoCuenta;
    END IF;

    -- Insertar el tipo de cuenta en la tabla
    INSERT INTO tipo_cuenta (id_tipo_cuenta, nombre, descripcion)
    VALUES (v_IdTipoCuenta, p_Nombre, p_Descripcion);

    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Tipo de cuenta registrado exitosamente.');
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error al registrar el tipo de cuenta: ' || SQLERRM);
END;
/
SET SERVEROUTPUT ON;

-- Registro de cuentas bancarias
CREATE OR REPLACE PROCEDURE registrarCuenta (
    p_id_cuenta IN INTEGER,
    p_monto_apertura IN NUMBER,
    p_saldo_cuenta IN NUMBER,
    p_descripcion IN VARCHAR2,
    p_fecha_apertura IN VARCHAR2,
    p_otros_detalles IN VARCHAR2,
    p_tipo_cuenta_id IN INTEGER,
    p_cliente_id IN INTEGER
)
AS
    v_count NUMBER; -- Variable para validar que no exista el número de cuenta
    v_ExistenciaIdCliente INTEGER;
    v_ExistenciaTipoCuenta INTEGER;
    v_Fecha TIMESTAMP; -- Cambio de DATE a TIMESTAMP para incluir hora
BEGIN
    -- Verificar que todos los campos obligatorios estén presentes
    IF p_id_cuenta IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo id_cuenta es obligatorio.');
    END IF;

    IF p_monto_apertura IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo monto_apertura es obligatorio.');
    END IF;

    IF p_saldo_cuenta IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo saldo_cuenta es obligatorio.');
    END IF;

    IF p_descripcion IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo descripcion es obligatorio.');
    END IF;

    IF p_tipo_cuenta_id IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo tipo_cuenta_id es obligatorio.');
    END IF;

    IF p_cliente_id IS NULL THEN
        RAISE_APPLICATION_ERROR(-20006, 'El campo cliente_id es obligatorio.');
    END IF;

    -- Validar que no exista el número de cuenta
    SELECT COUNT(*) INTO v_count FROM cuenta_bancaria WHERE id_cuenta = p_id_cuenta;
    IF v_count > 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'El número de cuenta ya existe.');
    END IF;

    -- Validar que el monto de apertura sea positivo
    IF p_monto_apertura <= 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'El monto de apertura debe ser positivo.');
    END IF;

    -- Validar que el saldo de la cuenta sea mayor o igual que cero
    IF p_saldo_cuenta < 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'El saldo de la cuenta debe ser mayor o igual que cero.');
    END IF;

    -- Validar que el id_cliente exista
    SELECT COUNT(*) INTO v_ExistenciaIdCliente
    FROM cliente
    WHERE id_cliente = p_cliente_id;

    IF v_ExistenciaIdCliente = 0 THEN
        RAISE_APPLICATION_ERROR(-20004, 'El id_cliente especificado no existe.');
    END IF;

    -- Validar que el tipo_cuenta exista
    SELECT COUNT(*) INTO v_ExistenciaTipoCuenta
    FROM tipo_cuenta
    WHERE id_tipo_cuenta = p_tipo_cuenta_id;

    IF v_ExistenciaTipoCuenta = 0 THEN
        RAISE_APPLICATION_ERROR(-20005, 'El tipo de cuenta especificado no existe.');
    END IF;

    -- Manejar la fecha de apertura
    IF p_fecha_apertura IS NULL OR p_fecha_apertura = '' THEN
        v_Fecha := CURRENT_TIMESTAMP; -- Utilizar la fecha y hora actuales
    ELSE
        v_Fecha := TO_TIMESTAMP(p_fecha_apertura, 'DD/MM/YYYY HH24:MI:SS'); -- Convertir la cadena de fecha al formato adecuado
    END IF;

    -- Agregar la cuenta bancaria
    INSERT INTO cuenta_bancaria (id_cuenta, monto_apertura, saldo_cuenta, descripcion, fecha_apertura, tipo_cuenta_id_tipo_cuenta, cliente_id_cliente, otros_detalles)
    VALUES (p_id_cuenta, p_monto_apertura, p_saldo_cuenta, p_descripcion, v_Fecha, p_tipo_cuenta_id, p_cliente_id, p_otros_detalles);

    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Cuenta bancaria registrada con éxito.');
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error al registrar la cuenta bancaria: ' || SQLERRM);
        RAISE;
END registrarCuenta;
/
SET SERVEROUTPUT ON;

-- Productos y servicios
CREATE OR REPLACE PROCEDURE crearProductoServicio (
    p_codigo_producto IN INTEGER,
    p_tipo IN INTEGER,
    p_costo IN NUMBER,
    p_descripcion IN VARCHAR2
)
AS
    v_CodigoProducto INTEGER;
BEGIN

    -- Verificar que todos los campos obligatorios estén presentes
    IF p_codigo_producto IS NULL THEN
        RAISE_APPLICATION_ERROR(-20001, 'El código del producto es obligatorio.');
    END IF;
    
    -- Verificar que todos los campos obligatorios estén presentes
    IF p_tipo IS NULL THEN
        RAISE_APPLICATION_ERROR(-20001, 'El tipo son obligatorios.');
    END IF;

    IF p_codigo_producto <= 0 THEN
        -- Autoincrementar el IdTipo empezando en 1
        SELECT NVL(MAX(id_produc), 0) + 1 INTO v_CodigoProducto FROM producto_servicio;
    ELSE
        v_CodigoProducto := p_codigo_producto;
    END IF;

    -- Verificar si el tipo es un servicio (1) y el costo es NULL o menor o igual a cero
    IF p_tipo = 1 AND (p_costo IS NULL OR p_costo <= 0) THEN
        RAISE_APPLICATION_ERROR(-20002, 'El costo es obligatorio para los servicios y debe ser mayor que cero.');
    END IF;
    
    -- Insertar el producto o servicio
    INSERT INTO producto_servicio (id_produc, tipo, costo, des_produc)
    VALUES (v_CodigoProducto, p_tipo, p_costo, p_descripcion);
    
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Crear producto/servicio registrada con éxito.');
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error al crear producto/servicio: ' || SQLERRM);
        RAISE;
END crearProductoServicio;
/
SET SERVEROUTPUT ON;

-- Compras
CREATE OR REPLACE PROCEDURE realizarCompra (
    p_id_compra IN INTEGER,
    p_fecha IN VARCHAR2,
    p_importe_compra IN NUMBER,
    p_otros_detalles IN VARCHAR2,
    p_codigo_producto_servicio IN INTEGER,
    p_id_cliente IN INTEGER
)
AS
    v_ExistenciaIdCliente INTEGER;
    v_TipoProducto INTEGER;
    v_fecha DATE;
BEGIN
        -- Verificar que todos los campos obligatorios estén presentes
    IF p_id_compra IS NULL THEN
        RAISE_APPLICATION_ERROR(-20001, 'El ID de compra es obligatorio.');
    END IF;
    
    IF p_fecha IS NULL THEN
        RAISE_APPLICATION_ERROR(-20002, 'La fecha es obligatoria.');
    END IF;
    
    IF p_codigo_producto_servicio IS NULL THEN
        RAISE_APPLICATION_ERROR(-20003, 'El código de producto/servicio es obligatorio.');
    END IF;

    IF p_id_cliente IS NULL THEN
        RAISE_APPLICATION_ERROR(-20004, 'El ID de cliente es obligatorio.');
    END IF;

    -- Verificar si es un producto para validar el importe de la compra
    SELECT tipo INTO v_TipoProducto
    FROM producto_servicio
    WHERE id_produc = p_codigo_producto_servicio;

    IF v_TipoProducto = 2 AND (p_importe_compra IS NULL OR p_importe_compra = 0) THEN 
        RAISE_APPLICATION_ERROR(-20003, 'El campo "Importe compra" es obligatorio para un producto y debe ser mayor a 0.');
    END IF;

    IF v_TipoProducto = 1 AND p_importe_compra <> 0 THEN 
        RAISE_APPLICATION_ERROR(-20003, 'El campo "Importe compra" debe ser 0 porque el servicio ya tiene un costo establecido');
    END IF;

    -- Verificar que el código del producto/servicio existe
    SELECT COUNT(*)
    INTO v_ExistenciaIdCliente
    FROM producto_servicio
    WHERE id_produc = p_codigo_producto_servicio;

    IF v_ExistenciaIdCliente = 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'El código del producto/servicio no existe.');
    END IF;

    -- Validar que el id_cliente exista
    SELECT COUNT(*)
    INTO v_ExistenciaIdCliente
    FROM cliente
    WHERE id_cliente = p_id_cliente;

    IF v_ExistenciaIdCliente = 0 THEN
        RAISE_APPLICATION_ERROR(-20004, 'El id_cliente especificado no existe.');
    END IF;

    -- Manejar la fecha 
    IF p_fecha IS NULL OR p_fecha = '' THEN
        v_Fecha := SYSTIMESTAMP; -- Utilizar la fecha y hora actuales
    ELSE
        v_Fecha := TO_DATE(p_fecha, 'DD/MM/YYYY'); -- Convertir la cadena de fecha al formato adecuado
    END IF;

    -- Insertar la compra
    INSERT INTO compra (id_compra, fecha, importe_compra, otros_detalles, cliente_id_cliente, producto_servicio_id_produc)
    VALUES (p_id_compra, v_Fecha, p_importe_compra, p_otros_detalles, p_id_cliente, p_codigo_producto_servicio);
    
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Compra registrada con éxito.');
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error al registrar la compra: ' || SQLERRM);
        RAISE;
END realizarCompra;
/
SET SERVEROUTPUT ON;

-- Depósitos
CREATE OR REPLACE PROCEDURE realizarDeposito (
    p_id_deposito IN INTEGER,
    p_fecha IN VARCHAR2,
    p_monto IN NUMBER,
    p_otros_detalles IN VARCHAR2,
    p_id_cliente IN INTEGER
)
AS
    v_fecha DATE;
    v_ExistenciaIdCliente INTEGER;
BEGIN
    -- Verificar que todos los campos obligatorios estén presentes
    IF p_id_deposito IS NULL THEN
        RAISE_APPLICATION_ERROR(-20001, 'El Id del depósito es obligatorio.');
    END IF;
    IF p_fecha IS NULL THEN
        RAISE_APPLICATION_ERROR(-20002, 'La fecha es obligatoria.');
    END IF;
    IF p_monto IS NULL OR p_monto = 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'El monto es obligatorio y debe ser mayor a 0.');
    END IF;
    IF p_id_cliente IS NULL THEN
        RAISE_APPLICATION_ERROR(-20004, 'El Id del cliente es obligatorio.');
    END IF;

    -- Verificar que el cliente exista
    SELECT COUNT(*)
    INTO v_ExistenciaIdCliente
    FROM cliente
    WHERE id_cliente = p_id_cliente;

    IF v_ExistenciaIdCliente = 0 THEN
        RAISE_APPLICATION_ERROR(-20004, 'El id_cliente especificado no existe.');
    END IF;
    
    -- Manejar la fecha 
    IF p_fecha IS NULL OR p_fecha = '' THEN
        v_Fecha := SYSTIMESTAMP; -- Utilizar la fecha y hora actuales
    ELSE
        v_Fecha := TO_DATE(p_fecha, 'DD/MM/YYYY'); -- Convertir la cadena de fecha al formato adecuado
    END IF;

    -- Insertar el depósito
    INSERT INTO deposito (id_dep, fecha, monto, otros_detalles, cliente_id_cliente)
    VALUES (p_id_deposito, v_Fecha, p_monto, p_otros_detalles, p_id_cliente);
    
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Depósito registrado con éxito.');
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error al registrar el déposito: ' || SQLERRM);
        RAISE;
END realizarDeposito;
/
SET SERVEROUTPUT ON;

-- Débitos
CREATE OR REPLACE PROCEDURE realizarDebito (
    p_id_debito IN INTEGER,
    p_fecha IN VARCHAR2,
    p_monto IN NUMBER,
    p_otros_detalles IN VARCHAR2,
    p_id_cliente IN INTEGER
)
AS
    v_fecha DATE;
    v_ExistenciaIdCliente INTEGER;
BEGIN
    -- Verificar que todos los campos obligatorios estén presentes
    IF p_id_debito IS NULL THEN
        RAISE_APPLICATION_ERROR(-20001, 'El Id del débito es obligatorio.');
    END IF;
    IF p_fecha IS NULL THEN
        RAISE_APPLICATION_ERROR(-20002, 'La fecha es obligatoria.');
    END IF;
    IF p_monto IS NULL OR p_monto = 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'El monto es obligatorio y debe ser mayor a 0.');
    END IF;
    IF p_id_cliente IS NULL THEN
        RAISE_APPLICATION_ERROR(-20004, 'El Id del cliente es obligatorio.');
    END IF;

    -- Verificar que el cliente exista
    SELECT COUNT(*)
    INTO v_ExistenciaIdCliente
    FROM cliente
    WHERE id_cliente = p_id_cliente;

    IF v_ExistenciaIdCliente = 0 THEN
        RAISE_APPLICATION_ERROR(-20004, 'El id_cliente especificado no existe.');
    END IF;
    
    -- Manejar la fecha 
    IF p_fecha IS NULL OR p_fecha = '' THEN
        v_Fecha := SYSTIMESTAMP; -- Utilizar la fecha y hora actuales
    ELSE
        v_Fecha := TO_DATE(p_fecha, 'DD/MM/YYYY'); -- Convertir la cadena de fecha al formato adecuado
    END IF;
    
    -- Insertar el débito
    INSERT INTO debito (id_deb, fecha, monto, otros_detalles, cliente_id_cliente)
    VALUES (p_id_debito, v_Fecha, p_monto, p_otros_detalles, p_id_cliente);
    
    COMMIT;
    -- Output success message
    DBMS_OUTPUT.PUT_LINE('Débito realizado con éxito.');
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error al registrar el débito: ' || SQLERRM);
        RAISE;
END realizarDebito;
/
SET SERVEROUTPUT ON;

-- Registrar tipo transacciones 
CREATE OR REPLACE PROCEDURE registrarTipoTransaccion (
    p_IdTipoTransaccion IN INTEGER,
    p_Nombre IN VARCHAR2,
    p_Descripcion IN VARCHAR2
) AS
    v_IdTipoTransaccion INTEGER;
BEGIN
    -- Validar que ninguno de los campos esté vacío o contenga solo espacios en blanco
    IF p_Nombre IS NULL OR TRIM(p_Nombre) = '' THEN
        RAISE_APPLICATION_ERROR(-20001, 'El campo Nombre es requerido.');
    END IF;

    IF p_Descripcion IS NULL OR TRIM(p_Descripcion) = '' THEN
        RAISE_APPLICATION_ERROR(-20002, 'El campo Descripcion es requerido.');
    END IF;

    IF p_IdTipoTransaccion <= 0 THEN
        -- Autoincrementar el IdTipoTransaccion empezando en 1
        SELECT NVL(MAX(id_tipo_trans), 0) + 1 INTO v_IdTipoTransaccion FROM tip_trans;
    ELSE
        v_IdTipoTransaccion := p_IdTipoTransaccion;
    END IF;

    -- Insertar el tipo de transacción en la tabla
    INSERT INTO tip_trans (id_tipo_trans, nombre, descripcion)
    VALUES (v_IdTipoTransaccion, p_Nombre, p_Descripcion);

    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Tipo de transacción registrado exitosamente.');
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        DBMS_OUTPUT.PUT_LINE('Error al registrar el tipo de transacción: ' || SQLERRM);
END;
/
SET SERVEROUTPUT ON;

-- Transacciones
CREATE OR REPLACE PROCEDURE asignarTransaccion(
    p_IdTransaccion IN INTEGER,
    p_Fecha IN VARCHAR2,
    p_OtrosDetalles IN VARCHAR2,
    p_IdTipoTransaccion IN INTEGER,
    p_trans IN INTEGER,
    p_NoCuenta IN INTEGER
) AS
    v_SaldoCuenta NUMBER;
    v_fecha DATE;
    v_monto DECIMAL;
    v_ExistenciaTrans INTEGER;
    v_IdCliente INTEGER;
    v_IdClienteCuenta INTEGER;
    v_IdCompra INTEGER;
    v_IdDeposito INTEGER;
    v_IdDebito INTEGER;
BEGIN
    -- Validar que la cuenta corresponda al cliente y tenga saldo suficiente (en caso de débito o compra)
    SELECT saldo_cuenta, cliente_id_cliente INTO v_SaldoCuenta, v_IdClienteCuenta
    FROM cuenta_bancaria
    WHERE id_cuenta = p_NoCuenta;
    IF (p_trans IS NULL OR p_trans = 0) THEN
         RAISE_APPLICATION_ERROR(-20001, 'Se tiene que ingresar una compra/deposito/debito');
    END IF;

    IF p_IdTipoTransaccion = 1 THEN
        SELECT COUNT(importe_compra) INTO v_ExistenciaTrans
        FROM compra
        WHERE id_compra = p_trans;

        IF v_ExistenciaTrans = 0 THEN
            RAISE_APPLICATION_ERROR(-20001, 'No existe la compra que se esta efectuando');
        END IF;

        SELECT importe_compra, cliente_id_cliente INTO v_monto, v_IdCliente
        FROM compra
        WHERE id_compra = p_trans;
        IF v_IdClienteCuenta <> v_IdCliente THEN
            RAISE_APPLICATION_ERROR(-20001, 'La cuenta no pertenece al cliente que efectuó la compra');
        END IF;
        v_IdCompra := p_trans;

    ELSIF p_IdTipoTransaccion = 2 THEN
        SELECT COUNT(id_dep) INTO v_ExistenciaTrans
        FROM deposito
        WHERE id_dep = p_trans;

        IF v_ExistenciaTrans = 0 THEN
            RAISE_APPLICATION_ERROR(-20001, 'No existe el déposito que se esta efectuando');
        END IF;

        SELECT monto, cliente_id_cliente INTO v_monto, v_IdCliente
        FROM deposito
        WHERE id_dep = p_trans;
        IF v_IdClienteCuenta <> v_IdCliente THEN
            RAISE_APPLICATION_ERROR(-20001, 'La cuenta no pertenece al cliente que efectuó el depósito');
        END IF;
        v_IdDeposito := p_trans;

    ELSIF p_IdTipoTransaccion = 3 THEN
        SELECT COUNT(monto) INTO v_ExistenciaTrans
        FROM debito
        WHERE id_deb = p_trans;

        IF v_ExistenciaTrans = 0 THEN
            RAISE_APPLICATION_ERROR(-20001, 'No existe la compra que se esta efectuando');
        END IF;

        SELECT monto, cliente_id_cliente INTO v_monto, v_IdCliente
        FROM debito
        WHERE id_deb = p_trans;
        IF v_IdClienteCuenta <> v_IdCliente THEN
            RAISE_APPLICATION_ERROR(-20001, 'La cuenta no pertenece al cliente que efectuó el débito');
        END IF;
        v_IdDebito:= p_trans;
    ELSE
        RAISE_APPLICATION_ERROR(-20001, 'El tipo de transacción indicado no existe');
    END IF;

    IF p_IdTipoTransaccion = 1 OR p_IdTipoTransaccion = 3 THEN
        IF v_SaldoCuenta - v_monto < 0 THEN
            RAISE_APPLICATION_ERROR(-20001, 'La cuenta no tiene saldo suficiente para realizar la transacción');
        END IF;
    END IF;
    
    -- Manejar la fecha 
    IF p_fecha IS NULL OR p_fecha = '' THEN
        v_Fecha := SYSTIMESTAMP; -- Utilizar la fecha y hora actuales
    ELSE
        v_Fecha := TO_DATE(p_fecha, 'DD/MM/YYYY'); -- Convertir la cadena de fecha al formato adecuado
    END IF;
    
    -- Asignar la transacción
    INSERT INTO transaccion (id_trans, fecha, otros_detalles, tip_trans_id_tipo_trans, compra_id_compra, deposito_id_dep, debito_id_deb, cuenta_bancaria_id_cuenta)
    VALUES (p_IdTransaccion, v_Fecha, p_OtrosDetalles, p_IdTipoTransaccion, v_IdCompra, v_IdDeposito, v_IdDebito, p_NoCuenta);
    
    IF p_IdTipoTransaccion = 1 OR p_IdTipoTransaccion = 3 THEN
        update cuenta_bancaria
        SET saldo_cuenta = saldo_cuenta - v_monto 
        WHERE id_cuenta = p_NoCuenta;
    ELSE
        update cuenta_bancaria
        SET saldo_cuenta = saldo_cuenta + v_monto 
        WHERE id_cuenta = p_NoCuenta;
    END IF;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE_APPLICATION_ERROR(-20006, 'Error al asignar la transacción: ' || SQLERRM);
END asignarTransaccion;
/
SET SERVEROUTPUT ON;

