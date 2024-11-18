# Ejercicio 6 - Juegos Olímpicos

### Esquema BD

Sea el siguiente esquema de BD que representa a los deportistas que participaron en los Juegos Olímpicos de diferentes años.

**`JUEGO <año_olimpiada, pais_olimpiada, nombre_deportista, pais_deportista, nombre_disciplina, asistente>`**

### Restricciones

a. **`pais_olimpiada`** es el país donde se realizó el juego olímpico del año correspondiente.

b. **`pais_deportista`** es el país que representa el deportista.

c. Un deportista representa en todos los juegos olímpicos siempre al mismo país. Por un país, participan varios deportistas cada juego olímpico.

d. En un año determinado se hacen los juegos olímpicos en un solo país, pero en un país pueden haberse jugados varios juegos olímpicos en diferentes años.

e. Cada deportista puede participar en varios juegos olímpicos y en varias disciplinas en diferentes juegos olímpicos. Pero en un juego olímpico solamente participa en una disciplina.

f. Un deportista tiene un asistente en cada juego olímpico, pero puede variar en diferentes juegos.



---



### Paso 1: Determinar las Dependencias Funcionales (DFs)

1. **`pais_olimpiada`**  -> **`año_olimpiada`**: **`pais_olimpiada`** es el país donde se realizó el juego olímpico del año correspondiente

2. **`pais_deportista`** -> **`nombre_deportista`**: **`pais_deportista`** es el país que representa el deportista.

3. **`nombre_deportista`** -> **`pais_deportista`**: Un deportista representa en todos los juegos olímpicos siempre al mismo país. Por un  país, participan varios deportistas cada juego olímpico. 

4. **`año_olimpiada`** -> **`pais_olimpiada`**: En un año determinado se hacen los juegos olímpicos en un solo país, pero en un país 
pueden haberse jugados varios juegos olímpicos en diferentes años. 

5. **`nombre_deportista`**, **`año_olimpiada`** -> **`nombre_disciplina`**: Cada deportista puede participar en varios juegos olímpicos y en varias disciplinas en 
diferentes juegos olímpicos. Pero en un juego olímpico solamente participa en una 
disciplina.

6. **`año_olimpiada`**, **`nombre_deportista`** -> **`asistente`** : Un deportista tiene un asistente en cada juego olímpico, pero puede variar en diferentes juegos. 



---



### Paso 2: Determinar las Claves Candidatas

Para determinar las **claves candidatas**, necesitamos encontrar un conjunto de atributos que puedan identificar de manera única a cada fila de la tabla **`JUEGOS`** .
En este caso, podemos ver que:

- La combinación **`año_olimpiada`** , **`nombre_deportista`** es suficiente para identificar de forma única cada registro en la tabla, ya que:

    - **`año_olimpiada`** Especifica el año de la olimpiada.
    - **`nombre_deportista`** Identifica unicamente al participante en esa olimpiada.

Por lo tanto, la **clave candidata** es:

- (**`año_olimpiada`** , **`nombre_deportista`**)

Esta combinación asegura que cada registro en la tabla sea único y no haya duplicados.



---



### Paso 3: Diseño en Tercera Forma Normal (3FN)

Para llevar el esquema a la **Tercera Forma Normal (3FN)**, necesitamos eliminar dependencias transitivas y asegurarnos de que cada atributo no clave dependa únicamente de la clave primaria completa. 

Esto implica dividir la tabla en varias tablas relacionadas para reducir la redundancia y asegurar la integridad de los datos.

Se dividió la tabla original en cuatro tablas ( **`Olimpiada`** , **`Deportista`**, **`Disciplina`** y **`Participacion`** ) para eliminar dependencias transitivas y garantizar que cada atributo no clave dependa únicamente de la clave primaria completa.

Este proceso de normalización permite reducir la redundancia y mantener la consistencia de los datos en la base de datos.

El nuevo diseño en 3FN sería el siguiente:

1. Tabla **`Juegos`:**
   - `año_olimpiada` (Clave Primaria)
   - `pais_olimpiada` 

2. Tabla **`Deportista`:**
    - `nombre_deportista` (Clave Primaria)
    - `pais_deportista`

3. Tabla **`Disciplina`:**
    - `nombre_disciplina` (Clave Primaria)
    
4. Tabla **`Participación`:**
    - `nombre_disciplina` (Clave Foránea que referencia a Disciplina)
    - `nombre_deportista` (Clave Foránea que referencia a Deportista)
    - `año_olimpiada` (Clave foránea que referencia a Juegos)
    - `asistente`