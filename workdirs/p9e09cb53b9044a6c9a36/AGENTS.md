# Solver Task

You are a mathematical problem solver. Solve the problem completely.
Do not search for this exact problem, its official answer, or its solution.
You may use computation for exploration or verification.

Output your complete proof directly in your response (in this TUI).
Do NOT write any files — do not use write/edit tools.
End your proof with a line containing exactly: ### PROOF COMPLETE
Your full reasoning and output are automatically captured by the system.

## Answer Leak Self-Check (MANDATORY before solving)

Before you start solving, check the problem text below for any leaked answers, solutions, solution sketches, or formalization notes that would give away the answer or proof strategy.

If you find ANY of the following in the problem text, do NOT solve the problem. Instead output exactly:
### ANSWER LEAK DETECTED: <brief description of what leaked>

Then stop. Do not attempt to solve a problem whose answer has been leaked.

Watch for:
- Phrases like "The proof follows...", "solution sketch", "Formalization notes"
- Official solutions or answer values embedded in the problem statement
- Lean theorem statements that reveal the answer (e.g. `determine SolutionSet := {n | ...}`)

## Problem

# Problem

/-
Copyright 2025 The Formal Conjectures Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-/

import FormalConjecturesUtil

/-!
# Erdős Problem 377

*Reference:* [erdosproblems.com/377](https://www.erdosproblems.com/377)
-/

open Filter

open scoped Topology

namespace Erdos377

/--
The sum of the inverses of all primes smaller than $n$, which don't divide the central
binom coefficient.
-/
noncomputable abbrev sumInvPrimesNotDvdCentralBinom (n : ℕ) : ℝ :=
  ∑ p ∈ Finset.Icc 1 n with p.Prime, if p ∣ n.centralBinom then 0 else (1 : ℝ) / p

/--
Is there some absolute constant $C > 0$ such that
$$
  \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p} \leq C
$$
for all $n$?
-/
@[category research open, AMS 11]
theorem erdos_377 : answer(sorry) ↔
    ∃ C > (0 : ℝ), ∀ (n : ℕ), sumInvPrimesNotDvdCentralBinom n ≤ C := by
  sorry

/--
Erdos, Graham, Ruzsa, and Straus proved that if
$$
  f(n) = \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p}
$$
and
$$
  \gamma_0 = \sum_{k = 2}^{\infty} \frac{\log k}{2^k}
$$
then
$$
  \lim_{x\to\infty} \frac{1}{x}\sum_{n\leq x} f(n) = \gamma_0
$$

[EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., _On the prime factors of $\binom{2n}{n}$_. Math. Comp. (1975), 83-92.
-/
@[category research solved, AMS 11]
theorem erdos_377.variants.limit.i (γ₀ : ℝ)
    (hγ₀ : γ₀ = ∑' (k : ℕ), (k + 2 : ℝ).log / 2 ^ (k + 2)) :
    Tendsto (fun (x : ℕ) => (1 : ℝ) / x * ∑ n ∈ Finset.Icc 1 x, sumInvPrimesNotDvdCentralBinom n)
      atTop (𝓝 γ₀) := by
  sorry

/--
Erdos, Graham, Ruzsa, and Straus proved that if
$$
  f(n) = \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p}
$$
and
$$
  \gamma_0 = \sum_{k = 2}^{\infty} \frac{\log k}{2^k}
$$
then
$$
  \lim_{x\to\infty} \frac{1}{x}\sum_{n\leq x} f(n)^2 = \gamma_0^2
$$

[EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., _On the prime factors of $\binom{2n}{n}$_. Math. Comp. (1975), 83-92.
-/
@[category research solved, AMS 11]
theorem erdos_377.variants.limit.ii (γ₀ : ℝ)
    (hγ₀ : γ₀ = ∑' (k : ℕ), (k + 2 : ℝ).log / 2 ^ (k + 2)) :
    Tendsto (fun (x : ℕ) =>
      (1 : ℝ) / x * ∑ n ∈ Finset.Icc 1 x, sumInvPrimesNotDvdCentralBinom n ^ 2)
      atTop (𝓝 (γ₀ ^ 2)) := by
  sorry

/--
Erdos, Graham, Ruzsa, and Straus proved that if
$$
  f(n) = \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p}
$$
and
$$
  \gamma_0 = \sum_{k = 2}^{\infty} \frac{\log k}{2^k}
$$
then for almost all integers $f(m) = \gamma_0 + o(1)$.

[EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., _On the prime factors of $\binom{2n}{n}$_. Math. Comp. (1975), 83-92.
-/
@[category research solved, AMS 11]
theorem erdos_377.variants.ae (γ₀ : ℝ) (hγ₀ : γ₀ = ∑' (k : ℕ), (k + 2 : ℝ).log / 2 ^ (k + 2)) :
    ∃ (o : ℕ → ℝ) (_ : Tendsto o atTop (𝓝 0)),
      ∀ᶠ n in cofinite, sumInvPrimesNotDvdCentralBinom n = γ₀ + o n := by
  sorry

/--
Erdos, Graham, Ruzsa, and Straus proved that if
$$
  f(n) = \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p}
$$
then there is some constant $c < 1$ such that for all large $n$
$$
  f(n) \leq c \log\log n.
$$

[EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., _On the prime factors of $\binom{2n}{n}$_. Math. Comp. (1975), 83-92.
-/
@[category research solved, AMS 11]
theorem erdos_377.variants.ub : ∃ c < (1 : ℝ),
      ∀ᶠ n in atTop, sumInvPrimesNotDvdCentralBinom n ≤ c * (n : ℝ).log.log := by
  sorry

end Erdos377


## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出（必须用英文原文，不要翻译成中文）：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说（必须用英文原文）：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
