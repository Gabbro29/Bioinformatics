import os

repo=os.getcwd()
 ### revisar el codigo
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
    def __init__(self, code:str):
        self.code=code
    def largo(self):
        return len(self.code)
    def masa_total(self):
        return sum([pep_mass[c] for c in self.code])
    def append(self,code):
        return Peptide(self.code+code)
    def expand(self):
        return [Peptide(self.code+p) for p in aminoacidos]
    def __str__(self):
        return f"[peptide{self.code}]"
    def masas(self):
        return [pep_mass[aa] for aa in self.code]
    def __repr__(self):
        return self.__str__
    def __lt__(self,other):
        return self.code<other.code
    def cyclospectrum(self):
        cycli=self.code+self.code
        spectrum=[0]
        for largo_spec in range(1, self.largo()+1):
            for i in range(0,self.largo()):
                spe=sum([pep_mass[c] for c in cycli[i:i+largo_spec]])
                spectrum.append(spe)
        spectrum.append(self.masa_total())
        return Spectrum(spectrum) ## se genera un objeto spectrum
    def linearspectrum(self):
        spectrum=[0]
        for largo_spec in range(1,self.largo()+1):
            for i in range(0,self.largo()-largo_spec+1):
                spe=sum([pep_mass[c] for c in self.code])
                spectrum.append(spe)
        spectrum.append(self.masa_total())
        return Spectrum(spectrum)
class Spectrum:
    def __init__(self, spectrum:list):
        self.spectrum=sorted(spectrum)
        self.masa_spec=int(spectrum[-1])
    def __str__(self):
        return f"[spectrum {self.spectrum.__str__()}]"

    def __repr__(self):
        return self.__str__()
    def expand_peptides(self,candidates_pep):
        candidates_pepti=[peptide.expand() for peptide in candidates_pep]
        candidates_pepti=[p for sublist in candidates_pepti for p in sublist]
        return candidates_pepti
    def leaderboardcyclopeptidesequencing(self,n):
        leader=Peptide("")
        candidates=[leader]
        while len(candidates)>0:
            candidates=self.expand_peptides(candidates)
            leaderboard=Leaderboard(self)
            for pep in candidates:
                if pep.masa_total()==self.masa_spec:
                    if self.score(pep.cyclospectrum())>self.score(leader.cyclospectrum()):
                        leader=pep
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
if __name__ == "__main__":      
                
    #n=10
    #spect=Spectrum([0 ,71 ,113 ,129 ,147 ,200 ,218 ,260 ,313 ,331 ,347 ,389 ,460])
    #print(str(spect.leaderboardcyclopeptidesequencing(10).masas()))
    with open(repo+"/genome_seq/inputs/leader.txt","r") as reader:
        inp=list(map(str.strip,reader.readlines()))
        n=int(inp[0])
        spec_list=list(map(int,inp[1].split(" ")))
        spectr=Spectrum(spec_list)
        print(spectr.leaderboardcyclopeptidesequencing(n).masas())

