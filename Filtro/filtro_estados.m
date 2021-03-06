clc 
clear all

load('filtro_conv.mat');

fs = 250; %Frecuencia de muestre de la senal 1kHz
Ts = 1/fs;

% Cargo el filtro
A = [0     0     0     0     0     0     0     0     0     0;
     1     0     0     0     0     0     0     0     0     0;
     0     1     0     0     0     0     0     0     0     0;
     0     0     1     0     0     0     0     0     0     0;
     0     0     0     1     0     0     0     0     0     0;
     0     0     0     0     1     0     0     0     0     0;
     0     0     0     0     0     1     0     0     0     0;
     0     0     0     0     0     0     1     0     0     0;
     0     0     0     0     0     0     0     1     0     0;
     0     0     0     0     0     0     0     0     1     0];
     
B = [1;0;0;0;0;0;0;0;0;0];
C = 1000*[-0.131643055995946  -0.132008742782508  -0.001836274975534   0.187348576956375   0.278006552946558 0.187348576956375  -0.001836274975534  -0.132008742782508  -0.131643055995946  -0.059334149714913];
C = floor(C);
D = -0.059334149714913*1000;
D = floor(D);

%Simulando
delta = Ts; %Periodo de muestreo del sistema

u = ch_1;

t = 0:Ts:(length(t_1)-1)*Ts;

x = zeros(10,1);
x_ = x;

%Algoritmo de Euler 
 for i=1:length(t)        
%         x1 = A*x_+B*U;
%         y1 = C*x_+D*U;
%         Y2(i) = y1;
%         x_ = x1;
%         x1 = 0;

    
    Y(i) = C(1)*x(1) + C(2)*x(2) + C(3)*x(3) + C(4)*x(4) + C(5)*x(5) + C(6)*x(6) + C(7)*x(7) + C(8)*x(8) + C(9)*x(9) + C(10)*x(10) +  D*u(i);     
    
    x(10) = x(9);
    x(9) = x(8);
    x(8) = x(7);
    x(7) = x(6);
    x(6) = x(5);
    x(5) = x(4);
    x(4) = x(3);
    x(3) = x(2);
    x(2) = x(1);
    x(1) = u(i);
   
 end

 figure(1)
 subplot(2,1,1);
 plot(t,Y/max(Y),'b');
 axis([0 1 -1.2 1.2]);
 title('Salida filtrado');
 ylabel('Voltaje[V]');
 xlabel('Tiempo[s]');
 subplot(2,1,2);
 plot(t,ch_1,'r');
 axis([0 1 -1.2 1.2]);
 title('Salida ADC');
 ylabel('Voltaje[V]');
 xlabel('Tiempo[s]');