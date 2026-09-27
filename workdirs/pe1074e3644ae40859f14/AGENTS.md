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

In a vast desert, a circular oasis $C$ with a radius of $1$ kilometer is located at the center of a coordinate system $(0,0)$. A nomadic tribe builds a perimeter fence $P$ in the shape of a convex polygon such that every straight section of the fence is perfectly tangent to the edge of the central oasis.

The tribe utilizes a specialized circular sensor drone that can scan an area with a radius of exactly $1$ kilometer. For any point $(h, k)$ where the drone might be stationed, let $N(P, h, k)$ represent the number of distinct locations where the drone's circular scanning perimeter intersects or touches the perimeter fence $P$.

The tribe defines a "Detection Zone" $H(P)$ consisting of all coordinates $(x, y)$ from which the drone’s scan would detect the fence at least once (i.e., $N(P, x, y) \geq 1$). Let $F(P)$ denote the total surface area of this Detection Zone.

The tribe’s lead mathematician is interested in the average number of detections across this zone. For a given fence $P$, this is calculated by the ratio:
$$\frac{1}{F(P)} \iint_{H(P)} N(P, x, y) \, dx \, dy$$

Find the smallest real number $u$ such that this average value is strictly less than $u$ for every possible convex polygonal fence $P$ that remains tangent to the central oasis.

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
