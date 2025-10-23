DROP TABLE IF EXISTS Usuarios;
DROP TABLE IF EXISTS Diarios;
DROP TABLE IF EXISTS Sentimentos;
DROP TABLE IF EXISTS PerguntasQuestionario;
DROP TABLE IF EXISTS OpcoesQuestionario;

DROP TABLE IF EXISTS RespostasQuestionario;


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

CREATE TABLE PerguntasQuestionario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL
);

INSERT INTO PerguntasQuestionario(texto) VALUES
('1. Você costuma pular refeições ao longo do dia?'),
('2. Quantas vezes por semana você consome frutas e verduras?'),
('3. Costuma fazer dietas restritivas por conta própria?'),
('4. Sente necessidade de controlar constantemente as calorias dos alimentos?'),
('5. Come rapidamente ou em grandes quantidades sem perceber?'),
('6. Tem episódios de comer compulsivamente (ingerir muita comida de uma vez, mesmo sem fome)?'),
('7. Evita certos alimentos por medo de engordar, mesmo gostando deles?'),
('8. Já usou laxantes, diuréticos ou medicamentos para emagrecer sem prescrição médica?'),
('9. Costuma praticar atividade física em excesso para “compensar” o que comeu?'),
('10. Sente culpa ou arrependimento após se alimentar?'),
('11. Faz refeições em ambientes com distrações (TV, celular, etc.)?'),
('12. Costuma sentir fome real ou mais vontade emocional de comer (ansiedade, tristeza, tédio)?'),
('13. Controla seu peso na balança com muita frequência (todos os dias ou mais de uma vez por dia)?'),
('14. Já teve grandes variações de peso em pouco tempo (perder ou ganhar vários quilos rapidamente)?'),
('15. Sente que sua alimentação impacta diretamente sua autoestima?'),
('16. Você sente ansiedade ou estresse relacionados à comida ou ao seu corpo?'),
('17. Evita sair ou participar de eventos sociais por medo da comida que será servida?'),
('18. Costuma comparar seu corpo com o de outras pessoas de forma negativa?'),
('19. Já foi alvo de críticas ou comentários sobre seu corpo que ainda afetam sua autoestima?'),
('20. Sente que sua imagem no espelho não corresponde à realidade (acha-se maior ou menor do que realmente é)?'),
('21. Tem dificuldade em aceitar elogios relacionados à aparência?'),
('22. Seu humor muda de forma significativa conforme seu peso ou forma corporal?'),
('23. Já deixou de realizar atividades importantes (trabalho, estudo, lazer) por causa da preocupação com peso ou alimentação?'),
('24. Sente que precisa ter controle absoluto sobre sua alimentação, e isso gera sofrimento?'),
('25. Já teve pensamentos obsessivos sobre comida ou peso que atrapalham seu dia a dia?'),
('26. Tem sentimentos de inadequação ou vergonha relacionados ao corpo?'),
('27. Costuma usar a alimentação como forma de lidar com emoções (recompensa, conforto, alívio)?'),
('28. Já teve episódios de restrição alimentar severa (ficar longos períodos sem comer)?'),
('29. Acredita que seu valor pessoal depende do peso ou da forma física?'),
('30. Tem consciência de que sua relação com a comida pode estar prejudicando sua saúde física e emocional?');

CREATE TABLE OpcoesQuestionario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

INSERT INTO OpcoesQuestionario(nome) VALUES
('Nunca'),
('Raramente'),
('Às vezes'),
('Frequentemente'),
('Sempre');

CREATE TABLE RespostasQuestionario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    data_questionario DATE NOT NULL DEFAULT CURRENT_DATE,
    resposta_questao_1 INTEGER,
    resposta_questao_2 INTEGER,
    resposta_questao_3 INTEGER,
    resposta_questao_4 INTEGER,
    resposta_questao_5 INTEGER,
    resposta_questao_6 INTEGER,
    resposta_questao_7 INTEGER,
    resposta_questao_8 INTEGER,
    resposta_questao_9 INTEGER,
    resposta_questao_10 INTEGER,
    resposta_questao_11 INTEGER,
    resposta_questao_12 INTEGER,
    resposta_questao_13 INTEGER,
    resposta_questao_14 INTEGER,
    resposta_questao_15 INTEGER,
    resposta_questao_16 INTEGER,
    resposta_questao_17 INTEGER,
    resposta_questao_18 INTEGER,
    resposta_questao_19 INTEGER,
    resposta_questao_20 INTEGER,
    resposta_questao_21 INTEGER,
    resposta_questao_22 INTEGER,
    resposta_questao_23 INTEGER,
    resposta_questao_24 INTEGER,
    resposta_questao_25 INTEGER,
    resposta_questao_26 INTEGER,
    resposta_questao_27 INTEGER,
    resposta_questao_28 INTEGER,
    resposta_questao_29 INTEGER,
    resposta_questao_30 INTEGER,
    FOREIGN KEY(id_usuario) REFERENCES Usuarios(id),
    FOREIGN KEY(
        resposta_questao_1,
        resposta_questao_2,
        resposta_questao_3,
        resposta_questao_4,
        resposta_questao_5,
        resposta_questao_6,
        resposta_questao_7,
        resposta_questao_8,
        resposta_questao_9,
        resposta_questao_10,
        resposta_questao_11,
        resposta_questao_12,
        resposta_questao_13,
        resposta_questao_14,
        resposta_questao_15,
        resposta_questao_16,
        resposta_questao_17,
        resposta_questao_18,
        resposta_questao_19,
        resposta_questao_20,
        resposta_questao_21,
        resposta_questao_22,
        resposta_questao_23,
        resposta_questao_24,
        resposta_questao_25,
        resposta_questao_26,
        resposta_questao_27,
        resposta_questao_28,
        resposta_questao_29,
        resposta_questao_30
        ) REFERENCES OpcoesQuestionario(id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id, id)
  );