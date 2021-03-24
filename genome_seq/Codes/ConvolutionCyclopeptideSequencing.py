import os
from collections import defaultdict
from typing import Sequence
repo=os.getcwd()
 ### revisar el codigo
## this code is thanks to guilhermesilveira
pep_mass = {"G": 57,
"A": 71,
"S": 87,
"P": 97,
"V": 99,
"T": 101,
"C": 103,
"I": 113,
"L": 113,
"N": 114,
"D": 115,
"K": 128,
"Q": 128,
"E": 129,
"M": 131,
"H": 137,
"F": 147,
"R": 156,
"Y": 163,
"W": 186}


aminoacidos = "GASPVTCINDKEMHFRYW"
class Peptide:
    def __init__(self, masses:list):
        self.masas=masses
    def largo(self):
        return len(self.masas)
    def masa_total(self):
        return sum(self.masas)
    def append(self,code):
        return Peptide(self.masas+[pep_mass[code]])
    def expand(self,complete_aa=False,convolution=[]):
        if len(convolution)!=0:
            return [Peptide(self.masas+[p])for p in convolution]
        if complete_aa:
            return [Peptide(self.masas + [p]) for p in range(57,201)]
        return [Peptide(self.masas + [pep_mass[p]]) for p in aminoacidos]
    def to_code(self):
        return [pep_mass.get(m, str(m)) for m in self.masas]

    def __str__(self):
        return f"[peptide{self.masas}]"

    def __repr__(self):
        return self.__str__()

    def __lt__(self,other):
        return self.masas<other.masas
    def cyclospectrum(self):
        cycli=self.masas+self.masas
        spectrum=[0]
        for largo_spec in range(1, self.largo()):
            for i in range(0,self.largo()):
                spe=sum(cycli[i:i+largo_spec])
                spectrum.append(spe)
        spectrum.append(self.masa_total())
        return Spectrum(spectrum) ## se genera un objeto spectrum
    def linearspectrum(self):
        spectrum=[0]
        for largo_spec in range(1,self.largo()+1):
            for i in range(0,self.largo()-largo_spec+1):
                spe=sum(self.masas[i:i+largo_spec])
                spectrum.append(spe)
        return Spectrum(spectrum)
class Spectrum:
    def __init__(self, spectrum:list):
        self.spectrum=sorted(spectrum)
        self.masa_spec=max(spectrum)
    def __str__(self):
        return f"[spectrum {self.spectrum.__str__()}]"

    def __repr__(self):
        return self.__str__()

    def expand_peptides(self,candidates_pep,complete_aa=False,convolution=[]):
        candidates_pepti=[peptide.expand(complete_aa=complete_aa,convolution=convolution) for peptide in candidates_pep]
        candidates_pepti=[p for sublist in candidates_pepti for p in sublist]
        return candidates_pepti

    def leaderboardcyclopeptidesequencing(self,n,complete_aa=False,convolution=[]):
        leader=Peptide([])
        candidates=[leader]
        while len(candidates)>0:
            candidates=self.expand_peptides(candidates,complete_aa,convolution)
            leaderboard=Leaderboard(self)
            for pep in candidates:
                if pep.masa_total()==self.masa_spec:
                    if self.score(pep.cyclospectrum())>= self.score(leader.cyclospectrum()):
                        leader=pep
                    leaderboard.add(pep)
                elif pep.masa_total()<self.masa_spec:
                    leaderboard.add(pep)
            candidates=leaderboard.trim(n)
        return leader
    def score(self, comparison_spectrum):
        total=0
        comp_spec=comparison_spectrum.spectrum.copy()
        for mass in self.spectrum:
            if mass in comp_spec:
                comp_spec.remove(mass)
                total+=1
        return total
    def convolution(self):
        convolution_dic=defaultdict(int)
        #print(convolution_list)
        for vertical in self.spectrum:
            for horizontal in self.spectrum:
                #print(vertical-horizontal)
                if vertical-horizontal>0:
                    if convolution_dic[vertical-horizontal]==0:
                        convolution_dic[vertical-horizontal]=1
                    else:
                        convolution_dic[vertical-horizontal]+=1
        return dict(convolution_dic)
    def frequent_in_convolution(self,M):
        #print(self.convolution())
        convol=dict(filter(lambda elem: 57<=int(elem[0])<=200,self.convolution().items()))
        frequencies=sorted(list(([p[1] for p in convol.items()])),reverse=True)
        #print(frequencies)
        limiter=frequencies[M]
        return dict(filter(lambda elem: elem[1]>=limiter, convol.items()))
        #return frequencies
    
class Leaderboard:
    def __init__(self, experimental_spectrum):
        self.board=[] ## this board has the elemnts score and peptides
        self.experimental_spectrum=experimental_spectrum

    def add(self,pep):
        score=pep.linearspectrum().score(self.experimental_spectrum) ##hacer score 👍
        t = (score,pep)
        self.board.append(t)
        return self

    def add_all(self,peptides:list):
        for pep in peptides:
            self.add(pep)
        return self
        
    def trim(self,n:int):
        order=list(reversed(sorted(self.board)))
        trimmed=order[0:n]
        while n<len(order) and order[n][0]==order[n-1][0]: ## viewing ties
            n+=1
            trimmed=order[0:n]
        return [pep for _,pep in trimmed] ## we want only the peptide

if __name__=="__main__":

    with open(repo+"/genome_seq/inputs/convseq.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        M=int(inp[0])
        N=int(inp[1])
        spec=Spectrum(list(map(int,inp[2].split(" "))))
        frequent=[p[0] for p in spec.frequent_in_convolution(M).items()]
        conv_seq=spec.leaderboardcyclopeptidesequencing(N,convolution=frequent).masas
        out="-".join(list(map(str,conv_seq)))
    with open(repo+"/genome_seq/outputs/convseq_solve.txt","w") as writter:
        writter.write(out)
