class EvenRange:
    
    def __init__(self, min_val, max_val):
        self.max_val = max_val
        self.min_val = min_val
        self.num = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.min_val <= self.max_val:
            self.num += 1
            self.min_val += 1
            if self.num % 2 == 0:
                return self.num
        print("Out of numbers")

n = EvenRange(1, 6)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
