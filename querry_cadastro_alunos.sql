use escola;

CREATE TABLE escola(
	codigo INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    serie INT
);


CREATE TABLE cursos(
	codigo INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100)
);

INSERT INTO cursos values(1, 'Informatica');
INSERT INTO cursos values(2, 'Eletronica');
INSERT INTO cursos values(3, 'Edificacoes');
INSERT INTO cursos values(4, 'Meio Ambiente');

