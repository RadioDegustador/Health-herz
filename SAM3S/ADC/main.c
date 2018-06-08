#include "ch.h"
#include "hal.h"
#include "test.h"
#include "chprintf.h"
#include "atmel_adc.h"  //Libreria ADC atmel_adc.c en ChibiOS
#include "pio.h"
#include "pmc.h"
#include "board.h"
#include "stddef.h"
#include "math.h"


#define PLL_A            0           /* PLL A */
#define PLL_B            1           /* PLL B */
#define ELEMENT_COUNT(X) (sizeof(X) / sizeof((X)[0])) //Saca el tamaño de un vector

/** Pin PCK2 (PA31 Peripheral B) */
const Pin pinPCK[] = PIN_PCK2;  

static WORKING_AREA(waThread1, 1024);//aumentar el tamaño a 1024 o 65536
static msg_t Thread1(void *arg) {
  (void)arg;
  while (TRUE) {
    palClearPad(IOPORT3, 17);
    chThdSleepMilliseconds(50);
    palSetPad(IOPORT3, 17);
    chThdSleepMilliseconds(50);
  }
  return(0);
}


/*
 * Application entry point.
 */
int main(void) {
   int ADC_Val; //tiene que ser un entero
   int x1=0, x2=0,x3=0 ,x4= 0,x5=0,x6=0,x7=0,x8=0,x9=0,x10=0,y=0;
   //int i = 0;
   //int max = 12;
   //int Y[max];
   halInit();
   chSysInit();
   sdStart(&SD2, NULL);  /* Activates the serial driver 2 sdStart(SerialDriver *sdp, const SerialConfig *config) de la libreria Serial	*/
   /*Baud rate por defecto del serial 115200*/
   
   // Configure PCK2 as FPGA clock

   PIO_Configure(pinPCK, 1);
   PmcConfigurePllClock( PLL_A, (32 - 1), 3  ) ;
   /* If a new value for CSS field corresponds to PLL Clock, Program the PRES field first*/
   PmcMasterClockSelection( PMC_MCKR_CSS_MAIN_CLK, PMC_MCKR_PRES_CLK_2);
   /* Then program the CSS field. */
   PmcMasterClockSelection( PMC_MCKR_CSS_PLLA_CLK, PMC_MCKR_PRES_CLK_2 ) ;
   ConfigurePck( PMC_PCK_CSS_PLLA_CLK, PMC_PCK_PRES_CLK_2 ) ;
 
   /* ADC configuration*/
   ADC_Initialize( ADC);
   /* startup = 15:    640 periods of ADCClock
    * for prescal = 11
    *     prescal: ADCClock = MCK / ( (PRESCAL+1) * 2 ) => 48MHz / ((11+1)*2) = 2MHz
    *     ADC clock = 2 MHz
    */
   ADC_cfgFrequency( ADC, 15, 95999); /*//ADC_cfgFrequency( Adc* pAdc, uint32_t startup, uint32_t prescal )
                                    //startup =  ciclos de reloj que cuenta el ADC antes de inicial 15 = 960 periodos de Clk ADC
                                   // prescal = 11, divide la velocidad del clk externo para obtener el valor de adc_freq = mck_freq / 					   ((prescal+1)*2) */
                                    // freqADC = 2Mhz para pescal = 11 y clk_ext = 48MHz
   ADC_check( ADC, 48000000 ); // Board Clock 48000000 ADC_check( Adc* pAdc, uint32_t mck_freq )
                                    //mck_freq=  frecuencia de la placa, adc_freq = mck_freq / ((prescal+1)*2);
   ADC->ADC_CHER = 0x00000033;  // Enable Channels 0, 1, 4, 5 //pines de entrada del ADC "llamados AD"
   ADC->ADC_MR |= 0x80; //Encender el Adc "leer el datasheet" 
   ADC_StartConversion(ADC); /* Start conversion */

   /* Creates the blinker thread. */
   chThdCreateStatic(waThread1, sizeof(waThread1), NORMALPRIO, Thread1, NULL);

   while (TRUE) {
    while( !(ADC->ADC_ISR & ADC_ISR_EOC0));//Este While revisa que no halla una interrupción, de existir vuelve a iniciar el ciclo While(TRUE)

    	chThdSleepMilliseconds(4);  /*cada 50 milisegundos hago el procedimiento de tomar todos los valores ADC_DCR y alojarlos en cada
    	espacio de ADC_Val[]*/    
      	ADC_Val = ADC->ADC_CDR[0]; //ADC_CDR registro que lee el ADC, existen hasta 14 
    	//chprintf((BaseChannel *)&SD2, "%d \r\n", ADC_Val[i]*3300/4096);
    	
//Falta arreglar el valor de ADC_Val, multiplicando por 33000/4096, para trabajar desde un principio con los valores de tensión reales
    	
    	
    	y = 91*x1-37*x2-290*x3+22*x4+387*x5+22*x6-290*x7-37*x8+91*x9+3*x10+3*ADC_Val*3300/4096;
    	
    	x10 = x9;
    	x9  = x8;
    	x8  = x9;
    	x7  = x6;
    	x6  = x5;	
    	x5  = x4;
    	x4  = x3;
    	x3  = x2;
    	x2  = x1;
    	x1  = ADC_Val*3300/4096;
    	
    	chprintf((BaseChannel *)&SD2, "%d \r\n",y);
    	
/*    	i = i + 1; 	
 	if(i>max) {
 	chprintf((BaseChannel *)&SD2, "%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d \r\n",Y[0],Y[1],Y[2],Y[3],Y[4],Y[5],Y[6],Y[7],Y[8],Y[9],Y[10],Y[11]);
 	i = 0;
 	} else {
 	Y[i-1] = y;
 	}   */
   };
   
   return(0);
}
