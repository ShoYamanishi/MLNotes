
# PRML (1.58) : Why <a><img src="eq_001.png" style="position:relative;top:0px;height:10px;"></a> ?

The equation (1.58) in **Pattern Recogntion and Machine Learming** by Bishop is apparently 
the first problem many readers including me encounter.
It's in pp27, Chapter 1, Introduction.
It was not apparent to me why it holds, but no proof is given in the book.
The following is my take on the proof why the sample variance is biased.



## Because <a><img src="eq_002.png" style="position:relative;top:10px;height:30px;"></a>, if <a><img src="x_1.png" style="position:relative;top:5px;height:20px;"></a> and <a><img src="x_2.png" style="position:relative;top:5px;height:20px;"></a> are independent.

Assume $x$ is a random variable with distribution $p(x)$ , and $x_1, x_2, \cdots, x_N$ are i.i.d. samples of $x$,
$\mu_s$ and $\sigma^2_s$ denote the sample mean and the sample variance respectively.
In the following argument all the expectations are over $p(x)$.

