clc 
clear 

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
C = [-0.131643055995946  -0.132008742782508  -0.001836274975534   0.187348576956375   0.278006552946558 0.187348576956375  -0.001836274975534  -0.132008742782508  -0.131643055995946  -0.059334149714913];
D = [-0.059334149714913];
% load('ssModel.mat');

%Simulando
delta = Ts; %Periodo de muestreo del sistema

U = 1;

t = 0:Ts:(length(t_1)-1)*Ts;

I = eye(10);
Ab = I+delta*A;
Bb = delta*B;
X = zeros(10,1);

% Y1 = zeros(1,length(t)); 

% U= %entrada

%Algoritmo de Euler 
 for i=1:length(t)
%         x(1) = Ab(1,1)*x(1)+Ab(1,2)*x(2)+Ab(1,3)*x(3)+Ab(1,4)*x(4)+A(1,5)*x(5)+A(1,6)*x(6)+A(1,7)*x(7)+A(1,8)*x(8)+A(1,9)*x(9)+A(1,10)*x(10)+B(1)*U(n);
%         x(2) = Ab(2,1)*x(1);
%         x(3) = Ab(3,2)*x(2);
%         x(4) = Ab(4,3)*x(3);
%         x(5) = Ab(5,4)*x(4);
%         x(6) = Ab(6,5)*x(5);
%         x(7) = Ab(7,6)*x(6);
%         x(8) = Ab(8,7)*x(7);
%         x(9) = Ab(9,8)*x(8);
%         x(10) =Ab(10,9)*x(9); 
%         y1 = C(1)*x(1)+C(2)*x(2)+C(3)*x(3)+C(4)*x(4)+C(5)*x(5)+C(6)*x(6)+C(7)*x(7)+C(8)*x(8)+C(9)*x(9)+C(10)*x(10) + D*U(n);
%                 
%         Y1(n)=y1; %Salida
Xa(:,1) = X(:,i);

Xt = Ab*Xa + Bb*U;
Yt = C*Xa + D*U(i);

Y(:,i) = Yt(:,1);
X(:,i+1) = Xt(:,1);
 end
 

 figure(1)
 plot(t,Y);