// 1-Funciones de Manipulación de Datos

/**
 * Suma los precios de un array de productos.
 * @param {Array<Object>} items - Un array de objetos, cada uno con una propiedad 'price'.
 * @returns {number} - El precio total.
 */
function calculateTotalPrice(items) {
  return items.reduce((total, item) => total + item.price, 0);
}

// Uso:
const cart = [{ name: 'Laptop', price: 1200 }, { name: 'Mouse', price: 25 }];
console.log(`Precio total: ${calculateTotalPrice(cart)}`); // Precio total: 1225

/**
 * Limpia y estandariza la entrada de un usuario (quita espacios y convierte a minúsculas).
 * @param {string} text - El texto de entrada.
 * @returns {string} - El texto formateado.
 */
function formatUserInput(text) {
  return text.trim().toLowerCase();
}

// Uso:
const userInput = " Los Sin Chamba ";
console.log(`'${formatUserInput(userInput)}'`);

/**
 * Valida si una cadena de texto tiene el formato de un email.
 * @param {string} email - La dirección de correo a validar.
 * @returns {boolean} - True si es válido, false si no lo es.
 */
function validateEmailAddress(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;// si colocara orozcolean@dominio.com me daria False
  return emailRegex.test(email);
}

// Uso:
console.log(validateEmailAddress("usuario@dominio.com")); 
console.log(validateEmailAddress("esto-no-es-un-email")); 

/**
 * Convierte una cadena de texto (ej. "hola-mundo") a Camel Case ("holaMundo").
 * @param {string} str - La cadena de texto a convertir.
 * @returns {string} - La cadena en Camel Case.
 */
function convertToCamelCase(str) {
  return str.replace(/[-_](\w)/g, (_, c) => c.toUpperCase());
}

// Uso:
console.log(convertToCamelCase("convertir-este-texto"));

/**
 * Filtra un array de usuarios para devolver solo los que están activos.
 * @param {Array<Object>} users - Array de objetos de usuario.
 * @returns {Array<Object>} - Array con usuarios activos.
 */
function filterActiveUsers(users) {
  return users.filter(user => user.isActive);
}

// Uso:
const allUsers = [
  { name: 'Ana', isActive: true },
  { name: 'Luis', isActive: false },
  { name: 'Carlos', isActive: true },
];
console.log(filterActiveUsers(allUsers));

// 2-Eventos o Interacción

/**
 * Simula la lógica que se ejecuta al hacer clic en un botón.
 */
function handleButtonClick() {
  console.log("¡El botón ha sido presionado!");
  // Aquí iría la lógica para, por ejemplo, mostrar un modal.
}

// Uso (se llamaría desde un evento en HTML):
// <button onclick="handleButtonClick()">Púlsame</button>
handleButtonClick(); // Simulación

/**
 * Simula el manejo del envío de un formulario, previniendo la recarga de la página.
 * @param {Event} event - El objeto del evento del formulario.
 */
function onFormSubmit(event) {
  event.preventDefault(); // Evita que la página se recargue
  console.log("Formulario enviado. Procesando datos...");
}

// Uso (simulación):
const fakeEvent = { preventDefault: () => console.log("Recarga de página prevenida.") };
onFormSubmit(fakeEvent);

/**
 * Alterna una clase en el body para cambiar entre modo claro y oscuro.
 */
function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  console.log(`Modo oscuro ${document.body.classList.contains('dark-mode') ? 'activado' : 'desactivado'}.`);
}



/**
 * Actualiza el ancho de una barra de progreso en el DOM.
 * @param {number} percentage - El porcentaje de progreso (0-100).
 */
function updateProgressBar(percentage) {
  // const progressBar = document.getElementById('myProgressBar');
  // if (progressBar) {
  //   progressBar.style.width = `${percentage}%`;
  // }
  console.log(`Barra de progreso actualizada al ${percentage}%.`);
}

// Uso:
updateProgressBar(75);

/**
 * Simula los pasos de configuración inicial de una aplicación.
 */
function initializeApp() {
  console.log("Inicializando aplicación...");
  // 1. Cargar configuración.
  // 2. Conectar a la base de datos.
  // 3. Renderizar la vista principal.
  console.log("Aplicación lista.");
}

// Uso:
initializeApp();

// 3-Operaciones CRUD (Crear, Leer, Actualizar, Borrar)

/**
 * Simula la creación de un nuevo usuario en el sistema.
 * @param {Object} userData - Los datos del nuevo usuario.
 * @returns {Object} - El usuario creado con un ID.
 */
function createNewUser(userData) {
  console.log(`Creando usuario: ${userData.name}`);
  return { id: Date.now(), ...userData };
}

// Uso:
const newUser = createNewUser({ name: 'Elena', email: 'elena@example.com' });
console.log(newUser);

/**
 * Simula la obtención de datos de un usuario desde una API.
 * @param {number} userId - El ID del usuario a buscar.
 * @returns {Promise<Object>} - Una promesa que resuelve con los datos del usuario.
 */
async function fetchUserData(userId) {
  console.log(`Buscando datos del usuario con ID: ${userId}...`);
  // Simulamos una llamada a una API
  return new Promise(resolve => {
    setTimeout(() => {
      resolve({ id: userId, name: 'Juan', role: 'Admin' });
    }, 1000);
  });
}

// Uso:
fetchUserData(123).then(user => console.log(user));

/**
 * Simula la actualización de la información de un perfil de usuario.
 * @param {number} userId - El ID del usuario a actualizar.
 * @param {Object} updates - Un objeto con los campos a actualizar.
 */
function updateUserProfile(userId, updates) {
  console.log(`Actualizando perfil de ${userId} con:`, updates);
  // Lógica para guardar los cambios en la base de datos...
}

// Uso:
updateUserProfile(123, { role: 'Editor' });

/**
 * Simula la eliminación de la cuenta de un usuario.
 * @param {number} userId - El ID del usuario a eliminar.
 */
function deleteUserAccount(userId) {
  console.warn(`Eliminando la cuenta del usuario con ID: ${userId}. Esta acción no se puede deshacer.`);
}

// Uso:
deleteUserAccount(456);

// 4-Utilidades

/**
 * Genera una cadena de texto aleatoria simple que sirve como ID.
 * @returns {string} - Un ID alfanumérico.
 */
function generateRandomId() {
  return Math.random().toString(36).substring(2, 9);
}

// Uso:
console.log(`ID generado: ${generateRandomId()}`);

/**
 * Formatea un número como una cadena de moneda local.
 * @param {number} amount - La cantidad numérica.
 * @param {string} currency - El código de moneda (ej. 'USD', 'EUR', 'ARS').
 * @returns {string} - La cantidad formateada como moneda.
 */
function formatCurrency(amount, currency = 'USD') {
  return new Intl.NumberFormat('es-AR', { style: 'currency', currency }).format(amount);
}

// Uso:
console.log(formatCurrency(1250.75, 'ARS')); 
console.log(formatCurrency(1250.75, 'USD')); 

/**
 * Crea una versión de una función que retrasa su ejecución hasta que hayan pasado
 * 'delay' milisegundos desde la última vez que fue invocada.
 * @param {Function} func - La función a la que aplicar el debounce.
 * @param {number} delay - El tiempo de espera en milisegundos.
 * @returns {Function} - La nueva función con debounce.
 */
function debounce(func, delay) {
  let timeoutId;
  return function(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(this, args), delay);
  };
}

// Uso:
const delayedSearch = debounce(() => console.log("Realizando búsqueda..."), 500);
// Si escribes rápido en un buscador, esto solo se ejecutaría una vez al final.
// delayedSearch();
// delayedSearch();

/**
 * Elimina etiquetas <script> de una cadena para prevenir ataques XSS simples.
 * @param {string} input - La cadena de texto a sanear.
 * @returns {string} - La cadena saneada.
 */
function sanitizeInput(input) {
  return input.replace(/<script.*?>.*?<\/script>/gi, '');
}

// Uso:
const maliciousInput = 'Hola <script>alert("hackeado")</script> mundo';
console.log(sanitizeInput(maliciousInput)); 

/**
 * Verifica si un usuario tiene un permiso específico.
 * @param {Object} user - El objeto de usuario con un array de permisos.
 * @param {string} requiredPermission - El permiso a verificar.
 * @returns {boolean} - True si el usuario tiene el permiso.
 */
function checkPermissions(user, requiredPermission) {
  return user.permissions && user.permissions.includes(requiredPermission);
}

// Uso:
const currentUser = { name: 'Marta', permissions: ['read', 'write'] };
console.log(checkPermissions(currentUser, 'write')); 
console.log(checkPermissions(currentUser, 'delete')); 