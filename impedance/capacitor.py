from impedance.rumus_x import Xrumus
import math

class CapacitorImpedance(Xrumus):
    def __init__(self, f,  c):
        super().__init__(f)
        self.c = c
    def display(self):
        return (f"Diketahui rangkaian dengan Kapasitansi = {self.c} dan frekuensi {self.f}. berapakah impedansinya?")
    def x(self):
        return f'Impedansi adalah {1/(2*math.pi*self.f*self.c)}'