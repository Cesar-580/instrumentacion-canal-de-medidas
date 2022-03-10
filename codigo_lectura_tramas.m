clear all;
close all;
clc;

delete(instrfind({'PORT'},{'COM9'}));
%s=serial('com5','baudrate',115200);
s = serialport('COM9',115200);
f =[];
x = 1;

%Constante
g = 9.8; %[m/s2]

while(x == 1)
    f = read(s,20,"uint8");
    A1 = int2bit( f(4) , 8)';
    A2 = int2bit( f(3) , 8)';
    %Lectura de la aceleración
        %Aceleración en X
        a_x_b = double([int2bit( f(4) , 8)',zeros(1,8)] | [zeros(1,8),int2bit( f(3) , 8)']);
        
        %condicional negativo
        if(a_x_b(1) == 1)
            a_x_b = not(a_x_b);
            %Cálculo de la aceleración
            ax = bit2int(a_x_b',16)*((16*g)/32768)*-1
        else
            ax = bit2int(a_x_b',16)*((16*g)/32768)
        end

    %Lectura de la aceleración
        %Aceleración en y
        a_y_b = double([int2bit( f(6) , 8)',zeros(1,8)] | [zeros(1,8),int2bit( f(5) , 8)']);

        %condicional negativo
        if(a_y_b(1) == 1)
            a_y_b = not(a_y_b);
            %Cálculo de la aceleración
            ay = bit2int(a_y_b',16)*((16*g)/32768)*-1
        else
            ay = bit2int(a_y_b',16)*((16*g)/32768)
        end

    %Lectura de la aceleración
        %Aceleración en Z
        a_z_b = double([int2bit( f(8) , 8)',zeros(1,8)] | [zeros(1,8),int2bit( f(7) , 8)']);

        %condicional negativo
        if(a_z_b(1) == 1)
            a_z_b = not(a_z_b);
            %Cálculo de la aceleración
            az = bit2int(a_z_b',16)*((16*g)/32768)*-1
        else
            az = bit2int(a_z_b',16)*((16*g)/32768)
        end


    %Lectura deL Roll, Pitch Yaw
      
        % Roll
        R_b = double([int2bit( f(16) , 8)',zeros(1,8)] | [zeros(1,8),int2bit( f(15) , 8)']);
    
        %Condicional Negativo

        if(R_b(1) == 1)
            R_b = not(R_b);
            Roll = bit2int(R_b',16)*(180/32768)*-1
        else
            Roll = bit2int(R_b',16)*(180/32768)
        end



      %Angulo Pitch
        P_b = double([int2bit( f(18) , 8)',zeros(1,8)] | [zeros(1,8),int2bit( f(17) , 8)']);
    
        %Condicional Negativo

        

        if(P_b(1) == 1)
            P_b = not(P_b);
            Pitch = bit2int(P_b',16)*(180/32768)*-1
        else
            Pitch = bit2int(P_b',16)*(180/32768)
        end
        
      %Angulo Yaw
        Y_b = double([int2bit( f(20) , 8)',zeros(1,8)] | [zeros(1,8),int2bit( f(19) , 8)']);
    
        %Condicional Negativo

        if(Y_b(1) == 1)
            Y_b = not(Y_b);
            Yaw = bit2int(Y_b',16)*(180/32768)*-1
        else
            Yaw = bit2int(Y_b',16)*(180/32768)
        end

    x = input("Continuar?");
end

clear s
fclose(s)