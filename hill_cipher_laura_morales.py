#Hill Cipher - Laura Morales
import numpy as np

def gcdx(a, b):
  if b == 0:
      return 0,1,0
  x0 = 1
  x1 = 0
  y0 = 0
  y1 = 1
  while b != 0:
      q = a//b
      r = a - b * q
      x = x0 - q * x1
      y = y0 - q * y1
      #Update
      a = b
      b = r
      x0 = x1
      x1 = x
      y0 = y1
      y1 = y
  return  a, x0, y0

dictionary = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15,"q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}

print("Seleccione la operación:\n 1. Cifrar\n 2. Decifrar")
operation = int(input())

#Cifrar
if operation == 1:
  print("Ingrese el mensaje a cifrar:")
  plaintext = input()
  print("Ingrese la llave (matriz de 2x2):")
  key = np.array([[0]*2,[0]*2])
  for f in range(2):
    for c in range(2):
      key[f][c] = int(input("Posición %d,%d: " % (f,c)))

  det = int(np.linalg.det(key))
  if det == 0 or gcdx(det, 26)[0] != 1:
    print("La matriz es no invertible")
  
  print("Texto cifrado:")
  for i in range(0,len(plaintext),2):
    m = np.array([0]*2)
    m[0] = dictionary[plaintext[i]]
    m[1] = dictionary[plaintext[i+1]]
    c = np.remainder(m.dot(key), 26)
    print (list(dictionary.keys())[list(dictionary.values()).index(c[0])], end = '')
    print (list(dictionary.keys())[list(dictionary.values()).index(c[1])], end = '')
#Decifrar
else:
  print("Ingrese el texto cifrado:")
  ciphertext = input()
  print("Ingrese la llave (matriz de 2x2):")
  key = np.array([[0]*2,[0]*2])
  for f in range(2):
    for c in range(2):
      key[f][c] = int(input("Posición %d,%d: " % (f,c)))

  det = int(np.linalg.det(key))
  if det == 0 or gcdx(det, 26)[0] != 1:
    print("La matriz es no invertible")

  key_adj = np.array( [ [ key[1][1], -key[0][1] ] , [ -key[1][0], key[0][0] ] ])
  print("Texto plano:")
  for i in range(0,len(ciphertext),2):
    modular_inv = gcdx(det, 26)[1]
    c = np.array([0]*2)
    c[0] = dictionary[ciphertext[i]]
    c[1] = dictionary[ciphertext[i+1]]
    key_inv = modular_inv*key_adj
    m = np.remainder(c.dot(key_inv), 26)
    print (list(dictionary.keys())[list(dictionary.values()).index(m[0])], end = '')
    print (list(dictionary.keys())[list(dictionary.values()).index(m[1])], end = '')


