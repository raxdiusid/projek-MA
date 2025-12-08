import math

class Function:
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        self.dx = (b-a)/n

    def x_is_in_range(self, x):
        return self.a <= x <= self.b

class Disk:
    def __init__(self, a, b, scale, f, real_vol):
        self.a = a
        self.b = b
        self.scale = scale
        self.f = f
        self.real_vol = real_vol

        self.acc_vol = 0
        self.volume_each_function = []
        
        for f in self.f:
            f.a *= self.scale
            f.b *= self.scale
            f.dx = (f.b-f.a)/f.n

        self.run()

    def run(self):
        for f in self.f:
            vol = 0
            for i in range(f.n):
                xi = f.a + i*f.dx
                vol += math.pi * (self.scale*(f.f(xi/self.scale)))**2 * f.dx
            self.volume_each_function.append(vol)
        self.acc_vol = sum(self.volume_each_function)
                
        print("="*5)
        print(f"Scale: {self.scale}")
        print(f"Volume asli: {self.real_vol} mL")
        print(f"Volume integral: {self.acc_vol} mL")
        print(f"Galat: {(abs(self.real_vol-self.acc_vol)/self.real_vol)*100}%")
                    

# for i in range(1):
#     disk = Disk(0, 19.5, 10*(i+1), [
#         Function(lambda x: 1/math.sqrt(3) * math.sqrt(x) + 2.5, 0, 3),
#         Function(lambda x: 4/49 * x**2 - 52/49 * x + 583/98, 3, 10),
#         Function(lambda x: 3.5, 10, 11.5),
#         Function(lambda x: -0.28125*x+6.734375, 11.5, 19.5)
#     ], 350)

for i in range(1, 11):
    j = i/10
    disk = Disk(0, 19.5, j, [
            Function(lambda x: 1/math.sqrt(3) * math.sqrt(x) + 2.5, 0, 3, 100),
            Function(lambda x: 4/49 * x**2 - 52/49 * x + 583/98, 3, 10, 100),
            Function(lambda x: 3.5, 10, 11.5, 100),
            Function(lambda x: -0.28125*x + 6.734375, 11.5, 19.5, 100)
        ], 350)