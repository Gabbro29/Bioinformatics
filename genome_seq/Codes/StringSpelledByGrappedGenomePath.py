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

def StringSpelledByGrappedGenomePath(k,d,kdmers):
    li_pairs=UnGrapper(kdmers)
    FirstPatterns=[par[0] for par in li_pairs]
    SecondPatterns=[par[1] for par in li_pairs]
    FirstString=StringSpelledByPatterns(FirstPatterns)
    SecondString=StringSpelledByPatterns(SecondPatterns)
    return FirstString,SecondString

k=4
d=2
kdmers=["AG|AG","GC|GC","CA|CT","AG|TG","GC|GC","CT|CT","TG|TG","GC|GC","CT|CA"]
print(StringSpelledByGrappedGenomePath(k,d,kdmers))