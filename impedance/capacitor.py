import math
class CapacitorImpedance():
    def __init__(self, f, c):
        self.f = f
        self.c = c
    def display(self):
        return (f"Diketahui rangkaian dengan Kapasitansi = {self.c} dan frekuensi {self.f}. berapakah impedansinya?")
    def x(self):
        return f'Impedansi adalah {1/(2*math.pi*self.f*self.c)}'