import math
from impedance.rumus_x import Xrumus

class InductorImpedance(Xrumus):
    def __init__(self, f, l):
        super().__init__(f)
        self.l = l
    def display(self):
        return (f"Diketahui rangkaian dengan Induktansi = {self.l} dan frekuensi {self.f}. berapakah impedansinya?")
    def x(self):
        return f'Impedansi adalah {(2 * math.pi * self.f * self.l)}'