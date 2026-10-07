from persistencia.conexion import abrir_conexion, obtener_motor


def crear_tablas():
    conexion = None
    try:
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        if obtener_motor() == "sqlite":
            sentencias = [
                """
                CREATE TABLE IF NOT EXISTS departamento (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS empleado (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    correo TEXT NOT NULL UNIQUE,
                    telefono TEXT,
                    fecha_inicio TEXT NOT NULL,
                    salario_base REAL NOT NULL DEFAULT 0,
                    tipo TEXT NOT NULL DEFAULT 'BASE',
                    bono_anual REAL NOT NULL DEFAULT 0,
                    tarifa_hora REAL NOT NULL DEFAULT 0,
                    departamento_id INTEGER,
                    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
                        ON UPDATE CASCADE ON DELETE SET NULL
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS proyecto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE,
                    descripcion TEXT,
                    fecha_inicio TEXT NOT NULL,
                    activo INTEGER NOT NULL DEFAULT 1
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS proyecto_empleado (
                    proyecto_id INTEGER NOT NULL,
                    empleado_id INTEGER NOT NULL,
                    PRIMARY KEY (proyecto_id, empleado_id),
                    FOREIGN KEY (proyecto_id) REFERENCES proyecto(id) ON DELETE CASCADE,
                    FOREIGN KEY (empleado_id) REFERENCES empleado(id) ON DELETE CASCADE
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS registro_tiempo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT NOT NULL,
                    horas REAL NOT NULL CHECK (horas > 0 AND horas <= 24),
                    descripcion TEXT NOT NULL,
                    empleado_id INTEGER NOT NULL,
                    proyecto_id INTEGER NOT NULL,
                    FOREIGN KEY (empleado_id) REFERENCES empleado(id) ON DELETE CASCADE,
                    FOREIGN KEY (proyecto_id) REFERENCES proyecto(id) ON DELETE CASCADE
                )
                """,
            ]
        else:
            sentencias = [
                """
                CREATE TABLE IF NOT EXISTS departamento (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(100) NOT NULL UNIQUE
                ) ENGINE=InnoDB
                """,
                """
                CREATE TABLE IF NOT EXISTS empleado (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(120) NOT NULL,
                    correo VARCHAR(150) NOT NULL UNIQUE,
                    telefono VARCHAR(30),
                    fecha_inicio DATE NOT NULL,
                    salario_base DECIMAL(12,2) NOT NULL DEFAULT 0,
                    tipo VARCHAR(20) NOT NULL DEFAULT 'BASE',
                    bono_anual DECIMAL(12,2) NOT NULL DEFAULT 0,
                    tarifa_hora DECIMAL(12,2) NOT NULL DEFAULT 0,
                    departamento_id INT NULL,
                    CONSTRAINT fk_empleado_departamento FOREIGN KEY (departamento_id)
                        REFERENCES departamento(id) ON UPDATE CASCADE ON DELETE SET NULL
                ) ENGINE=InnoDB
                """,
                """
                CREATE TABLE IF NOT EXISTS proyecto (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(120) NOT NULL UNIQUE,
                    descripcion VARCHAR(500),
                    fecha_inicio DATE NOT NULL,
                    activo BOOLEAN NOT NULL DEFAULT TRUE
                ) ENGINE=InnoDB
                """,
                """
                CREATE TABLE IF NOT EXISTS proyecto_empleado (
                    proyecto_id INT NOT NULL,
                    empleado_id INT NOT NULL,
                    PRIMARY KEY (proyecto_id, empleado_id),
                    CONSTRAINT fk_pe_proyecto FOREIGN KEY (proyecto_id) REFERENCES proyecto(id) ON DELETE CASCADE,
                    CONSTRAINT fk_pe_empleado FOREIGN KEY (empleado_id) REFERENCES empleado(id) ON DELETE CASCADE
                ) ENGINE=InnoDB
                """,
                """
                CREATE TABLE IF NOT EXISTS registro_tiempo (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    fecha DATE NOT NULL,
                    horas DECIMAL(5,2) NOT NULL,
                    descripcion VARCHAR(500) NOT NULL,
                    empleado_id INT NOT NULL,
                    proyecto_id INT NOT NULL,
                    CONSTRAINT fk_rt_empleado FOREIGN KEY (empleado_id) REFERENCES empleado(id) ON DELETE CASCADE,
                    CONSTRAINT fk_rt_proyecto FOREIGN KEY (proyecto_id) REFERENCES proyecto(id) ON DELETE CASCADE
                ) ENGINE=InnoDB
                """,
            ]

        for sql in sentencias:
            cursor.execute(sql)
        conexion.commit()
    except Exception:
        if conexion:
            conexion.rollback()
        raise
    finally:
        if conexion:
            conexion.close()


if __name__ == "__main__":
    crear_tablas()
    print("Base de datos preparada correctamente.")
