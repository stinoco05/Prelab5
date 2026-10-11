Entradas: Páginas de cada uno de los 3 paquetes, el tipo de dato es numérico entero.
Salidas: Cantidad de paquetes aceptados, total de páginas, subtotal a pagar, descuento aplicado, total a pagar, mensaje en caso de que no haya paquetes aceptados, mensaje de error o advertencia.
Restricciones Explícitas: El pedido es de tres paquetes, cada paquete debe contener entre 1 y 50 páginas, cada página cuesta 2 unidades monetarias, si son más de 100 páginas hay un 10% de descuento, se permite un solo intento por paquete.
Restricciones Implícitas: Los paquetes omitidos no participan en la suma ni cálculos, el subtotal se calcula como total de páginas x 2, si no hay paquetes aceptados el descuento y total es 0.
Ambiguedades: Que pasa si se ingresa un numero decimal, solo dice que el valor debe poder convertirse a entero.
Precondiciones:El número de páginas debe ser un entero no negativo.
Postcondiciones: Se muestran de forma clara los resultados requeridos o el aviso que no se generó el pedido.

Pruebas del código
Caso 1
Entradas: 40, 35, 30
Resultado Obtenido: 3 paquetes aceptados; 105 páginas acumuladas; subtotal 210; descuento 21 (10% por superar 100 páginas); total a pagar 189. (coincide con el resultado esperado).

Caso 2
Entradas: 50, 50, hola
Resultado Obtenido: 2 paquetes aceptados (el 3° omitido por tipo de dato inválido); 100 páginas acumuladas; subtotal 200; descuento 0 (no supera las 100 páginas); total a pagar 200. (coincide con el resultado esperado).

Caso 3
Entradas: 0, 51, texto
Resultado Obtenido: 0 paquetes aceptados (1° y 2° fuera de rango 1-50, 3° tipo de dato inválido); 0 páginas acumuladas; importes en 0; se despliega el mensaje de que no se generó un pedido. (coincide con el resultado esperado).