from collections import defaultdict
import numpy as np

class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):

        # your code here ...

        self.term_dict = defaultdict(list)
        for i, term in enumerate(self.corpus.split()):
            if i < len(self.corpus.split()) - 1:
                self.term_dict[term].append(self.corpus.split()[i+1])
            else:
                self.term_dict[term]

        return self.term_dict


    def generate(self, seed_term=None, term_count=15):

        # raise ValueError if seed_term not in corpus
        if seed_term:
            try:
                next_term = np.random.choice(self.term_dict[seed_term])
            except ValueError as e:
                print(f'--{e}--:\n\t -->{seed_term} is not in corpus.')
                return self.term_dict.keys()
        else:
            seed_term = np.random.choice(list(self.term_dict.keys()))
            next_term = np.random.choice(self.term_dict[seed_term])

        # for each term in range of term_count, select the next term from the term's dictionary
        phrase = seed_term + ' ' + next_term
        for x in range(term_count):
            next_term = np.random.choice(self.term_dict[next_term])
            phrase += ' ' + next_term
        # if a term's dict is an empty list, start a new sentence and choose a random term next.
        return (phrase)