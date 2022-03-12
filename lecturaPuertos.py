# pip install pyserial

# Importación de la libreria
from ast import Not
import serial


# Limpia el puerto
serial.Serial("COM9", 115200).close()

# Inicia el puerto serial
ser = serial.Serial('COM9',115200)

x = 0

# Gravedad
g = 9.8


datosLeidos = ser.read(21)

def binar(dec):
    bina = ""
    while dec // 2 != 0:
        bina = str(dec % 2) + bina
        dec = dec // 2
    return str(dec) + bina

def completarCeros(nBinario):
    nBinario = nBinario.zfill(8)
    return nBinario

def inverso(nNegativo):
    l = ""
    for i in nNegativo:
        if i == "1":
            l = l + "0"
        else:
            l = l + "1"
    return l

        

tramaDecimal = [datosLeidos[i] for i in range(0,21)]
# print(tramaDecimal)
tramaBinaria = list(map(binar, tramaDecimal))
#print(tramaBinaria)
tramaBinariaCompleto = list(map(completarCeros, tramaBinaria))
print(tramaBinariaCompleto)

Ax = tramaBinariaCompleto[3]+tramaBinariaCompleto[2]
Ay = tramaBinariaCompleto[5]+tramaBinariaCompleto[4]
Az = tramaBinariaCompleto[7]+tramaBinariaCompleto[6]
Wx = tramaBinariaCompleto[9]+tramaBinariaCompleto[8]
Wy = tramaBinariaCompleto[11]+tramaBinariaCompleto[10]
Wz = tramaBinariaCompleto[13]+tramaBinariaCompleto[12]
R = tramaBinariaCompleto[15]+tramaBinariaCompleto[14]
P = tramaBinariaCompleto[17]+tramaBinariaCompleto[16]
Y = tramaBinariaCompleto[19]+tramaBinariaCompleto[18]

# ------------------------ Aceleración en X ------------------------

print("Ax")
if Ax[0] == "1":
    Ax_r = inverso(Ax)
    Ax_r = int(Ax_r,2)
    Ax_r = Ax_r*((16*g)/32768)*-1
    #print(Ax)
    print(Ax_r)
else:
    print(Ax)
    Ax_r = int(Ax,2)
    Ax_r = Ax_r*((16*g)/32768)
    print(Ax_r)

# ------------------------ Aceleración en Y ------------------------

print("Ay")
if Ay[0] == "1":
    Ay_r = inverso(Ay)
    Ay_r = int(Ay_r,2)
    Ay_r = Ay_r*((16*g)/32768)*-1
    print(Ay_r)
else:
    Ay_r = int(Ay,2)
    Ay_r = Ay_r*((16*g)/32768)
    print(Ay_r)

# ------------------------ Aceleración en Z ------------------------

print("Az")
if Az[0] == "1":
    Az_r = inverso(Az)
    Az_r = int(Az_r,2)
    Az_r = Az_r*(180/32768)*-1
    print(Az_r)
else:
    Az_r = int(Az,2)
    Az_r = Az_r*(180/32768)
    print(Az_r)

# ------------------------ Lectura Roll ------------------------

print("R")
if R[0] == "1":
    R_r = inverso(R)
    R_r = int(R_r,2)
    R_r = R_r*(180/32768)*-1
    print(R_r)
else:
    R_r = int(R,2)
    R_r = R_r*(180/32768)
    print(R_r)

# ------------------------ Lectura Pitch ------------------------

print("P")
if P[0] == "1":
    P_r = inverso(P)
    P_r = int(P_r,2)
    P_r = P_r*(180/32768)*-1
    print(P_r)
else:
    P_r = int(P,2)
    P_r = P_r*(180/32768)
    print(P_r)

# ------------------------ Lectura Yaw ------------------------

print("Y")
if Y[0] == "1":
    Y_r = inverso(Y)
    Y_r = int(Y_r,2)
    Y_r = Y_r*(180/32768)*-1
    print(Y_r)
else:
    Y_r = int(Y,2)
    Y_r = Y_r*(180/32768)
    print(Y_r)

ser.close()             # close port




