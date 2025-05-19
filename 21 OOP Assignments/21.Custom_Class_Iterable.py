class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        x = self.start
        self.start -= 1
        return x
    
for num in Countdown(10):
    print(num)
