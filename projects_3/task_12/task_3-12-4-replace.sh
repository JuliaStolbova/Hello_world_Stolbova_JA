#!/bin/bash

echo ">seq1 ATGCGTACGTTAG >seq2 GGCATGCTAGCTA >seq3 TTAGCGATCGTAC >seq4 CCGTATGCTAGGA" >> sequences.txt
sed 's/>/\n/g' sequences.txt
