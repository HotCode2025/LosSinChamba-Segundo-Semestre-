// Ejercicio 1: Función que valide una contraseña 27/10/2025

function validatePassword(password) {
    // Verificar que tenga al menos 8 caracteres
    if (password.length < 8) {
        return false;
    }
    
    // Verificar que tenga al menos una mayúscula
    let hasMayuscula = false;
    for (let i = 0; i < password.length; i++) {
        if (password[i] >= 'A' && password[i] <= 'Z') {
            hasMayuscula = true;
            break;
        }
    }
    
    // Verificar que tenga al menos un número
    let hasNumero = false;
    for (let i = 0; i < password.length; i++) {
        if (password[i] >= '0' && password[i] <= '9') {
            hasNumero = true;
            break;
        }
    }
    
    // Retornar true solo si cumple todas las condiciones
    return hasMayuscula && hasNumero;
}

console.log(validatePassword("Abc12345")); 
console.log(validatePassword("weak")); 
console.log(validatePassword("NoNumber")); 
console.log(validatePassword("nonumber123")); 


// Ejercicio 2: Sistema simple de gestión de tareas
function createTaskManager() {
    let tasks = [];
    let nextId = 1;
    
    return {
        addTask: function(task) {
            const newTask = {
                id: nextId++,
                description: task,
                completed: false
            };
            tasks.push(newTask);
            console.log(`Tarea agregada: "${task}" con ID ${newTask.id}`);
        },
        
        completeTask: function(taskId) {
            const task = tasks.find(t => t.id === taskId);
            if (task) {
                task.completed = true;
                console.log(`Tarea ${taskId} completada: "${task.description}"`);
            } else {
                console.log(`Tarea con ID ${taskId} no encontrada`);
            }
        },
        
        listTasks: function() {
            console.log("\n=== Lista de Tareas ===");
            if (tasks.length === 0) {
                console.log("No hay tareas registradas");
            } else {
                tasks.forEach(task => {
                    const estado = task.completed ? "✓ Completada" : "⏳ Pendiente";
                    console.log(`ID: ${task.id} | ${estado} | ${task.description}`);
                });
            }
            console.log("=====================\n");
        }
    };
}

// Uso del sistema de tareas:
const myTasks = createTaskManager();
myTasks.addTask("Aprender JavaScript");
myTasks.addTask("Hacer ejercicio");
myTasks.addTask("Leer un libro");

myTasks.listTasks();

myTasks.completeTask(1);
myTasks.completeTask(3);

myTasks.listTasks();