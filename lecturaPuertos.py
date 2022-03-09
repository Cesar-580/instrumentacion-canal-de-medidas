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

print("Trama uno")
while x < 21:
    datosLeidos = ser.read()
    datos = datosLeidos
    #print(datos)
    #print(type(datos))
    x+= 1

print("Trama dos")
datosLeidosDos = ser.read(20)
datosDos = datosLeidosDos
print(datosDos)
print(datosDos[1])
print("TIPOSSSSSSSSSSSSSSSSSSSSSSSS")
print(type(datosDos))
print(type(datosDos[1]))




ser.close()             # close port

