import numpy
import time
def read_corpus(filename):
	word_ids = dict()
	ids_word = dict()
	docs = []
	current_doc = []
	current_word = 0
	for l in open(filename, "rb").readlines():
			if l[0:4] == "### ":
				continue
			w = l.strip()
			if w == "###EOF###":
				docs.append(current_doc);
				current_doc = []
			else:
				if word_ids.has_key(w):
					current_doc.append(word_ids[w])
				else:
					current_doc.append(current_word)
					word_ids[w] = current_word
					ids_word[current_word] = w
					current_word = current_word + 1
	return docs, word_ids, ids_word

def initialize(docs):
	#Initialization with Online Gibbs Sampling
	for d, doc in enumerate(docs):
		tw = []
		for word in doc:
			p_t = numpy.divide(numpy.multiply(ntd[:,d], nwt[word,:]), nt)
			t = numpy.random.multinomial(1, p_t / p_t.sum()).argmax()
			tw.append(t)
			ntd[t][d] = ntd[t][d] + 1
			nwt[word,t] = nwt[word,t] + 1
			nt[t] = nt[t] + 1
		twd.append(numpy.array(tw))

def gibbs_iteration(docs):
	#Collapsed Gibbs Sampling Iteration
	for d, doc in enumerate(docs):
		for w, word in enumerate(doc):
			# Decrement counts for old topic of the word
			t = twd[d][w]
			ntd[t][d] = ntd[t][d] - 1
			nwt[word,t] = nwt[word,t] - 1
			nt[t] = nt[t] - 1
			
			# Sample new topic 
			p_t = numpy.divide(numpy.multiply(ntd[:,d], nwt[word,:]), nt)
			t = numpy.random.multinomial(1, p_t / p_t.sum()).argmax()
			
			# Increment counts for new topic of the word
			twd[d][w] = t 
			ntd[t][d] = ntd[t][d] + 1
			nwt[word,t] = nwt[word,t] + 1
			nt[t] = nt[t] + 1

def perplexity():
	nd = numpy.sum(ntd, 0)
	n = 0
	ll = 0.0
	for d, doc in enumerate(docs):
		for word in enumerate(doc):
			ll = ll + numpy.log(((nwt[word,:]/nt) * (ntd[:,d]/nd[d])).sum())
			n = n + 1
	return numpy.exp(ll/(-n))

def topwords(topic):
	ids_top_words = nwt[:,topic].argsort()
	top_words = []
	for j in ids_top_words:
		top_words.insert(0,ids_word[j])
	return top_words


print time.strftime('%X'), "Reading Data"
docs, word_ids, ids_word = read_corpus("data/stream.txt")

alpha = 5
beta = 0.1
k = 10	
n_iter = 10

# topic of word w in doc d
twd = []
# number of words of topic t in doc d 
ntd = numpy.zeros((k, len(docs))) + alpha
# number of times word w is in topic t
nwt = numpy.zeros((len(word_ids), k)) + beta
# number of words in topic t
nt = numpy.zeros(k) + (len(word_ids) * beta)

print time.strftime('%X'), "Initialize Gibbs Sampling"
initialize(docs)
print time.strftime('%X'), "Initialization Complete"

for i in range(n_iter):
	gibbs_iteration(docs)
	print time.strftime('%X'), "Iteration: ", i, " Completed", " Perplexity: ", perplexity()

for t in range(k):
	print topwords(t)[0:10]
