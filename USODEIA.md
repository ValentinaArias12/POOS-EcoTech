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


# Uso de IA en 3ra evaluación 
Se utilizó la IA como asistente complementario en el manejo de excepciones y en el consumo de la API, además de verificar los métodos DAO para que estén actualizados.
Se modificaron fragmentos dados por la IA cuando presentaban riesgos o cuando no respetaban la arquitectura del proyecto.

Se mantuvo estrictamente la arquitectura en capas del proyecto (se agregó servicios/), comprobando el funcionamiento mediante pruebas de inicio de sesión y simulación de fallos.

Su uso también pudo permitir el uso de la base de datos de MySql/MariaDB como también de SQLite 


Seguridad y Roles: Se aceptó el uso de bcrypt (hashpw/checkpw) para contraseñas y se estructuró el control de acceso por roles (admin/empleado) integrando el ID de sesión para automatizar fichas y registros; además de mejorar la interacción del menú exclusivo para usuarios con rol \`empleado\`.




