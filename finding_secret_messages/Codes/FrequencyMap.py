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

