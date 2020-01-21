# Backoff
Experimenting with CLTK backoff lemmatizer to identify unique words
in the first and second recensions of Gratian's Decretum.

### Cull, then lemmatize
+ lowercase input text
+ regularize spelling of input text (convert 'j' to 'i' and 'v' to 'u')
+ tokenize input text using Regex re.split() instead of CLTK WordTokenize()
+ remove '' from tokenized word lists (vestige of punctuation left by re.split())
+ remove duplicate forms from word lists
+ remove MGH stopwords from word lists
+ remove forms common to R1 and R2 word lists from both lists
+ generate lists of unique lemmas corresponding to R1 and R2 word lists
+ remove lemmas common to R1 and R2 lemma lists from both lists

### Lemmatize, then decline
+ lowercase input text
+ regularize spelling of input text (convert 'j' to 'i' and 'v' to 'u')
+ tokenize input text using Regex re.split() instead of CLTK WordTokenize()
+ remove '' from tokenized word lists (vestige of punctuation left by re.split())
+ generate list of unique lemmas for just the R2 word list
+ for each R2 lemma, decline the lemma
+ if any form the R2 lemma is found in the R1 word list, remove the lemma


### Notes
Attempting to import the 'phi5' and 'phi7' corpora causes an
`AttributeError: 'NoneType' object has no attribute 'endswith'`
error.

Case matters. CLTK backoff lemmatizer lemmatizes
'Humanum' as 'humanum', but 'humanum' as 'humanus'.

