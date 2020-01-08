#!/usr/local/bin/python3
# 
# Paul Evans (10evans@cua.edu)
# 6-7 January 2020
# 
from cltk.corpus.utils.importer import CorpusImporter
from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer
from cltk.stem.latin.j_v import JVReplacer
from cltk.tokenize.word import WordTokenizer

def setup():
    corpus_importer = CorpusImporter('latin')
    # corpus_importer.import_corpus('latin_models_cltk')
    corpora = corpus_importer.list_corpora
    corpora.remove('phi5')
    corpora.remove('phi7')
    for corpus in corpora:
        corpus_importer.import_corpus(corpus)

def process(text):
    tokens = WordTokenizer('latin').tokenize(text)
    # lemmatize() returns list of tuples
    results = BackoffLatinLemmatizer().lemmatize(tokens)
    lemmas = [] # unique lemmas
    for result in results:
        lemma = result[1]
        if lemma not in lemmas:
            lemmas.append(lemma)
    return lemmas

def main():
    # setup()
    a = open('./Gratian0.txt', 'r').read()
    b = open('./Gratian3.txt', 'r').read()
    a_lemmas = process(JVReplacer().replace(a.lower()))
    b_lemmas = process(JVReplacer().replace(b.lower()))
    a_only = [lemma for lemma in a_lemmas if lemma not in b_lemmas]
    b_only = [lemma for lemma in b_lemmas if lemma not in a_lemmas]

    a_only.sort()
    b_only.sort()
    print(a_only)
    print(b_only)

if __name__ == '__main__':
    main()

