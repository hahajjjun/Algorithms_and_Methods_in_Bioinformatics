from Bio import SeqIO
filename = "rosalind_tfsq.txt"

with open("output.fasta", "w") as output_handle:
    sequences = SeqIO.parse(filename, "fastq")
    SeqIO.write(sequences, output_handle, "fasta")

# more explicit way
# with open("rosalind_tfsq.txt", "r") as input_handle:
#     with open("output2.fasta", "w") as output_handle:
#         sequences = SeqIO.parse(input_handle, "fastq")
#         SeqIO.write(sequences, output_handle, "fasta")