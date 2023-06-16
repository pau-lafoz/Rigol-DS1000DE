from rigolds1000de import rigol
from time import sleep

r = rigol.Rigol("usbtmc", idProduct = 1416, idVendor = 6833)

r.stop()
sleep(1)
r.run()
sleep(1)
data = r.getWaveform("CHAN1") 

for b in data:
    print(b)

r.close()
