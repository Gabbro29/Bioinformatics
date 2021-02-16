import random
def WeightedDie(Probabilities):
    P=Probabilities
    n=random.uniform(0,1)
    #print(Probabilities.items())
    for p,v in Probabilities.items():
        n-=v
        if n<=0:
            return(p)
prob={'AC': 0.1, 'GC': 0.2, 'TA': 0.4, 'CA': 0.1, 'GT': 0.2}
print(WeightedDie(prob))
