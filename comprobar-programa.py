#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import psutil

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
        if name == p.info['name'] or \
                p.info['exe'] and os.path.basename(p.info['exe']) == name or \
                p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    return ls


def obtener_nombre_equipo():
    # Obtiene el nombre de la máquina donde se ejecuta el proceso
    import socket  
    nombre_equipo = socket.gethostname()
    return nombre_equipo

def ipv4():
    """ Obtiene una lista de todas las Ips locales de todas las interfaces. """
    try:
        from netifaces import interfaces, ifaddresses, AF_INET
        # to not take into account loopback addresses (no interest here)
        addresses = []
        for interface in interfaces():
            config = ifaddresses(interface)
            # AF_INET is not always present
            if AF_INET in config.keys():
                for link in config[AF_INET]:
                    # loopback holds a 'peer' instead of a 'broadcast' address
                    if 'addr' in link.keys() and 'peer' not in link.keys():
                        addresses.append(link['addr']) 
        return addresses
    except ImportError:
        return []

        
# Probamos con el programa
Programa = 'notepad.exe'
Lista = find_procs_by_name(Programa)
if (len(Lista) == 0):
    print 'No esta ejecutando ' + Programa
    '''
        Hacemos algo
    '''
    computadora = obtener_nombre_equipo()
    Ips = ipv4()
    ListaOrdenadaIps = sorted(Ips)
    asunto = 'Error: el programa ' + Programa + ' no se ejecuta en la máquina ' + computadora
    cadena_html = "<br>".join(str(x) for x in ListaOrdenadaIps)
    print cadena_html
    cuerpo = '<p>En el ordeandor ' + computadora + ' no se esta ejecutando el programa ' + Programa + '</p>'
    cuerpo = cuerpo + '<p>Conectate a la maquina ' + cadena_html + ' y ejecuta el programa si no quieres recibir mas mensajes como este</p>'
    print asunto
    print cuerpo    
else:
    print 'Programa ejecutandose'
