class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
    
m = Multiplier(12)
print(callable(m))

result = m(10)
print(result)