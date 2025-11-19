## vector space
>$$\text{vector: a ordered list of expressions}$$  

>$$\text{vector space: a set of vectors that is a closure}\\
\text{under addition and scalor mulitplication}\\
\text{and the usual rules of communativity, associativity, and distributivity apply}$$  

vector space:  
i.e. real number n-tuples. i.e. (4,2,5,6) , (1,6,7,8)  
i.e. matrixes M nm  
i.e. complex number n-tuples  
i.e. continuous real valued functions on closed interval  

formal requirements for a vector space:  
1. communitavity: $\vec{a} + \vec{b} = \vec{b} + \vec{a}$
2. associativity: $(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c})$  
(communativity means left and right operand cannot be switched  
associative means that in a chain of same operations it doesn't matter which one is done first  
matmuls are associative but not communitive, averaging is communitive but not associative)
3. additive identity: $\vec{0} + \vec{x} = \vec{x}$  
4. additive inverses: $\vec{x} + (-\vec{x}) = 0$  
5. vector distributivity: $a(\vec{x}+\vec{y}) = a\vec{x} + b \vec{y}$  
6. scalar distributivity: $(a+b)\vec{x} = a\vec{x} + b\vec{x}$  
7. multiplicative identity: $1\vec{x} = \vec{x}$
8. scalar multiplication associativity: $ab\vec{x} = a(b\vec{x})$

the simpler proof of a vector space:
1. prove or know it's a subspace of another vector space
2. prove it's closed under addition (with variable values)
3. prove it's closed under multiplication (with variable values)

i.e. polynomial functions is a subspace of continuous functions (infinite terms)


## Matrix

> $$\text{Matrix: a rectangle array of numbers arranged in rows and columns}$$

notation: each $\vec{a_n}$ means a column of A, each $\vec{a_n}^T$ means a row of A

> $$\text{Matrix Vector Mul: } A\vec{v} = \vec{a_1}v_1+ ... + \vec{a_n}v_n$$

each coordinate is like an axis an element of the transformed vector scales and each row is like a direction and scale the transformed vector gets projected to.



> $$c*(A\vec{v}) = A(c*\vec{v})$$

proof:  
$$c*(\vec{a_1}v_1+ ... + \vec{a_n}v_n) = \vec{a_1}*c*v_1 + ... + \vec{a_n}*c*v_n$$

> $$\text{Matmul: } AB = [Ab_1 , ... , Ab_n]$$

> $$ A(B(\vec{v})) = AB(\vec{v}) $$

proof:  

$$ \begin{aligned}
A(B(\vec{v})) &= A(b_1v_1 + ... + b_nv_n) \\
A(B(\vec{v})) &= A(b_1v_1) + ... + A(b_nv_n) \\
AB(\vec{v}) &= [Ab_1, ... ,Ab_n]v \\
AB(\vec{v}) &= (Ab_1)v_1 + ... + (Ab_n)v_n \\
\because c*(A\vec{v}) &= A(c*\vec{v}) \\
A(B(\vec{v})) &= AB(\vec{v})
\end{aligned}$$

> $$\text{Matmul associativity: }(AB)C = A(BC)$$

proof:  

$$ \begin{aligned}
(AB)C &= [ABc_1, ... ,ABc_n] \\
A(BC) &= A[Bc_1, ... ,Bc_n] \\
A(BC) &= [A(Bc_1), ... ,A(Bc_n)] \\
\because A(B(\vec{v})) &= AB(\vec{v}) \\
(AB)C &= A(BC)
\end{aligned}$$

> $$\text{elementary operation: row scale, different row add, row swap. expressed as a matrix to matmul target by}$$

A matmul B can be seen as A doing a series of row operations to B. $A_{ij}$ is the scale applied to the i row of B added to the j row of result.  

> $$\text{Inverse: }A A^{-1} = I $$

> $$\text{row reduce[A I] produces [I $A^{-1}$] (if possible)}$$

proof:  

$$ \begin{aligned}
\text{row reduce is a series of elementary operations} \\  
E_n*...*E_2*E_1*A &= I \\
\text{by definition, }\\
E_n*...*E_2*E_1 &= A^{-1} \\
\end{aligned}$$
on the augmented I part: it because same operations are done on it:  
$$E_n*...*E_2*E_1*I = A^{-1}$$

> $$Ax = b \implies x = A^{-1}b$$

proof: 
$$ \begin{aligned}
A^{-1}Ax &= A^{-1}b \\
(A^{-1}A)x &= A^{-1}b \\
Ix &= A^{-1}b \\
x &= A^{-1}b \\
\end{aligned}$$



## linear dependence

the set B is __linearly independent__ if whenever $a_1\vec{b_1}$ + ... + $a_n\vec{b_n}$, $a_1 = ... = a_n = 0$

if B is not linearly independent it is linearly dependent

the set B is __linearly dependent__ if one of the vectors $\vec{b_i}$ can be written as a linear combination of the others

if __Span(B)__ = V, then set B is said to span V

a __matrix__ is a rectangular array of expressions arranged in rows and columns. 

$A\vec{v}$ : linear combinations of columns of A with each element of v. 

theorem: let A be an n x m matrix, TFAE:
1. the columns of A are linearly independent
2. the only solution to $A\vec{x} = \vec{0}$ is $\vec{x} = \vec{0}$
3. the reduced row echelon form of the matrx A has a pivot in every column

theorem: let A be an n x m matrix, TFAE:
1. the columns of A span $\mathbb{R}^n$
2. the equation $A\vec{x} = \vec{b}$ has a solution for every b in $\mathbb{R}^n$
3. the reduced row echelon form of the matrix A has a pivot in every row

theorem: let A be an n x n matrix: TFAE:
1.-6.: all six statements before
7. A is an invertible matrix
8. The determinant of A is nonzero
9. A is row equivalent with identity matrix I


## basis

if B is linearly independent and B spans V then B is a __basis__ for the vector space V. and each $\vec{v} \in$ V can be uniquely written in terms of B

__standard basis__ is like ordered one hot encoding
i.e. standard basis for 4 size vector: {1,0,0,0} , {0,1,0,0} , {0,0,1,0} , {0,0,0,1}
i.e. polynomial standard basis: $P_0(t) = 1, P_1(t) = t,  P_2(t) = t^2 ... p_n(t) = t^n$

$[\vec{v}]_B$ means $\vec{v}$ expressed in B coordinates. $\vec{v}$ expressed in normal coordinates is each element of $[\vec{v}]_B$ times a column of B

1) if $\vec{x}, \vec{y} \in V$, then $[\vec{x} + \vec{y}]_B = [\vec{x}]_B + [\vec{y}]_B$ and $[c\vec{x}]_B = c[\vec{x}]_B$
2) if $\vec{w}$ is a linear combination of $\vec{vi}$ then $[\vec{w}]_B$ is a linear combination of $[\vec{vi}]_B$ 
3) if $\vec{v_i}$ s are linearly independent in V, then $[\vec{v}]_B$ s are linearly independent in $R^n$

cause each coordinate is a scale for a vector of constants in the basis and when adding or constant multiplying or solving the matrix equation what vector each row scales cancels out

> $$\text{isomorphism: there's a map L: V->W that is one to one and onto and linearly independent}$$

> $$\text{dimension: if vector space V has a basis with n elements we say that the dimension of V is n}$$

> $$\text{change of basis B to D } P_{DB} = ([\vec{b_1}]_D, [\vec{b_2}]_D, ... ,\vec{b_n}_D)$$  

$$\begin{aligned}
[\vec{v}]_B &= x_1b_1 + \ldots + x_nb_n \\
[\vec{v}]_D &= y_1d_1 + \ldots + y_nd_n
\end{aligned}$$

You want $b_1$ to be transformed to some column in D basis. Let the target be $t$.

$$x_1b_1 = t_1d_1 + \ldots + t_nd_n$$

Represent $b_1$ with D coordinates: $[b_1]_D = (s_1, \ldots, s_n)$

$$x_1(s_1d_1 + \ldots + s_nd_n) = t_1d_1 + \ldots + t_nd_n$$

$$t_i = x_1 \cdot s_i$$

therefore we scale each original element by it's original basis column expressed in the new base

> $$P_{BD} = {P_{DB}}^{-1}$$

> $$\text{if B,C,D are bases for the same vector space, then }P_{BD} = P_{BC} * P_{CD}$$

## internal and external direct sum 

> $$\text{external direct sum: suppose that V and W are two vector spaces } \\
\text{external direct sum V $\oplus$ W is the set of pairs  $\left( \substack{\vec{v} \\ \vec{w}} \right)$}

external direct sum result is a vector space because  
$\left( \substack{\vec{v} \\ \vec{w}} \right) + \left( \substack{\vec{v'} \\ \vec{w'}} \right) =  \left( \substack{\vec{v + v'} \\ \vec{w + w'}} \right)$,
$c \left( \substack{\vec{v} \\ \vec{w}} \right) = \left( \substack{\vec{cv} \\ \vec{cw}} \right), \left( \substack{\vec{0} \\ \vec{0}} \right) \text{exists in it}$  

if V has basis {$\vec{b_1}, ... \vec{b_n}$}, W has basis {$\vec{d_1}, ... \vec{d_n}$}, then V $\oplus$ W has the basis {$\left( \substack{\vec{b_1} \\ \vec{0} }\right),..., \left( \substack{\vec{b_n} \\ \vec{0} }\right), \left( \substack{\vec{0} \\ \vec{d_1} }\right), ... , \left( \substack{\vec{0} \\ \vec{d_n} }\right)$}

> $$\text{internal direct sum: let $W_1$ and $W_2$ be subspaces of a vector space V such that any vector $\vec{v}\in$ V}\\
\text{can be uniquely decomposed as $\vec{v} = \vec{w_1} + \vec{w_2}$ then V is the internal direct sum of $W_1$ and $W_2$}$$

> $W_1 \cap W_2 = {\vec{0}}$  

proof by contrapositive:  


$$\begin{aligned}
\text{let  }\vec{v} &= \vec{w_1} + \vec{w_2} = \vec{w1'} + \vec{w2'} \\
\vec{w_1} - \vec{w_1'} &= \vec{w_2'} - \vec{w_2} \\
\text{if } W_1 \cap W_2 !&= {\vec{0}}  \\
\end{aligned}$$
then $w_1$ and $w_1'$ do not have to be equal and $w_2$ and $w_2'$ do not have to be equal
therefore some non zero element of W equal V and it's not unique

> $$\text{the internal direct sum of two vector spaces and the external direct sum of those are isomorphoic}$$

> $$\text{let V be a n+m dimensional vector space, let $W_1$ be n dimensional subspace and $W_2$ be m dimensional subspace}\\
\text{and $W_1 \cap W_2 = \vec{0}$ then V is the internal direct sum of $W_1$ and $W_2$}$$


## linear transformation

> $$\text{linear transformation: let V and W be vector spaces and let L : V -> W be a map If for every} \\
\text{$\vec{v1}$ , $\vec{v2}$, $\in$ V and every scalor c, we have $L(\vec{v1} + \vec{v2} ) = L(\vec{v1}) + L(\vec{v2})$ and } \\
\text{$L(c\vec{v_1}) = c L(\vec{v_1})$, then we say L is a linear transformation from V to W}$$

different space also called linear map, same space also called operator

isomorphism is linear transformation

projection from external direct sum to one of the original one is a linear transformation

> $$\text{every linear transformation can be written as a matrix vector mul}$$
linear transformation respects the standard basis ground truth so basis matters. the matrix to transform a vector in the B basis must be made up of B basis columns transformed by L. 

proof:  
any vector v can be written as a linear combination of basis vectors:  
$v = v_1e_1 + ... + v_ne_n$  
applying L to both sides, due to L being linear  
$L(v) = v_1L(e_1) + ... + v_nL(e_n)$  
now let $L(e_i)$ equal to the ith column of a matrix  
then you can see L(v) is equal to that matrix being matrix vector muled with the input  
(for non standard basis it could be $b_1$ to $b_n$ rather than $e_1 to e_n$)  

i.e. B = D = {1,t,$t^2$,$t^3$}, L = d/dt  
$L(\vec{b1}) = 0, L(\vec{b2}) = 1, L(\vec{b3}) = 2t, L(\vec{b4}) = 3t^2$  
convert each to D basis. here it's the same as original but in other scenario might be different.  
new matrix = ([0,0,0,0], [1,0,0,0],[0,2,0,0],[0,0,3,0])


> $$[L\vec{v}]_D = [\vec{v}]_D P_{BD}[L]_{BB} P_{DB}$$

> $$\text{let V and W be vector spaces and let L be a linear transformation from V to W, and }\vec{v}\in V \\
\text{the Kernel of L denoted Ker(L), is the set of all vectors for which $L(\vec{V})=0$} \\
\text{the range of L denoted Range(L) is the set of all vectors of the form $L(\vec{v})$}$$

ker(L) is a subspace of V, Range(L) is a subspace of W

>$$\text{if ker(L) = {0} L is one to one. if Range(L) is equal to W it is onto}$$

## eigenvectors

> $$ \text{if } L(\vec{v}) = \lambda \vec{v} \text{ then $\lambda$ is an eignen value of L and $\vec{v}$ is an eigenvector}\\

> $$\text{if $\lambda$ is an eigenvalue, the set of $\vec{v}$ s such that $L(\vec{v}) = \lambda \vec{v}$ is called the eigenspace denoted $E_{\lambda}$ (eigenvectors and $\vec{0}$)}$$

> $$ \text{if L transformation matrix and V can be expressed in a basis of eigenvectors B, $L_B =$ diagonal matrix with eigenvalues}$$
proof:  
assume both L transformation matrix V can be expressed in a basis of eigenvectors B for the transformation matrix (sometimes not possible)  
$$ \begin{aligned}
v &= a_1\vec{b_1} + ... + a_n\vec{b_n}\\
L(v) &= L(a_1\vec{b_1} + ... + a_n\vec{b_n})\\
L(v) &= L(a_1\vec{b_1}) + ... + L(a_n\vec{b_n})\\
L(v) &= a_1L(\vec{b_1}) + ... + a_nL(\vec{b_n})\\
\because L(b_i) &= \lambda_ib_i \\
L(v) &= a_1\lambda_1\vec{b_1} + ... + a_n\lambda_n\vec{b_n}\\
\end{aligned}$$

> $$\text{determinant of a matrix tells you whether the rows are linearly dependent. if determinant is 0 it is linearly dependent.}$$

formula for deerminants:  
[a b]  
[c d]  
det = ad - bc  

[a b c]  
[d e f]  
[g h i]  
det = a(ei - fh) - b(di - fg) + c(dh - eg   )


> $$\text{characteristic polynomial to find eigenvalues of $L(\vec{v})=A\vec{v}: det(A-\lambda I)=0$}, $$
proof:  
$$ \begin{aligned}
A\vec{v} &= \lambda \vec{v}\\
(A - \lambda I ) \vec{v} &= 0\\
\end{aligned}$$
because eigen vectors are infinitely many and this matrix needs to be linearly dependent to have infinitely many solutions, the det($A-\lambda I$) must = 0.  
after getting the eigenvalues, plug into $(A-\lambda I)v = 0$ to solve for the eigenvector  
also $det(\lambda I - A) = 0$ gives the polynomial too

> $$\text{if $\vec{v}$ is eigenvector of L then $[\vec{v}]_D$ is an eigenvector $[L]_D$ and the corresponding values are the same: }$$
$\vec{v}$ --- L --> $\lambda \vec{v}$  
$\uparrow \quad \quad \quad \quad \uparrow$  
$\downarrow\quad \quad \quad \quad \downarrow$  
$[\vec{v}]_D$ --$L_D$ -> $\lambda [\vec{v}]_D $

> $$\text{rotational matrix: }
\begin{pmatrix}
\cos(\theta) & -\sin(\theta) \\
\sin(\theta) & \cos(\theta)
\end{pmatrix}$$

> $$\text{rotational matrix with angle $\tan^{-1}(\frac{b}{a})$ and scale $\sqrt{a^2+b^2}$}
\begin{pmatrix}
a & -b \\
b & a
\end{pmatrix}$$
proof:  
think of a right triangle on the axises with a horizontal and b vertical and hypotunuse $\sqrt{a^2+b^2}$ . the $\theta$ angle is $\tan^{-1}(\frac{b}{a})$ the $\cos{\theta}=\frac{a}{\sqrt{a^2+b^2}}$ and $\sin\theta=\frac{b}{\sqrt{a^2+b^2}}$ so $a = \cos{\theta\sqrt{a^2+b^2}}$ and $b = \sin{\theta\sqrt{a^2+b^2}}$

> $$\text{if a + bi is a eigenvalue then a - bi also is a eigenvalue with a corresponding conjugate eigenvector. }$$

proof:  
if a + bi is an eigenvalue, a - bi is also an eigenvalue due to the process of solving the quadratic equation the $\pm\sqrt{4ac}$ part (different a and c not related. just naming.)  
let B be a matrix,  suppose $\vec{v} = \vec{v}_R + \vec{v}_i$ , $\bar{\vec{v}} = \vec{v}_R - \vec{v}_i$, $B(\vec{v}) = (a-bi)\vec{v}$, $B(\bar{\vec{v}})= (a+bi)\vec{v}$

$$\begin{aligned}
B\vec{V}_R = B(\frac{\vec{v} + \bar{\vec{v}}}{2}) &= \frac{(a-bi)\vec{v} + (a+bi)\bar{\vec{v}}}{2} \\
\text{after simplifications} \\
B\vec{V}_R &= a\vec{v}_R + b\vec{v}_i \\
B\vec{V}_I = B(-i\frac{\vec{v} - \bar{\vec{v}}}{2}) &= -i\frac{(a-bi)\vec{v} - (a+bi)\bar{\vec{v}}}{2} \\
\text{after simplifications} \\
B\vec{V}_R &= -b\vec{v}_R + a\vec{v}_i \\
\text{if } \vec{V}_R, \vec{V}_I \text{ is a basis, B rotates and scales it}
\end{aligned}$$

> $$\text{let B = [$\vec{b}_1 ... \vec{b}_n$] be eigenvectors of L corresponding to different eigenvalues then B is LI}$$

proof by contradiction:  
suppose $b_1 ... b_m$ are LD, let r be the smallest integer such that the set $b_1 ... b_r$ is still LD  
apply $L - \lambda_rI$ to combination:
$$\begin{aligned}
[L - \lambda_rI] ( \vec{0} ) &= [L - \lambda_rI] \sum_{i=1}^{r}a_i\vec{b_i}\\
\vec{0} &= \sum_{i=1}^{r} a_i (\lambda_i \vec{b_i} - \lambda_r \vec{b_i}) \\
\vec{0} &= \sum_{i=1}^{r-1} a_i (\lambda_i \vec{b_i} - \lambda_r \vec{b_i}) + a_r (\lambda_r \vec{b_r} - \lambda_r \vec{b_r})\\
\vec{0} &= \sum_{i=1}^{r-1} a_i (\lambda_i \vec{b_i} - \lambda_r \vec{b_i}) \\
\end{aligned}$$
this is a smaller set than r, showing a contradiction. 

>$$\text{L is an operator on a n dimensional spaceif the characteristic polynomial $P_L(\lambda)$ has n distinct roots L is diagonzable}$$

>$$\text{the algebraic multiplicity $m_a(\lambda_o)$ of eigenvalue $\lambda_o$ is the multiplicity of $\lambda_o$ as a root of $P_L(\lambda)$}$$

($P_L(\lambda)$ is divisible by exactly $m_a(\lambda_o)$ powers of $(\lambda-\lambda_o)$) (how many times the root appears basically)

if $m_a(\lambda_o) > 1 \lambda_o$ is called a degenerate eigenvalue

>$$\text{the geometric multiplicity $m_g(\lambda_o)$ of eigenvalue $\lambda_o$ is the dimension of the eigenspace for $\lambda_o$}$$

>$$\text{the deficiency of $\lambda_o$ is $m_a(\lambda_o) - m_g(\lambda_o)$. deficiency will always $\ge$ 0}$$

proof:  

Let λ₀ be an eigenvalue of an n×n matrix A with geometric multiplicity m_g(λ₀) = k.

There exist k linearly independent eigenvectors v₁, v₂, ..., vₖ corresponding to λ₀.

Extend {v₁, ..., vₖ} to a basis of ℝⁿ: {v₁, ..., vₖ, vₖ₊₁, ..., vₙ}.

$$P^{-1}AP = \begin{bmatrix} \lambda_0 I_k & B \\ 0 & C \end{bmatrix}$$

Since P⁻¹AP and A are similar matrices, they have the same characteristic polynomial:
$$\det(A - \lambda I) = \det(P^{-1}AP - \lambda I)$$

$$\det(P^{-1}AP - \lambda I) = \det\begin{bmatrix} (\lambda_0 - \lambda)I_k & B \\ 0 & C - \lambda I_{n-k} \end{bmatrix}$$

$$= \det((\lambda_0 - \lambda)I_k) \cdot \det(C - \lambda I_{n-k}) = (\lambda_0 - \lambda)^k \cdot \det(C - \lambda I_{n-k})$$

The polynomial $\det(C - λI_{n-k})$ may contain (λ₀ - λ) as a factor with multiplicity j ≥ 0.

Therefore, the characteristic polynomial of A is:
$$\det(A - \lambda I) = (\lambda_0 - \lambda)^{k+j} \cdot (\text{other factors})$$

The algebraic multiplicity is:
$$m_a(\lambda_0) = k + j = m_g(\lambda_0) + j$$

Since j ≥ 0:
$$m_a(\lambda_0) \geq m_g(\lambda_0)$$

Therefore, the deficiency:
$$m_a(\lambda_0) - m_g(\lambda_0) = j \geq 0$$

>$$\text{a matrix A is diagnozable if there exist invertiple matrix P and diagonal matrix D such that $D = P^{-1}AP$}$$

>$$\text{an operator L on a complex vector space is diagonolizable if and only if all the eigenvalues have deficiency = 0 }$$

(all algebraic multiplicity added together always equal to the dimension of the matrix)  
(they must be LI because their respective sum for all the eigen vectors for a eigen value is still an eigen vector for that eigen value and if that can be equal to some other eigen vector of another eigen value then it's like their eigen value must be the same)

## tricks

> $$\text{the trace of a matrix Tr(A) is the sum of it's diagonal entries: }$$
1: the sum of trace is equal to the sum of eigenvalues  
2: Tr(AB) = Tr(BA)  
3: $Tr([L]_D) = Tr(P_{DB}[L]_BP_{DB}^{-1}) = Tr[L]_D$

> $$\text{the determinant is scale of geometric transformations. if it is 0 it means collapsed into a lower dimension with parts collapsed to 0}$$
1: determinant equal to product of eigenvalues  
2: det(AB) = det(A)det(B)  
3: the determinant of L on vector space V is the determinant of [L]_B where B is any basis of V  

> $$\text{scaling and adding multiples of identity matrix}$$

property: if A has eigenvalues $\lambda_1 ... \lambda_n$ and eigenvectors $\vec{b_1} ... \vec{b_n}$ so aA+cI has the same eigenvectors. 

> $$\text{block diagonal and block upper triangular M = $\left( \substack{A \\ 0} \substack{B \\ C}\right)$}$$

$P_{\lambda}(M) = P_{\lambda}(A)*P_{\lambda}(C)$

if diagonal: if $\vec{a_i}$ is the eigenvectors of A and $\vec{c_i}$ is the eigenvectors of C then the external direct sum of those two is the eigenvectors of M  

if upper block: 
$$
M \begin{pmatrix} x \\ y \end{pmatrix} = 
\lambda \begin{pmatrix} x \\ y \end{pmatrix}
\Rightarrow
\begin{cases}
(A - \lambda I)x + B y = 0,\\
(C - \lambda I)y = 0.
\end{cases}
$$  

---

**Case 1:** $\lambda \in \sigma(A)$ and $\lambda \notin \sigma(C)$  

$$
\begin{aligned}
(A - \lambda I)x &= 0,\\
y &= -(C - \lambda I)^{-1} B x.
\end{aligned}
$$  

---

**Case 2:** $\lambda \notin \sigma(A)$ and $\lambda \in \sigma(C)$  

$$
\begin{aligned}
(C - \lambda I)y &= 0,\\
x &= 0.
\end{aligned}
$$  

---

**Case 3:** $\lambda \in \sigma(A)$ and $\lambda \in \sigma(C)$  

$$
\begin{aligned}
(A - \lambda I)x + B y &= 0,\\
(C - \lambda I)y &= 0.
\end{aligned}
$$  

> $$\text{if A and B are diagonizable and commuting(AB = BA) then }\\
\text{there is a common P (common set of eigenvectors) such that $A=PD_AP^{-1}$ and $B=PD_BP^{-1}$}\\
\text{also $A(B(v)) = B(A(v))$}
$$

## powers

>$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

>$$e^{a+b} = e^a \cdot e^b$$

>$$e^{i\theta} = \cos(\theta) + i\sin(\theta)$$

>$$e^{a+bi} = e^a(\cos(b) + i\sin(b))$$

>$$e^A = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots = \sum_{n=0}^{\infty} \frac{A^n}{n!}$$

>$$\frac{dY}{dt} = AY \text{ with } Y(0) = I \text{ has solution } Y(t) = e^{At}$$

>$$\text{If } A = PDP^{-1} \text{ then } e^A = Pe^DP^{-1} \\
\text{where } e^D = \begin{pmatrix} e^{\lambda_1} & 0 & \cdots & 0 \ 0 & e^{\lambda_2} & \cdots & 0 \ \vdots & \vdots & \ddots & \vdots \ 0 & 0 & \cdots & e^{\lambda_n} \end{pmatrix}$$

>$$\text{If } AB = BA \text{ then } e^{A+B} = e^A e^B = e^B e^A$$

>$$\text{Eigenvectors of } e^A = \text{eigenvectors of } A$$

>$$\text{Eigenvalues of } e^A = e^{\text{eigenvalues of } A}$$

>$$\text{If } f(z) = a_0 + a_1z + a_2z^2 + \cdots \text{ and } A = PDP^{-1} \text{ then } f(A) = Pf(D)P^{-1}$$

>$$(L - \lambda I)^p \xi = 0 \text{ but } (L - \lambda I)^{p-1} \xi \neq 0$$
>$$e^{Lt} \xi = e^{\lambda t} \sum_{k=0}^{p-1} \frac{t^k (L - \lambda I)^k \xi}{k!}$$
>$$f(L)\xi = \sum_{k=0}^{p-1} a_k (L - \lambda I)^k \xi$$
>$$L^n \xi = [(L - \lambda I) + \lambda I]^n \xi = \sum_{k=0}^{p-1} \binom{n}{k} \lambda^{n-k} (L - \lambda I)^k \xi$$
>$$\text{Jordan block: } \begin{pmatrix} \lambda & 1 & 0 & \cdots & 0 \ 0 & \lambda & 1 & \cdots & 0 \ 0 & 0 & \lambda & \cdots & 0 \ \vdots & \vdots & \vdots & \ddots & \vdots \ 0 & 0 & 0 & \cdots & \lambda \end{pmatrix}$$
>$$\text{Power space dimension for } \lambda = m_a(\lambda)$$
>$$\text{Power vectors for different eigenvalues are linearly independent}$$

### inner products

> $$\text{the standard inner product of two vectors $\vec{x}$ and $\vec{y}$ in $R^n$ is $\langle\vec{x}|\vec{y}\rangle = \vec{x}^T\vec{y}=x_1y_1 + ... + x_ny_n$}$$ 

> $$\text{a real inner product satisfies the following 4 properties: }$$

properties:  
1: linearity in first factor $\langle c_1\vec{x}+c_2\vec{y}|\vec{z}\rangle = c_1\langle\vec{x}|\vec{z}\rangle + c_2\langle\vec{y}|\vec{z}\rangle$   
2: linearity in second factor $\langle\vec{x}|c_1\vec{y}+c_2\vec{z}\rangle = c_1\langle\vec{x}|\vec{y}\rangle + c_2\langle\vec{x}|\vec{z}\rangle$   
3: symmetry $\langle\vec{x}|\vec{y}\rangle = \langle\vec{y}|\vec{x}\rangle$  
4: positivity if $x \neq 0$ then $\langle x|x \rangle > 0$


bilinear means a funciton of two vectors that is linear in each other. a bilinear form is positive if it satiesfies property 2 and symmetric if it satisfies property 3. a inner products is a  positive, symmetric real valued bilinear form. A real vector space on which a inner product is defined is called an inner product space

> $$\text{the norm of a vector $\vec{x}$ is $|\vec{x}| = \sqrt{\langle\vec{x}|\vec{x}\rangle} = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$}$$


> $$|\langle\vec{x}|\vec{y}\rangle |\leq |\vec{x}||\vec{y}|$$

proof:  

$$\begin{aligned}
\text{if x and y are LD: } \\
\text{let } y &= cx\\
LHS: |\langle\vec{x}|c\vec{x}\rangle| &= c |\langle\vec{x}|\vec{x}\rangle| \\
RHS: |\vec{x}||c\vec{x}| &= c |\vec{x}|^2 = LHS\\
\text{if x and y are LI: } \\
\text{let } v_t &= x + ty \\
v_t \text{ is not 0 due to x and y being LI}\\
0 < |v_t|^2 &= \langle v_t|v_t\rangle = \langle x + ty|x + ty\rangle = t^2 \langle y|y\rangle + 2t\langle x|y\rangle + \langle x|x\rangle \\
\text{the equation hold for all t, plugging in } t&= -\frac{\langle x|y\rangle}{\langle y|y\rangle}\\
0 &< \frac{\langle x|y\rangle^2}{\langle y|y\rangle} -2\frac{\langle x|y\rangle^2}{\langle y|y\rangle}+ \langle x|x\rangle \\
0 &< \langle x|y\rangle^2 - 2\langle x|y\rangle^2 +\langle x|x\rangle\langle y|y\rangle \\
\langle x|y\rangle^2 &< |x|^2|y|^2 \\
\langle x|y\rangle &< |x||y|

\end{aligned}$$


> $$\text{the angle between $\vec{x}$ and $\vec{y}$ is $\theta \in [0, \pi]$, $\cos\theta=\frac{\langle\vec{x} | \vec{y}\rangle}{|\vec{x}||\vec{y}|}$}$$

> $$\text{complex inner product: }\langle\vec{x} | \vec{y}\rangle = \bar{\vec{x}}^T \vec{y} = \bar{x_1}y_1 + ... + \bar{x_n} y_n$$

$\bar{x_i}$ flips the imaginary part so a + bi becomes a - bi. this is done so $\langle\vec{x} | \vec{x}\rangle$ becomes real and positive. 

4 properties of complex inner product:  
1: conjugate linearity in first factor $\langle c_1\vec{x}+c_2\vec{y}|\vec{z}\rangle = \bar{c_1}\langle\vec{x}|\vec{z}\rangle + \bar{c_2}\langle\vec{y}|\vec{z}\rangle$   
2: linearity in second factor $\langle\vec{x}|c_1\vec{y}+c_2\vec{z}\rangle = c_1\langle\vec{x}|\vec{y}\rangle + c_2\langle\vec{x}|\vec{z}\rangle$   
3: conjugate symmetry $\langle\vec{x}|\vec{y}\rangle = \overline{\langle\vec{y}|\vec{x}\rangle}$  
4: positivity if $x \neq 0$ then $\langle x|x \rangle > 0$

property 1 is due to $\bar{ab} = \bar{a}\bar{b}$

a function of two vectors conjugate linear in the first factor and linear in the second is called sesquilinear. a sesquilinear form that is conjugate symmetric is called Hermitian.  

if V is a complex vector space, then an inner product on V is any complex valued function $\langle\vec{x} | \vec{y}\rangle$ that satisfies property 1-4. which is a positive Hermitian form. A complex vector space on which an inner product is defined is called a complex inner product space  

the real Schwarz inequality generalizes to complex inner products

> $$\text{a bra is $\langle x|$ which means the conjugate transpose of x}$$

the column vector becomes a row. real valued x as included because they have no i component

> $$\text{a ket is $| y \rangle$ which means the column vector y}$$

y and $| y \rangle$ can be used interchangebly

> $$\langle x | y\rangle = \overline{x^T}Gy \text{ where } G_{ij} = \langle e_i | e_j\rangle \text{ and }  \langle x | = \overline{x^T}G$$

(conjugate is for the complex case in real case just gets ignored)

G matrix is called the metric. 
proof:  

$$\begin{aligned}
\langle x | y\rangle  &= \langle \sum_i x_ie_i | \sum_j y_je_j\rangle  \\
\text{by laws of linearity} & \text{ and definition of G} \\
\langle x | y\rangle  &= \sum_{i,j}x_iG_{ij}y_j  \\
\langle x | y\rangle  &=(x_1,\dots,x_n)\,G\,\begin{pmatrix} y_1\\ \vdots\\ y_n \end{pmatrix} = x^T G y

\end{aligned}$$

> $$\langle x_B | y_B\rangle = \overline{x^T}_BG_By_B \text{ where } G_{ij} = \langle b_i | b_j\rangle \text{ and }  {}_B\langle x | = \overline{x^T_B}G_B$$

> $$\text{given a vector space V the dual space $V^*$ is the space of linear transformation from V to scalors }$$
elements of $V^*$ can be called covectors