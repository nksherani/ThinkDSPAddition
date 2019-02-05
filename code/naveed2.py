import thinkdsp
import matplotlib.pyplot as pyplot


pyplot.gcf().clear()

cos_sig = thinkdsp.SinSignal(440,1,0)
sin_sig = thinkdsp.SinSignal(880,1,0)


mix = cos_sig + sin_sig
wave = mix.make_wave(100,0,11025)
print(wave.ys[0])
print(wave.ys[1])
print(wave.ys[2])
print(wave.ys[3])
print(wave.ys[4])
print(wave.ys[5])
print(wave.ys[6])
print(wave.ys[7])
wave.plot()
pyplot.show()
period = mix.period
segment = wave.segment(0,3*period)
segment.plot()

