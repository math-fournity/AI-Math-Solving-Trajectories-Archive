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

/-! # Hartshorne's conjecture on Vector Bundles

*References:*
* [Har1974] R. Hartshorne, [Varieties of small codimension in projective space](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-80/issue-6/Varieties-of-small-codimension-in-projective-space/bams/1183535999.full).
* [MO2010] [Evidences on Hartshorne's conjecture? References?](https://mathoverflow.net/questions/13990/evidences-on-hartshornes-conjecture-references)
-/

namespace HartshorneConjecture

open HartshorneConjecture

universe u

open CategoryTheory Limits MvPolynomial AlgebraicGeometry

variable (S : Scheme.{u})

namespace AlgebraicGeometry.Scheme

attribute [local instance] CategoryTheory.Types.instConcreteCategory Types.instFunLike

-- TODO(lezeau): explain/investigate why the following two instances are needed.

local instance (X : TopologicalSpace.Opens S) :
    ((Opens.grothendieckTopology S).over X).WEqualsLocallyBijective (Type u) :=
  CategoryTheory.GrothendieckTopology.instWEqualsLocallyBijectiveTypeHomObjForget
    ((Opens.grothendieckTopology S).over X)

local instance (X : TopologicalSpace.Opens S) :
    ((Opens.grothendieckTopology S).over X).WEqualsLocallyBijective (AddCommGrpCat.{u}) :=
  inferInstance

/--
A vector bundle over a scheme `S` is a locally free $\mathcal{O}_S$-module of finite rank.
-/
structure VectorBundles where
  carrier : S.Modules
  rank : ℕ
  isLocallyFreeFiniteConstantRank : SheafOfModules.IsVectorBundleWithRank
    (J := Opens.grothendieckTopology S) carrier rank

instance (S : Scheme) : Coe S.VectorBundles S.Modules where
  coe 𝓕 := 𝓕.carrier

/--
Vector bundles form a category.
-/
instance : Category S.VectorBundles :=
  inferInstanceAs <| Category <| InducedCategory _ VectorBundles.carrier

def VectorBundles.toModule : S.VectorBundles ⥤ S.Modules where
  obj 𝓕 := 𝓕.carrier
  map f := f.hom

@[category API, AMS 14]
theorem hasFiniteCoproductsVectorBundles : HasFiniteCoproducts S.VectorBundles := by
  sorry

instance : HasFiniteCoproducts S.VectorBundles :=
  hasFiniteCoproductsVectorBundles S

variable {S} in
/--
A splitting of a vector bundle `𝓕` is a non-trivial direct sum decomposition of `𝓕`
-/
structure VectorBundles.Splitting (𝓕 : S.VectorBundles) (ι : Type) [Fintype ι] [Nonempty ι] where
  components : ι → S.VectorBundles
  iso : 𝓕 ≅ ∐ components
  non_trivial : ∀ i, IsEmpty (components i ≅ 𝓕)

instance {S : Scheme} (𝓕 : S.VectorBundles) (ι : Type) [Fintype ι] [Nonempty ι] :
    CoeOut (𝓕.Splitting ι) (ι → S.VectorBundles) where
  coe s := s.components

end AlgebraicGeometry.Scheme
-- TODO(lezeau): here we would really need some sanity checks and easier results.

open AlgebraicGeometry.Scheme

/--
There are no indecomposable vector bundles of rank 2 on $\mathbb{P}^n$ for $n \ge 7$.
This is Conjecture 6.3 in [Har1974].
-/
@[category research open, AMS 14]
theorem harthshorne_conjecture (n : ℕ) (hn : 7 ≤ n)
    (𝓕 : VectorBundles ℙ(Fin (n + 1); Spec (.of ℂ)))
    (h𝓕 : 𝓕.rank = 2) :
    Nonempty (𝓕.Splitting (Fin 2)) := by
  sorry

end HartshorneConjecture


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
