CREATE OR REPLACE FUNCTION get_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name TEXT, number TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.id,
        c.name::TEXT,
        COALESCE(p.phone, '')::TEXT
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(name TEXT, email TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.name::TEXT,
        c.email::TEXT,
        p.phone::TEXT
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;