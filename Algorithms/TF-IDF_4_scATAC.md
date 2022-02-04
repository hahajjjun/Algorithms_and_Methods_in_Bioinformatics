### Concept of scATAC-seq

---

### scATAC-seq data preprocessing

---

### Preprocessing method for scATAC seq data : TF-IDF way
---
#### Why TF-IDF?
- scATAC seq data are **very sparse**
- much sparser than scRNAseq
- in order to perform clustering of scATACseq data, preprocessing steps need to be done.
---
- Genome >> 5kb windows breakdown
- Score each cell for any insertion in these windows
- Generate large, sparse, binary matrix of 5kb windows by cels
- Reduce dimensionality of these large binary matrices using **frequency-inverse document frequencey transformation**
- Individual cells, 