from DatabaseSession import DatabaseSession

ds = DatabaseSession()

ds.session.execute(
"""
CREATE TABLE IF NOT EXISTS children(
    c_id UUID PRIMARY KEY,
    c_name TEXT,
    c_age INT
);
"""
)

ds.session.execute(
"""
CREATE TABLE IF NOT EXISTS parents(
    p_id UUID PRIMARY KEY,
    p_name TEXT,
    p_address TEXT,
    p_phone_number TEXT,
    p_teaching_required BOOLEAN,

    c_id UUID,
    c_name TEXT,
    c_age INT
);
"""
)

ds.session.execute(
"""
CREATE TABLE IF NOT EXISTS sitters(
    s_id UUID PRIMARY KEY,
    s_sitter_type TEXT,
    s_first_name TEXT,
    s_last_name TEXT,
    s_base_price FLOAT,
    s_is_available BOOLEAN,

    as_bonus FLOAT,
    as_max_age INT
);
"""
)

ds.session.execute(
"""
CREATE TABLE IF NOT EXISTS reservations(
    r_id UUID PRIMARY KEY,
    r_date TEXT,
    r_start_hour INT,
    r_end_hour INT,
    
    s_id UUID,
    s_sitter_type TEXT,
    s_first_name TEXT,
    s_last_name TEXT,
    s_base_price FLOAT,
    s_is_available BOOLEAN,

    as_bonus FLOAT,
    as_max_age INT,

    p_id UUID, 
    p_name TEXT,
    p_address TEXT,
    p_phone_number TEXT,
    p_teaching_required BOOLEAN,

    c_id UUID,
    c_name TEXT,
    c_age INT
);
"""
)
