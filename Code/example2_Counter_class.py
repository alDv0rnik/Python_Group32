"""
Create Counter Class with two methods - inc, reset
count
"""


class Counter:
    def __init__(self, count):
        self.count = count

    def inc(self, n=1):
        self.count += n

    def reset(self):
        self.count = 0


counter = Counter(2)
counter.inc(3)
print(counter.count)
counter.reset()
print(counter.count)