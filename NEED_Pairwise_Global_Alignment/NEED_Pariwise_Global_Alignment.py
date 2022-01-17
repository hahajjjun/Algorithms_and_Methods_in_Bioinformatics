# SeqIO, Entrez, pariwise2
from Bio import SeqIO, Entrez, pairwise2

with open("rosalind_need.txt", "r") as f:
    genbank_ids = ', '.join(f.readline().split())
Entrez.email = "XXX@XXX.XXX"
handle = Entrez.efetch(db = "nucleotide", id = genbank_ids, rettype = "fasta")
records = list(SeqIO.parse(handle, "fasta"))
print(pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2]) #[0 : first alignment][2 : second item means score]