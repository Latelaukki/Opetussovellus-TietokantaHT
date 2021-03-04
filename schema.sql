CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    code TEXT UNIQUE NOT NULL UNIQUE,
    name TEXT NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE privileges (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    admin INTEGER,
    teacher INTEGER
);
