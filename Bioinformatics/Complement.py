def Complement(Pattern):
    text=""
    for letra in Pattern:
        if letra=="T":
            text+="A"
        if letra=="A":
            text+="T"
        if letra=="G":
            text+="C"
        if letra=="C":
            text+="G"
    return text
print(Complement("AAAACCCGGT"))
