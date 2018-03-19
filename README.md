# CheckProgram
A veces tenemos la necesidad de comprobar en un momento dado si un programa se está ejecutando en nuestra máquina, para poder hacer alguna tarea o acción si se está ejecutando o si no se está ejecutando.
A veces necesitamos comprobar el estado de un servicio (programa).

Dejo un par de ejemplo para comprobar el estado de la ejecución de un programa en nuestro sistema

## Librerías necesarias
Nos apoyamos en la librería psutil. Debemos instalarla, podemos hacerlo mediante <code>pip install psutil</code>

He utilizado la libreria netifaces para obtener la dirección Ip local de la máquina.
Comentar este código si no se quiere usar o instalar la librería mediante <code>pip install netifaces</code>

Para comprobar los servicios de una máquina se debe instalar la librería win32service

## Ejemplo de comprobación de programa
Hay un fichero <b>comprobar-programa.py</b> que comprueba el estado de la ejecución en un momento dado de un programa.
La función devuelve una lista con las ejecuciones del programa

## Ejemplo de comprobación de servicio
Hay un fichero <b>comprobar-servicio.py</b> que comprueba el estado de la ejecución de un servicio en un momento definido en la variable Servicio.
Si está arrancado el servicio, lo para y lo vuelve a arrancar

## Ejemplo de salida de programa de comprobación de servicio
<code>
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: C:\Temp\chequear-servicio.py ===================
El servicio Temas esta arrancado
Parando el servicio Temas
Arrancando el servicio Temas
Se ha resetado el servicio Temas
Prueba finalizada.
</code>

## Ejemplo de salida de NO ejecución de programa

<code>
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Temp\comprobar-programa.py 
No esta ejecutando notepad.exe
127.0.0.1<br>
Error: el programa notepad.exe no se ejecuta en la mÃ¡quina TEST
<p>En el ordeandor TEST no se esta ejecutando el programa notepad.exe</p><p>Conectate a la maquina 127.0.0.1<br> y ejecuta el programa si no quieres recibir mas mensajes como este</p>
>>> 
</code>

## Ejemplo de salida de ejecución de comprobación de programa

<code>
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Temp\comprobar-programa.py 
Programa ejecutandose
>>> 
</code>