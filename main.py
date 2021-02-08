from impedance.capacitor import CapacitorImpedance
from impedance.inductor import InductorImpedance

xc = CapacitorImpedance(50, 22)
xl = InductorImpedance(60, 100)

print(xc.display())
print(xc.x())

print(xl.display())
print(xl.x())
