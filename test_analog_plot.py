import plot_analog

plot_data = plot_analog.AnalogP(analog_pin=36)

while True:    
    plot_data.plot(delay=0.1)
