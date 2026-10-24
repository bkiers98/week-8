from collections import defaultdict


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

        # your code here ...

        return None