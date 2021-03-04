import os
repo=os.getcwd()
def UnGrapper(kdmers):
    list_kdmers=[pair.split("|") for pair in kdmers]
    return list_kdmers

def StringSpelledByPatterns(patterns):
    string=""
    k=len(patterns[0])
    for elem in patterns:
        if string=="":
            string+=elem
        else:
            string+=elem[k-1]
    return string
def PrefixSuffixConcatenation(k,d,Prefix,Suffix):
    concatenation=Prefix+Suffix[len(Suffix)-(k+d):len(Suffix)]
    return concatenation

def StringSpelledByGrappedGenomePath(k,d,kdmers):
    li_pairs=UnGrapper(kdmers)
    FirstPatterns=[par[0] for par in li_pairs]
    SecondPatterns=[par[1] for par in li_pairs]
    PrefixString=StringSpelledByPatterns(FirstPatterns)
    SuffixString=StringSpelledByPatterns(SecondPatterns)
    for i in range(1+k+d,len(PrefixString)):
        if PrefixString[i] != SuffixString[i-k-d]:
            return ("there is no string spelled by the gapped patterns")
    return PrefixSuffixConcatenation(k,d,PrefixString,SuffixString)

#print(StringSpelledByGrappedGenomePath(2,1,["AG|AG","GC|GC","CA|CT","AG|TG","GC|GC","CT|CT","TG|TG","GC|GC","CT|CA"]))

with open(repo+"/genome_seq/inputs/grappedgenome.txt","r") as reader:
    grapped=list(map(str.strip,reader.readlines()))
    k,d=grapped[0].split(" ")
    kdmers=grapped[1:]
    out=StringSpelledByGrappedGenomePath(int(k),int(d),kdmers)
    
with open(repo+"/genome_seq/outputs/grappedgenome_solve.txt","w") as writter:
    writter.write(out)
