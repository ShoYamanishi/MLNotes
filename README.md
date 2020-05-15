# MLNOTES

This is a collection of expository documents about machine learning and neural networks 
that I have made during the Corona quarantine,
which has given me convenient time to sort out scribbles I have made 
in the past and to reorganize them into Tex documents.
I learned it mainly by the following books:

* Christopher M. Bishop. Pattern Recognition and Machine Learning (Information Science and Statistics). Springer, 1 edition, 2007.

* Deep Learning, Yoshua Bengio, Ian Goodfellow, Aaron Courville, MIT Press, In preparation., 2016.

* Simon J. D. Prince. Computer Vision: Models, Learning, and Inference. Cambridge University Press, 2012.

* David Barber. Bayesian Reasoning and Machine Learning. Cambridge University Press, 2011.

## Index

* [PRML 1.58](docs/expectation_of_sample_variance/exp_sample_var.pdf)
* [EM Algorithm](docs/em_algorithm/em_alg.pdf)
* [Variational Inference and Mean Field Approximation](docs/variational_inference/variational_inference.pdf)
* [Latent Direchlet Allocation](docs/latent_direchlet_allocation/lda.pdf)
* [Sampling](docs/sampling/sampling.pdf)
* [Graphical Models and Belief Propagation](docs/graphical_models/graphical_models.pdf)
* [Sequencial Models (HMM, Baum-Welch, Viterbi, Kalman Filter, RTS-Smoother)](docs/baum_welch_viterbi_kalman/baum_welch_viterbi_kalman.pdf)
* [Expectation Propagation](docs/expectation_propagation/expectation_propagation.pdf)

I made them, as it was simply fun, and also it solidifies my understanding of
those topics.
The official purpose would be:

* To provide a quick refresher to my future-self without going through books and articles and without using paper and a pencil to fill the gaps between equations.

* To help other independent-minded self-learners on important topics of machine learning.

Those documents are made such that the gaps between the equations along the derivations are minimized to avoid using paper and a pencil to fill them,
at the cost of redundancy and lengthy-ness.

# Topics

## [PRML 1.58](docs/expectation_of_sample_variance/exp_sample_var.pdf)

This is my take on why the sample variance is biased.
This equation (1.58) in PRML is apparently the first problem many readers 
including me encounter.
It’s in pp27, Chapter 1, Introduction.
It is not apparent to me why it holds, but no proof is given in the book.


## [EM Algorithm](docs/em_algorithm/em_alg.pdf)

This is a personal notes as my own memory aid on EM. for my future-self.
This is also a summplemental material to explain why the maximization 
step works for MLE with i.i.d. samples, 
which was not obvious to me in the text books.
PRML Chap 9.4. explains the EM algorithm with the standard graph plot of 
lower bounds and θ along the horizontal axis.
Computer Vision by JD Prince Chap 7.3., also has a better and more succinct 
explanation of EM.
The purpose of this document is to explain the EM algorithm without 
significant gap throught the course of deductions at the cost of lengthiness, 
and to explain why the M-Step works for MLE, 
which is omitted in the text books.


## [Variational Inference and Mean Field Approximation](docs/variational_inference/variational_inference.pdf)

This is a quick refresher on variational inference and mean field 
approximation.
The purpose of this document is as a self-contained document to enhance the 
course notes by D. Blei with my own annotations to fill the gaps 
between deductions in order for my future-self to refresh this topic quickly 
without a pencil and paper.
The variational inference and the mean field approximation are explained in 
PRML[2] 10.1 and Barber[1] 28.3, 28.4,
but I like the course notes by D. Blei available online at Princeton is best, 
as it gives the flow of explanation from the problem setting down to the 
optimality of the factroized approximator for the exponential families.
However, it is a bit too terse to me.

## [Latent Direchlet Allocation](docs/latent_direchlet_allocation/lda.pdf)

This is an expository document for latent Direchlet allocation in the full 
Bayesian setting for β matrix.
This is an outcome of my own self study into the original article, 
and it has turned out to be a very good streamlined study material 
for EM-algorithm and variational Bayes worth documenting by myself 
for my own better understanding.
The main purpose of this document is to quickly and effortlessly refresh 
my memory in the future as my own memory aid.
Another purpose is to fill the gap between the original article and the blog 
articles available on Internet.
The original article is too terse, and it takes me a lot of paper-and-pencil 
work to comprehend the contents.
It also briefly touches on the full Bayesian treatment.
On the other hand, the blog articles focus on a quick grasp of the concept 
with rich illustrations, and rigorous mathematical treatment is usually 
ommitted.
This document is characterized as follows.

* Comprehensive math treatment from the modeling down to just before implementation for both training and inference.

* Full-bayesian β with prior η.

* Small gaps between two adjacent equations through the course of deductions at the cost of lengthiness.

* Discussion on possibility of treatment of using the columns of β as word embeddings with non-informative priors.


## [Sampling](docs/sampling/sampling.pdf)

This is a personal expository material on sampling mainly for my future self 
to quickly refresh the topics.
It also contains explanations to the topics that are unclear to me 
in the books and articles.
The following topics are covered.

* Basic sampling : from uniform distribution to a particular distribution.

* Rejection sampling

* Importance sampling

* Uni/Bivariate Gaussian Distribution : Box-Muller algorithm

* Univariate Gaussian Distribution with rejectio sampling : Ziggurat algorithm

* Multivariate full-covariance Gaussian distribution MCMC (Metropolis-Hastings)

* Gibbs Sampling

* MCMC with Hamiltonian dynamics

The highlights are the comprehensive explanation of Ziggurat algorithm, which is
used to sample from multivariate normal distributions, and a rigorous formation
of MCMC using Hamiltonian dynamics.
Most articles and books put emphasis on Hamiltonian dynamics and its numerical 
integration, but more rigorous formation of MCMC using Hamiltonian dynamics is often
not well explained.
Especially, formation of a proposal function, an acceptance function, 
transition probability distribution and ergodicity are not well discussed.
This section focus on those topics, rather than the Hamiltonion dynamics and 
the numerical simulation.


## [Graphical Models and Belief Propagation](docs/graphical_models/graphical_models.pdf)
It summrizes some key points about the probabilistic graphical models.

* Conditional independence

* D-Separation

* Markov Blanket

It also treats the belief propagation in chains and trees for maginal distribution and MAP.


## [Sequencial Models (HMM, Baum-Welch, Viterbi, Kalman Filter, RTS-Smoother)](docs/baum_welch_viterbi_kalman/baum_welch_viterbi_kalman.pdf)

This is a personal notes as my own memory aid on Hidden Markov Models and Linear Dynamical Systems.
Specifically the following topics.

* Baum-Welch EM algorithm 
* Viterbi algorithm
* Kalman Filter
* Rauch-Tung-Striebel smoother and EM algorithm

Chapter 13 of PRML is an excellent source for HMM (Baum-Welch, Viterbi)
and Kalman Filter, but not so good for Kalman smoother (RTS smoother).
Especially the derivation of  p(z_n, zn+1| z_1, ..., z_N), 
which is required for EM-algorithm, is a bit shaky between (13.103) and (13.104).
For deriving RTS smoother, I used an excellent course notes from Professor Särkkä of Aalto Univ.
Also, Chap 24 of Barber contains comprehensive materials for LDS,
but it is a bit difficult to understand and I personally do not like the style of notations.

## [Expectation Propagation](docs/expectation_propagation/expectation_propagation.pdf)

This is an expository document for expectation propagation for my future self.
It is aimed at a self contained document.
It converts the following three topics

* general expectation propagation with the exponential family

* detailed explanation of the clutter problem

* detailed explanation of loopy belief propagation


I have found the following subtle but important points during my own learning, which are not well explained
in the existing literature. The emphasis are given on those points in this document.

### KL-divergence takes proper (normalized) density functions.
The algorithm depends on the minimization of the KL divergenace to which two proper (normalized) density
must be given, but we approximate a conditional q(θ) ~= p(x|θ) where x is observed.
This is not mormalized and a careful conversion is needed when applying the KL divergence.

### distinction between *moments* and *natural* parametes: The algorithm operates on
the moments, which are not necessarily the natural parameters for the underlying model.
For example, Gaussian distribution takes the 1st-order moment
 as the mean parameter but the 2nd-order moment is different from variance.

### careful treatment of normalization coefficients (partition function). Throughout the algorithm
factors are added and removed from the current approximations. For those operations the normalizations
coefficients are carefully maintaned.

### *moment matching* requires some tricks. The moment matching for the example clutter problem requires
some tricks, which are not explained well in the existing literature.

Minka is the original and seminal article of the expectation propagation.
That is too concise as a study material as a lot of details are omitted. It presents
the clutter problem, but the updated momments are presented without details.
PRML follows the same style as Minka but
the details of update of approximation maintaining the normalization coefficient (partition function)
is omitted.
Barber briefly touches on the belief propagation in relation to expectation propagation
in section 28.7.
The course notes by Honkela at Helsinki Univ. gives a very nice explanation.
However the treatment of the normalization coefficients is not thorough.
The lecture video by Simon Barthelmé
at Centre International de Rencontres Mathématiques gives a good explanation for cavity, hybrid,
narutal parameters and moment parameters.

None of the materials above are detailed enough for normies like me to study this topic, and that
was the motivation for me to write this up for my furuter self and possibly others.

## Back Propagation (Basics, CNN, RNN, LSTM)
[work in progress]

## Contrastive Divergence
[planned]

## RBM
[planned]