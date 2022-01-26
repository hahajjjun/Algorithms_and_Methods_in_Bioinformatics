# The Goal is to find some "short inexact repreat r" of 32~40bp.
# r will appear in both seq1 and seq1, with slight modifications
# Return the number of occureces of "r" in two sequences seq1, seq2

from Bio import SeqIO
from tqdm import tqdm

def hamming(s, t):
    ham = 0
    for ch in range(len(s)):
        if s[ch] != t[ch]:
            ham+=1
    return ham

def count_hamming(pattern, seq, dist = 3):
    count = 0
    pat_len = len(pattern)
    for i in range(len(seq)-pat_len+1):
        if hamming(seq[i:i+pat_len], pattern) < 4:
            count +=1
    return count

def subo(seq1, seq2):
    maxcnt1 = 0
    maxcnt2 = 0
    maxptn1 = ""
    maxptn2 = ""
    for i in tqdm(range(32, 41)):
        for j in range(len(seq1)-i):
            pattern1 = seq1[j:j+i]
            count1 = count_hamming(pattern1, seq1)
            if count1 > maxcnt1:
                maxcnt1 = count1
                maxptn1 = pattern1

    for i in tqdm(range(32, 41)):
        for j in range(len(seq2)-i):
            pattern2 = seq2[j:j+i]
            count2 = count_hamming(pattern2, seq2)
            if count2 > maxcnt2:
                maxcnt2 = count2
                maxptn2 = pattern2

    return maxcnt1, maxcnt2, maxptn1, maxptn2

filename = "rosalind_subo.txt"
seq1, seq2 = iter([fasta.seq for fasta in SeqIO.parse(filename, "fasta")])
maxcnt1, maxcnt2, maxptn1, maxptn2 = subo(seq1, seq2)

if maxptn1 in maxptn2 :
    maxcnt2 = count_hamming(maxptn1, seq2)
elif maxptn2 in maxptn1 :
    maxcnt1 = count_hamming(maxptn2, seq1)
print(maxcnt1, maxcnt2, maxptn1, maxptn2)


