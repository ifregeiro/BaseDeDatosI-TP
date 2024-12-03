import mysql.connector
from mysql.connector import Error

# pip install mysql-connector-python (Instalador .venv)

# Conexión a la base de datos
def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='proyecto_final',
            user='root',
            password='password'
        )
        return conexion
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

#Menú principal
def menu():
    print("""
    --- Menú Principal ---
    1. Gestión de Usuarios
    2. Gestión de Libros
    3. Manejo de Préstamos
    4. Reporte de Morosos
    5. Búsqueda y Filtrado
    6. Modificación de Cuota
    7. Salir
    """)

# Gestión de usuarios
def gestion_usuarios(conexion):
    while True:
        cursor = conexion.cursor()

        print("""
        --- Gestión de Usuarios ---
        1. Agregar Usuario
        2. Ver Usuarios
        3. Actualizar Usuario
        4. Eliminar Usuario
        5. Volver al Menú Principal
        """)

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre del usuario: ")
                fecha_registro = input("Fecha de registro (YYYY-MM-DD): ")
                cuota = float(input("Cuota mensual: "))
                query = "INSERT INTO usuarios (nombre, fecha_registro, cuota_mensual) VALUES (%s, %s, %s)"
                cursor.execute(query, (nombre, fecha_registro, cuota))
                conexion.commit()
                print("Usuario agregado con éxito.")
            except Exception as e:
                print(f"Error al agregar usuario: {e}")

        elif opcion == "2":
            try:
                cursor.execute("SELECT * FROM usuarios")
                print("\n--- Lista de Usuarios ---")
                for usuario in cursor.fetchall():
                    print(usuario)
            except Exception as e:
                print(f"Error al obtener usuarios: {e}")

        elif opcion == "3":
            try:
                id_usuario = input("ID del usuario a actualizar: ")
                nuevo_nombre = input("Nuevo nombre: ")
                query = "UPDATE usuarios SET nombre = %s WHERE id_usuario = %s"
                cursor.execute(query, (nuevo_nombre, id_usuario))
                conexion.commit()
                print("Usuario actualizado con éxito.")
            except Exception as e:
                print(f"Error al actualizar usuario: {e}")

        elif opcion == "4":
            try:
                id_usuario = input("ID del usuario a eliminar: ")
                query = "DELETE FROM usuarios WHERE id_usuario = %s"
                cursor.execute(query, (id_usuario,))
                conexion.commit()
                print("Usuario eliminado con éxito.")
            except Exception as e:
                print(f"Error al eliminar usuario: {e}")

        elif opcion == "5": #Rompe bucle
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida, intenta nuevamente.")

def gestion_libros(conexion):
    while True:

        print("""
        --- Gestión de Libros ---
        1. Agregar Libro
        2. Ver Libros
        3. Actualizar Libro
        4. Eliminar Libro
        5. Volver al Menú Principal
        """)
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            #Agregar un nuevo libro
            try:
                titulo = input("Título del libro: ")
                autor = input("Autor del libro: ")
                genero = input("Género del libro: ")
                año_publicacion = int(input("Año de publicación: "))
                cant_copias = int(input("Cantidad de copias: "))

                cursor = conexion.cursor()
                query = "INSERT INTO libros (titulo, autor, genero, año_publicacion, cant_copias) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (titulo, autor, genero, año_publicacion, cant_copias))
                conexion.commit()
                print("¡Libro agregado exitosamente!")
            except Exception as e:
                print(f"Error al agregar libro: {e}")

        elif opcion == "2":
            #Ver todos los libros
            try:
                cursor = conexion.cursor()
                query = "SELECT * FROM libros"
                cursor.execute(query)
                libros = cursor.fetchall()

                print("\n--- Lista de Libros ---")
                for libro in libros:
                    print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Género: {libro[3]}, Año: {libro[4]}, Copias: {libro[5]}")
            except Exception as e:
                print(f"Error al obtener los libros: {e}")

        elif opcion == "3":
            #Actualizar información de un libro
            try:
                id_libro = int(input("ID del libro a actualizar: "))
                titulo = input("Nuevo título (dejar vacío para no cambiar): ")
                autor = input("Nuevo autor (dejar vacío para no cambiar): ")
                genero = input("Nuevo género (dejar vacío para no cambiar): ")
                año_publicacion = input("Nuevo año de publicación (dejar vacío para no cambiar): ")
                cant_copias = input("Nueva cantidad de copias (dejar vacío para no cambiar): ")

                cursor = conexion.cursor()
                query = "UPDATE libros SET "
                valores = []
                if titulo:
                    query += "titulo = %s, "
                    valores.append(titulo)
                if autor:
                    query += "autor = %s, "
                    valores.append(autor)
                if genero:
                    query += "genero = %s, "
                    valores.append(genero)
                if año_publicacion:
                    query += "año_publicacion = %s, "
                    valores.append(int(año_publicacion))
                if cant_copias:
                    query += "cant_copias = %s, "
                    valores.append(int(cant_copias))

                query = query.rstrip(", ") + " WHERE id_libro = %s"
                valores.append(id_libro)

                cursor.execute(query, tuple(valores))
                conexion.commit()
                print("¡Libro actualizado exitosamente!")
            except Exception as e:
                print(f"Error al actualizar libro: {e}")

        elif opcion == "4":
            #Eliminar un libro
            try:
                id_libro = int(input("ID del libro a eliminar: "))
                cursor = conexion.cursor()
                query = "DELETE FROM libros WHERE id_libro = %s"
                cursor.execute(query, (id_libro,))
                conexion.commit()
                print("¡Libro eliminado exitosamente!")
            except Exception as e:
                print(f"Error al eliminar libro: {e}")

        elif opcion == "5":
            #Volver al menú principal
            break
        else:
            print("Opción no válida, intenta nuevamente.")


# Gestión de préstamos
def manejo_prestamos(conexion):
    while True:

        print("""
        --- Manejo de Préstamos ---
        1. Registrar Préstamo
        2. Devolver Libro
        3. Ver Préstamos Activos
        4. Volver al Menú Principal
        """)
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            #Registrar un nuevo préstamo
            try:
                id_usuario = int(input("ID del usuario: "))
                id_libro = int(input("ID del libro: "))
                fecha_prestamo = input("Fecha de préstamo (YYYY-MM-DD): ")

                cursor = conexion.cursor()
                query = "INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, estado) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (id_usuario, id_libro, fecha_prestamo, "En progreso"))
                conexion.commit()
                print("¡Préstamo registrado exitosamente!")
            except Exception as e:
                print(f"Error al registrar préstamo: {e}")

        elif opcion == "2":
            #Devolver un libro
            try:
                id_prestamo = int(input("ID del préstamo a devolver: "))
                fecha_devolucion = input("Fecha de devolución (YYYY-MM-DD): ")

                cursor = conexion.cursor()
                query = "UPDATE prestamos SET fecha_devolucion = %s, estado = %s WHERE id_prestamo = %s"
                cursor.execute(query, (fecha_devolucion, "Devuelto", id_prestamo))
                conexion.commit()
                print("¡Libro devuelto exitosamente!")
            except Exception as e:
                print(f"Error al devolver libro: {e}")

        elif opcion == "3":
            #Ver préstamos activos
            try:
                cursor = conexion.cursor()
                query = """
                    SELECT p.id_prestamo, u.nombre, l.titulo, p.fecha_prestamo, p.estado
                    FROM prestamos p
                    JOIN usuarios u ON p.id_usuario = u.id_usuario
                    JOIN libros l ON p.id_libro = l.id_libro
                    WHERE p.estado = 'En progreso'
                """
                cursor.execute(query)
                prestamos = cursor.fetchall()

                print("\n--- Préstamos Activos ---")
                for prestamo in prestamos:
                    print(f"ID: {prestamo[0]}, Usuario: {prestamo[1]}, Libro: {prestamo[2]}, Fecha Préstamo: {prestamo[3]}, Estado: {prestamo[4]}")
            except Exception as e:
                print(f"Error al obtener los préstamos activos: {e}")

        elif opcion == "4":
            #Volver al menú principal
            break
        else:
            print("Opción no válida, intenta nuevamente.")


#Reporte de morosos
def reporte_morosos(conexion):

    cursor = conexion.cursor()

    query = """
    SELECT Usuarios.Nombre, AVG(MONTH(CURDATE()) - MONTH(FechaRegistro)) AS Antiguedad
    FROM Usuarios
    LEFT JOIN Prestamos ON Usuarios.ID = Prestamos.UsuarioID
    GROUP BY Usuarios.Nombre
    """
    cursor.execute(query)
    for registro in cursor.fetchall():
        print(registro)

#Búsqueda y Filtrado
def busqueda_filtrado(conexion):
    cursor = conexion.cursor()
    print("""
    --- Búsqueda y Filtrado ---
    1. Buscar Usuarios
    2. Buscar Libros
    3. Volver al Menú Principal
    """)

    opcion = input("Selecciona una opción: ")

    if opcion == "1":  #Buscar Usuarios
        atributo = input("Buscar por (nombre, email, id_usuario): ").lower()
        valor = input("Introduce el valor a buscar: ")
        query = f"SELECT * FROM usuarios WHERE {atributo} LIKE %s"
        cursor.execute(query, (f"%{valor}%",))
        resultados = cursor.fetchall()

        if resultados:
            print("\n--- Resultados de la Búsqueda ---")
            for usuario in resultados:
                print(usuario)
        else:
            print("No se encontraron usuarios que coincidan con la búsqueda.")

    elif opcion == "2":  #Buscar Libros
        atributo = input("Buscar por (titulo, autor, genero): ").lower()
        valor = input("Introduce el valor a buscar: ")
        query = f"SELECT * FROM libros WHERE {atributo} LIKE %s"
        cursor.execute(query, (f"%{valor}%",))
        resultados = cursor.fetchall()

        if resultados:
            print("\n--- Resultados de la Búsqueda ---")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")

    elif opcion == "3":  #Volver al menú principal
        print("Volviendo al menú principal...")
        return

    else:
        print("Opción no válida. Intenta nuevamente.")

#Modificación de Cuota
def modificacion_cuota(conexion):
    cursor = conexion.cursor()
    print("\n--- Modificación de Cuota ---")
    try:
        id_usuario = input("ID del usuario: ")
        mes = input("Mes de la cuota a modificar (1-12): ")
        anio = input("Año de la cuota a modificar: ")
        nueva_cuota = float(input("Nuevo valor de la cuota: "))

        #Actualizar cuota en la tabla de pagos
        query = """
        UPDATE pagos 
        SET valor_cuota = %s 
        WHERE id_usuario = %s AND MONTH(fecha_pago) = %s AND YEAR(fecha_pago) = %s
        """
        cursor.execute(query, (nueva_cuota, id_usuario, mes, anio))
        conexion.commit()

        if cursor.rowcount > 0:
            print("Cuota modificada con éxito.")
        else:
            print("No se encontró un pago para ese usuario en el mes y año especificados.")

    except Exception as e:
        print(f"Error al modificar la cuota: {e}")

#Programa principal
def main():
    conexion = conectar()

    if conexion:
        while True:
            menu()
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                gestion_usuarios(conexion)
            elif opcion == "2":
                gestion_libros(conexion)
            elif opcion == "3":
                manejo_prestamos(conexion)
            elif opcion == "4":
                reporte_morosos(conexion)
            elif opcion == "5":
                busqueda_filtrado(conexion)
            elif opcion == "6":
                modificacion_cuota(conexion)
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")

        conexion.close()

if __name__ == "__main__":
    main()
