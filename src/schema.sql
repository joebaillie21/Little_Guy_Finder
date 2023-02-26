DROP TABLE IF EXISTS Little_Guys;
DROP TABLE IF EXISTS Traits;

CREATE TABLE Little_Guys
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    info TEXT NOT NULL,
    friend_shaped BOOLEAN NOT NULL DEFAULT TRUE,
    primary_trait INT NOT NULL,
    secondary_trait INT,
    tertiary_trait INT
);

CREATE TABLE Traits
(
    id SERIAL PRIMARY KEY,
    trait TEXT
);
