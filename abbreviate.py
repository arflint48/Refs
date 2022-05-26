#take updated refs.bib file and create one with abbreviated journals

import sys, os, re
import pandas as pd

bib = open("refs.bib", "r") #refs.bib calls the bibtex file

bib.close()