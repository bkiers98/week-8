from collections import defaultdict
import numpy as np

class MarkovText(object):

    def __init__(self, corpus):
        '''Initializes self with a corpus and null dictionary'''
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):
        '''
        Given a corpus, generates a dictionary so that each value is a list
        of terms that follow the key term in the corpus. Duplicate values
        are kept to increase the chances of their selection in generate().
        '''
        self.term_dict = defaultdict(list)
        for i, term in enumerate(self.corpus.split()):
            if i < len(self.corpus.split()) - 1:
                self.term_dict[term].append(self.corpus.split()[i+1])
            else:
                self.term_dict[term]

        return self.term_dict


    def generate(self, seed_term=None, term_count=15):
        '''
        Generates a string of terms following the term patterns in the
        term_dict. 

        Parameters
        ----------
        seed_term : str, optional
            Term from the corpus to start the 'phrase'. By default is None,
            which prompts a random seed_term.
        term_count : int, optional
            Number of terms to generate into the 'phrase'. By default is 15.
        '''
        term_dict = dict(self.term_dict)
        # raise ValueError if seed_term not in corpus
        if seed_term:
            try:
                type(term_dict[seed_term]) != list
                # next_term = np.random.choice(self.term_dict[seed_term])
            except KeyError as e:
                print(f'--{e}--:\n\t -->{seed_term} is not in corpus.')
                return term_dict.keys()
        else:
            seed_term = np.random.choice(list(term_dict.keys()))

        phrase = seed_term
        next_term = seed_term
        for x in range(term_count-1):
            if term_dict[next_term] == []:
                next_term = np.random.choice(list(term_dict.keys()))
            else:
                next_term = np.random.choice(term_dict[next_term])
            phrase += ' ' + next_term
        return (phrase)
