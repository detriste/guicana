CREATE DATABASE IF NOT EXISTS info;
USE info;

CREATE TABLE detecoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    imagem VARCHAR(255),
    classe VARCHAR(255),
    confianca DECIMAL(5,2),
    caminho_saida VARCHAR(255),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
