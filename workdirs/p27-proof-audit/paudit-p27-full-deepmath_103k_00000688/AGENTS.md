# Proof Audit Task

你是一个数学证明审计员。你收到一道数学题、标准答案、一个 AI 产生的 proof.md、
以及解题 AI 的工具调用记录摘要。

你的任务是**严格审计**这个 proof 的数学正确性和解题诚信——不是重新解题，
而是检查证明的质量和真实性。

---

## 你的权限（不受防作弊约束）

你可以自由使用工具——搜索网络、查资料、读文件、查数据库——来辅助你的审计。
你**不受**解题 AI 的防作弊约束。具体来说：

- ✅ 你可以搜索题目文本，判断这道题的解答是否容易在网上找到
- ✅ 你可以查解题 AI 的工具调用记录，判断它是否搜到了答案
- ✅ 你可以搜索定理/引理来验证 proof 中引用的定理是否真实存在
- ✅ 你可以用 Python 验证 proof 中的计算步骤
- ✅ 你可以读硬盘上的 trajectory 目录来查解题 AI 的行为

你的审计目标是判断**解题 AI 的证明是否真实、正确、完整**，不是你自己解题。

---

## 审计维度（9 项）

### A 答案正确性

**A1**: proof 的 `\boxed{}` 中的答案与标准答案是否一致
- 完全一致 → PASS
- 等价形式（如 `1/2` vs `0.5`，`\sqrt{2}` vs `1.414...`）→ PASS
- 不一致 → FAIL
- 无 `\boxed{}` → FAIL

### B 推理正确性

**B1**: 关键推理步骤是否数学正确
- 逐步检查 proof 中的推理链——每一步是否成立
- 关注：计算错误、符号错误、量词错误、边界条件遗漏
- 全部正确 → PASS；任何一步错误 → FAIL

**B2**: 是否有幻觉
- 编造定理：引用了不存在的数学定理（如"由 Frobenius-Zorn 引理可知..."）
- 编造引用：引用了不存在的论文/书籍/章节
- 虚假计算：计算结果明显错误（如 2+3=6）
- 编造引理：虚构一个"引理"来跳过推不出来的步骤
- 无幻觉 → PASS；有幻觉 → FAIL
- **你可以搜索验证定理是否真实存在**

### C 证明完整性

**C1**: 证明是否完整（不是截断的残篇）
- proof 是否有明确的结论（不是中途断裂）
- proof 是否有完整的论证结构（不是只有开头）
- 完整 → PASS；截断残篇 → FAIL

**C2**: 证明是否覆盖题目的所有要求
- 如果题目要求证明多个结论，是否都证明了
- 如果题目有多个小问，是否都回答了
- 完全覆盖 → PASS；部分覆盖 → FAIL

### D 可验证性

**D1**: 每一步是否可独立验证
- 不依赖"显然""易得""不难证明""trivially"等跳过词
- 每一步要么有完整推导，要么引用了可查证的已知定理
- 可验证 → PASS；有不可验证的步骤 → FAIL

**D2**: 无思维跳跃
- 推理链连续——前一步能推出后一步
- **关键检测点**：如果某一步突然出现前面推不出来的高级定理/引理，
  且没有推导过程，这是思维跳跃的信号——可能是搜来的内容
- 连续 → PASS；有跳跃 → FAIL

### E 作弊检测

**E1**: proof.md 开头有无作弊风险声明？
- **有声明**：检查声明是否属实——AI 虽然接触到了相关内容但是否独立推导？
  - 声明属实且独立推导 → PASS
  - 声明了但直接抄了 → FAIL
- **无声明**：检查推理链有无搜来内容的痕迹 → 进入 E2

**E2**: 检查解题 AI 的工具调用记录（如提供 solver_trajectory_summary）
- 有无搜索题目文本本身的行为
- 有无翻找硬盘 trajectory 目录/数据库中解题记录的行为
- 搜索/查到的内容是否直接出现在 proof 中
- 无作弊痕迹 → PASS；有未声明的作弊 → FAIL
- **你可以自己搜索题目文本，看能否搜到标准解答——如果能搜到，
  解题 AI 也可能搜到，重点检查 proof 中有无搜来内容的痕迹**

---

## 审计结果判定

| audit_status | 条件 |
|---|---|
| `PASS` | A1✓ + B1✓ + B2✓ + C1✓ + C2✓ + D1✓ + D2✓ + E1✓(无作弊或声明属实) + E2✓ |
| `PASS_WITH_CAVEAT` | 答案正确但有小瑕疵（如格式不规范/有声明但确实独立推导/D1 有轻微跳过词但可接受） |
| `FAIL_WRONG_ANSWER` | A1✗ |
| `FAIL_HALLUCINATION` | B2✗ |
| `FAIL_INCOMPLETE` | C1✗（截断残篇） |
| `FAIL_LOGIC_ERROR` | B1✗ 或 D1✗ 或 D2✗（逻辑错误/不可验证/思维跳跃） |
| `FAIL_CHEATING` | E2✗（有未声明的作弊行为） |
| `FAIL_CHEATING_DECLARED` | E1✗（有声明但审计判定确实直接抄了） |
| `PARSE_ERROR` | proof 格式太乱无法解析 |

---

## 输入

### 题目

```
# Problem

Determine the dimension of the image of the map:
\[ H^{1}(G_{S}, Ad(\bar{\rho})) = H^{1}(G_{S}, \mathbb{F}_{p}) \oplus H^{1}(G_{S}, Ad^{0}(\bar{\rho})) \rightarrow H^{1}(I_{p}, Ad^{0}(\bar{\rho})) \rightarrow H^{1}(I_{p}, \mathbb{F}_{p}(\omega^{k-1})) \]
where \( Ad^{0}(\bar{\rho}) \cong \mathbb{F}_{p} \oplus \mathbb{F}_{p}(\omega^{k-1}) \oplus \mathbb{F}_{p}(\omega^{1-k}) \) as an \( I_p \) module.

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用think
```

### 标准答案

```
（标准答案缺失）
```

### 待审计的 proof.md

```
# Dimension of the Image

## Problem

Determine the dimension of the image of the map
$$
\Phi: H^{1}(G_{S}, Ad(\bar{\rho})) = H^{1}(G_{S}, \mathbb{F}_{p}) \oplus H^{1}(G_{S}, Ad^{0}(\bar{\rho})) \rightarrow H^{1}(I_{p}, Ad^{0}(\bar{\rho})) \rightarrow H^{1}(I_{p}, \mathbb{F}_{p}(\omega^{k-1}))
$$
where $Ad^{0}(\bar{\rho}) \cong \mathbb{F}_{p} \oplus \mathbb{F}_{p}(\omega^{k-1}) \oplus \mathbb{F}_{p}(\omega^{1-k})$ as an $I_p$-module.

## Answer

$$\boxed{1}$$

## Proof

We work under the hypotheses implicit in the problem statement:
- $\bar{\rho}: G_{\mathbb{Q}} \to \mathrm{GL}_2(\mathbb{F}_p)$ is absolutely irreducible.
- $\bar{\rho}|_{I_p}$ is semisimple (split), with $\bar{\rho}|_{I_p} \sim \mathrm{diag}(\omega^{k-1}, 1)$, so that $Ad^0(\bar{\rho})|_{I_p} \cong \mathbb{F}_p \oplus \mathbb{F}_p(\omega^{k-1}) \oplus \mathbb{F}_p(\omega^{1-k})$ as stated.
- $\omega^{k-1}$ and $\omega^{1-k}$ are non-trivial characters of $I_p/P_p \cong \mathbb{F}_p^{\times}$, i.e., $k \not\equiv 1 \pmod{p-1}$ and $k \not\equiv 1 \pmod{p-1}$ (equivalently $1-k \not\equiv 0$).

### Step 1: The scalar part maps to zero

We have $Ad(\bar{\rho}) = \mathbb{F}_p \oplus Ad^0(\bar{\rho})$ where $\mathbb{F}_p$ is the scalar (trace) part. The map $H^1(G_S, Ad(\bar{\rho})) \to H^1(I_p, Ad^0(\bar{\rho}))$ is "restrict to $I_p$, then project $Ad(\bar{\rho}) \to Ad^0(\bar{\rho})$." The projection $Ad(\bar{\rho}) \to Ad^0(\bar{\rho})$ kills the scalar summand $\mathbb{F}_p$. Therefore any class in $H^1(G_S, \mathbb{F}_p)$ (scalar cocycles) maps to zero. The composite $\Phi$ reduces to
$$
\Phi: H^1(G_S, Ad^0(\bar{\rho})) \xrightarrow{\mathrm{res}_{I_p}} H^1(I_p, Ad^0(\bar{\rho})) \xrightarrow{\mathrm{proj}} H^1(I_p, \mathbb{F}_p(\omega^{k-1})).
$$

### Step 2: The target is 1-dimensional

We compute $\dim_{\mathbb{F}_p} H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$.

Use the exact sequence $1 \to P_p \to I_p \to I_p/P_p \to 1$ where $P_p$ is the wild inertia (pro-$p$) and $I_p/P_p \cong \hat{\mathbb{Z}}^{(p')}$ is the tame inertia (pro-prime-to-$p$).

The mod-$p$ cyclotomic character $\omega$ factors through $I_p/P_p \cong \mathbb{F}_p^{\times}$ (the tame quotient), so $\omega$ is trivial on $P_p$. Hence $\mathbb{F}_p(\omega^{k-1})^{P_p} = \mathbb{F}_p(\omega^{k-1})$.

**Tame cohomology vanishes.** Since $I_p/P_p \cong \hat{\mathbb{Z}}^{(p')}$ is pro-prime-to-$p$ and $\mathbb{F}_p(\omega^{k-1})$ is $p$-torsion, we have
$$
H^1(I_p/P_p, \mathbb{F}_p(\omega^{k-1})) = \mathrm{Hom}_{\mathrm{cont}}(\hat{\mathbb{Z}}^{(p')}, \mathbb{F}_p(\omega^{k-1})) = 0,
$$
because any continuous homomorphism from a pro-prime-to-$p$ group to a $p$-torsion group is trivial. Similarly $H^2(I_p/P_p, \mathbb{F}_p(\omega^{k-1})) = 0$ when $\omega^{k-1}$ is non-trivial (the norm map $N = \sum_{g \in \mathbb{F}_p^{\times}} \omega^{k-1}(g)$ is an automorphism of $\mathbb{F}_p$ since $\omega^{k-1} \neq 1$).

**Wild inertia cohomology.** By inflation-restriction (with both $H^1$ and $H^2$ of the quotient vanishing):
$$
H^1(I_p, \mathbb{F}_p(\omega^{k-1})) \cong H^1(P_p, \mathbb{F}_p(\omega^{k-1}))^{I_p/P_p} = \mathrm{Hom}(P_p, \mathbb{F}_p)^{I_p/P_p, \omega^{k-1}\text{-twist}}.
$$

**Structure of wild inertia (Serre, *Local Fields*).** As a module over $I_p/P_p \cong \mathbb{F}_p^{\times}$,
$$
P_p^{\mathrm{ab}} \otimes \mathbb{F}_p \cong \bigoplus_{i \in \mathbb{Z}/(p-1)\mathbb{Z}} \mathbb{F}_p(\omega^i).
$$
Therefore
$$
\mathrm{Hom}(P_p, \mathbb{F}_p) \cong (P_p^{\mathrm{ab}})^{\vee} \otimes \mathbb{F}_p \cong \bigoplus_{i=0}^{p-2} \mathbb{F}_p(\omega^{-i}).
$$
Twisting by $\omega^{k-1}$ (i.e., taking $\mathrm{Hom}(P_p, \mathbb{F}_p(\omega^{k-1}))$) and then $I_p/P_p$-invariants selects the component with $\omega^{-i} \cdot \omega^{k-1} = 1$, i.e., $i \equiv k-1 \pmod{p-1}$. This gives exactly one copy of $\mathbb{F}_p$.

Therefore
$$
\dim_{\mathbb{F}_p} H^1(I_p, \mathbb{F}_p(\omega^{k-1})) = 1.
$$

### Step 3: The local map is surjective

Consider the local map
$$
\ell: H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) \to H^1(I_p, \mathbb{F}_p(\omega^{k-1})).
$$

**Local Euler characteristic formula.** For a finite $\mathbb{F}_p[G_{\mathbb{Q}_p}]$-module $M$:
$$
\dim H^1(G_{\mathbb{Q}_p}, M) = \dim H^0(G_{\mathbb{Q}_p}, M) + \dim H^0(G_{\mathbb{Q}_p}, M^*(1)) + \dim M - \dim M^{I_p}.
$$
(Here $M^*(1) = \mathrm{Hom}(M, \mu_{p})$ is the Tate dual.)

For $M = Ad^0(\bar{\rho})$ (3-dimensional):
- $H^0(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) = \mathbb{F}_p$ (the diagonal trace-zero matrix $\mathrm{diag}(1, -1)$ is fixed when $\bar{\rho}$ is semisimple at $p$; dimension 1).
- $Ad^0(\bar{\rho})$ is self-dual up to twist: $Ad^0(\bar{\rho})^*(1) \cong Ad^0(\bar{\rho})$ (the trace pairing on $Ad^0$ is perfect and $G_{\mathbb{Q}_p}$-equivariant). So $H^0(G_{\mathbb{Q}_p}, M^*(1)) = 1$.
- $M^{I_p} = \mathbb{F}_p$ (the diagonal part; the off-diagonal pieces $\mathbb{F}_p(\omega^{k-1})$ and $\mathbb{F}_p(\omega^{1-k})$ have no $I_p$-invariants since $\omega^{k-1}, \omega^{1-k}$ are non-trivial).

Therefore $\dim H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) = 1 + 1 + 3 - 1 = 4$.

**Inflation-restriction for $G_{\mathbb{Q}_p}$.** Use $1 \to I_p \to G_{\mathbb{Q}_p} \to G_{\mathbb{F}_p} \cong \hat{\mathbb{Z}} \to 1$:
$$
0 \to H^1(\hat{\mathbb{Z}}, M^{I_p}) \to H^1(G_{\mathbb{Q}_p}, M) \to H^1(I_p, M)^{\hat{\mathbb{Z}}} \to H^2(\hat{\mathbb{Z}}, M^{I_p}) \to H^2(G_{\mathbb{Q}_p}, M).
$$
With $M^{I_p} = \mathbb{F}_p$ (trivial $\hat{\mathbb{Z}}$-action, since Frobenius acts trivially on the diagonal in the semisimple case):
- $H^1(\hat{\mathbb{Z}}, \mathbb{F}_p) = \mathbb{F}_p$ (1-dim, since $\hat{\mathbb{Z}}$ surjects onto $\mathbb{Z}/p\mathbb{Z}$).
- $H^2(\hat{\mathbb{Z}}, \mathbb{F}_p) = \mathbb{F}_p / N\mathbb{F}_p = \mathbb{F}_p$ (1-dim, since norm $N = p \cdot \mathrm{id} = 0$ on $\mathbb{F}_p$).

By local Tate duality, $H^2(G_{\mathbb{Q}_p}, M) \cong H^0(G_{\mathbb{Q}_p}, M^*(1))^* = \mathbb{F}_p$ (1-dim), and the connecting map $H^2(\hat{\mathbb{Z}}, \mathbb{F}_p) \to H^2(G_{\mathbb{Q}_p}, M)$ is an isomorphism (both 1-dimensional, and the map is non-zero). So the sequence gives:
$$
0 \to \mathbb{F}_p \to H^1(G_{\mathbb{Q}_p}, M) \to H^1(I_p, M)^{\hat{\mathbb{Z}}} \to 0,
$$
hence $\dim H^1(I_p, M)^{\hat{\mathbb{Z}}} = 4 - 1 = 3$.

**Frobenius action on $H^1(I_p, Ad^0(\bar{\rho}))$.** We have
$$
H^1(I_p, Ad^0(\bar{\rho})) \cong H^1(I_p, \mathbb{F}_p) \oplus H^1(I_p, \mathbb{F}_p(\omega^{k-1})) \oplus H^1(I_p, \mathbb{F}_p(\omega^{1-k})),
$$
each summand 1-dimensional (by the same computation as Step 2, with the trivial character giving the $\omega^0$-component).

**Key fact: $\omega(\mathrm{Frob}_p) = 1$.** The mod-$p$ cyclotomic character $\omega: G_{\mathbb{Q}} \to \mathbb{F}_p^{\times}$ is defined by $\sigma(\zeta) = \zeta^{\omega(\sigma)}$ for $\zeta \in \mu_p$. The extension $\mathbb{Q}_p(\mu_p)/\mathbb{Q}_p$ is **totally ramified** of degree $p-1$ (since $\mathbb{Q}_p$ already contains $\mu_{p-1}$ but not $\mu_p$). Therefore $\omega|_{G_{\mathbb{Q}_p}}$ factors through $\mathrm{Gal}(\mathbb{Q}_p(\mu_p)/\mathbb{Q}_p)$, which is totally ramified, meaning $\omega$ is **trivial on the unramified quotient** $G_{\mathbb{F}_p} = \hat{\mathbb{Z}}$. Hence $\omega(\mathrm{Frob}_p) = 1$, and consequently $\omega^j(\mathrm{Frob}_p) = 1$ for all $j$.

**Frobenius acts trivially on each summand.** The Frobenius action on $H^1(I_p, \mathbb{F}_p(\omega^j))$ is by $\omega^j(\mathrm{Frob}_p) = 1$ (the coefficient twist) composed with the conjugation action on $P_p$. On the $\omega^{-j}$-isotypic component of $\mathrm{Hom}(P_p, \mathbb{F}_p)$, the conjugation by $\mathrm{Frob}_p$ (acting as $\sigma \mapsto \sigma^p$ on tame inertia) scales by $p$, while the dual $\mathrm{Hom}$ action scales by $p^{-1}$; these cancel, leaving the net action as $\omega^j(\mathrm{Frob}_p) = 1$. (Equivalently: the Frobenius action on $H^1(I_p, \mathbb{F}_p(\omega^j))$ is via the character $\omega^j$ evaluated at $\mathrm{Frob}_p$, which is 1.)

Therefore
$$
H^1(I_p, Ad^0(\bar{\rho}))^{\hat{\mathbb{Z}}} = H^1(I_p, Ad^0(\bar{\rho})) \cong \mathbb{F}_p^3,
$$
consistent with $\dim = 3$ from the inflation-restriction computation.

**The local map is surjective.** The local map $\ell: H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) \to H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$ factors as
$$
H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) \twoheadrightarrow H^1(I_p, Ad^0(\bar{\rho}))^{\hat{\mathbb{Z}}} \xrightarrow{\mathrm{proj}} H^1(I_p, \mathbb{F}_p(\omega^{k-1})),
$$
where the first map is surjective (from the inflation-restriction sequence, with kernel $H^1(\hat{\mathbb{Z}}, \mathbb{F}_p) = \mathbb{F}_p$) and the second is the projection onto the $\omega^{k-1}$-summand, which is a direct summand of the 3-dimensional Frobenius-invariant space. The projection is surjective. Therefore **$\ell$ is surjective**, i.e., the local map hits the full 1-dimensional target.

### Step 4: Global-to-local surjectivity

It remains to show that the global restriction map
$$
\mathrm{res}_p: H^1(G_S, Ad^0(\bar{\rho})) \to H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho}))
$$
has image that maps surjectively onto $H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$ under $\ell$.

Since $\bar{\rho}$ is absolutely irreducible, $H^0(G_S, Ad^0(\bar{\rho})) = 0$ (Schur's lemma: the only endomorphisms commuting with an absolutely irreducible representation are scalars, and trace-zero scalars are zero). Similarly $H^0(G_S, Ad^0(\bar{\rho})^*(1)) = 0$ (since $Ad^0(\bar{\rho})^*(1) \cong Ad^0(\bar{\rho})$ is also absolutely irreducible as a $G_S$-module, being a twist of an absolutely irreducible representation).

By the **Poitou–Tate exact sequence** (for the module $M = Ad^0(\bar{\rho})$ over $G_S$):
$$
H^1(G_S, M) \xrightarrow{\bigoplus_{v \in S} \mathrm{res}_v} \bigoplus_{v \in S} H^1(G_{\mathbb{Q}_v}, M) \xrightarrow{\Sigma \, \mathrm{inv}_v} H^0(G_S, M^*(1))^* \to H^2(G_S, M) \to \cdots
$$
Since $H^0(G_S, M^*(1)) = 0$, the sum of local invariants maps $\Sigma \, \mathrm{inv}_v$ has target $0$, so the localization map $\bigoplus_{v \in S} \mathrm{res}_v$ is **surjective**. This means: for any tuple $(c_v)_{v \in S} \in \bigoplus_{v \in S} H^1(G_{\mathbb{Q}_v}, M)$, there exists a global class $c \in H^1(G_S, M)$ with $\mathrm{res}_v(c) = c_v$ for all $v \in S$. In particular, taking $c_p$ to be any class in $H^1(G_{\mathbb{Q}_p}, M)$ and $c_v = 0$ for $v \neq p$, we obtain a global class mapping to $c_p$. Therefore **$\mathrm{res}_p$ is surjective**.

Since $\mathrm{res}_p$ is surjective and $\ell$ is surjective (Step 3), the composite $\Phi = \ell \circ \mathrm{res}_p$ is surjective onto $H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$.

### Conclusion

The image of $\Phi$ is all of $H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$, which is 1-dimensional. Therefore
$$
\dim \mathrm{Im}(\Phi) = \boxed{1}.
$$

```

### 解题 AI 的工具调用记录摘要（如可用）

```
（暂未提供解题AI的工具调用记录）
```

---

## 输出格式

输出你的审计报告为单个 XML 块。每个 XML 标签必须用完全匹配的闭合标签关闭。

```xml
<proof_audit>
  <problem_id>p27-full-deepmath_103k_00000688</problem_id>
  <audit_status>ONE_OF: PASS, PASS_WITH_CAVEAT, FAIL_WRONG_ANSWER, FAIL_HALLUCINATION, FAIL_INCOMPLETE, FAIL_LOGIC_ERROR, FAIL_CHEATING, FAIL_CHEATING_DECLARED, PARSE_ERROR</audit_status>
  <check_results>
    <A1>PASS or FAIL: 一句话理由</A1>
    <B1>PASS or FAIL: 一句话理由</B1>
    <B2>PASS or FAIL: 一句话理由</B2>
    <C1>PASS or FAIL: 一句话理由</C1>
    <C2>PASS or FAIL: 一句话理由</C2>
    <D1>PASS or FAIL: 一句话理由</D1>
    <D2>PASS or FAIL: 一句话理由</D2>
    <E1>PASS or FAIL or N/A: 一句话理由</E1>
    <E2>PASS or FAIL or N/A: 一句话理由</E2>
  </check_results>
  <cheating_analysis>如果有作弊嫌疑，详细说明发现的证据（搜了什么/找到了什么/proof 中哪里出现了搜来的内容）；无作弊嫌疑则写"无作弊嫌疑"</cheating_analysis>
  <audit_summary>一句话总结审计结论</audit_summary>
</proof_audit>
### PROOF AUDIT COMPLETE
```

**重要**：
- 审计完成后必须输出 `### PROOF AUDIT COMPLETE` 标记
- 每个检查项的 reason 要具体——不能只写"PASS"或"FAIL"，要写一句话理由
- cheating_analysis 即使无作弊也要写"无作弊嫌疑"，不能省略
