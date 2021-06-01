import plot_analog

plot_data = plot_analog.AnalogP(analog_pin=36, # pin analogo
                                X=128, # ancho de la pantalla
                                screen_y=64, # alto de la pantalla
                                i2c_scl=4, # pin scl de la pantalla oled
                                i2c_sda=5) # pin sda pantalla oled

while True:    
    plot_data.plot(Y=54, # este es el ancho util de la pantala para el plot la diferencia es la franja blanca inferior
                   seq=4, # cada cuantos puntos den x se traza una linea
                   delay=0.1, # tiempo de muestreo en segundos
                   scale=2500) # ajuste de escala entre la señasl del sensor y la pantalla
