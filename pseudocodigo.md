Algoritmo PedidoImpresion
    Definir i, paginas_paquete, paquetes_aceptados, total_paginas como Entero
    Definir subtotal, descuento, total_paginar como Real
    Definir entrada_valida como Lógico

    paquetes_aceptados <- 0
    total_paginas <- 0
    subtotal <- 0
    descuento <- 0
    total_paginar <- 0

    // Recorrido de los 3 paquetes
    Para i <- 1 Hasta 3 Hacer
        Escribir "Ingrese la cantidad de páginas del paquete ", i, " (entre 1 y 50):"
        Leer entrada_usuario

        // Intentar conversión a entero y validación de rango (1 a 50)
        Si EsEntero(entrada_usuario) Entonces
            paginas_paquete <- ConvertirEntero(entrada_usuario)
            
            Si paginas_paquete >= 1 Y paginas_paquete <= 50 Entonces
                paquetes_aceptados <- paquetes_aceptados + 1
                total_paginas <- total_paginas + paginas_paquete
            Sino
                Escribir "Error: El paquete ", i, " está fuera del rango permitido (1-50). Paquete omitido."
            FinSi
        Sino
            Escribir "Error: La entrada del paquete ", i, " no pudo convertirse a entero. Paquete omitido."
        FinSi
    FinPara

    // Reporte final y cálculos
    Si paquetes_aceptados = 0 Entonces
        Escribir "No se generó un pedido. No se aceptó ningún paquete."
        Escribir "Cantidad de paquetes aceptados: 0"
        Escribir "Total de páginas: 0"
        Escribir "Subtotal: 0 unidades monetarias"
        Escribir "Descuento: 0 unidades monetarias"
        Escribir "Total a pagar: 0 unidades monetarias"
    Sino
        subtotal <- total_paginas * 2

        // Aplicar descuento del 10% solo si supera estrictamente 100 páginas
        Si total_paginas > 100 Entonces
            descuento <- subtotal * 0.10
        Sino
            descuento <- 0
        FinSi

        total_paginar <- subtotal - descuento

        // Mostrar resultados finales
        Escribir "--- REPORTE FINAL DEL PEDIDO ---"
        Escribir "Cantidad de paquetes aceptados: ", paquetes_aceptados
        Escribir "Total de páginas: ", total_paginas
        Escribir "Subtotal: ", subtotal
        Escribir "Descuento aplicado: ", descuento
        Escribir "Total a pagar: ", total_paginar
    FinSi
FinAlgoritmo