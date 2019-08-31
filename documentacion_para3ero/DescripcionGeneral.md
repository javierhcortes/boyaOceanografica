#Descripción general del repositorio

En este repositorio encontraras las tareas realizadas para la sincronizacion de datos entre la boya oceanográfica y el pc 104. La siguiente descripción detalla la información por carpetas

1) Hardware :
Distintas carpetas indican los Datasheets de los componentes utilizados en este desarrollo. Tambien se incluye a lgunos links de web para adquirir estos productos.

2) Diagramas :
Diagrama de flujo de las tareas que debe implementar el codigo (no esta actualizado)

3) Readme :
Especificaciones de diseño según Victor. Se agregan documentos donde se describieron las tareas a realizar.
El documento mas actualizado es cytobot.pdf
También se incluyen instrucciones para configurar FTP en windows, asi como la configuración del router, si se quiere realizar este trabajo en remoto.

4) Data:
Carpeta de ayuda para comprobar el funcionamiento del FTP

5) Code:
Código en python3 de la rutina a implementar en el PC 104. el punto de entrada es main.py.
Dentro existe una carpeta de nombre 'configIFCB_files' que contiene distintos archivos .IFCB que se deben enviar al realizar ciertas tareas.

6) Cobertura 4G:
Diagrama de cobertura de internet movil de diferentes operadores en chile.


#Descripción del código en python

El código en python realiza las tareas descritas en le documento 'citobot.pdf'.
Se compone de distintos módulos que se comunican entre si.

- main.py : Llama a los modulo y los comunica entre si
- const.py : son las constantes del programa, como por ejemplo la división de tareas y horas o los nombres de las subrutinas.
- fechas.py : modulo que calcula, según el momento del día, que tarea es la que corresponde.
- iniReader.py : modulo encargado de leer el archivo de configuración donde están los datos de servidor remoto, carpetas y contraseñas
- rutinas.py : modulo que contine las tareas generales y especificas a implementar. Se destaca dentro de estas tareas la transferencia de datos por FTP, la escritura del archivo Flag.txt y el envío del archivo de configuración IFCB donde se requiera.