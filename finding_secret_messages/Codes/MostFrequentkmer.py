def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

def MostFrequentKmer(Text,k):
    kmer_fin=""
    counter=0
    for i in range(0,len(Text),k):
        if i+k<len(Text):
            kmer=Text[i:i+k]    
            num=PatternCount(Text,kmer)
            if num>counter:
                counter=num
                kmer_fin=kmer
    return kmer_fin
print(MostFrequentKmer("TCTCGCATACCCGCTATCTGGATTGACGGATTGACCCCGCTATCTGGATTGACCTCAGCTAGCCCGCTATCTCCCGCTATCTCTCAGCTAGCTCAGCTAGCTCAGCTAGCCCGCTATCTCTCAGCTAGCCCGCTATCTCTCAGCTAGGGATTGACGGATTGACCTCAGCTAGTCTCGCATATCTCGCATAGGATTGACCCCGCTATCTCTCAGCTAGCCCGCTATCTTACCATATATTACCATATATCCCGCTATCTTCTCGCATACCCGCTATCTGGATTGACCTCAGCTAGTACCATATATGGATTGACTCTCGCATACTCAGCTAGGGATTGACGGATTGACTACCATATATTACCATATATCTCAGCTAGCTCAGCTAGCTCAGCTAGTCTCGCATACCCGCTATCTCTCAGCTAGTCTCGCATATACCATATATGGATTGACGGATTGACCTCAGCTAGGGATTGACCTCAGCTAGCTCAGCTAGGGATTGACGGATTGACTACCATATATCTCAGCTAGTCTCGCATAGGATTGACTACCATATATGGATTGACCTCAGCTAGTACCATATATGGATTGACTACCATATATTACCATATATCTCAGCTAGGGATTGACTCTCGCATATCTCGCATATCTCGCATACTCAGCTAGTACCATATATCCCGCTATCTTCTCGCATAGGATTGACCCCGCTATCTGGATTGACTCTCGCATACCCGCTATCTCCCGCTATCTGGATTGACTCTCGCATATCTCGCATACCCGCTATCTGGATTGACCTCAGCTAGCTCAGCTAGGGATTGACCCCGCTATCTCTCAGCTAGGGATTGACTCTCGCATACTCAGCTAGCCCGCTATCTGGATTGACTACCATATATTCTCGCATA",12))

