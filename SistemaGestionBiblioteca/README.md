# 📚 Sistema de Gestión de Biblioteca - NetBeans

## Proyecto Integrador 2º Semestre

---

## 🚀 Abrir en Apache NetBeans

### Opción 1: Importar Proyecto Existente

1. Abre **Apache NetBeans**
2. Ve a **File** → **Open Project**
3. Navega hasta la carpeta `SistemaGestionBiblioteca`
4. Selecciona el proyecto y haz clic en **Open Project**
5. ¡Listo! NetBeans reconocerá automáticamente la estructura

### Opción 2: Desde Archivo ZIP

1. Descomprime el archivo ZIP
2. Abre NetBeans
3. **File** → **Open Project**
4. Selecciona la carpeta descomprimida
5. Click en **Open Project**

---

## ▶️ Ejecutar el Proyecto

### Desde NetBeans:

1. **Método 1**: Presiona **F6** (Run Project)
2. **Método 2**: Click derecho en el proyecto → **Run**
3. **Método 3**: Click en el botón verde ▶️ en la barra de herramientas

### Clase Principal:
```
com.biblioteca.main.BibliotecaApp
```

---

## 📁 Estructura del Proyecto

```
SistemaGestionBiblioteca/
├── src/
│   └── com/
│       └── biblioteca/
│           ├── main/
│           │   └── BibliotecaApp.java      (Clase principal)
│           ├── modelo/
│           │   ├── Libro.java              (Modelo)
│           │   └── Usuario.java            (Modelo)
│           └── controlador/
│               └── Biblioteca.java         (Controlador)
├── nbproject/                              (Configuración NetBeans)
│   ├── project.xml
│   ├── project.properties
│   └── build-impl.xml
├── build/                                  (Archivos compilados)
└── dist/                                   (JAR ejecutable)
```

---

## 🎯 Packages Implementados

### `com.biblioteca.main`
- **BibliotecaApp.java** - Clase principal con menú interactivo

### `com.biblioteca.modelo`
- **Libro.java** - Modelo de datos para libros
- **Usuario.java** - Modelo de datos para usuarios

### `com.biblioteca.controlador`
- **Biblioteca.java** - Lógica de negocio y controlador

---

## 🔧 Compilar y Generar JAR

### Desde NetBeans:

1. Click derecho en el proyecto
2. Selecciona **Clean and Build**
3. El JAR se generará en `dist/SistemaGestionBiblioteca.jar`

### Ejecutar el JAR generado:

```bash
java -jar dist/SistemaGestionBiblioteca.jar
```

---

## ✅ Requisitos Cumplidos

- ✅ **Estructura de packages** profesional
- ✅ **Menú interactivo** - 9 opciones funcionales
- ✅ **POO completo** - Encapsulamiento, herencia, polimorfismo
- ✅ **Bucles** - for, while, foreach, anidados
- ✅ **Condicionales** - if-else, switch-case
- ✅ **Proyecto NetBeans** - Completamente configurado

---

## 📝 Configuración de NetBeans

El proyecto está configurado con:

- **Java Version**: 1.8 (compatible con versiones superiores)
- **Source Encoding**: UTF-8
- **Main Class**: `com.biblioteca.main.BibliotecaApp`
- **Build System**: Ant (estándar de NetBeans)

---

## 🐛 Solución de Problemas en NetBeans

### Error: "Cannot find main class"

1. Click derecho en el proyecto → **Properties**
2. Ve a **Run**
3. Verifica que **Main Class** sea: `com.biblioteca.main.BibliotecaApp`
4. Click **OK**

### Error: "Package does not exist"

1. Click derecho en el proyecto → **Clean and Build**
2. Si persiste: **Tools** → **Palette** → **Code Snippets**

### Los emojis no se ven correctamente

1. **File** → **Project Properties** → **Sources**
2. Verifica que **Encoding** sea **UTF-8**

---

## 🎨 Características del Proyecto

### Datos Precargados:
- 5 libros de ejemplo
- 3 usuarios de ejemplo
- Listo para demostración inmediata

### Funcionalidades:
1. Agregar libros
2. Listar libros
3. Buscar libros (por título, autor, ISBN)
4. Prestar libros
5. Devolver libros
6. Registrar usuarios
7. Listar usuarios
8. Ver estadísticas
9. Salir

---

## 📊 Testing en NetBeans

Para probar el proyecto:

1. Ejecuta con **F6**
2. Prueba la opción **2** (Listar libros) - Deberías ver 5 libros
3. Prueba la opción **4** (Prestar libro):
   - ISBN: `978-0307474728`
   - Usuario: `USR1000`
4. Verifica con opción **8** (Estadísticas)

---

## 🔄 Modificar el Código

1. Navega en el panel **Projects** a la izquierda
2. Expande **Source Packages**
3. Expande los packages: `com.biblioteca.main`, `modelo`, `controlador`
4. Doble click en cualquier archivo para editarlo
5. NetBeans auto-completará y mostrará errores en tiempo real

---

## 📦 Exportar para Entrega

### Generar ZIP desde NetBeans:

1. Click derecho en el proyecto
2. **Export** → **To ZIP**
3. Selecciona ubicación y nombre
4. Click **OK**

### O manualmente:

1. Comprime la carpeta completa del proyecto
2. Incluye: `src/`, `nbproject/`, `manifest.mf`, `README.md`

---

## 🎓 Información del Proyecto

- **Nombre**: Sistema de Gestión de Biblioteca
- **Tipo**: Java Application (J2SE)
- **IDE**: Apache NetBeans
- **Java Version**: 8+
- **Build Tool**: Ant
- **Encoding**: UTF-8

---

## 📚 Archivos Importantes

- `src/` - Código fuente con packages
- `nbproject/` - Configuración de NetBeans
- `manifest.mf` - Configuración del JAR
- `build/` - Archivos compilados (.class)
- `dist/` - JAR ejecutable final

---

## ✨ Ventajas de esta Estructura

1. ✅ Organización profesional con packages
2. ✅ Separación de responsabilidades (MVC)
3. ✅ Fácil de mantener y extender
4. ✅ Compatible con NetBeans
5. ✅ Genera JAR ejecutable
6. ✅ Estructura estándar de la industria

---

## 🎯 Próximos Pasos

1. Abre el proyecto en NetBeans
2. Explora los packages y clases
3. Ejecuta el proyecto (F6)
4. Prueba todas las funcionalidades
5. Lee los comentarios en el código
6. ¡Listo para entregar!

---

## 📞 Notas Finales

Este proyecto está **100% listo** para:
- ✅ Abrir en Apache NetBeans
- ✅ Compilar sin errores
- ✅ Ejecutar inmediatamente
- ✅ Generar JAR ejecutable
- ✅ Entregar como proyecto integrador

---

**¡Disfruta tu proyecto en NetBeans!** 🎉
