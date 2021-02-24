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


prof={'A': [0.4 , 0.3 , 0.0 , 0.1 , 0.0 , 0.9], 'C': [0.2 , 0.3 , 0.0  ,0.4 , 0.0 , 0.1], 'G': [ 0.1 , 0.3 , 1.0  ,0.1 , 0.5 , 0.0], 'T': [0.3 , 0.1 , 0.0 , 0.4 , 0.5 , 0.0]}

text='TCGGTA'

print(Pr(text,prof))