from Bio.Seq import translate
filename = "rosalind_ptra.txt"
f = open(filename, "r")
dna_seq = f.readline().strip('\n')
pro_seq = f.readline().strip('\n')

codon_tables = [i for i in range(1,17) if i not in range(7,9)] + [j for j in range(21,24)]
for table in codon_tables:
    translated_seq = translate(dna_seq, table = table, to_stop = True)
    if translated_seq == pro_seq:
        print(table)
