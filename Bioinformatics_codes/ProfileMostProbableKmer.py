import os
repo=os.getcwd()
def Pr(Text, Profile):
    pro=1
    for col in range(len(Profile['A'])):
        if Text[col]=='A':
            pro=pro*Profile['A'][col]
        elif Text[col]=='C':
            pro=pro*Profile['C'][col]
        elif Text[col]=='G':
            pro=pro*Profile['G'][col]
        elif Text[col]=='T':
            pro=pro*Profile['T'][col]
    return pro

def ProfileMostProbableKmer(text, k , profile):
    pro_max=-1
    k_mer_max=''
    for i in range(len(text)):
        k_mer=text[i:i+k]
        if len(k_mer)==k:
            if Pr(k_mer, profile)>pro_max :
                pro_max=Pr(k_mer,profile)
                k_mer_max=k_mer
    return k_mer_max

text='ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
k=5
profile={'A': [0.2, 0.2, 0.3,0.2,0.3], 'C': [0.4,0.3,0.1,0.5,0.1], 'G': [0.3,0.3,0.5,0.2,0.4], 'T':[0.1,0.2,0.1,0.1,0.2]}

r=open(repo+"/texts/profilekmer.txt","r")
profilekmer=r.readlines()
r.close()
for i in range(len(profilekmer)):
    profilekmer[i]=profilekmer[i].strip()

text=profilekmer[0]
k=int(profilekmer[1])
profile={"A":list(map(float,profilekmer[2].split(" "))),"C":list(map(float,profilekmer[3].split(" "))),"G":list(map(float,profilekmer[4].split(" "))),"T":list(map(float,profilekmer[5].split(" ")))}

print(ProfileMostProbableKmer(text,k,profile))
