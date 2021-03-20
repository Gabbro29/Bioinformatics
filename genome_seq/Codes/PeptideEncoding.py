import os
repo=os.getcwd()
def Reverse(Pattern):
    return Pattern[::-1]

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

def ReverseComplement(Pattern):   
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

def GeneticCode():
    code = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
        "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    return code

def DnaToRna(dnastring):
    return dnastring.replace("T","U")

def Traductor(mRnaSequence):
    peptide=""
    traductiontable=GeneticCode()
    for i in range(0,len(mRnaSequence),3): 
        codon=mRnaSequence[i:i+3]
        if len(codon)==3:
            if traductiontable[codon]!="STOP":
                peptide+=traductiontable[codon]
            else:
                peptide+="*"
    return peptide
## it seems like there is no need to review the three reading frames
def PeptideEncoding(DnaString,peptide):
    lenpep=len(peptide)
    Dna_out=[]
    for i in range(0,len(DnaString)-(lenpep*3)):
        substring=DnaString[i:i+lenpep*3]
        #print(substring)
        if len(substring)==lenpep*3:
            if Traductor(DnaToRna(substring))==peptide or Traductor(DnaToRna(ReverseComplement(substring)))==peptide:
                Dna_out.append(substring)
    return Dna_out

with open(repo+"/genome_seq/inputs/peptideencoding.txt","r") as reader:
    inp=list(map(str.strip,reader.readlines()))
    dna_string=inp[0]
    peptide=inp[1]
    substrings="\n".join(PeptideEncoding(dna_string,peptide))

with open(repo+"/genome_seq/outputs/peptideencoding_solve.txt","w") as writter:
    writter.write(substrings)