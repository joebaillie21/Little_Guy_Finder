DROP TABLE IF EXISTS Little_Guys;
DROP TABLE IF EXISTS Traits;

CREATE TABLE Little_Guys
(
    id SERIAL PRIMARY KEY,
    lg_name TEXT,
    info TEXT,
    primary_trait INT NOT NULL,
    secondary_trait INT,
    tertiary_trait INT
);

CREATE TABLE Traits
(
    id SERIAL PRIMARY KEY,
    trait TEXT
);
