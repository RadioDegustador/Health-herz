#include "ch.h"
#include "hal.h"
#include "test.h"
#include "chprintf.h"
#include "atmel_adc.h"  //Libreria ADC atmel_adc.c en ChibiOS
#include "pio.h"
#include "pmc.h"
#include "board.h"
#include "stddef.h"


#define PLL_A            0           /* PLL A */
#define PLL_B            1           /* PLL B */
#define ELEMENT_COUNT(X) (sizeof(X) / sizeof((X)[0]))

/** Pin PCK2 (PA31 Peripheral B) */
const Pin pinPCK[] = PIN_PCK2;  

static WORKING_AREA(waThread1, 128);
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


//Kernel es la respuesta al impulso del filtro
void convolve (const double Signal[/* SignalLen */], size_t SignalLen,const double Kernel[/* KernelLen */], size_t KernelLen,double Result[/* SignalLen + KernelLen - 1 */])
{
  size_t n;

  for (n = 0; n < SignalLen + KernelLen - 1; n++)
  {
    size_t kmin, kmax, k;

    Result[n] = 0;

    kmin = (n >= KernelLen - 1) ? n - (KernelLen - 1) : 0; //Desplaza el valor minimo con lo que desplaza el arreglo Kernel
    kmax = (n < SignalLen - 1) ? n : SignalLen - 1; //Desplaza el valor máximo hasta donde debe ir Signal para terminar la convolución

    for (k = kmin; k <= kmax; k++)
    {
      Result[n] += Signal[k] * Kernel[n - k];
    }
  }
};

/*h es la respuesta al impulso del filtro con fs = 250Hz*/
double h [] = {-0.0593341497149129 ,-0.131643055995946, -0.132008742782508, -0.00183627497553400, 0.187348576956375, 0.278006552946558, 0.187348576956375, -0.00183627497553400, -0.132008742782508, -0.131643055995946, -0.0593341497149129};


/*
 * Application entry point.
 */
int main(void) {
   double ADC_Val[1000]; //tiene que ser un entero

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
   ADC_cfgFrequency( ADC, 15, 95999 ); /*//ADC_cfgFrequency( Adc* pAdc, uint32_t startup, uint32_t prescal )
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
    while( !(ADC->ADC_ISR & ADC_ISR_EOC0));//Cuando hay interrupción "ADC_ISR" este while vuelve a while(true)
    for (int i= 0;i<1000; i ++){
    	chThdSleepMilliseconds(500);  /*cada 500 milisegundos hago el procedimiento de tomar todos los valores ADC_DCR y alojarlos en cada //
    	espacio de ADC_Val[]*/    
      	ADC_Val[i] = ADC->ADC_CDR[0]; //ADC_CDR registro que lee el ADC, existen hasta 14 registros	
    	chprintf((BaseChannel *)&SD2, "%d \r\n", ADC_Val[i]*3300/4096) ;
    };
    
    
    chThdSleepMilliseconds(1000);
    double  salida[ELEMENT_COUNT(ADC_Val)+ELEMENT_COUNT(h)-1];
   
    convolve(ADC_Val,ELEMENT_COUNT(ADC_Val),h,ELEMENT_COUNT(h),salida);// Si no sirve comentar esa línea
   }
   
   
   return(0);
}
