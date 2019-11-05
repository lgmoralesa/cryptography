#Vigenere Cipher - Laura Morales

dictionary = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15,"q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
print("Seleccione la operación:\n 1. Cifrar\n 2. Decifrar")
operation = int(input())
if operation == 1:
  print("Ingrese el mensaje a cifrar:")
  plaintext = input()
  print("Ingrese la llave:")
  key = input()
  keyl = (key * (int(len(plaintext)/len(key))+1))[:len(plaintext)]
  print("Texto cifrado:")
  for i in range(len(plaintext)):
    print (list(dictionary.keys())[list(dictionary.values()).index((dictionary[plaintext[i]] + dictionary[keyl[i]]) % 26)], end = '')
else:
  print("Ingrese el texto cifrado:")
  ciphertext = input()
  print("Ingrese la llave:")
  key = input()
  keyc = (key * (int(len(ciphertext)/len(key))+1))[:len(ciphertext)]
  print("Texto plano:")
  for i in range(len(ciphertext)):
    print (list(dictionary.keys())[list(dictionary.values()).index((dictionary[ciphertext[i]] - dictionary[keyc[i]]) % 26)], end = '')


