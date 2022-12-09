import random
import json
import time

#Variables Globales:
class colores:
  BLUE = '\033[95m' #Color para la máquina
  GREEN = '\033[92m' #Color para el usuario
  WHITE = '\033[0m' #Color predeterminado
  PURPLE = '\033[94m'
  YELLOW = '\033[93m'
  PINK = '\033[91m'

class init:
  filas = 13
  columnas = 17
  casillasMaximas = 48
  tablero_de_juego = [ 
    [9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
	  [6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9]
  ]
  limitePrimerasJugadas = 0
  estadisticas = []

def respaldoOriginal():
  respaldo = [ 
    [9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
	  [6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9],
  	[6,0,6,0,6,0,6,0,6,0,6,0,6,0,6,0,6],
  	[9,6,9,6,9,6,9,6,9,6,9,6,9,6,9,6,9]
  ]
  for i in range(init.filas):
    for j in range(init.columnas):
      respaldo[i][j] = init.tablero_de_juego[i][j]
  return respaldo
  
#Función para imprimir tablero 
def ImprimirTablero():
  numero_de_casilla = 1;
  for i in range(init.filas):
    for j in range(init.columnas):
      #print(init.tablero_de_juego[i][j], end='')
      if(init.tablero_de_juego[i][j] == 0):
        #Casilla limpia
        print(colores.WHITE + str(numero_de_casilla).zfill(2), end='')
        numero_de_casilla += 1;
      elif(init.tablero_de_juego[i][j] == 1):
        #Casilla con 1 elemento
        print(colores.WHITE + str(numero_de_casilla).zfill(2), end='')
        numero_de_casilla += 1;
      elif(init.tablero_de_juego[i][j] == 2):
        #Casilla con 2 elementos
        print(colores.WHITE + str(numero_de_casilla).zfill(2), end='')
        numero_de_casilla += 1;
      elif(init.tablero_de_juego[i][j] == 3):
        #Casilla con 3 elementos
        print(colores.WHITE + str(numero_de_casilla).zfill(2), end='')
        numero_de_casilla += 1;
      elif(init.tablero_de_juego[i][j] == 4):
        #Casilla dónde completó el Jugador Humano
        print(colores.GREEN + "PL", end='')
      elif(init.tablero_de_juego[i][j] == 5):
        #Casilla dónde completó la IA
        print(colores.BLUE + "MA", end='')
      elif((init.tablero_de_juego[i][j] == 6) and ((i%2)==0) ):
        #Se puede seleccionar el lugar y es horizontal 
        print(colores.WHITE + "--", end='')
      elif((init.tablero_de_juego[i][j] == 6) and ((i%2)==1) ):
        #Se puede seleccionar el lugar y es vertical 
        print(colores.WHITE + "|", end='')
      elif((init.tablero_de_juego[i][j] == 7) and ((i%2)==0) ):
        #No Se puede seleccionar el lugar y es horizontal 
        print(colores.GREEN + "--", end='')
      elif((init.tablero_de_juego[i][j] == 7) and ((i%2)==1) ):
        #No Se puede seleccionar el lugar y es vertical 
        print(colores.GREEN + "|", end='')
      elif((init.tablero_de_juego[i][j] == 8) and ((i%2)==0) ):
        #No Se puede seleccionar el lugar y es horizontal 
        print(colores.BLUE + "--", end='')
      elif((init.tablero_de_juego[i][j] == 8) and ((i%2)==1) ):
        #No Se puede seleccionar el lugar y es vertical 
        print(colores.BLUE + "|", end='')
      elif(init.tablero_de_juego[i][j] == 9):
        print(colores.PURPLE + "*", end='')
    print("\n", end='')


def imprimirTableroBackend():
  for i in range(init.filas):
    print(colores.WHITE + "[", end='')
    for j in range(init.columnas):
      if(init.tablero_de_juego[i][j] == 0):
        #Casilla limpia
        print(colores.WHITE + str(init.tablero_de_juego[i][j]), end=',')
      elif(init.tablero_de_juego[i][j] == 1):
        #Casilla con 1 elemento
        print(colores.WHITE + str(init.tablero_de_juego[i][j]), end=',')
      elif(init.tablero_de_juego[i][j] == 2):
        #Casilla con 2 elementos
        print(colores.WHITE + str(init.tablero_de_juego[i][j]), end=',')
      elif(init.tablero_de_juego[i][j] == 3):
        #Casilla con 3 elementos
        print(colores.WHITE + str(init.tablero_de_juego[i][j]), end=',')
      elif(init.tablero_de_juego[i][j] == 4):
        #Casilla dónde completó el Jugador Humano
        print(colores.GREEN + str(init.tablero_de_juego[i][j]), end=',')
      elif(init.tablero_de_juego[i][j] == 5):
        #Casilla dónde completó la IA
        print(colores.BLUE + str(init.tablero_de_juego[i][j]), end=',')
      elif((init.tablero_de_juego[i][j] == 6) and ((i%2)==0) ):
        #Se puede seleccionar el lugar y es horizontal 
        print(colores.WHITE + str(init.tablero_de_juego[i][j]), end=',')
      elif((init.tablero_de_juego[i][j] == 6) and ((i%2)==1) ):
        #Se puede seleccionar el lugar y es vertical 
        print(colores.WHITE + str(init.tablero_de_juego[i][j]), end=',')
      elif((init.tablero_de_juego[i][j] == 7) and ((i%2)==0) ):
        #No Se puede seleccionar el lugar y es horizontal 
        print(colores.GREEN + str(init.tablero_de_juego[i][j]), end=',')
      elif((init.tablero_de_juego[i][j] == 7) and ((i%2)==1) ):
        #No Se puede seleccionar el lugar y es vertical 
        print(colores.GREEN + str(init.tablero_de_juego[i][j]), end=',')
      elif((init.tablero_de_juego[i][j] == 8) and ((i%2)==0) ):
        #No Se puede seleccionar el lugar y es horizontal 
        print(colores.BLUE + str(init.tablero_de_juego[i][j]), end=',')
      elif((init.tablero_de_juego[i][j] == 8) and ((i%2)==1) ):
        #No Se puede seleccionar el lugar y es vertical 
        print(colores.BLUE + str(init.tablero_de_juego[i][j]), end=',')
      elif(init.tablero_de_juego[i][j] == 9):
        print(colores.PURPLE + str(init.tablero_de_juego[i][j]), end=',')
    print(colores.WHITE + "]")

def jugadaHumana():
  valor = True
  while(valor):
    numeroCasilla = input("El número de casilla: (1-12) ")
    sentidoCasilla = input("El número de casilla: (N-S-E-W) ")
    try:
      valor = not moverTablero(numeroCasilla, sentidoCasilla, 7, True)
    except:
      print("Errores en los valores introducidos, intentar de nuevo.")
      print("Values= numeroCasilla:" + str(numeroCasilla) + ", sentidoCasilla:" + str(sentidoCasilla))
      valor=True

def jugador2():  
  valor = True
  while(valor):
    numeroCasilla = input("El número de casilla: (1-12) ")
    sentidoCasilla = input("El número de casilla: (N-S-E-W) ")
    try:
      valor = not moverTablero(numeroCasilla, sentidoCasilla, 8)
    except:
      print("Errores en los valores introducidos, intentar de nuevo.")
      valor=True
  

def moverTablero(numeroCasilla, sentidoCasilla, player, MostrarTablero):
  numero_de_casilla = 1;
  if(numeroCasilla=="" or sentidoCasilla==""):
    print("Movimiento inválido, revise de nuevo: ")
    return False
  if(casillasDisponibles()==0):
    return True
  for i in range(init.filas):
    for j in range(init.columnas):
      #Búsqueda del número de casilla 
      if(init.tablero_de_juego[i][j] == 0):
        #Búsqueda de casilla:
        #Casilla limpia
        if(int(numero_de_casilla) == int(numeroCasilla)):
          if(sentidoCasilla == 'n' or sentidoCasilla == 'N'):
              if(int(init.tablero_de_juego[i-1][j]) != 6):
                print("Espacio "+ str(numeroCasilla) + "-Norte ya está ocupado. " )
                return False
              init.tablero_de_juego[i-1][j] = player
              if(i-2 >= 0):
                if(init.tablero_de_juego[i-2][j] == 3):
                  init.tablero_de_juego[i-2][j] = player -3
                else:
                  init.tablero_de_juego[i-2][j] += 1
          elif(sentidoCasilla == 's' or sentidoCasilla == 'S'):
              if(int(init.tablero_de_juego[i+1][j]) != 6):
                print("Espacio "+ str(numeroCasilla) + "-Sur ya está ocupado. " )
                return False
              init.tablero_de_juego[i+1][j] = player
              if(i+2 < init.filas):
                if(init.tablero_de_juego[i+2][j] == 3):
                  init.tablero_de_juego[i+2][j] = player -3
                else:
                  init.tablero_de_juego[i+2][j] += 1
          elif(sentidoCasilla == 'e' or sentidoCasilla == 'E'):
              if(int(init.tablero_de_juego[i][j+1]) != 6):
                print("Espacio "+ str(numeroCasilla) + "-Este ya está ocupado. " )
                return False
              init.tablero_de_juego[i][j+1] = player
              if(j+2 < init.columnas):
                if(init.tablero_de_juego[i][j+2] == 3):
                  init.tablero_de_juego[i][j+2] = player -3
                else:
                  init.tablero_de_juego[i][j+2] += 1
          elif(sentidoCasilla == 'w' or sentidoCasilla == 'W'):
              if(int(init.tablero_de_juego[i][j-1]) != 6):
                print("Espacio "+ str(numeroCasilla) + "-Oeste ya está ocupado. " )
                return False
              init.tablero_de_juego[i][j-1] = player
              if(j-2 >= 0):
                if(init.tablero_de_juego[i][j-2] == 3):
                  init.tablero_de_juego[i][j-2] = player -3
                else:
                  init.tablero_de_juego[i][j-2] += 1
          else:
            print("El sentido seleccionado es inválido. Seleccione de nuevo. Valor Introducido: " + str(sentidoCasilla))
            return False
          init.tablero_de_juego[i][j] += 1
          return True
        numero_de_casilla += 1;
      elif(init.tablero_de_juego[i][j] == 1):
        #Casilla con 1 elemento
        if(int(numero_de_casilla) == int(numeroCasilla)):
          if(sentidoCasilla == 'n' or sentidoCasilla == 'N'):
              if(int(init.tablero_de_juego[i-1][j]) != 6):
                print("Espacio "+ str(numeroCasilla) + "-Norte ya está ocupado. " )
                return False
              init.tablero_de_juego[i-1][j] = player
              if(i-2 >= 0):
                if(init.tablero_de_juego[i-2][j] == 3):
                  init.tablero_de_juego[i-2][j] = player -3
                else:
                  init.tablero_de_juego[i-2][j] += 1
          elif(sentidoCasilla == 's' or sentidoCasilla == 'S'):
              if(int(init.tablero_de_juego[i+1][j]) != 6):
                print("Espacio "+ str(numeroCasilla) + "-Sur ya está ocupado. " )
                return False
              init.tablero_de_juego[i+1][j] = player
              if(i+2 < init.filas):
                if(init.tablero_de_juego[i+2][j] == 3):
                  init.tablero_de_juego[i+2][j] = player -3
                else:
                  init.tablero_de_juego[i+2][j] += 1
          elif(sentidoCasilla == 'e' or sentidoCasilla == 'E'):
              if(int(init.tablero_de_juego[i][j+1]) != 6):
                print("Espacio "+ str(numeroCasilla) + "-Este ya está ocupado. " )
                return False
              init.tablero_de_juego[i][j+1] = player
              if(j+2 < init.columnas):
                if(init.tablero_de_juego[i][j+2] == 3):
                  init.tablero_de_juego[i][j+2] = player -3
                else:
                  init.tablero_de_juego[i][j+2] += 1
          elif(sentidoCasilla == 'w' or sentidoCasilla == 'W'):
              if(int(init.tablero_de_juego[i][j-1]) != 6):
                print("Espacio "+ str(numeroCasilla) + "-Oeste ya está ocupado. " )
                return False
              init.tablero_de_juego[i][j-1] = player
              if(j-2 >= 0):
                if(init.tablero_de_juego[i][j-2] == 3):
                  init.tablero_de_juego[i][j-2] = player -3
                else:
                  init.tablero_de_juego[i][j-2] += 1
          else:
            print("El sentido seleccionado es inválido. Seleccione de nuevo. Valor Introducido: " + str(sentidoCasilla))
            return False
          init.tablero_de_juego[i][j] += 1
          return True
        numero_de_casilla += 1;
      elif(init.tablero_de_juego[i][j] == 2):
        #Casilla con 2 elementos
        if(int(numero_de_casilla) == int(numeroCasilla)):
          if(sentidoCasilla == 'n' or sentidoCasilla == 'N'):
              if(int(init.tablero_de_juego[i-1][j]) != 6):
                print("Espacio "+ numeroCasilla + "-Norte ya está ocupado. " )
                return False
              init.tablero_de_juego[i-1][j] = player
              if(i-2 >= 0):
                if(init.tablero_de_juego[i-2][j] == 3):
                  init.tablero_de_juego[i-2][j] = player -3
                else:
                  init.tablero_de_juego[i-2][j] += 1
          elif(sentidoCasilla == 's' or sentidoCasilla == 'S'):
              if(int(init.tablero_de_juego[i+1][j]) != 6):
                print("Espacio "+ numeroCasilla + "-Sur ya está ocupado. " )
                return False
              init.tablero_de_juego[i+1][j] = player
              if(i+2 < init.filas):
                if(init.tablero_de_juego[i+2][j] == 3):
                  init.tablero_de_juego[i+2][j] = player -3
                else:
                  init.tablero_de_juego[i+2][j] += 1
          elif(sentidoCasilla == 'e' or sentidoCasilla == 'E'):
              if(int(init.tablero_de_juego[i][j+1]) != 6):
                print("Espacio "+ numeroCasilla + "-Este ya está ocupado. " )
                return False
              init.tablero_de_juego[i][j+1] = player
              if(j+2 < init.columnas):
                if(init.tablero_de_juego[i][j+2] == 3):
                  init.tablero_de_juego[i][j+2] = player -3
                else:
                  init.tablero_de_juego[i][j+2] += 1
          elif(sentidoCasilla == 'w' or sentidoCasilla == 'W'):
              if(int(init.tablero_de_juego[i][j-1]) != 6):
                print("Espacio "+ numeroCasilla + "-Oeste ya está ocupado. " )
                return False
              init.tablero_de_juego[i][j-1] = player
              if(j-2 >= 0):
                if(init.tablero_de_juego[i][j-2] == 3):
                  init.tablero_de_juego[i][j-2] = player -3
                else:
                  init.tablero_de_juego[i][j-2] += 1
          else:
            print("El sentido seleccionado es inválido. Seleccione de nuevo. Valor Introducido: " + str(sentidoCasilla))
            return False
          init.tablero_de_juego[i][j] += 1
          return True
        numero_de_casilla += 1;
      elif(init.tablero_de_juego[i][j] == 3):
        #Casilla con 3 elementos
        if(int(numero_de_casilla) == int(numeroCasilla)):
          if(sentidoCasilla == 'n' or sentidoCasilla == 'N'):
              if(int(init.tablero_de_juego[i-1][j]) != 6):
                print("Espacio "+ numeroCasilla + "-Norte ya está ocupado. " )
                return False
              init.tablero_de_juego[i-1][j] = player
              if(i-2 >= 0):
                if(init.tablero_de_juego[i-2][j] == 3):
                  init.tablero_de_juego[i-2][j] = player -3
                else:
                  init.tablero_de_juego[i-2][j] += 1
          elif(sentidoCasilla == 's' or sentidoCasilla == 'S'):
              if(int(init.tablero_de_juego[i+1][j]) != 6):
                print("Espacio "+ numeroCasilla + "-Sur ya está ocupado. " )
                return False
              init.tablero_de_juego[i+1][j] = player
              if(i+2 < init.filas):
                if(init.tablero_de_juego[i+2][j] == 3):
                  init.tablero_de_juego[i+2][j] = player -3
                else:
                  init.tablero_de_juego[i+2][j] += 1
          elif(sentidoCasilla == 'e' or sentidoCasilla == 'E'):
              if(int(init.tablero_de_juego[i][j+1]) != 6):
                print("Espacio "+ numeroCasilla + "-Este ya está ocupado. " )
                return False
              init.tablero_de_juego[i][j+1] = player
              if(j+2 < init.columnas):
                if(init.tablero_de_juego[i][j+2] == 3):
                  init.tablero_de_juego[i][j+2] = player -3
                else:
                  init.tablero_de_juego[i][j+2] += 1
          elif(sentidoCasilla == 'w' or sentidoCasilla == 'W'):
              if(int(init.tablero_de_juego[i][j-1]) != 6):
                print("Espacio "+ numeroCasilla + "-Oeste ya está ocupado. " )
                return False
              init.tablero_de_juego[i][j-1] = player
              if(j-2 >= 0):
                if(init.tablero_de_juego[i][j-2] == 3):
                  init.tablero_de_juego[i][j-2] = player -3
                else:
                  init.tablero_de_juego[i][j-2] += 1
          else:
            print("El sentido seleccionado es inválido. Seleccione de nuevo. Valor Introducido: " + str(sentidoCasilla))
            return False
          init.tablero_de_juego[i][j] = player-3
          if(MostrarTablero):
            ImprimirTablero()
          return False
        numero_de_casilla += 1;
  print ("Numero de casillas: " + str(numero_de_casilla))

def jugadasDisponibles(casilla):
  numero_de_casilla = 1;
  for i in range(init.filas):
    for j in range(init.columnas):
      if(init.tablero_de_juego[i][j] == 0 or init.tablero_de_juego[i][j] == 1 or init.tablero_de_juego[i][j] == 2 or init.tablero_de_juego[i][j] == 3):
        if(int(numero_de_casilla) == int(casilla)):
          #Explorando casilla: N/S/E/W
          return init.tablero_de_juego[i-1][j], init.tablero_de_juego[i+1][j], init.tablero_de_juego[i][j+1], init.tablero_de_juego[i][j-1]
        numero_de_casilla += 1

def casillasDisponibles():
  casillas = 0
  for i in range(init.filas):
    for j in range(init.columnas):
      if(init.tablero_de_juego[i][j]==0 or init.tablero_de_juego[i][j]==1 or init.tablero_de_juego[i][j]==2 or init.tablero_de_juego[i][j]==3):
        casillas += 1
  return (casillas)

def JugadaMaquina(jugadasMaquina):
  #Resuelve indistintamente los 3
  while completaTerceros(8,True):
    print ("Máquina: ¡He completado 1 cuadro!")

  if(init.limitePrimerasJugadas > jugadasMaquina):
    while (not primerasJugadas()):
      print("ERROR 409: Ninguno Seleccionado ")
  else:
    jugadasIA()

def completaTerceros(player,imprimir):
  #Función para buscar los números terceros y completarlos
  numero_de_casilla = 1;
  for i in range(init.filas):
    for j in range(init.columnas):
      if(init.tablero_de_juego[i][j] == 3):
        #Encontró un tercero
        jugadas = jugadasDisponibles(numero_de_casilla)
        #Encontrando Faltante 
        for k in range (0,4):
          if(int(jugadas[k]) == 6):
            if k == 0:
              if imprimir:
                print("Máquina: Elijo: "+ str(numero_de_casilla) + "-N ")
              moverTablero(numero_de_casilla, 'n', player,imprimir)
              return True
            elif k == 1:
              if imprimir:
                print("Máquina: Elijo: "+ str(numero_de_casilla) + "-S ")
              moverTablero(numero_de_casilla, 's', player,imprimir)
              return True
            elif k == 2:
              if imprimir:
                print("Máquina: Elijo: "+ str(numero_de_casilla) + "-E ")
              moverTablero(numero_de_casilla, 'e', player,imprimir)
              return True
            elif k == 3:
              if imprimir:
                print("Máquina: Elijo: "+ str(numero_de_casilla) + "-W ")
              moverTablero(numero_de_casilla, 'w', player,imprimir)
              return True
      elif (init.tablero_de_juego[i][j] == 0 or init.tablero_de_juego[i][j] == 1 or init.tablero_de_juego[i][j] == 2):
        numero_de_casilla += 1
  return False


def primerasJugadas():
  inicioSec = time.localtime().tm_sec
  inicioMs  = time.time()
  if(casillasDisponibles() == 0):
    return True
  casillaSeleccionada = random.randrange(1, casillasDisponibles()+1)
  jugadas = jugadasDisponibles(casillaSeleccionada)
  if(jugadas.count(6) == 4 or jugadas.count(6) == 3):
    valor = True
    while(valor):      
      sentidoSeleccionado = random.randrange(0, 4)
      try:
        if sentidoSeleccionado == 0:
          print("Máquina: Elijo: "+ str(casillaSeleccionada) + "-Norte ")
          valor = not moverTablero(casillaSeleccionada, 'n', 8,True)
        elif sentidoSeleccionado == 1:
          print("Máquina: Elijo: "+ str(casillaSeleccionada) + "-Sur ")
          valor = not moverTablero(casillaSeleccionada, 's', 8,True)
        elif sentidoSeleccionado == 2:
          print("Máquina: Elijo: "+ str(casillaSeleccionada) + "-Este ")
          valor = not moverTablero(casillaSeleccionada, 'e', 8,True)
        elif sentidoSeleccionado == 3:
          print("Máquina: Elijo: "+ str(casillaSeleccionada) + "-Oeste ")
          valor = not moverTablero(casillaSeleccionada, 'w', 8,True)
        else:
          print("Error 471 - Valor: "+str(valor) + 
                " - Casilla Seleccionada: " + str(casillaSeleccionada) +
                " - Sentido: (N/S/E/W)" + str(sentidoSeleccionado)
               )
          return False
      except:
        print("Máquina: Me equivoqué al seleccionar los valores. Lo intentaré de nuevo.")
    finalSec = time.localtime().tm_sec
    finalMs  = time.time()
    jsonTiempo = json.loads('{}')
    jsonTiempo.update({"TiempoMs":finalMs-inicioMs})
    jsonTiempo.update({"TiempoSec":finalSec-inicioSec})
    jsonTiempo.update({"Type":2})
    init.estadisticas.append(jsonTiempo)
    return True
  return False

def restaurarTableroOriginal(respaldo):
  for i in range(init.filas):
    for j in range(init.columnas):
      init.tablero_de_juego[i][j] = respaldo[i][j]
  return True

def contarCasillas(numero):
  casillas = 0 
  for i in range(init.filas):
    for j in range(init.columnas):
      if(init.tablero_de_juego[i][j] == numero):
        casillas += 1
  return casillas

def jugadasIA():
  inicioSec = time.localtime().tm_sec
  inicioMs  = time.time()
  print("Espera... Estoy tomando una decisión... ")
  #Primero completa todas las jugadas posibles 
  completaTerceros(8,True)
  #Copia el tablero original
  respaldoTablero = respaldoOriginal()
  casillasUsuario = contarCasillas(4)
  casillasMaquina = contarCasillas(5)
  casillasPosibles = casillasDisponibles()
  if casillasDisponibles == 0:
    return
  primeraPasada= []
  primeraPasadaNoOptimos= []

  segundaPasada= []
  segundaPasadaNoOptimos= []
  for i in range(1,casillasPosibles+1): #GENERACIÓN DE TABLEROS POSIBLES
    jugadas = jugadasDisponibles(i)
    #Encontrando Tirada Correcta 
    for k in range (0,4):
      jsonObject = json.loads('{}')
      if(int(jugadas[k]) == 6):
        jsonObject.update({"CasillaElegida":i})
        if k == 0:
          moverTablero(i, 'n', 8,False)
          jsonObject.update({"SentidoElegido":'N'})
        elif k == 1:
          moverTablero(i, 's', 8,False)
          jsonObject.update({"SentidoElegido":'S'})
        elif k == 2:
          moverTablero(i, 'e', 8,False)
          jsonObject.update({"SentidoElegido":'E'})
        elif k == 3:
          moverTablero(i, 'w', 8,False)
          jsonObject.update({"SentidoElegido":'W'})
        CasillasUsuario = 0
        while completaTerceros(7,False):
          CasillasUsuario += 1
        jsonObject.update({"Tablero":respaldoOriginal()})
        jsonObject.update({"CasillasNuevasUsuario":contarCasillas(4)-casillasUsuario})
        jsonObject.update({"CasillasNuevasMaquina":contarCasillas(5)-casillasMaquina})
        if(jsonObject['CasillasNuevasUsuario'] != 0):
          primeraPasadaNoOptimos.append(jsonObject)
        else:
          primeraPasada.append(jsonObject)
        restaurarTableroOriginal(respaldoTablero) #Restaura el tablero Original
        
  if(len(primeraPasada)==0):
    #No hay óptimos
    restaurarTableroOriginal(respaldoTablero) #Restaura el tablero Original
    #Buscando la mnor cantidad de juegadas posibles: 
    menorSolucion = init.casillasMaximas
    mayorSolucionMaquina = 0
    for i in range (0,len(primeraPasadaNoOptimos)):
      objetoJSON = primeraPasadaNoOptimos[i]
      if(objetoJSON['CasillasNuevasUsuario'] < menorSolucion):
        menorSolucion = objetoJSON['CasillasNuevasUsuario']
      if(objetoJSON['CasillasNuevasMaquina'] > mayorSolucionMaquina):
        mayorSolucionMaquina = objetoJSON['CasillasNuevasMaquina']
    #Perderá de todas formas: Elige la que cumpla el menor posible al usuario 
    if(mayorSolucionMaquina == 0):
      mejorLista = []
      peorLista = []
      for i in range (0,len(primeraPasadaNoOptimos)):
        objetoJSON = primeraPasadaNoOptimos[i]
        if(objetoJSON['CasillasNuevasUsuario'] == menorSolucion and objetoJSON['CasillasNuevasMaquina'] == mayorSolucionMaquina):
          mejorLista.append(i)
        elif (objetoJSON['CasillasNuevasUsuario'] == menorSolucion):
          peorLista.append(i)
      #Selecciona de la lista uno aleatorio
      if(len(mejorLista) > 0):
        eleccion = random.randrange(0, len(mejorLista))
        objetoJSON = primeraPasadaNoOptimos[eleccion]
        print("Máquina: Elijo: "+ str(objetoJSON['CasillaElegida']) + "-" + str(objetoJSON['SentidoElegido']))
        moverTablero(objetoJSON['CasillaElegida'], objetoJSON['SentidoElegido'], 8, True)
        finalSec = time.localtime().tm_sec
        finalMs  = time.time()
        jsonTiempo = json.loads('{}')
        jsonTiempo.update({"TiempoMs":finalMs-inicioMs})
        jsonTiempo.update({"TiempoSec":finalSec-inicioSec})
        jsonTiempo.update({"SolucionesCreadas":len(primeraPasada)})
        jsonTiempo.update({"SolucionesRechazadas":len(primeraPasadaNoOptimos)})
        jsonTiempo.update({"Type":5})
        init.estadisticas.append(jsonTiempo)
        return True
      else:
        eleccion = random.randrange(0, len(peorLista))
        objetoJSON = primeraPasadaNoOptimos[eleccion]
        print("Máquina: Elijo: "+ str(objetoJSON['CasillaElegida']) + "-" + str(objetoJSON['SentidoElegido']))
        moverTablero(objetoJSON['CasillaElegida'], objetoJSON['SentidoElegido'], 8, True)
        finalSec = time.localtime().tm_sec
        finalMs  = time.time()
        jsonTiempo = json.loads('{}')
        jsonTiempo.update({"TiempoMs":finalMs-inicioMs})
        jsonTiempo.update({"TiempoSec":finalSec-inicioSec})
        jsonTiempo.update({"SolucionesCreadas":len(primeraPasada)})
        jsonTiempo.update({"SolucionesRechazadas":len(primeraPasadaNoOptimos)})
        jsonTiempo.update({"Type":6})
        init.estadisticas.append(jsonTiempo)
        return True

  if(len(primeraPasada)==1): #Solo hay 1 óptimo: 
    restaurarTableroOriginal(respaldoTablero) #Restaura el tablero Original
    objetoJSON = primeraPasada[0]
    print("Máquina: Elijo: "+ str(objetoJSON['CasillaElegida']) + "-" + str(objetoJSON['SentidoElegido']))
    moverTablero(objetoJSON['CasillaElegida'], objetoJSON['SentidoElegido'], 8, True)
    finalSec = time.localtime().tm_sec
    finalMs  = time.time()
    jsonTiempo = json.loads('{}')
    jsonTiempo.update({"TiempoMs":finalMs-inicioMs})
    jsonTiempo.update({"TiempoSec":finalSec-inicioSec})
    jsonTiempo.update({"SolucionesCreadas":len(primeraPasada)})
    jsonTiempo.update({"SolucionesRechazadas":len(primeraPasadaNoOptimos)})
    jsonTiempo.update({"Type":7})
    init.estadisticas.append(jsonTiempo)
    return True
    
  #Continua generando: 
  #Genera posibles tiradas del usuario 
  casillasPosibles = casillasDisponibles()
  for j in range (0,len(primeraPasada)):
    objetoJSON = primeraPasada[j]
    restaurarTableroOriginal(objetoJSON['Tablero'])
    casillasUsuario = contarCasillas(4)
    casillasMaquina = contarCasillas(5)
    casillasPosibles = casillasDisponibles()

    totalSoluciones = 0
    mejoresSoluciones = 0
    
    for i in range(1,casillasPosibles+1): #GENERACIÓN DE TABLEROS POSIBLES
      jugadas = jugadasDisponibles(i)
      #Encontrando Tirada Correcta 
      for k in range (0,4):
        jsonObject = json.loads('{}')
        if(int(jugadas[k]) == 6):
          jsonObject.update({"CasillaElegida":i})
          if k == 0:
            moverTablero(i, 'n', 7,False)
            jsonObject.update({"SentidoElegido":'N'})
          elif k == 1:
            moverTablero(i, 's', 7,False)
            jsonObject.update({"SentidoElegido":'S'})
          elif k == 2:
            moverTablero(i, 'e', 7,False)
            jsonObject.update({"SentidoElegido":'E'})
          elif k == 3:
            moverTablero(i, 'w', 7,False)
            jsonObject.update({"SentidoElegido":'W'})
          CasillasMaquina = 0
          while completaTerceros(8,False):
            CasillasMaquina += 1
          jsonObject.update({"Tablero":respaldoOriginal()})
          jsonObject.update({"Padre":j})
          jsonObject.update({"CasillasNuevasUsuario":contarCasillas(4)-casillasUsuario})
          jsonObject.update({"CasillasNuevasMaquina":contarCasillas(5)-casillasMaquina})
          if(jsonObject['CasillasNuevasUsuario'] == 0):
            segundaPasada.append(jsonObject)
            mejoresSoluciones += 1
          else:
            segundaPasadaNoOptimos.append(jsonObject)
          restaurarTableroOriginal(objetoJSON['Tablero'])
          totalSoluciones += 1
    objetoJSON.update({"TotalSoluciones":totalSoluciones})
    objetoJSON.update({"MejoresSoluciones":mejoresSoluciones})
    primeraPasada[j] = objetoJSON
  restaurarTableroOriginal(respaldoTablero) #Restaura el tablero Original
  #Evalúa el mejor caso, la probabilidad de la mejor solución es el total de soluciones. 
  Soluciones = []
  Probabilidades = []
  for j in range (0,len(primeraPasada)):
    objetoJSON = primeraPasada[j]
    if(objetoJSON['TotalSoluciones'] == objetoJSON['MejoresSoluciones']):
      Soluciones.append(objetoJSON)
    Probabilidades.append(objetoJSON['MejoresSoluciones']/objetoJSON['TotalSoluciones'])

  if(len(Soluciones) != 0):
    if(len(Soluciones) == 1):
      objetoJSON = primeraPasada[0]
    else:
      eleccion = random.randrange(0, len(Soluciones))
      objetoJSON = primeraPasada[eleccion]
    print("Máquina: Elijo: "+ str(objetoJSON['CasillaElegida']) + "-" + str(objetoJSON['SentidoElegido']))
    moverTablero(objetoJSON['CasillaElegida'], objetoJSON['SentidoElegido'], 8, True)
    finalSec = time.localtime().tm_sec
    finalMs  = time.time()
    jsonTiempo = json.loads('{}')
    jsonTiempo.update({"TiempoMs":finalMs-inicioMs})
    jsonTiempo.update({"TiempoSec":finalSec-inicioSec})
    jsonTiempo.update({"SolucionesCreadas":len(primeraPasada)})
    jsonTiempo.update({"SolucionesRechazadas":len(primeraPasadaNoOptimos)})
    jsonTiempo.update({"SolucionesCreadasSegunda":len(segundaPasada)})
    jsonTiempo.update({"SolucionesRechazadasSegunda":len(segundaPasadaNoOptimos)})
    jsonTiempo.update({"Type":3})
    init.estadisticas.append(jsonTiempo)
    return True
    
  prob = 2
  eleccion = -1 
  for j in range (0,len(Probabilidades)):
    if(Probabilidades[j]<prob):
      prob = Probabilidades[j]
      eleccion = j
  objetoJSON = primeraPasada[eleccion]
  print("Máquina: Elijo: "+ str(objetoJSON['CasillaElegida']) + "-" + str(objetoJSON['SentidoElegido']))
  moverTablero(objetoJSON['CasillaElegida'], objetoJSON['SentidoElegido'], 8, True)
  finalSec = time.localtime().tm_sec
  finalMs  = time.time()
  jsonTiempo = json.loads('{}')
  jsonTiempo.update({"TiempoMs":finalMs-inicioMs})
  jsonTiempo.update({"TiempoSec":finalSec-inicioSec})
  jsonTiempo.update({"SolucionesCreadas":len(primeraPasada)})
  jsonTiempo.update({"SolucionesRechazadas":len(primeraPasadaNoOptimos)})
  jsonTiempo.update({"SolucionesCreadasSegunda":len(segundaPasada)})
  jsonTiempo.update({"SolucionesRechazadasSegunda":len(segundaPasadaNoOptimos)})
  jsonTiempo.update({"Type":4})
  init.estadisticas.append(jsonTiempo)
  return True

def primeroHumano():
  jugadasMaquina = 0
  partida = 1
  while(casillasDisponibles() != 0):
    print("Número de Partida: "+str(partida))
    ImprimirTablero()
    jugadaHumana()
    #imprimirTableroBackend()
    inicioSec = time.localtime().tm_sec
    inicioMs  = time.time()
    JugadaMaquina(jugadasMaquina)
    finalSec = time.localtime().tm_sec
    finalMs  = time.time()
    jsonTiempo = json.loads('{}')
    jsonTiempo.update({"TiempoMs":finalMs-inicioMs})
    jsonTiempo.update({"TiempoSec":finalSec-inicioSec})
    jsonTiempo.update({"Type":8})
    init.estadisticas.append(jsonTiempo)
    #imprimirTableroBackend()
    jugadasMaquina += 1
    partida += 1
    
def primeroMaquina():
  jugadasMaquina = 0
  partida = 1
  while(casillasDisponibles() != 0):
    print("Número de Partida: "+str(partida))
    ImprimirTablero()
    inicioSec = time.localtime().tm_sec
    inicioMs  = time.time()
    JugadaMaquina(jugadasMaquina)
    finalSec = time.localtime().tm_sec
    finalMs  = time.time()
    jsonTiempo = json.loads('{}')
    jsonTiempo.update({"TiempoMs":finalMs-inicioMs})
    jsonTiempo.update({"TiempoSec":finalSec-inicioSec})
    jsonTiempo.update({"Type":8})
    init.estadisticas.append(jsonTiempo)
    #imprimirTableroBackend()
    ImprimirTablero()
    jugadasMaquina += 1
    jugadaHumana()
    #imprimirTableroBackend()
    partida += 1


def partida():
  #Lanzar moneda
  moneda = random.randrange(0, 2)
  try:
    if(moneda==0):
      print("La moneda seleccionó al Humano para jugar primero ")
      primeroHumano()
    else:
      print("La moneda seleccionó a la Máquina para jugar primero ")
      primeroMaquina()
  except Exception as e:
    print("Error!")
    print(e)
  print("Fin del Juego")
  print("Resultado del Juego: ")
  print("Jugador humano: "+str(contarCasillas(4)))
  print("Máquina: "+str(contarCasillas(5)))
  if(contarCasillas(4)==contarCasillas(5)):
    print("Hubo un empate")
  elif(contarCasillas(4)>contarCasillas(5)):
    print("Ganó el jugador Humano")
  else:
    print("Ganó la máquna")
  


def guardarResultados():
  # Print to the text file
  file = open('output.json', 'w')
  print(init.estadisticas, file = file)
  file.close()
  
partida()
guardarResultados()

