# Convenciones de Nomenclatura en JavaScript

Este documento establece las directrices para la **nomenclatura de identificadores (funciones)** en nuestros proyectos de JavaScript. Adoptamos la convención **Camel Case** y utilizamos el **inglés** para la legibilidad y estandarización global.

## Principios Clave para la Nomenclatura de Funciones

Una buena función debe ser:

1. Muy descriptiva:** Debe indicar de forma inequívoca lo que hace.
2. Específica:** Debe enfocarse en una sola tarea (Principio de Responsabilidad Única).
3. Activa:** Debe comenzar con un **verbo** que describa la acción.
4. Natural en inglés:** Debe sonar bien y ser idiomática.
5. Fácil de entender:** Debe ser legible por cualquier desarrollador.

> **Ejemplo:** En lugar de `function abc()`, usamos `function calculateMonthlyRevenue()`.


##  Estructura de Nomenclatura por Categoría

La siguiente tabla desglosa las convenciones para diferentes tipos de operaciones comunes:

### 1. Funciones de Manipulación de Datos

Estas funciones se centran en el procesamiento, formato o verificación de la información.

| Función (Camel Case) | Traducción al Español | Verbo Clave | Objeto Clave | Propósito |
| :--- | :--- | :--- | :--- | :--- |
| `calculateTotalPrice()` | Calcular Precio Total | `calculate` | `TotalPrice` | Retorna un valor numérico/monetario. |
| `formatUserInput()` | Formatear Entrada de Usuario | `format` | `UserInput` | Ajusta la estructura de un dato. |
| `validateEmailAddress()` | Validar Dirección de Correo | `validate` | `EmailAddress` | Comprueba la validez de un dato. |
| `convertToCamelCase()` | Convertir a Camel Case | `convert` | `CamelCase` | Transforma un valor entre tipos/formatos. |
| `filterActiveUsers()` | Filtrar Usuarios Activos | `filter` | `ActiveUsers` | Selecciona un subconjunto de datos. |

---

### 2. Eventos o Interacción

Estas funciones responden a acciones del usuario o a cambios en el estado de la aplicación.

| Función (Camel Case) | Traducción al Español | Prefijo/Verbo Clave | Propósito |
| :--- | :--- | :--- | :--- |
| `handleButtonClick()` | Manejar Clic de Botón | `handle` | Ejecuta lógica tras una interacción genérica. |
| `onFormSubmit()` | Al Enviar Formulario | `on` | **Callback** que se ejecuta cuando ocurre un evento. |
| `toggleDarkMode()` | Alternar Modo Oscuro | `toggle` | Invierte el estado booleano de un ajuste o *setting*. |
| `updateProgressBar()` | Actualizar Barra de Progreso | `update` | Modifica el estado visible o interno de un componente. |
| `initializeApp()` | Inicializar Aplicación | `initialize` | Función principal de arranque y configuración. |

---

### 3. Operaciones CRUD (Crear, Leer, Actualizar, Borrar)

Estas funciones son esenciales para la persistencia de datos y la comunicación con APIs o bases de datos.

| Función (Camel Case) | Traducción al Español | Operación CRUD | Verbo Clave |
| :--- | :--- | :--- | :--- |
| `createNewUser()` | Crear Nuevo Usuario | **C**reate | `create` |
| `fetchUserData()` | Obtener Datos de Usuario | **R**ead | `fetch` (o `get`) |
| `updateUserProfile()` | Actualizar Perfil de Usuario | **U**pdate | `update` |
| `deleteUserAccount()` | Borrar Cuenta de Usuario | **D**elete | `delete` |

---

### 4. Utilidades

Funciones de soporte que realizan tareas genéricas o técnicas.

| Función (Camel Case) | Traducción al Español | Verbo/Término Clave | Propósito |
| :--- | :--- | :--- | :--- |
| `generateRandomId()` | Generar Identificador Aleatorio | `generate` | Crea un valor o recurso. |
| `formatCurrency()` | Formatear Moneda | `format` | Aplica una estructura a un dato. |
| `debounceSearch()` | Retrasar Búsqueda | `debounce` | Técnica de optimización de rendimiento y tiempo. |
| `sanitizeInput()` | Sanear Entrada | `sanitize` | Limpia una entrada de código o datos inseguros. |
| `checkPermissions()` | Verificar Permisos | `check` | Realiza una comprobación de condición. |