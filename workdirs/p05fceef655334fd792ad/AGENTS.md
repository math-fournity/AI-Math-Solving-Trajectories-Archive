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

Let $ABC$ be a scalene triangle. The incircle is tangent to lines $BC$, $AC$, and $AB$ at points $D$, $E$, and $F$, respectively, and the $A$-excircle is tangent to lines $BC$, $AC$, and $AB$ at points $D_1$, $E_1$, and $F_1$, respectively. Suppose that lines $AD$, $BE$, and $CF$ are concurrent at point $G$, and suppose that lines $AD_1$, $BE_1$, and $CF_1$ are concurrent at point $G_1$. Let line $GG_1$ intersect the internal bisector of angle $BAC$ at point $X$. Suppose that $AX=1$, $\cos{\angle BAC}=\sqrt{3}-1$, and $BC=8\sqrt[4]{3}$. Then $AB \cdot AC = \frac{j+k\sqrt{m}}{n}$ for positive integers $j$, $k$, $m$, and $n$ such that $\gcd(j,k,n)=1$ and $m$ is not divisible by the square of any integer greater than $1$. Compute $1000j+100k+10m+n$. 

[i]Proposed by Luke Robitaille and Brandon Wang[/i]

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
