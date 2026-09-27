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

A specialized architecture firm is designing a small decorative plaza located at the corner of two perpendicular city boulevards, Avenue B and Boulevard B. The plaza is shaped like a right-angled isosceles triangle, defined by three landmarks: $A$, $B$, and $C$. The corner landmark $B$ sits at the intersection of the two boulevards. The distance from $B$ to landmark $A$ (along Avenue B) is exactly 4 meters, and the distance from $B$ to landmark $C$ (along Boulevard B) is also exactly 4 meters. A straight pedestrian path connects landmarks $A$ and $C$.

Inside this plaza, a landscaping team is installing a perfectly equilateral triangular flowerbed denoted by vertices $M$, $N$, and $K$. The placement of the flowerbed must follow these strict survey constraints:
- Vertex $N$ must be positioned exactly at the midpoint of the boundary segment $BC$.
- Vertex $M$ must lie somewhere along the pedestrian path $AC$.
- Vertex $K$ must lie somewhere along the boundary segment $AB$.

Calculate the total surface area of this equilateral flowerbed $MNK$ in square meters.

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
