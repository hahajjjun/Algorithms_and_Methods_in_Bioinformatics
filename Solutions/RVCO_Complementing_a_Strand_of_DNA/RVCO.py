from Bio.Seq import Seq
from Bio import SeqIO

# from Bio.Alphabet import IUPAC : No more need
# find the number of strand that ... self = self.reverse_complement()
cnt = 0
record = SeqIO.parse("rosalind_rvco.txt", "fasta")

for rec in record:
    seqline = Seq(rec.seq)
    # seqline = Seq(rec.seq, IUPAC.unambiguous_dna) : Old notation
    if seqline == seqline.reverse_complement():
        cnt += 1

print(cnt)