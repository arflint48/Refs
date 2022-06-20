#take updated refs.bib file and create one with abbreviated journal names abbrevrefs.bib

import sys, os, re

bib = open("refs.bib", "r").read() #refs.bib calls the bibtex file
journallist = open("journallist.txt") #calls the list of journals and their abbreviations

#for ApJ and related journals only:
apjlist = open("apjlist.txt")

for apjref in apjlist.readlines():
    full, abbrev = apjref.strip().split(" = ")
    full = ("{" + full + "}")
    if full != full.upper():
        bib = bib.replace(full.strip(),("{" + abbrev.strip() + "}"))

for journal in journallist.readlines(): #reads in each journal individually
    full, abbrev = journal.strip().split(" = ") #creates journal/abbreviation pair
    full = ("{" + full + "}") #forces the journal name to be a full match rather than a partial one
    if full != full.upper() and (" ") in full:
        bib = bib.replace(full.strip(),("{" + abbrev.strip() + "}")) #replaces the journal name with the abbreviation and restores bibtex formatting

with open("abbrevrefs.bib", "w") as abbrevbib: #file the modified bibliography will be written to
    abbrevbib.write(bib)

abbrevbib.close()
