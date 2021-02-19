healthy = ["kale chips", "broccoli"]
backpack = ["pizza", "broccoli","frozen custard", "apple crisp", "kale chips"]

backpack[:]= [item for item in backpack if item in healthy]
print(backpack)