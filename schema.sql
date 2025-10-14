DROP TABLE IF EXISTS Usuarios;
DROP TABLE IF EXISTS Diarios;
DROP TABLE IF EXISTS Sentimentos;

CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    telefone TEXT NOT NULL
);

CREATE TABLE Sentimentos (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(10)
);

INSERT INTO Sentimentos(id, nome) VALUES 
(1, 'raiva'),
(2, 'tristeza'),
(3, 'felicidade'),
(4, 'medo'),
(5, 'frustacao');

CREATE TABLE Diarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    data_diario DATE NOT NULL DEFAULT CURRENT_DATE,
    id_sentimento INTEGER NOT NULL,
    texto TEXT NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES Usuarios(id),
    FOREIGN KEY(id_sentimento) REFERENCES Sentimentos(id)
);