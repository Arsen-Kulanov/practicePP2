CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_number TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_number) THEN
        UPDATE contacts
        SET number = p_number
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, number)
        VALUES (p_name, p_number);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names TEXT[],
    p_numbers TEXT[],
    OUT invalid_data TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    invalid_data := ARRAY[]::TEXT[];

    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_numbers[i] ~ '^[0-9]+$' THEN
            CALL insert_or_update_user(p_names[i], p_numbers[i]);
        ELSE
            invalid_data := array_append(invalid_data, p_names[i] || ':' || p_numbers[i]);
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR number = p_value;
END;
$$;