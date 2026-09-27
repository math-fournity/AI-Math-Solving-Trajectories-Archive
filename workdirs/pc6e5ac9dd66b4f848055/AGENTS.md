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

A specialized robotic delivery drone is stationed at a central logistics hub located at coordinates $A_0$. The drone is assigned $n$ distinct delivery tasks, represented by displacement vectors $\vec{a}_1, \dots, \vec{a}_n$. The sum of these vectors is exactly $\vec{0}$, meaning that after completing all $n$ deliveries, the drone will always return to the hub $A_0$.

The drone's flight path is determined by the order (permutation $\sigma$) in which it executes these tasks. Starting from the hub $A_0$, it visits locations $A_1, A_2, \dots$ until it reaches the final destination $A_n$, which coincides with the hub $A_0$. Specifically, the path from the $(k-1)$-th location to the $k$-th location is defined by the vector $\vec{a}_{\sigma(k)}$.

An efficiency consultant wants to determine the minimum possible angular width of a "service sector"—a wedge-shaped region with its vertex at the hub $A_0$—that can contain the drone's entire flight path. 

Let $\alpha$ be the smallest angle such that, regardless of the specific set of vectors $\{\vec{a}_i\}$ provided (as long as they sum to zero), there is always at least one ordering of those vectors that keeps all intermediate stops $A_1, \dots, A_{n-1}$ within or on the boundary of an angle of size $\alpha$ emanating from $A_0$.

Find $\alpha$ in degrees.

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
