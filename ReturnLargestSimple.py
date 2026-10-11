names = ["anna", "gorge", "frank", "frank", "anna", "jogn"]

counts = {}

for name in names:
    counts[name] = counts.get(name, 0) + 1
    
print(counts)
    