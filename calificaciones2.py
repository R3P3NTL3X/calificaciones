print("\n BIENVENIDO A EL SISTEMA DE CALIFICACIONES INSTITUCIONALES.")

def determinar_estado(calificacion):
    if calificacion >= 60:
        return "Aprobado"
    else:
        return "Reprobado"

def calcular_promedio(lista):
    suma = 0
    for nota in lista:
        suma += nota
    promedio = suma / len(lista)
    return promedio

def contar_mayores(lista, valor):
    contador = 0
    i = 0
    while i < len(lista):
        if lista[i] > valor:
            contador += 1
        i += 1
    return contador

def verificar_y_contar(lista, valor):
    contador = 0
    for nota in lista:
        if nota != valor:
            continue
        contador += 1
        if contador > 0:
            break
    return contador

def solicitar_calificacion():
    while True:
        try:
            calificacion = int(input("Ingresa una calificación entre 0 y 100: "))
            if 0 <= calificacion <= 100:
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def main():
    print("\n--- Gestión de Calificaciones ---\n")

    calificacion = solicitar_calificacion()
    estado = determinar_estado(calificacion)
    print(f"\nEstado del estudiante: {estado}")

    entrada = input("\nIngresa una lista de calificaciones separadas por comas: ")
    lista = [int(nota.strip()) for nota in entrada.split(',') if nota.strip().isdigit()]

    if not lista:
        print("No ingresaste calificaciones válidas.")
        return

    promedio = calcular_promedio(lista)
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")

    valor_comparar = int(input("\nIngresa un valor para contar cuántas calificaciones son mayores: "))
    mayores = contar_mayores(lista, valor_comparar)
    print(f"\nHay {mayores} calificación(es) mayor(es) que {valor_comparar}.")

    valor_especifico = int(input("\nIngresa una calificación específica para buscar en la lista: "))
    conteo = verificar_y_contar(lista, valor_especifico)

    if conteo > 0:
        total = lista.count(valor_especifico)
        print(f"\nLa calificación {valor_especifico} aparece {total} vez(veces) en la lista.")
    else:
        print(f"\nLa calificación {valor_especifico} no está en la lista.")

    print("\nPrograma finalizado. Gracias por usarlo.")

if __name__ == "__main__":
    main()