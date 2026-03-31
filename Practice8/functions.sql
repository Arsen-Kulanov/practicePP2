CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(id INT, name TEXT, number TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.id,
        c.name::TEXT,
        c.number::TEXT
    FROM contacts c
    WHERE c.name ILIKE '%' || p_pattern || '%'
       OR c.number ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name TEXT, number TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.id,
        c.name::TEXT,
        c.number::TEXT
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;