import pygame
import json
from datos import lista
import random

def cargar_fuente(ruta,tamaño):
    return pygame.font.Font(ruta, tamaño)

def importar_json():
    with open('C:/Users/usuario/Documents/python/Preguntados/puntuacion.json', 'r') as file:
        data = json.load(file)
        lista_puntuaciones = data['puntuaciones']
        return lista_puntuaciones

def guardar_modificacion_json(usuario):
    #abrira el archivo data.json para poder escribir sobre el
    #pero para no modificar el original hice que se creara uno nuevo asi siempre se puede mostrar desde el principio el proceso
    #si se desea cambiar el proceso y que este modifique al original solo tiene que cambiar el directorio de /data_modificada.json a /data_.json
    with open('C:/Users/usuario/Documents/python/Preguntados/puntuacion_modificada.json', 'w') as file:
        json.dump({"puntuaciones": usuario}, file, indent = 4)

def nuevo_usuario(lista , nombre , score):
    nuevo_usuario = {}
    nuevo_usuario['nombre'] = nombre
    nuevo_usuario['puntos'] = score
    lista.append(nuevo_usuario)
    guardar_modificacion_json(lista)

def listar_ordenado_puntuacion(usuarios, criterio):
    for i in range(len(usuarios) - 1):
        for j in range(i + 1, len(usuarios)):
            if (criterio == "ASC" and usuarios[i]["puntos"] > usuarios[j]["puntos"]) or (criterio == "DESC" and usuarios[i]["puntos"] < usuarios[j]["puntos"]):
                # Swap
                aux = usuarios[i]
                usuarios[i] = usuarios[j]
                usuarios[j] = aux
    return usuarios 

# Función para dibujar el texto centrado en un botón
def dibujar_texto_boton(ventana, texto, fuente, boton, color):
    texto_superficie = fuente.render(texto, True, color)
    texto_rect = texto_superficie.get_rect(center=boton.center)
    ventana.blit(texto_superficie, texto_rect)

def dibujar_botones_de_preguntas(ventana, color, a, b, c):
    pygame.draw.rect(ventana, color, a, border_radius = 15)
    pygame.draw.rect(ventana, color, b, border_radius = 15)
    pygame.draw.rect(ventana, color, c, border_radius = 15)





