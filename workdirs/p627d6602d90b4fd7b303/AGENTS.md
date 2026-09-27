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

In a specialized urban planning zone, a central plaza is defined by a square region $ABCD$ with a side length of $6$ kilometers. Two major transit boulevards extend indefinitely as rays $AB$ and $AD$. A rectangular experimental zone is marked by placing a point $E$ on the boulevard extending from $AB$ and a point $F$ on the boulevard extending from $AD$, such that the city landmark $D$ is located between the origin $A$ and the point $F$. 

The boundary of this zone is the straight line segment $EF$, which intersects the plaza boundary $BC$ at a specific checkpoint $L$. To comply with local zoning laws, the triangular area formed by the points $A$, $E$, and $F$ must be exactly $36$ square kilometers.

An architect is commissioned to design a commemorative garden in the shape of a triangle $PQR$. The side lengths of this garden are determined by specific distances measured in the transit zone: the side $PQ$ must equal the length of the segment $BL$, the side $QR$ must equal the length of the segment $CL$, and the side $RP$ must equal the length of the segment $DF$. 

Upon completing the design, the architect calculates that the area of the triangular garden $PQR$ is exactly $\sqrt{6}$ square kilometers. If the sum of all possible lengths of the segment $DF$ can be expressed in the form $\sqrt{m} + \sqrt{n}$ for positive integers $m \ge n$, compute the value of $100m + n$.

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
