## Uso de Inteligencia Artificial

Se utilizó IA como apoyo para revisar la estructura de los DAO,
manejo de excepciones y coherencia entre relaciones UML y base de datos.

Las sugerencias fueron revisadas y probadas antes de incorporarlas.

## Adaptación de persistencia a MariaDB

Se utilizó IA como apoyo para revisar y adaptar la persistencia del proyecto.

El proyecto mantenía compatibilidad con SQLite y MariaDB, pero se decidió
mantener únicamente MariaDB debido al alcance trabajado en clases.

La IA fue utilizada para apoyar:
- la eliminación de referencias a SQLite;
- la revisión de la configuración de PyMySQL;
- el diagnóstico del error de clave foránea en `proyecto_empleado`;
- la verificación de compatibilidad entre claves primarias y foráneas;
- la revisión del orden de creación de tablas;
- la revisión de imports después de eliminar archivos `__init__.py`.

Los cambios fueron comprobados mediante ejecución del proyecto y revisión
de las tablas desde phpMyAdmin.

Ejemplo:
- Se aceptó el uso de try/except/finally y rollback en operaciones de escritura.
- Se mantuvo el patrón DAO trabajado en clases.
- No se incorporaron capas Service o Controller porque no corresponden
  al alcance trabajado en la unidad.