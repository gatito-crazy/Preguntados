import pygame
from funciones_preguntados import *

pygame.init()

# Configuración de la ventana principal
ancho = 500
largo = 500
ventana_menu = pygame.display.set_mode((ancho, largo))
pygame.display.set_caption("Menu")

# Posiciones y dimensiones de los botones
# menu
boton_ver_puntajes = pygame.Rect(150, 220, 200, 60)
boton_jugar = pygame.Rect(150, 90, 200, 60)
boton_salir = pygame.Rect(150, 350, 200, 60)
boton_volumen = pygame.Rect(20, 440, 120, 50)

#puntuaciones
volver_al_menu_puntuaciones = pygame.Rect(860, 495, 100, 40)
#Juego
boton_volumen_juego = pygame.Rect(5, 15, 120, 50)
volver_al_menu_juego = pygame.Rect(5, 85, 120, 40)
boton_reiniciar = pygame.Rect(200, 60, 200, 60)
boton_empezar = pygame.Rect(800, 60, 200, 60)
boton_a = pygame.Rect(390, 240, 420, 50)
boton_b = pygame.Rect(390, 340, 420, 50)
boton_c = pygame.Rect(390, 440, 420, 50)
#Usuario
usuario_ingreso = pygame.Rect(100,350,250,40)
volver_usuario = pygame.Rect(280,500,100,45)
# Cargar imágenes de fondo
fondo_menu = pygame.image.load("C:/Users/usuario/Documents/python/Preguntados/fondos o imagenes/patron-signo-interrogacion-dibujado-mano_23-2149416652.jpg").convert()
fondo_puntajes = pygame.image.load("C:/Users/usuario/Documents/python/Preguntados/fondos o imagenes/fondo de puntuacion.jpg").convert()
fondo_carga = pygame.image.load("C:/Users/usuario/Documents/python/Preguntados/fondos o imagenes/pantalla de carga.jpg").convert()
fondo_juego = pygame.image.load("C:/Users/usuario/Documents/python/Preguntados/fondos o imagenes/fondo de juegos.png").convert()
fondo_usuario = pygame.image.load("C:/Users/usuario/Documents/python/Preguntados/fondos o imagenes/fondo de victoria.png").convert()
# Centrado de los fondos
centrado_menu = fondo_menu.get_rect(center=(ancho // 2, largo // 2))
centrado_puntuaciones = fondo_puntajes.get_rect(center=(500, 275))
centrado_carga = fondo_carga.get_rect(center=(120,120))
centrado_juegos = fondo_juego.get_rect(center=(580, 350))
centrado_usuario = fondo_usuario.get_rect(center=(351, 320))

# Colores
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fuente 
fuente_minecraft_20 = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/minecraft_font.ttf', 20)
fuente_minecraft_10 = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/minecraft_font.ttf',10)
fuente_minecraft_15 = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/minecraft_font.ttf', 15)
fuente_minecraft_35 = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/minecraft_font.ttf', 35)

fuente_futurista = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/SHUTTLE-X.ttf',20)

fuente_preguntados = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/MikadoBold.ttf',20)
fuente_preguntados_35 = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/MikadoBold.ttf',35)

fuente_principal = pygame.font.Font(None, 35)
fuente_principal_40 = pygame.font.Font(None, 40)
fuente_principal_50 = pygame.font.Font(None, 50)
#Musica
pygame.mixer.music.load('C:/Users/usuario/Documents/python/Preguntados/musica/musica de fondo.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

#archivo Json
lista_puntuaciones =  importar_json()
#sonidos
sonido_de_carga = pygame.mixer.Sound('C:/Users/usuario/Documents/python/Preguntados/musica/pantalla de carga.wav')
sonido_de_carga.set_volume(0.3)
sonido_de_puntuacion = pygame.mixer.Sound('C:/Users/usuario/Documents/python/Preguntados/musica/musica de puntuaciones.wav')
sonido_de_puntuacion.set_volume(0.3)
sonido_de_preguntas = pygame.mixer.Sound('C:/Users/usuario/Documents/python/Preguntados/musica/nueva pregunta 2.wav')
sonido_de_preguntas.set_volume(0.3)
sonido_de_reinicio = pygame.mixer.Sound('C:/Users/usuario/Documents/python/Preguntados/musica/siguiente pregunta.wav')
sonido_de_reinicio.set_volume(0.3)
sonido_de_correcto = pygame.mixer.Sound('C:/Users/usuario/Documents/python/Preguntados/musica/correcto.wav')
sonido_de_correcto.set_volume(0.3)
sonido_incorrecto= pygame.mixer.Sound('C:/Users/usuario/Documents/python/Preguntados/musica/incorrecta.wav')
sonido_incorrecto.set_volume(0.3)
sonido_victoria= pygame.mixer.Sound('C:/Users/usuario/Documents/python/Preguntados/musica/Victoria.ogg')
sonido_victoria.set_volume(0.2)

# Banderas de estado
running = True
menu = True
puntuaciones = False
juego = False
volumen = True
carga = False
esperando_fin_carga = False
usuario = False
entrada_de_usuario= True
#criterio de orden para las puntuaciones
criterio = "DESC"
# Configuración del juego
indice_pregunta = 0
erronea = 0
pregunta_actual= lista[indice_pregunta]
respuesta_a = "a"
respuesta_b = "b"
respuesta_c = "c"
mal_a = False
mal_b = False
mal_c = False
score = 0
#Usuario
usuario_nombre = ""

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            posicion_mouse = pygame.mouse.get_pos()
            if menu == True:
                if boton_ver_puntajes.collidepoint(posicion_mouse):
                    # Mostrar la ventana de puntajes
                    menu = False
                    puntuaciones = True
                    ventana_puntuaciones = pygame.display.set_mode((1000, 550))
                    pygame.display.set_caption("Puntuaciones")
                    pygame.mixer.music.set_volume(0.0)
                    sonido_de_puntuacion.play(-1)
                elif boton_salir.collidepoint(posicion_mouse):
                    running = False
                elif boton_volumen.collidepoint(posicion_mouse) and volumen == True:
                    volumen = False
                    pygame.mixer.music.set_volume(0.0)
                elif boton_volumen.collidepoint(posicion_mouse) and volumen == False:
                    volumen = True
                    pygame.mixer.music.set_volume(0.5)

                elif boton_jugar.collidepoint(posicion_mouse):
                    menu = False
                    carga = True
                    pygame.mixer.music.set_volume(0.0)
                    sonido_de_carga.play()
                    ventana_de_carga = pygame.display.set_mode((240, 240))
                    pygame.display.set_caption("Cargando")
                    esperando_fin_carga = True

            elif puntuaciones== True :
                if volver_al_menu_puntuaciones.collidepoint(posicion_mouse):
                    # Volver al menú principal
                    menu = True
                    puntuaciones = False
                    ventana_menu = pygame.display.set_mode((500, 500))
                    pygame.display.set_caption("Menu")
                    sonido_de_puntuacion.stop()
                    pygame.mixer.music.set_volume(0.5)
                    
            elif juego == True:
                if boton_volumen_juego.collidepoint(posicion_mouse) and volumen == True:
                    volumen = False
                    pygame.mixer.music.set_volume(0.0)
                elif boton_volumen_juego.collidepoint(posicion_mouse) and volumen == False:
                    volumen = True
                    pygame.mixer.music.set_volume(0.5)
                if volver_al_menu_juego.collidepoint(posicion_mouse):
                    # Volver al menú principal
                    
                    menu = True
                    juego = False
                    ventana_menu = pygame.display.set_mode((500, 500))
                    pygame.display.set_caption("Menu")

                if boton_reiniciar.collidepoint(posicion_mouse):
                    sonido_de_reinicio.play()
                    score = 0
                    indice_pregunta = 0
                    erronea = 0
                    if indice_pregunta > len(lista):
                        indice_pregunta -= 1
                    if indice_pregunta < len(lista):
                        pregunta_actual = lista[indice_pregunta]
                    pregunta_actual = lista[indice_pregunta]
                    mal_a = False
                    mal_b = False
                    mal_c = False
                if boton_empezar.collidepoint(posicion_mouse):
                    sonido_de_preguntas.play()
                    indice_pregunta += 1
                    erronea = 0
                    if indice_pregunta > len(lista):
                        indice_pregunta -= 1
                    if indice_pregunta < len(lista):
                        pregunta_actual = lista[indice_pregunta]
                    mal_a = False
                    mal_b = False
                    mal_c = False
                if boton_a.collidepoint(posicion_mouse) and respuesta_a == lista[indice_pregunta]["correcta"]:
                    sonido_de_correcto.play()
                    score += 10
                    indice_pregunta +=1
                    if indice_pregunta > len(lista):
                        indice_pregunta -= 1
                    if indice_pregunta < len(lista):
                        pregunta_actual = lista[indice_pregunta]
                    erronea = 0                    
                    mal_b = False
                    mal_c = False
                elif boton_a.collidepoint(posicion_mouse) and respuesta_a != lista[indice_pregunta]["correcta"]:
                    sonido_incorrecto.play()
                    erronea += 1
                    mal_a = True
                    mal_b = False
                    mal_c = False
                    if erronea == 2:
                        erronea = 0 
                        indice_pregunta +=1
                        if indice_pregunta > len(lista):
                            indice_pregunta -= 1
                        if indice_pregunta < len(lista):
                            pregunta_actual = lista[indice_pregunta]
                        mal_a = False
                        
                if boton_b.collidepoint(posicion_mouse) and respuesta_b == lista[indice_pregunta]["correcta"]:
                    sonido_de_correcto.play()
                    score += 10
                    indice_pregunta +=1
                    erronea = 0
                    if indice_pregunta > len(lista):
                        indice_pregunta -= 1
                    if indice_pregunta < len(lista):
                        pregunta_actual = lista[indice_pregunta]
                    mal_a = False
                    mal_c = False
                elif boton_b.collidepoint(posicion_mouse) and respuesta_b != lista[indice_pregunta]["correcta"]:
                    sonido_incorrecto.play()
                    erronea += 1
                    mal_a = False
                    mal_c = False
                    mal_b = True
                    if erronea == 2:
                        erronea = 0 
                        indice_pregunta +=1
                        if indice_pregunta > len(lista):
                            indice_pregunta -= 1
                        if indice_pregunta < len(lista):
                            pregunta_actual = lista[indice_pregunta]
                        mal_b = False
                        
                if boton_c.collidepoint(posicion_mouse) and respuesta_c == lista[indice_pregunta]["correcta"]:
                    sonido_de_correcto.play()
                    score += 10
                    indice_pregunta +=1
                    erronea = 0
                    if indice_pregunta > len(lista):
                        indice_pregunta -= 1
                    if indice_pregunta < len(lista):
                        pregunta_actual = lista[indice_pregunta]
                    mal_a = False
                    mal_b = False
                elif boton_c.collidepoint(posicion_mouse) and respuesta_c != lista[indice_pregunta]["correcta"]:
                    sonido_incorrecto.play()
                    erronea += 1
                    mal_c = True
                    mal_a = False
                    mal_b = False
                    if erronea == 2:
                        erronea = 0 
                        indice_pregunta +=1
                        if indice_pregunta > len(lista):
                            indice_pregunta -= 1
                        if indice_pregunta < len(lista):
                            pregunta_actual = lista[indice_pregunta]
                        mal_c = False
                        
                if indice_pregunta >= len(lista):
                    juego = False
                    indice_pregunta = 0
                    erronea = 0
                    mal_a = False
                    mal_b = False
                    mal_c = False
                    usuario = True
                    ventana_usuario = pygame.display.set_mode((701, 630))
                    pygame.mixer.music.set_volume(0.0)
                    sonido_victoria.play(-1)
                    pygame.display.set_caption("Termino el juego")
            if usuario == True:
                if usuario_ingreso.collidepoint(posicion_mouse):
                    entrada_de_usuario= True
                if volver_usuario.collidepoint(posicion_mouse):
                    sonido_victoria.stop()
                    pygame.mixer.music.set_volume(0.5)
                    score = 0
                    usuario = False
                    menu = True
                    ventana_menu = pygame.display.set_mode((500, 500))
                    pygame.display.set_caption("Menu")
        if evento.type == pygame.KEYDOWN:
            if entrada_de_usuario == True:
                if evento.key == pygame.K_RETURN:
                    nuevo_usuario(lista_puntuaciones, usuario_nombre, score)
                    usuario = False
                    menu = True
                    sonido_victoria.stop()
                    pygame.mixer.music.set_volume(0.5)
                    ventana_menu = pygame.display.set_mode((500, 500))

                elif evento.key == pygame.K_BACKSPACE:
                    usuario_nombre = usuario_nombre[:-1]
                else:
                    usuario_nombre += evento.unicode

    

    if volumen == False:
        pygame.mixer.music.set_volume(0.0)
    if menu == True:
        ventana_menu.blit(fondo_menu, centrado_menu)
        pygame.draw.rect(ventana_menu, YELLOW, boton_ver_puntajes, border_radius=15)
        pygame.draw.rect(ventana_menu, YELLOW, boton_jugar, border_radius=15)
        pygame.draw.rect(ventana_menu, YELLOW, boton_salir, border_radius=15)
        if volumen == True:
            pygame.draw.rect(ventana_menu, BLACK, boton_volumen, border_radius = 15)
        elif volumen == False:
            pygame.draw.rect(ventana_menu, RED, boton_volumen, border_radius = 15)
        texto_jugar = fuente_preguntados.render("Jugar", True, GRAY)
        ventana_menu.blit(texto_jugar, texto_jugar.get_rect(center=(ancho // 2, 120)))

        texto_ver_puntajes = fuente_futurista.render("Ver Puntajes", True, GRAY)
        ventana_menu.blit(texto_ver_puntajes, texto_ver_puntajes.get_rect(center=(ancho // 2, 250)))

        texto_salir = fuente_minecraft_20.render("Salir", True, GRAY)
        ventana_menu.blit(texto_salir, texto_salir.get_rect(center=(ancho // 2, 380)))

        fuente = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/minecraft_font.ttf', 15)
        texto_musica = fuente.render(f"musica", True, GRAY)
        ventana_menu.blit(texto_musica, texto_musica.get_rect(center=(80,455)))
        fuente = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/minecraft_font.ttf',10)
        texto_musica = fuente.render("prendido/apagado", True, GRAY)
        ventana_menu.blit(texto_musica, texto_musica.get_rect(center=(80,473)))
        
    if puntuaciones == True:
        ventana_puntuaciones.blit(fondo_puntajes, centrado_puntuaciones)
        
        pygame.draw.rect(ventana_puntuaciones, YELLOW, (390, 80, 200, 5), border_radius=15)
        pygame.draw.rect(ventana_puntuaciones, YELLOW, (390, 45, 200, 5), border_radius=15)
        pygame.draw.rect(ventana_puntuaciones, YELLOW, (390, 45, 5, 40), border_radius=15)
        pygame.draw.rect(ventana_puntuaciones, YELLOW, (585, 45, 5, 40), border_radius=15)
        texto_puntuacion = fuente_futurista.render("Puntuacion", True, GRAY)
        ventana_puntuaciones.blit(texto_puntuacion, (430, 55))

        pygame.draw.rect(ventana_puntuaciones, BLACK, volver_al_menu_puntuaciones, border_radius=15)
        texto_volver = fuente_futurista.render("Volver", True, GRAY)
        ventana_puntuaciones.blit(texto_volver, (875, 510))
        ordenar = listar_ordenado_puntuacion(lista_puntuaciones, "DESC")
        fuente_futurista_grande = cargar_fuente('C:/Users/usuario/Documents/python/Preguntados/tipografias/SHUTTLE-X.ttf',40)

        for mejores_3, puntuacion in enumerate(lista_puntuaciones[:3]):
            nombre_texto = fuente_futurista_grande.render(puntuacion["nombre"], True, YELLOW)
            puntos_texto = fuente_futurista_grande.render(str(puntuacion["puntos"]), True, YELLOW)
            ventana_puntuaciones.blit(nombre_texto, (190, 130 + mejores_3 * 100))
            ventana_puntuaciones.blit(puntos_texto, (590, 130 + mejores_3 * 100))  # Espacio entre cada puntuación

    if carga == True:
        ventana_de_carga.blit(fondo_carga, centrado_carga)
        if esperando_fin_carga == True:
            if not pygame.mixer.get_busy():
                carga = False
                juego = True
                ventana_de_juego = pygame.display.set_mode((1200, 600))
                pygame.display.set_caption("Juego")
                pygame.mixer.music.set_volume(0.5)

        

    if juego == True:
        ventana_de_juego.blit(fondo_juego,centrado_juegos)
        if volumen == True:
            pygame.draw.rect(ventana_de_juego, BLACK, boton_volumen_juego, border_radius = 15)
        elif volumen == False:
            pygame.draw.rect(ventana_de_juego, RED, boton_volumen_juego, border_radius = 15)
        texto_musica = fuente_minecraft_15.render(f"musica", True, GRAY)
        ventana_de_juego.blit(texto_musica, texto_musica.get_rect(center=(65,27)))
        
        texto_musica = fuente_minecraft_10.render("prendido/apagado", True, GRAY)
        ventana_de_juego.blit(texto_musica, texto_musica.get_rect(center=(65,45)))
        
        pygame.draw.rect(ventana_de_juego, BLACK, volver_al_menu_juego, border_radius = 15)
        texto_volver = fuente_minecraft_15.render(f"Volver", True, GRAY)
        ventana_de_juego.blit(texto_volver, texto_volver.get_rect(center=(65,107)))
        
        pygame.draw.rect(ventana_de_juego, BLACK, boton_reiniciar, border_radius = 15)
        texto_reiniciar = fuente_preguntados_35.render(f"Reiniciar", True, GRAY)
        ventana_de_juego.blit(texto_reiniciar, texto_reiniciar.get_rect(center=(300, 90)))
        pygame.draw.rect(ventana_de_juego, BLACK, boton_empezar, border_radius = 15)
        texto_reiniciar = fuente_preguntados_35.render(f"Pregunta", True, GRAY)
        ventana_de_juego.blit(texto_reiniciar, texto_reiniciar.get_rect(center=(900, 90)))
        dibujar_botones_de_preguntas(ventana_de_juego, YELLOW, boton_a, boton_b, boton_c)
        puntuacion_rectangulo = pygame.Rect(900, 540, 250, 50)
        # Dibujar texto de la pregunta
        texto_pregunta = fuente_principal_40.render(pregunta_actual["pregunta"], True, GRAY)
        pygame.draw.rect(ventana_de_juego, BLACK, (50, 210, 570, 5), border_radius=15)
        ventana_de_juego.blit(texto_pregunta, (50, 180))
        texto_boton_a = fuente_principal.render(pregunta_actual["a"], True, GRAY)
        ventana_de_juego.blit(texto_boton_a, (570, 250))
        texto_boton_b = fuente_principal.render(pregunta_actual["b"], True, GRAY)
        ventana_de_juego.blit(texto_boton_b, (570, 350))
        texto_boton_c = fuente_principal.render(pregunta_actual["c"], True, GRAY)
        ventana_de_juego.blit(texto_boton_c, (570, 450))
        puntos= fuente_minecraft_20.render("Score:", True, WHITE)
        pygame.draw.rect(ventana_de_juego, BLACK, puntuacion_rectangulo, border_radius=15)
        ventana_de_juego.blit(puntos, (920, 550))
        puntuacion = fuente_minecraft_20.render(str(score), True, WHITE)
        ventana_de_juego.blit(puntuacion, (1050, 550))
        if mal_a == True:
            if respuesta_a != lista[indice_pregunta]["correcta"] and erronea == 1:
                texto_boton_a = fuente_principal.render(pregunta_actual["a"], True, RED)
                ventana_de_juego.blit(texto_boton_a, (570, 250))
        if mal_b == True:
            if respuesta_b != lista[indice_pregunta]["correcta"]and erronea == 1:
                texto_boton_b = fuente_principal.render(pregunta_actual["b"], True, RED)
                ventana_de_juego.blit(texto_boton_b, (570, 350))
        if mal_c == True:
            if respuesta_c != lista[indice_pregunta]["correcta"]and erronea == 1:
                texto_boton_c = fuente_principal.render(pregunta_actual["c"], True, RED)
                ventana_de_juego.blit(texto_boton_c, (570, 450))

    if usuario == True:
        ventana_usuario.fill(BLACK)
        ventana_usuario.blit(fondo_usuario,centrado_usuario)
        pygame.draw.rect(ventana_usuario, WHITE,(230,30,250,70), border_radius=15)
        pygame.draw.rect(ventana_usuario, WHITE,(230,120,250,40), border_radius=15)
        pygame.draw.rect(ventana_usuario, YELLOW,(430,350,160,40), border_radius=15)
        pygame.draw.rect(ventana_usuario, WHITE,(usuario_ingreso), border_radius=15)
        pygame.draw.rect(ventana_usuario, WHITE,(volver_usuario), border_radius=15)
        texto_score = fuente_minecraft_20.render("Score:", True, BLACK)
        ventana_usuario.blit(texto_score, (440, 355))
        texto_score_2 = fuente_minecraft_20.render(str(score), True, BLACK)
        ventana_usuario.blit(texto_score_2, (535, 355))
        texto_felicidades = fuente_minecraft_20.render("COMPLETASTE TODO", True, BLACK)
        ventana_usuario.blit(texto_felicidades, (240, 45))
        texto_felicidades_2 = fuente_minecraft_15.render("Ingresa tu usuario abajo", True, BLACK)
        ventana_usuario.blit(texto_felicidades_2, (245, 130))
        texto_usuario = fuente_minecraft_20.render(str(usuario_nombre), True, BLACK)
        ventana_usuario.blit(texto_usuario, (120, 355))
        texto_volver_usuario = fuente_minecraft_15.render("VOLVER", True, BLACK)
        ventana_usuario.blit(texto_volver_usuario, (300, 505))
        texto_volver_usuario = fuente_minecraft_10.render("(sin guardar)", True, BLACK)
        ventana_usuario.blit(texto_volver_usuario, (293, 520))
        

    pygame.display.update()

pygame.quit()
