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

In a sprawling industrial sector, there are 8001 independent manufacturing plants, uniquely identified by their assigned serial numbers from 2000 through 10000. For any plant identified by the serial number $n$, there are exactly $n+1$ production units operating within that facility. 

Each production unit in plant $n$ is tasked with producing exactly $n$ precision components per day. On a specific day of inspection, the yield of these units within plant $n$ followed a distinct pattern: exactly one unit produced 0 functional components, one unit produced 1 functional component, and so on, with the final unit producing $n$ functional components.

The efficiency rating of a production unit is defined as the percentage of its total components that are functional, rounded to the nearest tenth of a percent (where values like 32.45% are rounded up to 32.5%).

An auditor randomly selects one unit from the pool of all production units across all 8001 plants that achieved an efficiency rating of exactly $66.6\%$. Given that this selected unit belongs to a plant with a serial number $k$, the probability that $k \geq 6000$ can be expressed as an irreducible fraction $\frac{a}{b}$.

Find the value of $a + b$.

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
