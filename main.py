import math

class Function:
    def __init__(self, f, a, b):
        self.f = f
        self.a = a
        self.b = b

    def x_is_in_range(self, x):
        return self.a <= x <= self.b

class Disk:
    def __init__(self, a, b, n, f, real_vol):
        self.a = a
        self.b = b
        self.n = n
        self.dx = (b-a)/n
        self.f = f
        self.real_vol = real_vol

        self.acc_vol = 0

        self.run()

    def run(self):
        for i in range(self.n):
            xi = self.a + i*self.dx
            for f in self.f:
                if not f.x_is_in_range(xi):
                    continue
                print(f"x_{i} = {xi} | f({xi}) = {f.f(xi)}")
                self.acc_vol += math.pi*(f.f(xi))**2 * self.dx
                break
        print("="*5)
        print(f"n: {self.n}")
        print(f"dx: {self.dx}")
        print(f"Volume asli: {self.real_vol} mL")
        print(f"Volume integral: {self.acc_vol} mL")
        print(f"Galat: {(abs(self.real_vol-self.acc_vol)/self.real_vol)*100}%")
                    

for i in range(6):
    disk = Disk(0, 19.5, 10*(i+1), [
        Function(lambda x: 1/math.sqrt(3) * math.sqrt(x) + 2.5, 0, 3),
        Function(lambda x: 4/49 * x**2 - 52/49 * x + 583/98, 3, 10),
        Function(lambda x: 3.5, 10, 11.5),
        Function(lambda x: -0.28125*x+6.734375, 11.5, 19.5)
    ], 350)