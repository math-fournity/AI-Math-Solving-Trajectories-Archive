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

A specialized logistics company, Trans-Global, operates six main distribution hubs: the North-Link (NL), the Primary (P), the National-Parcel (NP), the Postal-Hub (PH), the Pacific-Space (PSPACE), and the Express (EXP). Additionally, there are two specialized nodes: the Counter-North (coNL) and the Counter-National (coNP).

The CEO wants to map the hierarchical flow of resources between these hubs using two specific types of connectors: the "standard-link" ($\subseteq$), which indicates the first hub’s capacity is less than or equal to the second, and the "restricted-link" ($\subsetneq$), which indicates the first hub’s capacity is strictly less than the second.

The CEO requires two flow-maps to be completed by placing one connector into each box:
Map A: $\text{NL} \square \text{P} \square \text{NP} \square \text{PH} \square \text{PSPACE} \square \text{EXP}$
Map B: $\text{coNL} \square \text{P} \square \text{coNP} \square \text{PH}$

To maintain operational integrity, the following four constraints must be satisfied:
1. The capacity of the Primary hub (P) is strictly less than the Express hub (EXP).
2. The capacity of the North-Link (NL) is strictly less than the Pacific-Space (PSPACE).
3. The capacity of the Counter-North (coNL) is strictly less than the Pacific-Space (PSPACE).
4. If the capacity of National-Parcel (NP) is not equal to Counter-National (coNP), then the Primary hub (P) must have a strictly smaller capacity than both National-Parcel (NP) and Counter-National (coNP).

How many ways are there to fill the 8 boxes with connectors such that all four constraints are satisfied?

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
