create or replace TRIGGER trig_CLIENTE_audit
AFTER INSERT OR UPDATE OR DELETE ON CLIENTE
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "CLIENTE"', opt);

END;

create or replace TRIGGER trig_COMPRA_audit
AFTER INSERT OR UPDATE OR DELETE ON COMPRA
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "COMPRA"', opt);

END;

create or replace TRIGGER trig_CORREO_audit
AFTER INSERT OR UPDATE OR DELETE ON CORREO
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "CORREO"', opt);

END;

create or replace TRIGGER trig_CUENTA_BANCARIA_audit
AFTER INSERT OR UPDATE OR DELETE ON CUENTA_BANCARIA
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "CUENTA_BANCARIA"', opt);

END;

create or replace TRIGGER trig_DEBITO_audit
AFTER INSERT OR UPDATE OR DELETE ON DEBITO
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "DEBITO"', opt);

END;

create or replace TRIGGER trig_DEPOSITO_audit
AFTER INSERT OR UPDATE OR DELETE ON DEPOSITO
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "DEPOSITO"', opt);

END;

create or replace TRIGGER trig_PRODUCTO_SERVICIO_audit
AFTER INSERT OR UPDATE OR DELETE ON PRODUCTO_SERVICIO
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "PRODUCTO_SERVICIO"', opt);

END;

create or replace TRIGGER trig_TELEFONO_audit
AFTER INSERT OR UPDATE OR DELETE ON TELEFONO
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "TELEFONO"', opt);

END;

create or replace TRIGGER trig_TIP_TRANS_audit
AFTER INSERT OR UPDATE OR DELETE ON TIP_TRANS
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "TIP_TRANS"', opt);

END;

create or replace TRIGGER trig_TIPO_CLIENTE_audit
AFTER INSERT OR UPDATE OR DELETE ON TIPO_CLIENTE
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "TIPO_CLIENTE"', opt);

END; 

create or replace TRIGGER trig_TIPO_CUENTA_audit
AFTER INSERT OR UPDATE OR DELETE ON TIPO_CUENTA
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "TIPO_CUENTA"', opt);

END; 

create or replace TRIGGER trig_TRANSACCION_audit
AFTER INSERT OR UPDATE OR DELETE ON TRANSACCION
FOR EACH ROW
DECLARE
  opt VARCHAR2(10);
BEGIN
  IF INSERTING THEN
    opt := 'INSERT';
  ELSIF UPDATING THEN
    opt := 'UPDATE';
  ELSE
    opt := 'DELETE';
  END IF;

  INSERT INTO HISTORIAL (id_histo, fecha, descrip, tipo )
  VALUES (HISTORIAL_ID.NEXTVAL, SYSDATE, 'Se ha realizado una acción en la tabla "TRANSACCION"', opt);

END;