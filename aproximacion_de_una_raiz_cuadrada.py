objectivo=int(input('Escoge un numero: '))
epsilon=0.02
paso= epsilon**2
respuesta= 0.0

while abs(respuesta**2 - objectivo)>= epsilon and respuesta <=objectivo:
    print(abs(respuesta**2 -objectivo), respuesta)
    respuesta+=paso


if( abs(respuesta**2 - objectivo)>=epsilon):
    print(f'No se encontro a raiz cuadrada {objectivo}')
else:
    print(f'La raiz cuadrada de {objectivo} es {respuesta}')
