#!/usr/local/bin/python3
# 
# Paul Evans (10evans@cua.edu)
# 8-10 January 2020
# 
from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer
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
    return ' '.join([word for word in words if word != ''])

def stage2(text):
    '''
    Returns arbitrarily ordered list of unique forms not in stoplist.
    '''
    words = list(set(re.split('\W', text)))
    stopwords = [word.rstrip() for word in open('./mgh.txt', 'r').readlines()]
    return [word for word in words if word not in stopwords]

def stage4(tokens):
    # lemmatize() returns list of tuples
    results = BackoffLatinLemmatizer().lemmatize(tokens)
    lemmas = [] # unique lemmas
    for result in results:
        lemma = result[1]
        if lemma not in lemmas:
            lemmas.append(lemma)
    return lemmas

def main():
    r1 = open('./Gratian1.txt', 'r').read().lower()
    r2 = open('./Gratian2.txt', 'r').read().lower()
    r1_forms = stage2(stage1(r1)) # list
    r2_forms = stage2(stage1(r2)) # list

    r1_only_forms = [word for word in r1_forms if word not in r2_forms]
    r2_only_forms = [word for word in r2_forms if word not in r1_forms]
    # remove forms common to both 
    r1_lemmas = stage4(r1_only_forms)
    r2_lemmas = stage4(r2_only_forms)
    r1_only_lemmas = [word for word in r1_lemmas if word not in r2_lemmas]
    r2_only_lemmas = [word for word in r2_lemmas if word not in r1_lemmas]
    print(len(r1_only_lemmas))
    r2_only_lemmas.sort()
    print(r2_only_lemmas)

    for word in r2_only_lemmas:
        if word in r1_lemmas:
            print(word)

if __name__ == '__main__':
    main()

