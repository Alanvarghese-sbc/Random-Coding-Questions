happy = float(input())
sad = float(input())

for _ in range(4):
    new_happy = 0.5 * sad
    new_sad = 0.7 * happy
    
    happy = new_happy
    sad = new_sad

print("Happy =", round(happy, 2))
print("Sad =", round(sad, 2))
