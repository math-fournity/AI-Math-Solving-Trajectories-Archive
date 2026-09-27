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

In the remote archipelago of Geometria, three major logistics hubs—Station A, Station B, and Station C—form a triangular supply network. The direct shipping lane from A to B spans 15 miles, the route from B to C spans 22 miles, and the path from A to C spans 20 miles.

A central distribution node, Node K, is located within this triangle. Three primary pipelines, AD, BE, and CF, are constructed such that they all intersect perfectly at Node K. The terminal point D lies on the shipping lane BC, point E lies on lane AC, and point F lies on lane AB. 

Regional engineers have recorded specific measurements for this network: point D is located exactly 6 miles away from Station B along the 22-mile BC lane. Furthermore, the ratio of the pipeline length from Station A to Node K relative to the length from Node K to terminal D is exactly 11/7.

To monitor local pressure, two circular sensor zones were established. Sensor Zone Alpha is defined by the unique circle passing through points B, F, and K. Sensor Zone Beta is defined by the unique circle passing through points C, E, and K. These two circular zones intersect at Node K and at a secondary point, designated as Location L.

A technician needs to calculate the squared distance between the distribution node K and the intersection Location L. If this squared distance $KL^2$ is expressed as a reduced fraction $a/b$, find the value of $a + b$.

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
