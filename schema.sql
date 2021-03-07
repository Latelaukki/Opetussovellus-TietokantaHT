CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE privileges (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    admin INTEGER,
    teacher INTEGER
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    code TEXT UNIQUE NOT NULL UNIQUE,
    name TEXT NOT NULL,
    content TEXT,
    teacher_id INTEGER REFERENCES users ON DELETE CASCADE 
);

CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL UNIQUE,
    course_id INTEGER REFERENCES courses,
    choice1 TEXT NOT NULL,             --vaihtoehdot oli ensin tallennettu omaksi taulukseen, mutta en keksinyt keinoa iteroida          
    choice2 TEXT NOT NULL,             --html-sivulla yhtä aikaa kysymyksiä ja vaihtoehtoja, niin tämä toteutus olis helpompi siinä suhteessa
    choice3 TEXT,                      --Max kysymysten määrää voi kuitenkin halutessaan muuttaa helposti ja vaihtoehdot voi jättää myös
    choice4 TEXT                       --tyhjäksi paitsi vähintään 2 pitää olla               
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    quiz_id INTEGER REFERENCES quizzes,
    right_answer INTEGER NOT NULL
);

CREATE TABLE participants (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    course_id INTEGER REFERENCES courses
);
