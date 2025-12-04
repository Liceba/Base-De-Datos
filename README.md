SELECT u.email, p.nombre, p.apellido, fecha_registro, Activo FROM Usuarios u JOIN Perfiles p ON u.usuario_id = p.usuario_id WHERE u.usuario_id = 1; -- consultar datos del usuario 1
SELECT u.email, p.nombre, p.apellido, fecha_registro, Activo FROM Usuarios u JOIN Perfiles p ON u.usuario_id = p.usuario_id WHERE u.usuario_id = 2; -- consultar datos del usuario 2

UPDATE Usuarios SET email = 'Bianchi.email@web.com' WHERE usuario_id = 1; -- cambiar el gmail del usuario, ejemplo: Bianchi.email@web.com
UPDATE Usuarios SET password_hash = '251150' WHERE usuario_id = 1;
UPDATE perfiles SET nombre = 'Bianchi' WHERE usuario_id = 1;
UPDATE perfiles SET apellido = 'Naz' WHERE usuario_id = 1;

UPDATE Usuarios SET email = 'ale.email@web.com' WHERE usuario_id = 2; -- cambiar el gmail del usuario, ejemplo: Bianchi.email@web.com
UPDATE Usuarios SET password_hash = '67094' WHERE usuario_id = 2;
UPDATE perfiles SET nombre = 'alejandro' WHERE usuario_id = 2;
UPDATE perfiles SET apellido = 'Molina' WHERE usuario_id = 2;

DELETE FROM Perfiles WHERE usuario_id = 1; --  esto sirve para eliminar datos personales del usuario 1
DELETE FROM Usuarios WHERE usuario_id = 1; -- esto sirve para eliminar el usuario 1 por completo 
DELETE FROM Perfiles WHERE usuario_id = 2; --  esto sirve para eliminar datos personales del usuario 2
DELETE FROM Usuarios WHERE usuario_id = 2; -- esto sirve para eliminar el usuario 2 por completo 

DROP DATABASE Trabajo_web_GreenUp;  -- esto sirve para borra toda la Database por si tubiste un error...
