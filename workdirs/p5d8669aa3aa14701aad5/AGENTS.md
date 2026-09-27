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

A high-security logistics hub manages exactly 3000 distinct storage vaults, indexed from 1 to 3000. To ensure security, the hub uses two automated sorting protocols, $f$ and $g$. Each protocol is a "reassignment map" that takes the contents of a vault and reassigns them to a unique vault in the same set, such that every vault's contents are moved and every vault is filled (a bijection).

The efficiency of a pair of protocols is measured by a "Spread Score." For each vault $k$, the hub monitors four potential destination vaults reached by applying the protocols twice in succession:
1. The destination if protocol $f$ is applied to the result of protocol $f$ ($f(f(k))$).
2. The destination if protocol $g$ is applied to the result of protocol $f$ ($g(f(k))$).
3. The destination if protocol $f$ is applied to the result of protocol $g$ ($f(g(k))$).
4. The destination if protocol $g$ is applied to the result of protocol $g$ ($g(g(k))$).

For a specific vault $k$, the "vault displacement" is defined as the difference between the highest index and the lowest index among these four destinations. The total Spread Score of the system is the sum of these displacements across all 3000 vaults.

An external auditor claims that even if a malicious actor chooses the most disruptive protocol $f$ possible, the hub's manager can always counter it by selecting a specific protocol $g$ that guarantees the total Spread Score is at least $X$.

What is the maximum possible integer $X$ for which this claim holds true for all possible choices of $f$?

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
