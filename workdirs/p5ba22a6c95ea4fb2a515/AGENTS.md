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

In a remote industrial district, there are 9 cargo silos arranged in a single straight line. A massive supply of raw ore sits in a nearby reservoir. Two logistics managers, Julia and Yusef, are competing to determine the final inventory levels.

The process follows these rules:
Julia and Yusef take turns, with Julia acting first. On her turn, Julia receives exactly 25 units of ore from the reservoir and must distribute them across the 9 silos in any way she chooses (she can put all 25 in one silo, or split them among several). On Yusef’s turn, he selects any two adjacent silos (e.g., silos 3 and 4) and completely empties them, returning all their contents to the reservoir.

Julia has the power to stop the process at any time, including immediately after her own turn or immediately after Yusef’s turn. When she stops the process, she designates one single silo. The amount of ore currently inside that specific silo is her "Yield." Julia plays to maximize this Yield, while Yusef plays to keep the Yield as low as possible.

Assuming both managers play with perfect strategy, what is the maximum Yield Julia can achieve?

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
