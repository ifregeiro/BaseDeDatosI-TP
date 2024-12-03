DROP DATABASE IF EXISTS proyecto_final;
CREATE DATABASE proyecto_final;
USE proyecto_final;

-- Eliminación de tablas si existen
DROP TABLE IF EXISTS pagos;
DROP TABLE IF EXISTS prestamos;
DROP TABLE IF EXISTS libros;
DROP TABLE IF EXISTS usuarios;

-- Tabla de Usuarios
CREATE TABLE usuarios(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    direccion VARCHAR(270),
    fecha_registro DATE NOT NULL
);

-- Tabla de Libros
CREATE TABLE libros(
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(300) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    genero VARCHAR(100) NOT NULL,
    año_publicacion INT NOT NULL,
    cant_copias INT NOT NULL
);

-- Tabla de Préstamos
CREATE TABLE prestamos(
    id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_libro INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE,
    estado VARCHAR(25) NOT NULL DEFAULT 'En progreso',
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro)
);

-- Tabla de Pagos
CREATE TABLE pagos(
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    valor_cuota INT NOT NULL,
    fecha_pago DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Datos iniciales en Usuarios
INSERT INTO usuarios (nombre, email, telefono, direccion, fecha_registro)
VALUES 
('Juan Pérez', 'juan.perez@example.com', '555-1234', 'Calle Falsa 123', DATE_SUB(CURRENT_DATE, INTERVAL 280 DAY)),
('María Gómez', 'maria.gomez@example.com', '555-5678', 'Avenida Siempreviva 742', DATE_SUB(CURRENT_DATE, INTERVAL 320 DAY)),
('Carlos Rodríguez', 'carlos.rod@example.com', '555-9101', 'Boulevard Central 456', DATE_SUB(CURRENT_DATE, INTERVAL 300 DAY)),
('Ana López', 'ana.lopez@example.com', '555-1111', 'Calle Nueva 789', DATE_SUB(CURRENT_DATE, INTERVAL 290 DAY)),
('Luis Martínez', 'luis.mart@example.com', '555-1212', 'Avenida del Sol 321', DATE_SUB(CURRENT_DATE, INTERVAL 310 DAY)),
('Sofía Torres', 'sofia.torres@example.com', '555-1313', 'Calle Luna 654', DATE_SUB(CURRENT_DATE, INTERVAL 305 DAY)),
('Pedro Sánchez', 'pedro.san@example.com', '555-1414', 'Calle Real 987', DATE_SUB(CURRENT_DATE, INTERVAL 275 DAY)),
('Laura Fernández', 'laura.fernandez@example.com', '555-1515', 'Avenida Norte 222', DATE_SUB(CURRENT_DATE, INTERVAL 290 DAY)),
('Andrés Ruiz', 'andres.ruiz@example.com', '555-1616', 'Calle Sur 111', DATE_SUB(CURRENT_DATE, INTERVAL 310 DAY)),
('Clara Morales', 'clara.morales@example.com', '555-1717', 'Boulevard Este 333', DATE_SUB(CURRENT_DATE, INTERVAL 285 DAY));

-- Datos iniciales en Libros
INSERT INTO libros (titulo, autor, genero, año_publicacion, cant_copias)
VALUES 
('Cien años de soledad', 'Gabriel García Márquez', 'Novela', 1967, 5),
('El principito', 'Antoine de Saint-Exupéry', 'Ficción', 1943, 3),
('1984', 'George Orwell', 'Distopía', 1949, 4),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Novela', 1605, 6),
('Matar a un ruiseñor', 'Harper Lee', 'Ficción', 1960, 2),
('La Odisea', 'Homero', 'Épico', -800, 3),
('Fahrenheit 451', 'Ray Bradbury', 'Distopía', 1953, 4),
('El Alquimista', 'Paulo Coelho', 'Ficción', 1988, 5),
('Orgullo y prejuicio', 'Jane Austen', 'Romance', 1813, 3),
('Los miserables', 'Victor Hugo', 'Novela', 1862, 4);
