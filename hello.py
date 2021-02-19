healthy = ["kale chips", "broccoli"]
backpack = ["pizza", "broccoli","frozen_custard", "apple_crisp", "kale chips"]

print(backpack)

for i in backpack: 
    if i not in healthy:
        backpack.remove(i)

print(healthy)
print(backpack)