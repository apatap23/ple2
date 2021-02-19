healthy = ["kale chips", "broccoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]


for i in backpack: 
    if backpack[i] not in healthy:
        backpack[i].remove