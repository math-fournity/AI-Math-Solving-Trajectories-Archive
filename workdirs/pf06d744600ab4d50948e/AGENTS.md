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

In the city of Gridville, a delivery drone begins its journey at the central hub located at the intersection of 0th Street and 0th Avenue (0,0). Every minute, the drone automatically executes a single command to move exactly one block in one of four cardinal directions: North, South, East, or West. The flight software is programmed to choose one of these four directions at random for each move, with each direction having an equal probability of 1/4. Every choice is independent of all previous maneuvers.

The drone is programmed with a safety perimeter defined by the "Taxicab distance" from the hub. It will continue its random flight until it reaches any intersection $(x, y)$ that satisfies the boundary condition $|x| + |y| = 3$. As soon as it hits any point on this boundary, the drone must land and stop moving immediately.

The expected number of minutes the drone spends in flight before it reaches the boundary and stops can be expressed as a simplified fraction $\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. 

Calculate the value of $100m + n$.

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
