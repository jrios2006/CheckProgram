#!/usr/bin/env python
# -*- coding: utf-8 -*-


def EsWindows():
	# funcion que nos dice si donde ejecutamos el programa 
	# es windows o no
	import platform
	Aux = False
	if platform.system() == "Windows":
		Aux = True
	return Aux
  
def obtener_nombre_equipo():
  # Obtiene el nombre de la máquina donde se ejecuta el proceso
  import socket  
  nombre_equipo = socket.gethostname()
  return nombre_equipo


def svcStatus( svc_name, machine=None):
	# Devuelve el estado de un servicio
	import win32service
	import win32serviceutil
	RUNNING = win32service.SERVICE_RUNNING #4
	#print 'Corriendo ' + str(RUNNING)
	STARTING = win32service.SERVICE_START_PENDING #2
	#print 'Arrancando ' + str(STARTING)
	STOPPING = win32service.SERVICE_STOP_PENDING #3
	#print 'Parando ' + str(STOPPING)
	STOPPED = win32service.SERVICE_STOPPED #1
	#print 'Parado ' + str(STOPPED)
	return win32serviceutil.QueryServiceStatus( svc_name, machine)[1]	# scvType, svcState, svcControls, err, svcErr, svcCP, svcWH

def svcStop( svc_name, machine=None):
	# Paro el servicio
	import win32service
	import win32serviceutil
	import time
	RUNNING = win32service.SERVICE_RUNNING	
	STARTING = win32service.SERVICE_START_PENDING
	STOPPING = win32service.SERVICE_STOP_PENDING
	STOPPED = win32service.SERVICE_STOPPED
	status = win32serviceutil.StopService( svc_name, machine)[1]
	while status == STOPPING:
		time.sleep(1)
		status = svcStatus( svc_name, machine)
	return status

def svcStart( svc_name, svc_arg = None, machine=None):
	# Arranco el servicio
	import win32service
	import win32serviceutil
	import time
	RUNNING = win32service.SERVICE_RUNNING
	STARTING = win32service.SERVICE_START_PENDING
	STOPPING = win32service.SERVICE_STOP_PENDING
	STOPPED = win32service.SERVICE_STOPPED
	if not svc_arg is None:
		if type(svc_arg) in StringTypes:
			# win32service expects a list of string arguments
			svc_arg = [ svc_arg]
	win32serviceutil.StartService( svc_name, svc_arg, machine)
	status = svcStatus( svc_name, machine)
	while status == STARTING:
		time.sleep(1)
		status = svcStatus( svc_name, machine)
	return status



# Inicio del ejemplo	
Servicio = "Temas"
machine = obtener_nombre_equipo()
Argumentos = None
if (svcStatus(Servicio, machine) == 4):
  print 'El servicio ' + Servicio + ' esta arrancado'
  print 'Parando el servicio ' + Servicio
  svcStop(Servicio, machine)
  print 'Arrancando el servicio ' + Servicio
  svcStart(Servicio, Argumentos, machine)
else:
  print 'El servicio ' + Servicio + ' no estaba corrinedo'
  print 'Fin de la prueba'
if (svcStatus(Servicio, machine) == 4):
  print 'Se ha resetado el servicio ' + Servicio
  print 'Prueba finalizada.'
