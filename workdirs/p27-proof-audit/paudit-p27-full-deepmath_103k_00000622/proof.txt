# Proof that the statement is FALSE

## Statement

Determine whether the following is true for any finite field extension $L/K$:

$$\min_{\substack{\{\alpha_1, \ldots, \alpha_n\} \\ L = K(\alpha_1, \ldots, \alpha_n)}} \left(\prod_{i=1}^n [K(\alpha_i): K] \right) = [L:K].$$

## Answer

The statement is **FALSE**. We provide an explicit counterexample.

## Lower bound (always holds)

For any generating set $\{\alpha_1, \ldots, \alpha_n\}$ with $L = K(\alpha_1, \ldots, \alpha_n)$, by the tower formula:

$$[L:K] = \prod_{i=1}^{n} [K(\alpha_1, \ldots, \alpha_i) : K(\alpha_1, \ldots, \alpha_{i-1})] \leq \prod_{i=1}^{n} [K(\alpha_i):K],$$

since $[K(\alpha_1, \ldots, \alpha_i):K(\alpha_1, \ldots, \alpha_{i-1})] \leq [K(\alpha_i):K]$ (the minimal polynomial of $\alpha_i$ over $K$ may factor over the larger field $K(\alpha_1, \ldots, \alpha_{i-1})$). So $\min \prod [K(\alpha_i):K] \geq [L:K]$ always.

The question is whether equality can always be achieved.

## Counterexample

Let $p$ be any prime. Set $K = \mathbb{F}_p(x, y)$ (rational function field in two variables), and define

$$L = K(\alpha, \beta), \quad \alpha^{p^2} = x, \quad \beta^p = y + \alpha^p.$$

### Step 1: Compute $[L:K] = p^3$.

Since $x$ is transcendental over $\mathbb{F}_p$, the polynomial $t^{p^2} - x$ is irreducible over $K$, so $[K(\alpha):K] = p^2$.

Now $L = K(\alpha)(\beta)$ and $\beta^p = y + \alpha^p = y + x^{1/p} \in K(\alpha)$. The polynomial $t^p - (y + x^{1/p})$ is irreducible over $K(\alpha)$ if and only if $y + x^{1/p} \notin K(\alpha)^p$.

We compute $K(\alpha)^p = \mathbb{F}_p(x^{1/p}, y^p)$ (since $K(\alpha) = \mathbb{F}_p(x^{1/p^2}, y)$ and taking $p$-th powers gives $\mathbb{F}_p(x^{1/p}, y^p)$).

Now $x^{1/p} \in \mathbb{F}_p(x^{1/p}, y^p)$, so $y + x^{1/p} \in \mathbb{F}_p(x^{1/p}, y^p)$ would require $y \in \mathbb{F}_p(x^{1/p}, y^p)$. But $y \notin \mathbb{F}_p(x^{1/p}, y^p)$ because $y$ is transcendental over $\mathbb{F}_p(x^{1/p})$ and $[\mathbb{F}_p(y):\mathbb{F}_p(y^p)] = p$ shows $y \notin \mathbb{F}_p(y^p)$.

Therefore $t^p - (y + x^{1/p})$ is irreducible over $K(\alpha)$, giving $[L:K(\alpha)] = p$ and

$$[L:K] = p^2 \cdot p = p^3.$$

### Step 2: $L/K$ is purely inseparable of exponent 2.

Every element of $L$ satisfies a $p^2$-power in $K$: $\alpha^{p^2} = x \in K$ and $\beta^{p^2} = (y + \alpha^p)^p = y^p + \alpha^{p^2} = y^p + x \in K$. So $L^{p^2} \subseteq K$, meaning the exponent is at most 2. Since $\alpha^p = x^{1/p} \notin K$, the exponent is exactly 2.

**Consequence:** Every element $\gamma \in L$ has $[K(\gamma):K] \leq p^2$ (since $\gamma^{p^2} \in K$, the minimal polynomial divides $t^{p^2} - \gamma^{p^2}$). Since $p^2 < p^3 = [L:K]$, the extension $L/K$ is **not simple**, so any generating set requires at least 2 elements.

### Step 3: Structure of $K_1 = K(L^p)$.

Compute $L^p = K^p(\alpha^p, \beta^p) = \mathbb{F}_p(x^p, y^p, x^{1/p}, y + x^{1/p})$. Since $y = \beta^p - \alpha^p \in K(L^p)$ and $x^{1/p} = \alpha^p \in K(L^p)$:

$$K_1 := K(L^p) = K(x^{1/p}) = \mathbb{F}_p(x^{1/p}, y).$$

This has $[K_1:K] = p$ (since $t^p - x$ is the minimal polynomial of $x^{1/p}$ over $K$).

### Step 4: Classification of element degrees.

- **Degree $p$ elements:** An element $\gamma$ has $[K(\gamma):K] = p$ iff $\gamma^p \in K$ and $\gamma \notin K$, i.e., $\gamma \in K_1 \setminus K$. Since $[K_1:K] = p$ is prime, every such $\gamma$ satisfies $K(\gamma) = K_1$.

- **Degree $p^2$ elements:** An element $\gamma$ has $[K(\gamma):K] = p^2$ iff $\gamma^p \notin K$ but $\gamma^{p^2} \in K$ (level exactly 2). Such $\gamma$ satisfies $\gamma^p \in L^p$, hence $\gamma^p \in K_1$.

### Step 5: No generating set achieves product $p^3$.

We need $\prod [K(\gamma_i):K] = p^3 = [L:K]$. Consider all possibilities:

**Case 1: Two generators with degrees $p$ and $p^2$ (product $= p^3$).**

Let $\gamma_1$ have degree $p$ and $\gamma_2$ have degree $p^2$. By Step 4, $K(\gamma_1) = K_1$ and $\gamma_2^p \in K_1 = K(\gamma_1)$. Therefore the minimal polynomial of $\gamma_2$ over $K(\gamma_1)$ divides $t^p - \gamma_2^p$, which has degree $p$. So:

$$[K(\gamma_1, \gamma_2):K] = [K(\gamma_1, \gamma_2):K(\gamma_1)] \cdot [K(\gamma_1):K] \leq p \cdot p = p^2 < p^3 = [L:K].$$

Thus $\{\gamma_1, \gamma_2\}$ **cannot generate** $L$.

**Case 2: Three (or more) generators all of degree $p$ (product $= p^3$).**

All generators lie in $K_1$, so $K(\gamma_1, \gamma_2, \gamma_3) \subseteq K_1 \neq L$. Cannot generate $L$.

**Case 3: Any other combination.**

Any generating set must include at least one element of degree $p^2$ (otherwise all generators are in $K_1$). If the product is to be $\leq p^3$, the only options are those in Cases 1 and 2, both of which fail. Every other option has product $\geq p^4$.

### Step 6: The minimum product is $p^4$.

The generating set $\{\alpha, \beta\}$ has $[K(\alpha):K] = p^2$ and $[K(\beta):K] = p^2$ (since $\beta^p = y + x^{1/p} \notin K$ and $\beta^{p^2} = y^p + x \in K$), giving product $p^2 \cdot p^2 = p^4$.

By Step 5, no generating set achieves product $p^3$, and by Step 2, no single generator suffices. So:

$$\min \prod_{i=1}^{n} [K(\alpha_i):K] = p^4 > p^3 = [L:K].$$

## Conclusion

The statement is **false**. For the extension $L = K(\alpha, \beta)$ with $K = \mathbb{F}_p(x,y)$, $\alpha^{p^2} = x$, $\beta^p = y + \alpha^p$, we have $[L:K] = p^3$ but the minimum product over all generating sets is $p^4 > p^3$.

The essential reason is that in a purely inseparable extension of exponent 2, every degree-$p^2$ element $\gamma$ has $\gamma^p \in K_1 = K(L^p)$, and every degree-$p$ element generates $K_1$. So adjoining a degree-$p$ element first always causes the minimal polynomial of any degree-$p^2$ element to drop from degree $p^2$ to degree $p$, making it impossible to achieve the product $p \cdot p^2 = p^3$.

$$\boxed{\text{The statement is false.}}$$

### PROOF COMPLETE
