def calcular_subtotal(total_paginas, precio_pagina):
    # TODO 1: retornar el subtotal correcto.
    return total_paginas * precio_pagina


paquetes = ["Apuntes", "Guía de ejercicios", "Material de consulta"]

PRECIO_PAGINA = 2
PORCENTAJE_DESCUENTO = 0.10

total_paginas = 0
cantidad_paquetes_aceptados = 0

for indice in range(len(paquetes)):
    # TODO : Imprimir el nombre del paquete actual.
    print(f"\nProcesando paquete: {paquetes[indice]}")

    try:
        paginas = int(input("Cantidad de páginas (1 a 50): "))
    except ValueError:
        print("Error: debes escribir un número entero. Paquete omitido.")
        continue

    # TODO 2:
    # Si paginas está fuera del rango 1 a 50,
    # mostrar un mensaje y omitir este paquete con continue.
    if paginas < 1 or paginas > 50:
        print("Error: la cantidad de páginas está fuera del rango (1 a 50). Paquete omitido.")
        continue

    # TODO 3:
    # Acumular las páginas y aumentar los paquetes aceptados.
    total_paginas += paginas
    cantidad_paquetes_aceptados += 1


subtotal = calcular_subtotal(total_paginas, PRECIO_PAGINA)
descuento = 0

# TODO 4:
# Aplicar 10% de descuento solo si total_paginas supera 100.
if total_paginas > 100:
    descuento = subtotal * PORCENTAJE_DESCUENTO

total_a_pagar = subtotal - descuento


print("\n--- RESUMEN DEL PEDIDO ---")
"""
 TODO 5: Mostrar un mensaje si no se aceptó ningún paquete. 
 E imprimir el resumen del pedido con la cantidad de paquetes aceptados, 
 total de páginas, subtotal, descuento y total a pagar.
"""
if cantidad_paquetes_aceptados == 0:
    print("No se generó un pedido. No se aceptó ningún paquete.")
    print("Cantidad de paquetes aceptados: 0")
    print("Total de páginas: 0")
    print("Subtotal: 0 unidades monetarias")
    print("Descuento: 0 unidades monetarias")
    print("Total a pagar: 0 unidades monetarias")
else:
    print(f"Cantidad de paquetes aceptados: {cantidad_paquetes_aceptados}")
    print(f"Total de páginas: {total_paginas}")
    print(f"Subtotal: {subtotal:.2f} unidades monetarias")
    print(f"Descuento aplicado: {descuento:.2f} unidades monetarias")
    print(f"Total a pagar: {total_a_pagar:.2f} unidades monetarias")