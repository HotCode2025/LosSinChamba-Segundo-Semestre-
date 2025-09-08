# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viceversa.

def celsius_a_fahrenheit(celsius):
    """Convierte Celsius a Fahrenheit: F = (C × 9/5) + 32"""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius: C = (F - 32) × 5/9"""
    return (fahrenheit - 32) * 5/9

# Ejemplos de uso
if __name__ == "__main__":
    print("=== CONVERTIDOR DE TEMPERATURAS ===")
    
    # Ejemplos Celsius a Fahrenheit
    print("Celsius a Fahrenheit:")
    print(f"0°C = {celsius_a_fahrenheit(0):.1f}°F")
    print(f"25°C = {celsius_a_fahrenheit(25):.1f}°F")
    print(f"37°C = {celsius_a_fahrenheit(37):.1f}°F")
    print(f"100°C = {celsius_a_fahrenheit(100):.1f}°F")
    
    print("\nFahrenheit a Celsius:")
    print(f"32°F = {fahrenheit_a_celsius(32):.1f}°C")
    print(f"77°F = {fahrenheit_a_celsius(77):.1f}°C") 
    print(f"98.6°F = {fahrenheit_a_celsius(98.6):.1f}°C")
    print(f"212°F = {fahrenheit_a_celsius(212):.1f}°C")