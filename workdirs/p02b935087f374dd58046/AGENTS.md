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

In a futuristic circular data-storage facility, there are 999 memory cells arranged in a perfect ring. Each cell stores a specific numerical voltage level. An engineer is testing the stability of these voltages based on a "gradient protocol" defined by a positive integer $m$.

Under this protocol, the facility is deemed "locally consistent" if, for every single cell $A$ in the ring and for every integer step-distance $k$ (where $1 \leq k \leq m$), at least one of these two conditions is met:
1. The voltage in the cell located $k$ positions clockwise from $A$ is exactly $k$ units higher than the voltage in $A$.
2. The voltage in the cell located $k$ positions counter-clockwise from $A$ is exactly $k$ units higher than the voltage in $A$.

The Lead Architect claims that if $m$ is large enough, any "locally consistent" ring must inevitably become "globally perfect." A ring is "globally perfect" if there exists at least one specific cell $S$ (with voltage $x$) such that one of the following is true:
- For every integer $k$ from 1 to 998, the cell $k$ positions clockwise from $S$ has a voltage of exactly $x + k$.
- For every integer $k$ from 1 to 998, the cell $k$ positions counter-clockwise from $S$ has a voltage of exactly $x + k$.

Find the smallest positive integer $m$ that guarantees the existence of such a cell $S$ in any ring satisfying the protocol.

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
