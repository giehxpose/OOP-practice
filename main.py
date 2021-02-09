from impedance.capacitor import CapacitorImpedance
from impedance.inductor import InductorImpedance
from impedance.rumus_x import Xrumus

xc = CapacitorImpedance(50, 22)
xl = InductorImpedance(50, 100)

print(xc.display())
print(xc.x())

print(xl.display())
print(xl.x())

xt = Xrumus(50)
print(xt.rumus())