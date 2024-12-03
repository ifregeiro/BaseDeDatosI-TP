# Sistema de Gestión de Biblioteca

### Esquema BD
Sea el siguiente esquema BD que representa el sistema de los usuarios, libros,préstamos y pagos de una biblioteca.
**`BIBLIOTECA <USUARIOS, LIBROS, PRESTAMOS, PAGOS>`**
### Restricciones
a. **`id_usuario`** es el identificador único para cada usuario.
b. **`id_libro`** es el identificador único para cada libro.
c. **`id_prestamo`** es el identificador único para cada préstamo.
d. **`id_pago`** es el identificador único para cada pago.
e. **`email`** debe ser único para cada usuario.
e. Un mismo usuario puede tener varios préstamos, y un mismo libro puede ser prestado a un usuario a la vez.
f. Un mismo usuario no puede tener varios pagos.
g. Un libro puede tener varios autores.
h. Un autor puede tener varios libros.

---

### Paso 1: Determinar las Dependencias Funcionales (DFs)
1. **`id_usuario`** -> **`nombre, email, telefono, direccion, fecha_registro`** : Cada usuario tiene un nombre, email, teléfono, dirección y fecha de registro.
2. **`id_libro`** -> **`titulo, autor, genero, año_publicacion, cant_copias`** : Cada libro tiene un título, autor, género, año de publicación y cantidad de copias.
3. **`id_prestamo`** -> **`id_usuario, id_libro, fecha_prestamo, fecha_devolucion, estado`** : Cada préstamo tiene un usuario, libro, fecha de préstamo, fecha de devolución y estado.
4. **`id_pago`** -> **`id_usuario, valor_cuota, fecha_pago`** : Cada pago tiene un usuario, valor de cuota y fecha de pago.

---
### Paso 2: Determinar las Claves Candidatas
- La combinación de **`id_usuario`** , **`id_libro`** es suficiente para identificar un préstamo o un pago, ya que:
    -**`id_usuario`** Especifica el usuario que realiza el préstamo o el pago.
    -**`id_libro`** Especifica el libro que se presta o se paga.

Por lo tanto, la **clave candidata** es: 
    
    - (**`id_usuario`** , **`id_libro`**).
Esta combinación asegura que cada préstamo o pago pueda ser identificado de manera única.

---
### Paso 3: Diseño en Tercera Forma Normal (3NF)

Para llevar el esquema a la **Tercera Forma Normal (3NF)**, se deben eliminar las dependencias funcionales que no sean triviales, y asegurarnos de que cada atributo no clave dependa únicamente de la clave primaria completa.

Por ende se crean 4 tablas para cumplir con la 3NF:

El diseño en 3FN quedaría de la siguiente manera:

1. Tabla **`USUARIOS`**:
    - **`id_usuario`** (Clave Primaria, Único)
    - **`nombre`**
    - **`email`** (Único)
    - **`telefono`**
    - **`direccion`**
    - **`fecha_registro`**

2. Tabla **`LIBROS`**:
    - **`id_libro`** (Clave Primaria, Único)
    - **`titulo`**
    - **`autor`**
    - **`genero`**
    - **`año_publicacion`**
    - **`cant_copias`**

3. Tabla **`PRESTAMOS`**:
    - **`id_prestamo`** (Clave Primaria, Único)
    - **`id_usuario`** (Clave Foránea que referencia USUARIOS)
    - **`id_libro`** (Clave Foránea que referencia LIBROS)
    - **`fecha_prestamo`**
    - **`fecha_devolucion`**
    - **`estado`**

4. Tabla **`PAGOS`**:
    - **`id_pago`** (Clave Primaria, Único)
    - **`id_usuario`** (Clave Foránea que referencia USUARIOS)
    - **`valor_cuota`**
    - **`fecha_pago`**


