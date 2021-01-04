def SkewArray(Genome):
    Skew={}
    for i in range(len(Genome)):
        if i == 0:
            Skew[0]=0
        if Genome[i]=="A" or Genome[i]=="T":
            Skew[i+1]= Skew[i]
        if Genome[i]=="G":
            Skew[i+1]=Skew[i]+1
        if Genome[i]=="C":
            Skew[i+1]=Skew[i]-1
    ske=[]
    for i in range(len(Skew)):
        ske.append(Skew[i])
    return ske
print(SkewArray("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"))