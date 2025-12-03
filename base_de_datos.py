CREATE DATABASE IF NOT EXISTS Trabajo_web_GreenUp;
USE Trabajo_web_GreenUp;

CREATE TABLE IF NOT EXISTS Usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,  
    password_hash VARCHAR(255) NOT NULL, 
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE -- Indica si la cuenta está activa
);

CREATE TABLE IF NOT EXISTS Perfiles (
    perfil_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL UNIQUE,    
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE,
    
   
    FOREIGN KEY (usuario_id) 
        REFERENCES Usuarios(usuario_id) 
        ON DELETE CASCADE 
);

INSERT INTO Usuarios (email, password_hash) VALUES ('ltceba@web.com', '1234'); -- registro
INSERT INTO Perfiles (usuario_id, nombre, apellido, fecha_nacimiento) VALUES (1, 'Liceba', 'Ceballos', '2009-11-28');  -- perfil

SELECT u.email, p.nombre, p.apellido, fecha_registro, activo FROM Usuarios u JOIN Perfiles p ON u.usuario_id = p.usuario_id WHERE u.usuario_id = 1; -- consultar datos del usuario 

SELECT usuario_id, password_hash, activo FROM Usuarios WHERE email = 'ltceba@web.com'; -- inicio de sesion (El inicio de sesion solo funciona media en el gmail)
UPDATE Usuarios SET email = 'Bianchi.email@web.com' WHERE usuario_id = 1; -- cambiar el gmail del usuario, ejemplo: Bianchi.email@web.com
UPDATE Usuarios SET password_hash = '777' WHERE usuario_id = 1;
UPDATE perfiles SET nombre = 'Bianchi' WHERE usuario_id = 1;
UPDATE perfiles SET apellido = 'alegre' WHERE usuario_id = 1;
DELETE FROM Perfiles WHERE usuario_id = 1; --  esto sirve para eliminar datos personales
DELETE FROM Usuarios WHERE usuario_id = 1; -- esto sirve para eliminar el usuario por completo 
