import thinkdsp
import matplotlib.pyplot as pyplot
import random


pyplot.gcf().clear()
cos_sig = thinkdsp.CosSignal(5,0.6,0)
sin_sig = thinkdsp.SinSignal(15,0.5,0)
sin_sig2 = thinkdsp.SinSignal(25,0.5,0)
sin_sig3 = thinkdsp.SinSignal(35,0.9,0)
for x in range(1,100,1):
    sin_sig3 += thinkdsp.SinSignal(x,random.uniform(0.001,0.11),0)
mix = cos_sig + sin_sig + sin_sig2 + sin_sig3
wave = mix.make_wave(100,0,11025)
print(wave.ys)
wave.plot()
pyplot.show()
period = mix.period
segment = wave.segment(0,3*period)
segment.plot()
spectrum = wave.make_spectrum()
spectrum.plot(high=100)
pyplot.show() 
wave.write(filename='naveed.wav')







#
#pyplot.gcf().clear()
#cos_sig = thinkdsp.CosSignal(5,0.6,0)
#sin_sig = thinkdsp.SinSignal(15,0.5,0)
#sin_sig2 = thinkdsp.SinSignal(25,0.5,0)
#sin_sig3 = thinkdsp.SinSignal(35,0.5,0)
#for x in range(1,100,1):
#    sin_sig3 += thinkdsp.SinSignal(x,random.uniform(0.001,0.11),0)
#mix = cos_sig + sin_sig + sin_sig2 + sin_sig3
#wave = mix.make_wave(1,0,11025)
#wave.plot()
#pyplot.show()
#period = mix.period
#segment = wave.segment(0,3*period)
#segment.plot()
#spectrum = wave.make_spectrum()
#spectrum.plot(high=100)
#pyplot.show() 
#wave.write(filename='naveed.wav')
