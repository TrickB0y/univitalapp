DROP TABLE IF EXISTS Usuarios;
DROP TABLE IF EXISTS Diario

CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    telefone VARCHAR(11) NOT NULL
);

CREATE TABLE Diario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    data_diario DATE NOT NULL DEFAULT CURRENT_DATE,
    sentimento ENUM('raiva', 'tristeza', 'felicidade', 'medo', 'frustacao') NOT NULL,
    texto TEXT NOT NULL
)