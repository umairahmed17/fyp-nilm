import numpy as np

from hmmlearn.hmm import MultinomialHMM

start_probability = np.array([0.5, 0.5])

transition_matrix = np.array([[0.7, 0.3], [0.3, 0.7]])

cover = np.array([[0.9, 0.1], [0.2, 0.8]])

model = MultinomialHMM(n_components=2, startprob_prior=start_probability, transmat_prior=transition_matrix )

X = [np.random.random_integers(0,1,4)] * 4

print(X)

model.fit(X=X)

print(model.transmat_)