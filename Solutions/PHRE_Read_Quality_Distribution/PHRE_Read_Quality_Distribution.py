from Bio import SeqIO
filename = "rosalind_phre.txt"

f = open(filename, 'r')
threshold = int(f.readline())
f_out = open("temp.txt", 'w')
temp = f.readlines()
for line in temp:
    f_out.write(line)

f.close()
f_out.close()

record = SeqIO.parse("temp.txt", "fastq")
cnt = 0
for rec in record:
    quality = rec.letter_annotations['phred_quality']
    if sum(quality)/len(quality) < threshold:
        cnt+=1
print(cnt)