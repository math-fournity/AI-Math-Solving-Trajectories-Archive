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

In a specialized digital vault, security codes are generated based on a system of three encrypted keys, $(x, y, z)$. Each key is an integer ranging from $0$ to $M-1$. A set of keys is considered "Stable" if it satisfies a specific balance equation: the sum of the squares of the three keys must yield the same remainder as a specific product term when divided by the vault's modulus $M$.

The balance equation is:
$$x^2 + y^2 + z^2 \equiv Kxyz \pmod{M}$$

An expert cryptographer is analyzing two different vault configurations:

1.  **Vault Alpha**: This vault uses a prime modulus $M = 11$. The internal "interference factor" is set to $K = 4$. Let $N_A$ be the total number of Stable key sets $(x, y, z)$ for this vault.
2.  **Vault Beta**: This vault uses a prime modulus $M = 13$. The internal "interference factor" is set to $K = 6$. Let $N_B$ be the total number of Stable key sets $(x, y, z)$ for this vault.

Find the total count of unique Stable key sets across both configurations, calculated as $N_A + N_B$.

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
