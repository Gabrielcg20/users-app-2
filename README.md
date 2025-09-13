# Documentación del Proyecto: users-app


## Visión General del Proyecto

El presente documento provee una descripción detallada de un proyecto de demostración, cuya finalidad es la implementación de una interfaz de programación de aplicaciones (API) con arquitectura \*\*RESTful\*\* para la gestión de entidades de usuario. La aplicación se fundamenta en el lenguaje de programación \*\*Python\*\*, utilizando el framework web \*\*Flask\*\*, y se adhiere a los principios de la metodología RESTful para una interacción coherente y predecible con los recursos del sistema.

El objetivo principal de esta iniciativa se centra en el establecimiento de los puntos de acceso (\*\*endpoints\*\*) necesarios para ejecutar un conjunto de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre la entidad User, lo cual asegura la escalabilidad y la mantenibilidad de la arquitectura subyacente.

- - -

## Estructura del Proyecto

La organización del proyecto se ha diseñado con un enfoque modular, facilitando la navegación y el mantenimiento del código fuente.

```
.
├── app.py
├── routes/
│   ├── __init__.py
│   └── users.py
├── templates/
│   ├── index.html
│   └── user_list.html
└── mock.py
```

*   **app.py:** Constituye el archivo principal del sistema, responsable de la inicialización y el arranque de la aplicación.
*   **routes/:** Este directorio alberga los módulos que definen los endpoints específicos para la entidad User.
*   **templates/:** Ubicación designada para las plantillas de presentación en formato HTML.
*   **mock.py:** Un archivo de utilidad empleado para la generación de datos simulados a efectos de prueba y desarrollo.

- - -

## Tecnologías y Metodologías

### Tecnologías de Implementación

*   **Python:** El lenguaje de programación primario utilizado para el desarrollo del backend de la aplicación.
*   **Flask:** Un micro-framework web que proporciona las herramientas esenciales para la construcción de la API.

### Metodología de Desarrollo

*   **RESTful:** La arquitectura de diseño que rige el comportamiento de la API. Dicha metodología utiliza los verbos del protocolo HTTP para la manipulación de los recursos del sistema de forma estandarizada y semántica.

- - -

## Procedimiento de Despliegue y Ejecución

El proceso de puesta en marcha del proyecto se realiza mediante una secuencia de pasos estandarizada.

1.  Se requiere la verificación de la instalación de Python en el entorno de ejecución.
2.  El repositorio del proyecto debe ser clonado localmente.
3.  Las dependencias requeridas han de ser instaladas mediante el siguiente comando:

```
pip install Flask
```

4.  La aplicación se ejecuta desde el directorio raíz del proyecto con la instrucción:

```
python app.py
```

Posteriormente, la API estará accesible en la siguiente dirección de red: [http://127.0.0.1:5000](http://127.0.0.1:5000).

- - -

## Puntos de Acceso (Endpoints) de la API RESTful

La API dispone de cinco puntos de acceso, los cuales permiten la completa manipulación de los datos de usuario de acuerdo con las convenciones de los métodos HTTP.

| Método HTTP | URL | Descripción |
| --- | --- | --- |
| GET | /users/list | Permite la recuperación de la totalidad de los registros de usuario. |
| GET | /user/ | Facilita la obtención de los detalles correspondientes a un usuario específico utilizando el nombre o email. |
| POST | /user/add | Se utiliza para la creación de un nuevo registro de usuario. |
| PUT | /user/modify | Habilita la actualización de los datos de un registro de usuario preexistente, modificando solamente nombre y edad. |
| DELETE | /user/delete | Se emplea para la eliminación de un registro de usuario del sistema por medio del email. |

- - -

## Proceso de Contribución

Se invita a la colaboración en el desarrollo del proyecto. El procedimiento para la contribución se articula en las siguientes fases:

1.  Se requiere la bifurcación (\*\*fork\*\*) del repositorio principal.
2.  La creación de una nueva rama de desarrollo es necesaria para la implementación de las modificaciones.
3.  Los cambios realizados deben ser confirmados a través de un \*\*commit\*\*.
4.  La rama local debe ser sincronizada con el repositorio remoto.
5.  Finalmente, se debe emitir una solicitud de incorporación (\*\*pull request\*\*) para su revisión y eventual integración.
