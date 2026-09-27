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
Copyright 2026 The Formal Conjectures Authors.

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
# Erdős Problem 649

*References:*
- [erdosproblems.com/649](https://www.erdosproblems.com/649)
- [Ma35] Mahler, Kurt, *Über den grössten Primteiler spezieller Polynome zweiten Grades*. Archiv
  für math. og naturvid (1935).
- [Ro64b] Rotkiewicz, André, *Sur les nombres naturels $n$ et $k$ tels que les nombres $n$ et $nk$
  sont à la fois pseudopremiers*. Atti Accad. Naz. Lincei Rend. Cl. Sci. Fis. Mat. Nat. (8)
  (1964), 816-818.
-/

namespace Erdos649

/--
Let $P(m)$ denote the greatest prime factor of $m$. Is it true that, for any two primes $p,q$,
there exists some integer $n$ such that $P(n)=p$ and $P(n+1)=q$?

In fact, the answer to this question as written is easily seen to be no, since there are no
solutions to $2^k\equiv -1\pmod{7}$, and hence this fails with $p=2$ and $q=7$. It is possible
that Erdős meant to exclude such obstructions, by amending this to 'odd primes' or 'all
sufficiently large primes' or such.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos649.lean"]
theorem erdos_649 : answer(False) ↔
    ∀ p q : ℕ, p.Prime → q.Prime →
      ∃ n : ℕ, n.maxPrimeFac = p ∧ (n + 1).maxPrimeFac = q := by
  sorry

/--
In fact, the answer to this question as written is easily seen to be no, since there are no
solutions to $2^k\equiv -1\pmod{7}$, and hence this fails with $p=2$ and $q=7$.
-/
@[category textbook, AMS 11]
theorem erdos_649.variants.no_solution_two_seven :
    ¬ ∃ n : ℕ, n.maxPrimeFac = 2 ∧ (n + 1).maxPrimeFac = 7 := by
  -- `maxPrimeFac m` is the greatest element of the (bounded, nonempty) set of prime factors of `m`.
  have hbdd : ∀ m : ℕ, 1 < m → BddAbove {p : ℕ | p.Prime ∧ p ∣ m} := fun m hm ↦
    ⟨m, fun p ⟨_, hp⟩ ↦ Nat.le_of_dvd (by omega) hp⟩
  have hne : ∀ m : ℕ, 1 < m → {p : ℕ | p.Prime ∧ p ∣ m}.Nonempty := by
    intro m hm
    simpa [Set.Nonempty, ← Nat.ne_one_iff_exists_prime_dvd] using by omega
  have hdvd : ∀ m : ℕ, 1 < m → m.maxPrimeFac ∣ m := fun m hm ↦
    (Nat.sSup_mem (hne m hm) (hbdd m hm)).2
  have hle : ∀ m p : ℕ, 1 < m → p.Prime → p ∣ m → p ≤ m.maxPrimeFac := fun m p hm hp hpd ↦
    le_csSup (hbdd m hm) ⟨hp, hpd⟩
  rintro ⟨n, hn, hn'⟩
  have h1n : 1 < n := by
    have := (Nat.one_lt_maxPrimeFac_iff n).mp (by omega)
    omega
  -- Since `2` is the greatest prime factor of `n`, it is the only one, so `n` is a power of `2`.
  obtain ⟨k, hpow⟩ : ∃ k, n = 2 ^ k :=
    ⟨_, Nat.eq_prime_pow_of_unique_prime_dvd (by omega)
      (fun {q} hq hqd ↦ le_antisymm (hn ▸ hle n q h1n hq hqd) hq.two_le)⟩
  -- On the other hand `7` divides `n + 1`, i.e. `2 ^ k ≡ -1 (mod 7)`.
  have h7 : 7 ∣ n + 1 := hn' ▸ hdvd (n + 1) (by omega)
  -- This is impossible: `2 ^ k` is congruent to `1`, `2` or `4` modulo `7`, never to `6`.
  have hmod : 2 ^ k % 7 = 2 ^ (k % 3) % 7 := by
    conv_lhs => rw [← Nat.div_add_mod k 3, pow_add, pow_mul]
    rw [Nat.mul_mod, Nat.pow_mod]
    norm_num
  have hk3 : k % 3 < 3 := Nat.mod_lt _ (by norm_num)
  interval_cases h : k % 3 <;> omega

/--
Even with such amendments, this problem is false in a strong sense: Alan Tong has provided the
following elegant elementary proof that, for any given prime $p$, there are infinitely many
primes $q$ such that this statement is false: let $m$ be the product of all primes $\leq p$, and
choose a prime $q$ congruent to $-1$ modulo $4m$. If $p$ is the greatest prime divisor of $n$
then, using quadratic reciprocity, every prime divisor of $n$ is a quadratic residue modulo $q$,
and hence $n$ is a quadratic residue modulo $q$. On the other hand, since $q\equiv 3\pmod{4}$ we
know that $-1$ is not a quadratic residue modulo $q$, and hence $n\not\equiv -1\pmod{q}$, so it
is impossible for $q\mid n+1$.
-/
@[category research solved, AMS 11]
theorem erdos_649.variants.tong (p : ℕ) (hp : p.Prime) :
    {q : ℕ |
      q.Prime ∧ ¬ ∃ n : ℕ, n.maxPrimeFac = p ∧ (n + 1).maxPrimeFac = q}.Infinite := by
  sorry

/--
Tong asks whether, for any given odd prime $q$, there are infinitely many primes $p$ such that
there is no integer $n$ with $P(n)=p$ and $P(n+1)=q$.
-/
@[category research open, AMS 11]
theorem erdos_649.variants.tong_question : answer(sorry) ↔
    ∀ q : ℕ, q.Prime → Odd q →
      {p : ℕ |
        p.Prime ∧ ¬ ∃ n : ℕ, n.maxPrimeFac = p ∧ (n + 1).maxPrimeFac = q}.Infinite := by
  sorry

/--
Sampaio independently observed that the answer t

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
