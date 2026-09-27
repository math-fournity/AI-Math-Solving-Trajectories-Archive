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

A specialized irrigation system is designed around three main control hubs: Alpha ($A$), Bravo ($B$), and Charlie ($C$), forming an acute triangular network with a total perimeter of 60 kilometers. A primary water valve, Delta ($D$), is positioned somewhere along the straight pipeline connecting Bravo and Charlie ($BC$).

To monitor flow, two circular sensor zones are established. The first zone is the circumcircle of the region defined by hubs $A$, $B$, and $D$; this circular boundary crosses the pipeline between Alpha and Charlie ($AC$) at a monitoring node Echo ($E$). The second zone is the circumcircle of the region defined by hubs $A$, $D$, and $C$; this boundary crosses the pipeline between Alpha and Bravo ($AB$) at a monitoring node Foxtrot ($F$). 

Technicians measure the direct distances from the water valve to these nodes, finding that the distance from Delta to Echo ($DE$) is exactly 8 kilometers, while the distance from Delta to Foxtrot ($DF$) is exactly 7 kilometers. Additionally, diagnostic sensors confirm that the angle formed by the path from Echo to Bravo to Charlie ($\angle EBC$) is congruent to the angle formed by the path from Bravo to Charlie to Foxtrot ($\angle BCF$).

The efficiency of the system depends on the ratio of the distance between hub Alpha and node Echo ($AE$) to the distance between hub Alpha and node Foxtrot ($AF$). If this ratio is expressed as a fraction $m/n$ in lowest terms, find the value of $m + n$.

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
