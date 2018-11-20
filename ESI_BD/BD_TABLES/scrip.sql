
CREATE TABLE buscas(
	idCliente BIGINT NOT NULL,
    busca VARCHAR(255) NOT NULL,
    dt timestamp NOT NULL
);


CREATE TABLE produto(
	idProduto BIGINT PRIMARY KEY NOT NULL,
	vizualizado INT,
    nome VARCHAR(70) NOT NULL,
    categoria VARCHAR(25) NOT NULL,
    preco decimal(6,2) NOT NULL
);

CREATE TABLE tag(
    idProduto BIGINT NOT NULL,
    tag_texto VARCHAR(25) NOT NULL,
    arrayTAG numeric[] NOT NULL,
    FOREIGN KEY (idProduto) REFERENCES produto(idProduto) ON DELETE CASCADE
);

CREATE TABLE visualizacao (
	idCliente BIGINT NOT NULL,
    idProduto BIGINT NOT NULL,
    dt timestamp NOT NULL
    -- FOREIGN KEY (idProduto) REFERENCES produto(idProduto) ON DELETE CASCADE
);


alter table produto alter column vizualizado set default 0;

