Latent Dirichlet Allocation for Topic Modelling
===============================================

Overview
--------
Latent Dirichlet Allocation (LDA) is used to model text corpora and discover topics addressed by a document.

The basic idea is that documents are represented as random mixtures over latent topics, where each topic is characterized by a distribution over words.

LDA assumes the following generative process for each document w in a corpus D:

1. Choose N ~ Poisson(ξ). 
2. Choose θ ~ Dir(α). 
3. For each of the N words wn:
	(a) Choose a topic zn ~ Multinomial(θ).
	(b) Choose a word wn from p(wn |zn, β), a multinomial probability conditioned on the topic zn.

Assuming the above described generative process we estimate the parameters.
The posterior distribution is intractable for exact inference, hence we need to use approximate inference algorithms like Laplace approximation, variational approximation, and Markov chain Monte Carlo etc. 

This code uses Collapsed Gibbs Sampling (MCMC) method.

Input Format
------------
The input corpus is expected to in the following format

		### doc_id 1 ###
		word1
		word2
		...
		###EOF###
		...
		...
		### doc_id 100 ###
		word500
		word501
		...
		###EOF###

To create an input file in the above format, do:

		for each document d:
			print ### doc id ###
			for each word in document d:
				print word
			print ###EOF###
	
Example: Topic Modelling on NIPS Papers
---------------------------------------

These are some of the topic learned by LDA from NIPS papers. The topics names are inferred from its top words.

**Topic Modelling/LDA** 
topic, lda, words, document, topics, documents, word, text, dirichlet, distribution, latent, corpus, semantic, perplexity, figure, probability, sense, distributions, web, collection, inference, specific, space, vocabulary, multinomial, terms, models, prior, nips, number, related, content, allocation

**Image Peocessing/ Computer Vision**
image, images, pixels, patches, pixel, patch, figure, color, resolution, natural, set, results, fig, scale, texture, high, input, denoising, field, method, intensity, gaussian, work, statistics, low, real, shown, values, small, filter, range, filters, non, similar, based, reconstruction, left, single, applied, row

**Encoding/Decodin**
sparse, coding, basis, code, representation, dictionary, reconstruction, bases, codes, error, representations, vectors, coefficients, linear, number, figure, energy, sparseness, decoder, encoding, overcomplete, learned, decoding, sparsity, coordinate, shown, compression, term, non, average, encoder

**Kernels**
kernel, kernels, space, mkl, gaussian, linear, operator, rkhs, hilbert, section, rbf, positive, defined, spaces, svm, based, set, feature, definite, reproducing, case, operators, eq, theorem, dimensional, compact, product, paper, methods, characteristic, kx, functions, measure, note, basis, mapping, svms

**Clustering**
clustering, cluster, clusters, data, means, spectral, number, similarity, based, affinity, normalized, cut, partition, points, measure, set, dataset, partitioning, approach, distance, results, centers, method, pairwise, quality, center, clusterings, partitions, eigenvectors, average, objective, 

**Neural Networks**
layer, hidden, units, training, input, layers, network, deep, output, networks, trained, rbm, unit, neural, visible, set, learning, weights, architecture, unsupervised, convolutional, features, results, function, recognition, mnist, vector, test, inputs, representations, top, connections, energy, weight, error

**Belief Propagation**
bp, propagation, belief, message, inference, messages, marginals, variables, marginal, product, exact, mrf, approximate, approximation, variable, potentials, passing, xs, energy, loopy, factor, graphical, node, nodes, max, assignment, pairwise, sum, free, graph, field, bethe, tree, partition, fixed, figure, local

**Boosting**
boosting, weak, adaboost, classifier, examples, base, classifiers, learner, error, distribution, risk, margin, hypothesis, ensemble, bound, training, set, pac, learners, ht, dt, probability, bayes, hypotheses, gq, ln, oost, algorithms, random, weighted, positive, algorithm, h1, noise, pr, final, def, decision
