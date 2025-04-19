c.execute('''CREATE TABLE main(
    user VARCHAR(100) PRIMARY KEY,
    password VARCHAR(100),
    total INTEGER,
    food INTEGER,
    fuel INTEGER,
    outing INTEGER,
    savings INTEGER,
    misc INTEGER,
    mandatory INTEGER,
    spending INTEGER)''')