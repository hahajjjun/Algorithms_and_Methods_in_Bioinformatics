from Bio import SeqIO

f = open('rosalind_bphr.txt', 'r')
threshold = int(f.readline())

cnt = 0
records = []
for rec in SeqIO.parse(f, 'fastq'):
    records.append(rec.letter_annotations['phred_quality'])

for i in range(len(records[0])):
    if sum([r[i] for r in records])/len(records) < threshold:
        cnt += 1

print(cnt)