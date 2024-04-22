CREATE OR REPLACE PROCEDURE audit_trigger
AS
  audit_table_name VARCHAR2(30) := 'HISTORIAL';
  seq_name VARCHAR2(30) := 'HISTORIAL_ID';
  trig_struct CLOB;
  v_count NUMBER;
  v_retention_days NUMBER := 30;  -- Adjust this value to define retention period

BEGIN
  -- Check if sequence exists
  SELECT COUNT(*)
  INTO v_count
  FROM user_sequences
  WHERE sequence_name = seq_name;

  -- Create sequence if it doesn't exist
  IF v_count = 0 THEN
    EXECUTE IMMEDIATE 'CREATE SEQUENCE ' || seq_name || ' START WITH 1 INCREMENT BY 1';
    DBMS_OUTPUT.PUT_LINE('La secuencia ha sido creada.');
  ELSE
    -- Reset sequence value to 1
    EXECUTE IMMEDIATE 'ALTER SEQUENCE ' || seq_name || ' RESTART';
    DBMS_OUTPUT.PUT_LINE('El valor de la secuencia ha sido reiniciado.');
  END IF;

  -- Delete old data from audit table based on retention period
  EXECUTE IMMEDIATE 'DELETE FROM '|| audit_table_name ||'';

  DBMS_OUTPUT.PUT_LINE('Datos antiguos de la tabla de auditoría eliminados.');

  -- Iterate over tables in the current schema
  FOR table_rec IN (SELECT table_name FROM user_tables WHERE table_name <> audit_table_name) LOOP
    trig_struct := 'CREATE OR REPLACE TRIGGER trig_' || table_rec.table_name || '_audit' || CHR(10)
                  || 'AFTER INSERT OR UPDATE OR DELETE ON ' || table_rec.table_name || CHR(10)
                  || 'FOR EACH ROW' || CHR(10)
                  || 'DECLARE' || CHR(10)
                  || '  opt VARCHAR2(10);' || CHR(10)
                  || 'BEGIN' || CHR(10)
                  || '  IF INSERTING THEN' || CHR(10)
                  || '    opt := ''INSERT'';' || CHR(10)
                  || '  ELSIF UPDATING THEN' || CHR(10)
                  || '    opt := ''UPDATE'';' || CHR(10)
                  || '  ELSE' || CHR(10)
                  || '    opt := ''DELETE'';' || CHR(10)
                  || '  END IF;' || CHR(10) || CHR(10)

                  || '  INSERT INTO ' || audit_table_name || ' (id_histo, fecha, descrip, tipo )' || CHR(10)
                  || '  VALUES (' || seq_name || '.NEXTVAL, SYSDATE, ''Se ha realizado una acción en la tabla "' || table_rec.table_name || '"'', opt);' || CHR(10) || CHR(10)

                  || 'END;';

    DBMS_OUTPUT.PUT_LINE(trig_struct);
    EXECUTE IMMEDIATE trig_struct;
  END LOOP;
END;
/
SET SERVEROUTPUT ON;