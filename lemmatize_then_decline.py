#!/usr/local/bin/python3
# 
# Paul Evans (10evans@cua.edu)
# 8-10 January 2020
# 
from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer
from cltk.stem.latin.declension import CollatinusDecliner
from cltk.stem.latin.j_v import JVReplacer
from cltk.tokenize.word import WordTokenizer
import re

def stage1(text):
    '''
    Lowercases text, normalizes spelling by converting 'j' to 'i'
    and 'v' to 'u', removes punctuation.
    '''
    text = JVReplacer().replace(text.lower())
    words = re.split('\W', text)
    # return ' '.join([word for word in words if word != ''])
    return [word for word in words if word != '']

def stage2(tokens):
    # lemmatize() returns list of tuples
    results = BackoffLatinLemmatizer().lemmatize(tokens)
    lemmas = [] # unique lemmas
    for result in results:
        lemma = result[1]
        if lemma not in lemmas:
            lemmas.append(lemma)
    return lemmas

def main():
    r1_words = stage1(open('./Gratian1.txt', 'r').read())
    r2_lemmas = stage2(stage1(open('./Gratian2.txt', 'r').read()))
    whats_left = r2_lemmas

    decliner = CollatinusDecliner()
    for lemma in r2_lemmas:
        found = False
        forms = decliner.decline(lemma, flatten=True)
        for form in forms:
            if form in r1_words:
                whats_left.remove(lemma)
                found = True
                break
        if found:
            break
    print(len(whats_left))

if __name__ == '__main__':
    main()

