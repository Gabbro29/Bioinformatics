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

text='AACCGGTT'
k=3
profile={'A': [1.0, 1.0, 1.0], 'C': [0.0, 0.0, 0.0,], 'G': [0.0, 0.0, 0.0,], 'T': [0.0, 0.0, 0.0,]}

print(ProfileMostProbableKmer(text,k,profile))
