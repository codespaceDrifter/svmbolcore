# PROOFS LATER NOT NOW

## the study of probability: a series of conditions leads to a bunch of data, collect these data, and can tell you something about those conditions lead to what. reality is deterministic if you have every variable, but you dont, so you use statistics. 


### probability basics
>$$ \text{Sample Space(S): The set of all possible outcomes of a random experiment. (i.e. for a coin flip, S is Heads, Tails)}$$

>$$ \text{Event: A subset of a sample space (i.e. getting Heads in a coin flip)}$$

>$$ \text{Probability (P): Measure of likelihood of an event. P(A) = number of times event happened / total number of experiments.  ranging from 0 to 1}$$

>$$\text{Conditional Probability: }P(A|B) = P(A \land B) / P(B)$$

>$$ \text{Independence: }P(A|B) = P(A)\text{, which means} P(A)*P(B) = P(A\land B)$$

>$$ \text{distribution: data values and their frequencies.}$$

>$$ \text{population: entire group i'm studying}$$

### discrete

>$$ \text{Y: a random variable. a mapping from sample space to a discrete numerical value. }$$

>$$ \text{y: a specific value}$$

>$$ \text{p(y) means p (y = Y)}$$
for all y, $0 \leq p(y) \leq 1$  
$\sum_{y}p(y) = 1$

>$$ \text{Expected Value:} E(Y) = \sum_{y} y * p(y)$$
expected value should equal mean. since p(y) is the number of cases of y divided by all cases  

>$$ \text{Linearity: }E[c_1 g_1 (Y) + c_2 g_2 (Y)] = c_1 E[g_1 (Y)] + c_2 E[g_2 (Y)]$$

>$$\text{Variance: }\sigma ^2 = E[(Y - \mu)^2] = E[Y^2] - E[Y]^2$$

proof:  
$$ \begin{aligned}
\sigma^2 &= E[(Y - \mu)^2] \\
&= E[Y^2 - 2Y\mu + \mu^2] \\
&= E[Y^2] - 2\mu E[Y] + \mu^2 \\
&= E[Y^2] - 2\mu^2 + \mu^2 \\
&= E[Y^2] - \mu^2 \\
&= E[Y^2] - (E[Y])^2
\end{aligned} $$

>$$V(cY) = c^2 V(Y)

### continuous

>$$ \text{Y: a random variable. a mapping from sample space to any values on a continuous range. }$$

>$$ \text{PDF probability density function f(y): }P(a\leq Y \leq b) = \int_{a}^{b} f(y)dy $$

>$$ E(Y) = \int_{-\infty}^{\infty} y f(y) dy  $$

expected value, variance, and linearity are the same as discrete

>$$\text{CDF cumalitive density function: } F(y \leq Y) = P(y \leq Y) = \int_{-\inf}^{y} f(y) dy $$

### normal
>$$\text{normal distribution:} f(x) = \frac{1}{\sigma \sqrt{2 \pi}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}  $$

>$$\text{standard normal: z =} \frac{y-\mu}{\sigma}$$

### statistics


>$$ \text{sample: a subset of population used for analysis}$$

>$$ \text{statistic: a number computed from the sample. i.e. mean, std}$$

>$$ \text{parameter: a numerical descriptor of population: i.e. mean, standard deviation}$$

>$$\text{mean:  } \mu = \frac{1}{N} \sum_{i=1}^{N} x_i$$

>$$\text{standard deviation: } \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}$$

>$$ \text{Central Limit Theorem: the distribution of the sample mean approaches a normal distribution if the sample size >30}$$

>$$ E[\bar{Y}] = \mu $$

>$$ V(\bar{Y}) = \frac{\sigma ^2}{n} $$



>$$ \text{estimate: value calculated from sample to approximate parameter. includes point and interval estimate  }$$




> $$\text{chi squared: n df\quad \quad}\chi^2 = \sum_{i=1}^n Z_i^2, \quad Z_i \sim N(0, 1) $$

> $$\text{population variance estimate: }S^2 = \frac{1}{n - 1} \sum_{i=1}^n (Y_i - \bar{Y})^2$$

>$$\frac{(n-1)S^2}{\sigma^2} \text{has a $X^2$ distribution with n-1 df}$$

>$$T =\frac{Z}{\sqrt{W/v}} $$
T distribution. Z: standard normal. W: $X^2$ distribution with v degrees of freedom. This T distribution also has v degress of freedom

>$$F = \frac{W_1 / v_1}{W_2 / v_2}$$

F distribution: used to compare two variances. df for each is n observations - 1. W is a $X^2$ distribution

> Maximum Likelihood Estimator: Pick the population probability that makes the observed probability most likely to happen

### Hypothesis Testing

>$$ \alpha \text{: probability of being wrong if reject $H_0$. Confidence level: 1 - $\alpha$}$$

use z when either  
population $\sigma$ is known  
or sample size > 30  (approximate $\sigma$ with S)


z test one sample
>$$ z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$$

z test two sample
>$$ z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$$

t test one sample
>$$ t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}, \quad df = n-1$$

t test two samples
>$$ t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \quad s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}, \quad df = n_1 + n_2 - 2$$

proportion one sample
>$$z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$

proportion two samples
>$$z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}, \quad \hat{p} = \frac{x_1 + x_2}{n_1 + n_2}$$

chi square
>$$ \chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

minimum sample size
>$$n = \frac{(z_{\alpha/2})^2 \sigma^2}{B^2}$$
B: margin of error

Formulas can be re-arranged to get confidence interval:
>$$ \bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

>$$ (\bar{x}_1 - \bar{x}_2) \pm z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$



### ANOVA
ANOVA tells you whether different treatments produce different average results  
$H_0$ is no groups is different, $H_A$ is at least one group is different.  
Assumption: each group is normal, all groups have equal variance, observations are independent  
SST: between group variation. df = number of groups -1  
SSE: within group variation. df = total sample size - number of groups  

> $$F = MST / MSE$$
>$$ MST = SST / df_{treatment} \quad \quad  \text{df = number of groups - 1}$$
>$$MSE = SSE / df_{error}   \quad \quad  \text{df = total sample size - number of groups}$$
>$$ SST = \sum_{i} n_i (\bar{y_i} - \bar{y})^2$$
$n_i$: sample size of group i  
$\bar{y_i}$: mean of group i  
$\bar{y}$ overall mean  
$\sum$ sum of all groups  
>$$SSE = \sum_{i} \sum_{j} (y_{ij} - \bar{y_i})^2$$
$y_{ij}$ each individual observation  

> then compare this to F distribution, df top and df bot equal the two dfs used to calculate MST and MSE

Alternative Formula:
>$$SS = SSE + SST$$
>$$SS = \sum_{i} \sum_{j} (y_{ij} - \bar{y})^2 = \sum_{i} \sum_{j} (y_{ij})^2 - n \bar{Y}^2$$ 

### categorical data analysis

Qualitative data rather than quantitative, one of k categories  
Use to see if category counts match expected counts  
n identical independent trials, $p_i$ remains constant  
$p_1 + p_2 + ... + p_k = 1$ and $n_1 + n_2 + ... + n_k = n$  
Requires: Expected Count > 5 for each category  
df = n - 1 - estimated parameters (i.e. (row-1) - (col - 1))   (df = how many cells can vary independently)


>$$\chi ^2 = \sum_{i=1}^{k}\frac{(n_i-E(n_i))^2}{E(n_i)} = \sum_{i=1}^{k}\frac{(n_i-np_i)^2}{np_i}$$ 


### linear regression

Simple linear regression
> $$y = \beta_0 + \beta_{\hat{i}} x$$
n data points, from i to n  
> $$\beta_{\hat{i}} = S_{xy} / S_{xx}$$
>$$S_{xy} = \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})  = \sum_{i=1}^{n} x_i y_i - \frac{1}{n}\left(\sum_{i=1}^{n} x_i\right)\left(\sum_{i=1}^{n} y_i\right)
$$
>$$S_{xx} = \sum_{i=1}^{n} (x_i - \bar{x})^2= \sum_{i=1}^{n} x_i^2 - \frac{1}{n}\left(\sum_{i=1}^{n} x_i\right)^2$$

>$$ \beta_0 = \hat{y} - \beta_{\hat{i}}  \hat{x}$$

>$$ SSE = \sum(\hat{y_i} - y_i)^2$$

>$$\hat{\beta} = (X^T X)^{-1} X^T Y$$