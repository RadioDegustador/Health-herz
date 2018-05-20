clc 
clear 

fs = 1e3; %Frecuencia de muestre de la señal 1kHz
fc = 200; %Frecuencia de corte 
wn = fc/(fs/2);
n = 6; %Orden del denominador
m = 6; %orden del numerador

[b,a] = maxflat(n,m,wn); % diseño de filtro IIR butterworth 
% fvtool(b,a)
% [A,B,D,C] = tf2ss(b,a) %SS del filtro


A = [1.1876   -1.3052    0.6743   -0.2635    0.0518   -0.0050;
    1.0000         0         0         0         0         0;
         0    1.0000         0         0         0         0;
         0         0    1.0000         0         0         0;
         0         0         0    1.0000         0         0;
         0         0         0         0    1.0000         0];
     
B = [1;0;0;0;0;0];
C = 0.0103;
D = [0.0741    0.1412    0.2132    0.1520    0.0624    0.0103];

delta = 1/fs; %Periodo de muestreo del sistema

t = 0:1/fs:fs*(1/fs)

I = eye(6)

Ab = I+delta*A;
Bb = delta*B;



Y1 = zeros(1,length(t)); 

Y2 = zeros(1,length(t));


%%Algoritmo de Euler "falta hacerlo bien"
 for n=1:length(t)
        x1 = Ab(1,1)*x1+Ab(1,2)*x2;
        x2 = Ab(2,1)*x1+Ab(2,2)*x2+Ab(2,3)*x3+Ab(2,4)*x4;
        x3 = Ab(3,3)*x3+Ab(3,4)*x4;
        x4 = Ab(4,1)*x1+Ab(4,2)*x2+Ab(4,3)*x3+Ab(4,4)*x4+Ab(4,5)*x5+Bb(4,1)*fuerza;
        x5 = Ab(5,5)*x5+Ab(5,6)*x6;
        x6 = Ab(6,3)*x3+Ab(6,5)*x5+Ab(6,6)*x6;
        y1 = x1;
                
        Y1(1,n)=y1; %Salida
 end
 
 
 
