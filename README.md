# plot_oled_esp32
Este repositorio contiene la liberia plot_analog que permite hacer una gráfica de linea en una pantalla oled de un microcontrolador ESP32, tomando los datos de la  entrada analógica del ESP32, también muestra el valor máximo, el numero de muestras de los datos y cuando se refresca muestra el promedio de las mediciones realizadas.

La idea es poder utilizar estos microcontroladores de bajo costo y poder calibrar o simplemente visualizar los datos integrándolos fácilmente en nuestros proyectos.

## IDE utilizado
Esta librería esta escrita en mycropython, se utilizó el IDE https://thonny.org/blog/2018/06/05/thonny_and_micropython.html
es posible que el código funcione para ESP32, ESP8266 y Raspberry Pi Pico solo cambiando la configuración de la pantalla

## Hardware utilizado
Se utilizó un ESP32 con la pantalla oled integrada este se puede conseguir en https://n9.cl/94yld, sugiero ver documentación del hardware utilizado

## Ejemplo de uso
Se puede apreciar un ejemplo de uso en el archivo test_analog_plot.py, para utilizar este código simplemente se requieren guardar los archivos en la memoria del microcontrolador se sugiere ver: https://www.profetolocka.com.ar/2020/10/03/programando-el-esp8266-en-micro-python/


## Video de muestra
https://youtu.be/8Ge0Bbb2jqE