## PROCEDIMIENTO
----
se describe el procedimiento a implementar en el pc104


1) El PC 104 y el IFCB son encendidos por el procesador central de la boya (CR1000X)

2) El PC 104 inicia ejecución de un archivo batch o equivalente, en donde se ejecutan vía comandos, la secuencia de tareas especificadas en los puntos siguientes.

3) Abrir archivo C: \contador.txt 

4) Si la variable contador es múltiplo de N entonces saltar a 7 (para actualizar a la configuración del blanco/estándar)

5)  Mediante ftp-put transferir el archivo de configuración pre-almacenado en \muestra\IFCB.cfg

6) Saltar a 8 

7) Mediante ftp-put transferir el archivo de configuración pre-almacenado en \Blanco-estandar\IFCB.cfg

8) Esperar por la aparición de los archivos generados por el IFCB : *.roi, *.adc y *.hdr


9) Terminado el ciclo de medición conseguir los archivos del IFCB via ftp-get

10) Incrementar variable contador en uno, y almacenarla en el archivo contador

11) Avisar al procesador CR1000X que la operación con el IFCB ha concluido 

## Notas
Quisiera que me aclararas el punto 4 donde dice "Si la variable contador es múltiplo de N ".
¿A que te refieres con esto?
Cada un numero determinado de mediciones de la muestra N, (ejemplo 10) se debe realizar la medición de una
muestra especial; llamada blanco o estandar. Esto es entendido por el Cytobot al leer el archivo de configuracion.

Entonces, se ejecutan 9 mediciones en donde el Cytobot lee el archivo de configuración correspondiente a las muestras; y en el décimo debe hacerlo para blanco/estandar, para lo cual se debe intercambiar el archivo de configuración.


## NOTAS

Estimado Javier,

    Con José vimos que sería mas conveniente que el flag para término
sea enviado desde uno de los puertos seriales de la PC/104

    Cuando el proceso concluya, el PC/104 enviará al CR1000 una
secuencia de caracteres: "FIN"+<CR>+<LF>

   Con el CR1000 transferiremos al PC/104, via ftp, un archivo de copia
con las mediciones meteorológicas y oceanográficas una vez al día.

   Respecto al modem 4G más económico que me mostraste, éste tiene
interface serial, por lo cual lo descartaría por el requerimiento

  de gran volumen de datos para transferir.

Voy a consultar con el proveedor del Tosibox respecto a las frecuencia
de las Bandas y si estas con compatibles con las compañias en Chile.

Tu podrias hacer lo mismo con la otra opción de modem que encontraste.

saludos

Víctor

----

para Victor
Victor,
para dejarlo claro, en este caso tengo que implementar la rutina serial de la secuencia pero no la transferencia de datos meteorológicos. Cierto?