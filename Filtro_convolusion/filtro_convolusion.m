clc
clear all

load('.\filtro_conv.mat');

fs = 250; %Frecuencia de muestreo
%Para poder utilziar este filtro se necesita que la se�al de entrada

%TF del filtro
filter = filt(FIRbp.tf.num,FIRbp.tf.den,1/fs);

%Generador de la respuesta al impulso del filtro
% impz(num,den,n de puntos,fs)
% [h t] = impz(FIRbp.tf.num,FIRbp.tf.den,20,250);

%Respues al impulso Filtro FIR con frecuencia de corte en 40Hz y frecuencia
% de muestreo fs = 250;
h = [-0.0593341497149129 -0.131643055995946 -0.132008742782508 -0.00183627497553400 0.187348576956375 0.278006552946558 0.187348576956375 -0.00183627497553400 -0.132008742782508 -0.131643055995946 -0.0593341497149129 0 0 0 0 0 0 0 0 0];

