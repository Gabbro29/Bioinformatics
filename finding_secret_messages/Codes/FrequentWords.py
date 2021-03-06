def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        #print(Pattern)
        freq[Pattern] = 0
        for elem in range(len(Text)):
            if Text[elem:elem+k]==Pattern:
                freq[Pattern]+=1
    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    print(m)
    for key in freq:
        #print(key)
        #print(freq[key])
        if freq[key]==m:
            words.append(key)
    return words

#print(FrequencyMap("atgaccgggatactgataaaaaaaagggggggggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccg",15))
print(FrequentWords("GTGAAGTTCTCCTTTAAACGAAGCTTTGAAGCTTTCGCCATAGACCTTTAAACCGCCATAGAGTGAAGTTCTGTGAAGTTCTTAACCACCGAAGCTTTCCTTTAAACGTGAAGTTCTCCTTTAAACTAACCACCTAACCACCCGCCATAGATAACCACCCGCCATAGAGTGAAGTTCTGTGAAGTTCTCCTTTAAACCGCCATAGATAACCACCGTGAAGTTCTTAACCACCCCTTTAAACGTGAAGTTCTCGCCATAGACGCCATAGAGAAGCTTTTAACCACCGAAGCTTTTAACCACCGAAGCTTTTAACCACCGAAGCTTTCCTTTAAACCGCCATAGAGAAGCTTTCGCCATAGATAACCACCCCTTTAAACTAACCACCGAAGCTTTTAACCACCGTGAAGTTCTCCTTTAAACCCTTTAAACGAAGCTTTCGCCATAGAGAAGCTTTGAAGCTTTGAAGCTTTGTGAAGTTCTGTGAAGTTCTGAAGCTTTGTGAAGTTCTCGCCATAGAGAAGCTTTGTGAAGTTCTTAACCACCGAAGCTTTCCTTTAAACCGCCATAGAGAAGCTTTTAACCACCGAAGCTTTCGCCATAGAGTGAAGTTCTGAAGCTTTGTGAAGTTCTGTGAAGTTCTGTGAAGTTCTCGCCATAGACGCCATAGAGAAGCTTTCGCCATAGAGAAGCTTTGTGAAGTTCTGAAGCTTTGTGAAGTTCTGTGAAGTTCTCGCCATAGATAACCACCGTGAAGTTCTTAACCACCGAAGCTTTGTGAAGTTCTGAAGCTTTTAACCACCGTGAAGTTCTGTGAAGTTCTTAACCACCTAACCACCCGCCATAGAGTGAAGTTCTGAAGCTTTGAAGCTTTTAACCACCTAACCACCGAAGCTTTTAACCACCCGCCATAGAGTGAAGTTCTCGCCATAGA",12))
