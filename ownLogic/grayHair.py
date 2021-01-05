hairPulled = ["brown","gray","brown", "brown","gray","brown","brown","gray","brown", "brown","gray","brown"]
count= 0
for color in hairPulled:
    if color == "gray":
        count+= 1
    
print(f"found {count} gray hairs")   
