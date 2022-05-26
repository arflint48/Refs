#take updated refs.bib file and create one with abbreviated journal names abbrevrefs.bib

import sys, os, re

bib = open("refs.bib", "r").read() #refs.bib calls the bibtex file
journallist = open("journallist.txt")

for journal in journallist.readlines()[::-1]:
    full, abbrev = journal.strip().split(" = ")
    if full != full.upper() and (" " in full):
        bib = bib.replace(full.strip(), abbrev.strip())

with open("abbrevrefs.bib", "w") as abbrevbib: #file the modified bibliography will be written to
    abbrevbib.write(bib)

abbrevbib.close()
bib.close()
