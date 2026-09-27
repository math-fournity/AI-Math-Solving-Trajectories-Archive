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

In a sprawling desert, a massive crystalline command center is built in the shape of a regular tetrahedron $T$, enclosing a total internal volume of exactly 1 unit. Within this structure, a single drone $P$ is stationed at an arbitrary interior point. 

To manage internal logistics, the facility’s computer generates four internal partition planes. Each plane passes through the drone's position $P$ and is perfectly parallel to one of the four triangular outer walls of the command center. These intersecting planes divide the total volume of the center into 14 distinct spatial zones.

Among these zones, there are three types of geometric sectors:
1. Four small tetrahedra, each located at a vertex of the main center.
2. Four parallelepipeds, each positioned along the center of a face.
3. Six remaining "edge-zones" which are adjacent to the main exterior edges of the command center but do not touch any of its vertices.

Let $f(P)$ represent the total combined volume of these six specific "edge-zones." As the drone $P$ moves to different coordinates within the interior of the command center, the volumes of these zones shift. 

Find the supremum of $f(P)$ as the drone $P$ varies over the interior of the structure.

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
