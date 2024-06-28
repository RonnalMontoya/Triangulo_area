# Este programa calcula el área de un triángulo desde su base y altura.

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo indicando su base y altura.
    
    Args:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.
    
    Returns:
    float: El área del triángulo.
    """
    # Fórmula para el área del triángulo
    area = (base * altura) / 2
    return area

def main():
    # Solicitar al usuario la base y la altura del triángulo
    base = float(input("Escribir la base del triángulo (en unidades): "))
    altura = float(input("Escribir la altura del triángulo (en unidades): "))
    
    # Calcular el área del triángulo
    area = calcular_area_triangulo(base, altura)
    
    # Mostrar el resultado al usuario
    print(f"El área del triángulo con base {base} y altura {altura} es: {area} unidades cuadradas")
    
    # Variable booleana para indicar si el cálculo fue exitoso
    calculo_exitoso = True
    
    # Verificar y mostrar si el cálculo fue exitoso
    if calculo_exitoso:
        print("El cálculo del área se realizó correctamente.")
    else:
        print("Hubo un error en el cálculo del área.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()