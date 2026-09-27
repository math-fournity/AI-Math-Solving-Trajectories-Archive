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

In a remote desert, two experimental irrigation drones, Drone 1 and Drone 2, are programmed to spray water in the shape of two perfect parabolas, Path 1 and Path 2, across the sand. 

Each drone has a fixed signal transmitter acting as its focus; Drone 1’s focus is at point $F_1$ and Drone 2’s focus is at $F_2$. Each path is also defined by a straight boundary line acting as its directrix; Path 1’s directrix is the line $\ell_1$ and Path 2’s directrix is the line $\ell_2$.

The survey team notes the following layout:
- The straight-line distance between the two transmitters, $F_1 F_2$, is exactly 1 kilometer.
- The line segment $F_1 F_2$ is perfectly parallel to both boundary lines $\ell_1$ and $\ell_2$.
- The transmitter for Drone 1 ($F_1$) lies exactly on the water path sprayed by Drone 2 (Path 2).
- The transmitter for Drone 2 ($F_2$) lies exactly on the water path sprayed by Drone 1 (Path 1).
- The two boundary lines $\ell_1$ and $\ell_2$ are distinct, as are the transmitter locations.

The two sprayed paths, Path 1 and Path 2, intersect at two distinct watering holes, point $A$ and point $B$. The squared distance between these two watering holes, $AB^2$, can be expressed as a fraction $\frac{m}{n}$ in lowest terms, where $m$ and $n$ are relatively prime positive integers.

Find the value of $100m + n$.

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
