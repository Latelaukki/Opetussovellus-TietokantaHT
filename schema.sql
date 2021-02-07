CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    privilige INTEGER -- 0 = student, 1 = teacher, 2 = admin
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    content TEXT
);


