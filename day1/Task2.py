elfsCalories = 0
caloriesPerElf = []
with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line == '\n':
            caloriesPerElf.append(elfsCalories)
            elfsCalories = 0
        else: 
            calories = int(line)
            elfsCalories += calories
caloriesPerElf.sort(reverse=True)    
indices = [0, 2]     
print(sum(caloriesPerElf[:3]))       