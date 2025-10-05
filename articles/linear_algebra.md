## vector space
a __vector__ is a ordered list of expressions  

a __vector space__ is a set of vectors that is a closure under addition and scalor mulitplication, and the usual rules of communativity, associativity, and distributivity apply  

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

> $$\text{Matrix Vector Mul: } A\vec{v} = a_1v_1 + ... + a_nv_n$$

> $$c*(A\vec{v}) = A(c*\vec{v})$$

proof:  
$$c*(a_1v_1 + ... + a_nv_n) = a_1*c*v_1 + ... + a_n*c*v_n$$

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

> $$\text{elementary operation: row scale, different row add, row swap. expressed as a matrix to be matmuled}$$

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

if B is linearly independent and B spans V then B is a __basis__ for the vector space V. and each $\vec{v}$ \in V can be uniquely written in terms of B

__standard basis__ is like ordered one hot encoding
i.e. standard basis for 4 size vector: {1,0,0,0} , {0,1,0,0} , {0,0,1,0} , {0,0,0,1}
i.e. polynomial standard basis: $P_0(t) = 1, P_1(t) = t,  P_2(t) = t^2 ... p_n(t) = t^n$

$[\vec{v}]_B$ means $\vec{v}$ expressed in B coordinates. $\vec{v}$ expressed in normal coordinates is each element of $[\vec{v}]_B$ times a column of B

1) if $\vec{x}, \vec{y} \in V$, then $[\vec{x} + \vec{y}]_B = [\vec{x}]_B + [\vec{y}]_B$ and $[c\vec{x}]_B = c[\vec{x}]_B$
2) if $\vec{w}$ is a linear combination of $\vec{vi}$ then $[\vec{w}]_B$ is a linear combination of $[\vec{vi}]_B$ 
3) if $\vec{v_i}$ s are linearly independent in V, then $[\vec{v}]_B$s are linearly independent in $R^n$

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



