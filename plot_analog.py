from machine import Pin, ADC, I2C
from time import sleep
import ssd1306


y_p = 0

class AnalogP():
    
    '''
    Esta clase es un objeto al que posteriormente se le aplica el metodo plot,
    y permite dibujar en una pantalla oled un gráfico líneal de la entrada analógica
    de un ESP32, tambien muestra en pantalla el valor máximo registrado y el promedio
    de los datos
    '''
    
    def __init__(self, analog_pin, X=128, screen_y=64, i2c_scl=4, i2c_sda=5):
        
        '''
        Esta variables inicializan la pantalla
        
        Parameters
        ----------
        analog_pin : TYPE int
            DESCRIPTION. este corresponde al pin de entrada analogíca que queremos graficar
        x : TYPE int
            DESCRIPTION. ancho de la pantalla oled
        screen_y : TYPE int
            DESCRIPTION. indica la altura d la pantalla oled
        i2c_scl : TYPE int
            DESCRIPTION. pin scl de la pantalla oled
        i2c_sda : TYPE int
            DESCRIPTION. pin sda de la pantalla oled
        '''
  
        self.analog_pin = analog_pin
        self.X = X
        self.screen_y = screen_y
        self.i2c_scl = i2c_scl
        self.i2c_sda = i2c_sda
        
        self.pot = ADC(Pin(analog_pin))
        self.pot.atten(ADC.ATTN_11DB)                       

        self.i2c = I2C(-1, scl=Pin(i2c_scl), sda=Pin(i2c_sda))          
        self.oled = ssd1306.SSD1306_I2C(X, screen_y, self.i2c)
        
        self.x_p = 0
        self.y_n = []
        
    def plot(self, Y=54, seq=4, delay=0.4, scale=2500):
        
        '''
        Esta variables controlan la grafica
        
        Parameters
        ----------
        y : TYPE int
            DESCRIPTION. esta es el alto que se utiliza para la grafica, la diferencia con
                        screen_y es el ancho de la franja blanca de la pantalla
        seq : TYPE int
            DESCRIPTION. el numero de pixeles en x que forman la línes recta de la grafica
        delay : TYPE int
            DESCRIPTION. tiempo en segundos entre lectura de la entrada analógica, entre mas
                        pequeño mas rápido el tiempo de la grafica
        scale : TYPE int
            DESCRIPTION. es el factor de escala para acomodar el eje y en la pantalla con el
                        valor que el sensor esta entregando por la entrada analogica
        '''
        
        global y_p
        self.Y = Y
        self.seq = seq
        self.delay = delay
        
        Y = self.Y
        seq = self.seq
        delay = self.delay
        oled = self.oled
        y_n = self.y_n
        x_p = self.x_p
        
        x_n = list(range(0, self.X, self.seq))
        
        if len(y_n) > 0:
            oled.text('MEAN:', 2, 10, 1)
            oled.text(str(round(sum(y_n) / len(y_n), 2)), 49, 10, 1)
            oled.show()
            sleep(2)
        oled.fill(0)
        oled.fill_rect(0, 55, 127, 63, 1)
        oled.text('MAX:', 0, 56, 0)
        oled.text('#:', 56, 56, 0)
        oled.show() 
        for x in x_n:
            if x <= self.X:
                y_temp = self.pot.read()
                y_n.append(int((y_temp * self.Y) / 2500))
                if not x_p == 0:
                    oled.line(x_n[x_p - 1], Y - y_n[y_p - 1],
                              x_n[x_p], Y - y_n[y_p],
                              1)
                    oled.fill_rect(28, 56, 28, 64, 1)
                    oled.text(str(max(y_n)), 33, 56, 0)
                    oled.fill_rect(76, 56, 124, 64, 1)
                    oled.text(str(len(y_n)), 76, 56, 0)
                oled.show()
                sleep(self.delay)
                x_p += 1
                y_p += 1
            else:
                x_p = 0
            
            