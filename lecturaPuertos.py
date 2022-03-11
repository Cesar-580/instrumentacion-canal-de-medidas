# pip install pyserial

# Importación de la libreria
import serial


# Limpia el puerto
serial.Serial("COM9", 115200).close()

# Inicia el puerto serial
ser = serial.Serial('COM9',115200)
# print(ser.name)         # check which port was really used
# ser.write(b'hello')     # write a string

#print(ser)

x = 0

#print("Trama uno")

# Lista almacenadora de los datos
            # cadenaHexadecimal = []

            # print("Trama uno")
            # while x < 21:
            #     datosLeidos = ser.read()
            #     datos = datosLeidos
            #     #print(x)
            #     #print(datos)
            #     print(f'{datos:0>8b}', end=' ')
            #     #print(type(datos))
            #     x+= 1

            # print(cadenaHexadecimal)

datosLeidos = ser.read(21)
# for i in range(0,21):
#     print(datosLeidos[i])

def binar(dec):
    bina = ""
    while dec // 2 != 0:
        bina = str(dec % 2) + bina
        dec = dec // 2
    return str(dec) + bina

def completarCeros(nBinario):
    nBinario = nBinario.zfill(8)
    return nBinario

tramaDecimal = [datosLeidos[i] for i in range(0,21)]
# print(tramaDecimal)
tramaBinaria = list(map(binar, tramaDecimal))
print(tramaBinaria)
tramaBinariaCompleto = list(map(completarCeros, tramaBinaria))
print(tramaBinariaCompleto)



#print(len(cadenaHexadecimal))
#print(int((cadenaHexadecimal[1]),2))

#datosLeidosDos = ser.read(20)
#datosDos = datosLeidosDos
# datosDos = (datosDos[1:-1])

# for i in range(0,19):
#     print(datosDos[i])


#print(datosDos)
#print(datosDos[1])
#print("TIPOSSSSSSSSSSSSSSSSSSSSSSSS")
#print(type(datosDos))
#print(datosDos[5])

a = bin(2)
b = bin(2)

#print(type(a))

# r = a[2:] + b[2:]
# print(type(r))
# r = r.zfill(8)
# print(type(int(r,2)))
# print(bin(int(r,2)))
# print(int(r,2))



ser.close()             # close port




