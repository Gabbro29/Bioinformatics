def HammingDistance(p,q):
    counter=0

    for j in range(len(p)):
        if p[j]!=q[j]:
            counter+=1
    return counter

pe=str(input("Sequence 1:"))
qu=str(input("Sequence 2:"))
print("HammingDistance:",HammingDistance(pe,qu))