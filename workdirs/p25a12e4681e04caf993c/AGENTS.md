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

In a specialized urban planning simulation, three major transit hubs are positioned at coordinates $A$, $B$, and $C$, forming a triangular sector. A central traffic control tower is located at point $O$, which is exactly equidistant from all three hubs.

To optimize network flow, two monitoring stations are established: 
- Station $P$ is placed exactly halfway along the direct maintenance road between hub $A$ and the central tower $O$.
- Station $Q$ is placed exactly at the midpoint of the high-speed rail line connecting hub $B$ and hub $C$.

The survey team identifies a specific reference angle formed between the tower $O$, station $P$, and station $Q$, denoted as $\angle OPQ$. Technical measurements of the sector's layout reveal two specific geographic constraints:
1. The angle formed at hub $B$ by the roads connecting to $A$ and $C$ (specifically $\angle ABC$) is exactly four times the magnitude of the reference angle $\angle OPQ$.
2. The angle formed at hub $C$ by the roads connecting to $A$ and $B$ (specifically $\angle ACB$) is exactly six times the magnitude of the reference angle $\angle OPQ$.

Based on these configurations, determine the degree measure of the reference angle $\angle OPQ$.

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
