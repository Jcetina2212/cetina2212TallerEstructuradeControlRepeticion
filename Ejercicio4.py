c=0
sumatoria=0
for i in range(6,70,5):
    c+=1
    if(c==13):
        break
    sumatoria+=i
    print(i)
print(f"La sumatoria es:{sumatoria}")