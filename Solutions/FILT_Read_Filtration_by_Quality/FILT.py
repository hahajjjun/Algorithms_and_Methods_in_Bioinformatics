from Bio import SeqIO
f = open('rosalind_filt.txt', 'r')
cutoff, freq = map(int, iter(f.readline().split()))
f_out = open('temp.txt', 'w')
text = f.read()
f_out.write(text)
f.close()
f_out.close()

quality_cnt = 0
for record in SeqIO.parse("temp.txt", "fastq"):
    quality = record.letter_annotations['phred_quality']
    cnt = 0
    
    for item in quality:
        if item >= cutoff:
            cnt += 1     

    if cnt/len(quality) >= freq/100:
        quality_cnt += 1

print(quality_cnt)