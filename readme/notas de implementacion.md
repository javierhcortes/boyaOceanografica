# Notas de implementacion
---
Considerar estos puntos al implementar la rutina de obtencion y datos del IFCB



1) Comprobar la comunicacion con el IFCB. no necesariamente enciende antes de que el PC104

2)  Esperar por la aparición de los archivos generados : ¿cual es la condicion?
estan ordenados por fecha? Determinar prefijos de los archivos

3) Terminado el ciclo de medición conseguir los archivos del IFCB via ftp-get. ¿Como comprobamos que termina el ciclo de medicion? ¿Ponemos un time out? ¿Solo nos fijamos en el timestamp del archivo?

4) Como avisamos que se ha concluido?

5)
la clase en python ftp-lib implenta el trabajo en cliente ftp. este debe ser soportoda en el server ftp del otro lado  (en este caso el IFCB) cooroborar este punto


6) considerar que la descarga del documeto no funcione

if not res.startswith('226 Transfer complete'):
    
    print('Download failed')
    if os.path.isfile(file_copy):
        os.remove(file_copy)  

In case the download failed, we print an error message and delete the local file. 