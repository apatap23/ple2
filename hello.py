healthy = ["kale chips", "broccoli"]
backpack = ["pizza", "broccoli","frozen custard", "apple crisp", "kale chips"]

backpack[:]= [item for item in backpack if item in healthy]
print(backpack)


def __iter__(self):
    cursor = 0
    while cursor < len(self):
        yield self._items [(self._front + cursor) % len(self._items)]
        cursor += 1 

        