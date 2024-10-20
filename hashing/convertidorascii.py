# caracter = 'A'
# valor_ascii = ord(caracter)
# print(f"El valor ASCII de '{caracter}' es {valor_ascii}")
valor="E010-267"
valorx="".join(str(ord(c)) for c in valor)
print(valorx)
valorfinal=int(valorx)%67
print(valorfinal)
print('skibidi')