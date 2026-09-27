# IMO 1974 Problem 5

**Problem.** What are the possible values of
$$S = \frac{a}{a+b+d} + \frac{b}{a+b+c} + \frac{c}{b+c+d} + \frac{d}{a+c+d}$$
as $a,b,c,d$ range over the positive real numbers?

**Answer.** The set of possible values is the open interval $(1,\,2)$.

---

## Setup

Let $T = a+b+c+d > 0$. Each denominator is $T$ minus one variable:
$$S = \frac{a}{T-c} + \frac{b}{T-d} + \frac{c}{T-a} + \frac{d}{T-b}.$$
Every denominator is positive since $a,b,c,d > 0$.

---

## Step 1 — Upper bound: $S < 2$

**Claim.** For positive reals, $\dfrac{a}{T-c} < \dfrac{a+c}{T}$.

*Proof.* Cross-multiplying (all quantities positive):
$$aT < (a+c)(T-c) = (a+c)T - c(a+c),$$
which simplifies to $c(a+c) < cT$, i.e. $a+c < T$, i.e. $b+d > 0$. True since $b,d>0$. $\square$

Applying the same argument cyclically (each denominator misses one variable; pair the numerator with the missing variable):
$$\frac{a}{T-c} < \frac{a+c}{T},\qquad \frac{c}{T-a} < \frac{a+c}{T},\qquad \frac{b}{T-d} < \frac{b+d}{T},\qquad \frac{d}{T-b} < \frac{b+d}{T}.$$

Summing all four inequalities:
$$S < \frac{2(a+c) + 2(b+d)}{T} = \frac{2T}{T} = 2. \qquad\blacksquare$$

---

## Step 2 — Lower bound: $S > 1$

**Claim.** For positive reals, $\dfrac{a}{T-c} > \dfrac{a}{T}$.

*Proof.* Since $c > 0$, we have $T - c < T$, and with $a > 0$ the inequality follows. $\square$

Applying this to every term:
$$\frac{a}{T-c} > \frac{a}{T},\quad \frac{b}{T-d} > \frac{b}{T},\quad \frac{c}{T-a} > \frac{c}{T},\quad \frac{d}{T-b} > \frac{d}{T}.$$

Summing:
$$S > \frac{a+b+c+d}{T} = \frac{T}{T} = 1. \qquad\blacksquare$$

Combining Steps 1 and 2: **$1 < S < 2$** for all positive $a,b,c,d$.

---

## Step 3 — Every value in $(1,2)$ is attained

We exhibit two continuous one-parameter families whose ranges together cover $(1,2)$.

### Path A: $a = c = t,\; b = d = 1$, $t > 0$

$$f(t) = \frac{2t}{t+2} + \frac{2}{2t+1}.$$

- $f$ is continuous on $(0,\infty)$.
- $f(t) \to 2$ as $t \to 0^{+}$ and as $t \to \infty$.
- $f'(t) = \dfrac{4}{(t+2)^2} - \dfrac{4}{(2t+1)^2} = 0 \iff (t+2)^2 = (2t+1)^2 \iff t = 1$ (positive solution).
- $f(1) = \tfrac{2}{3} + \tfrac{2}{3} = \tfrac{4}{3}$, the global minimum.

So $f$ maps $(0,\infty)$ onto $\bigl[\tfrac{4}{3},\,2\bigr)$, attaining $\tfrac{4}{3}$ at $t=1$ and approaching $2$ (never reaching it).

### Path B: $a = b = t,\; c = d = 1$, $t > 0$

$$g(t) = \frac{2t}{2t+1} + \frac{2}{t+2}.$$

- $g$ is continuous on $(0,\infty)$.
- $g(t) \to 1$ as $t \to 0^{+}$ and as $t \to \infty$.
- $g'(t) = \dfrac{2}{(2t+1)^2} - \dfrac{2}{(t+2)^2} = 0 \iff (2t+1)^2 = (t+2)^2 \iff t = 1$.
- $g(1) = \tfrac{2}{3} + \tfrac{2}{3} = \tfrac{4}{3}$, the global maximum.

So $g$ maps $(0,\infty)$ onto $\bigl(1,\,\tfrac{4}{3}\bigr]$, attaining $\tfrac{4}{3}$ at $t=1$ and approaching $1$ (never reaching it).

### Union

$$\bigl[\tfrac{4}{3},\,2\bigr) \;\cup\; \bigl(1,\,\tfrac{4}{3}\bigr] = (1,\,2).$$

Every value in $(1,2)$ is achieved by one of the two paths, and by Steps 1–2 no value outside $[1,2]$ is achievable (with $1$ and $2$ themselves excluded as strict bounds).

---

## Conclusion

The set of all possible values is $\boxed{(1,\,2)}$.

QED.
