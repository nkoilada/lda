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
	(b) Choose a word wn from p(wn |zn,β), a multinomial probability conditioned on the topic zn.

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
	
		
