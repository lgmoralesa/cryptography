#Turning Grille Cipher - Laura Morales

import numpy as np

# Datos
print("Tamaño de la retícula")
grille_len = int(input())

print("Dirección de la rotación:\n 1. Sentido de las manecillas del reloj\n 2. Sentido contrario")
rotation_dir = int(input())

print("Seleccione la operación:\n 1. Cifrar\n 2. Decifrar")
operation = int(input())

print("Mensaje a (de)cifrar")
message = input().replace(' ', '')

print("Número de hoyos")
holes = int(input())
print("Posiciones de los hoyos")

#Matriz de hoyos representados con 1
grille = [[0]*grille_len for n in range(grille_len)]
for h in range(holes):
  hole_x, hole_y = input().split(',')
  grille[int(hole_x)][int(hole_y)] = 1


def rotate(grille, grille_len, rotation_dir):
  grille2 = [row[:] for row in grille]
  if rotation_dir == 1:
    for i in range(grille_len):
      for j in range(grille_len):
        grille2[i][j] = grille[grille_len-1-j][i]
    return grille2
  else:
    for i in range(grille_len):
      for j in range(grille_len):
        grille2[grille_len-1-j][i] = grille[i][j]
    return grille2

def encrypt(grille, grille_len, message, rotation_dir):
  message_list = list(message)
  matrix = [[0]*grille_len for m in range(grille_len)]
  c = 0
  for r in range(4):
    for i in range(grille_len):
      for j in range(grille_len):
        if grille[i][j] == 1:
          matrix[i][j] = message_list[c]
          c+=1
    grille = rotate(grille,grille_len,rotation_dir)
  
  encrypt_message = ""
  for i in range(grille_len):
    for j in range(grille_len):
      encrypt_message += matrix[i][j]
  return encrypt_message

def decrypt(grille, grille_len, message, rotation_dir):
  message_list = list(message)
  matrix = [[0]*grille_len for m in range(grille_len)]
  c = 0
  for i in range(grille_len):
    for j in range(grille_len):
      matrix[i][j] = message_list[c]
      c+=1
  
  decrypt_message = ""
  for r in range(4):
    for i in range(grille_len):
      for j in range(grille_len):
        if grille[i][j] == 1:
          decrypt_message += matrix[i][j]
    grille = rotate(grille,grille_len,rotation_dir)
  return decrypt_message

if operation == 1:
  print (encrypt(grille, grille_len, message, rotation_dir))
else:
  print (decrypt(grille, grille_len, message, rotation_dir))