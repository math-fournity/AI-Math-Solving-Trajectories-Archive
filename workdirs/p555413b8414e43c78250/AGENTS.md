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

In a remote sector of the Arctic, a team of geologists has mapped out a base camp in the shape of a perfect equilateral triangle, labeled $ABC$. Within this triangular perimeter, several research stations and pathways have been established:

On the western boundary $AB$, a weather station $D$ is placed exactly midway, such that the distances $AD$ and $DB$ are both 4 kilometers. On the eastern boundary $AC$, a communications hub $E$ is also placed at the midpoint, making $AE$ and $EC$ both 4 kilometers. Along the southern boundary $BC$, two geological sensors, $F$ and $G$, are positioned such that the distance from the southwest corner $B$ to $F$ is 2 kilometers, the distance between the sensors $FG$ is 4 kilometers, and the distance from $G$ to the southeast corner $C$ is 2 kilometers.

The team has cleared a straight supply route $EF$ connecting the hub and the first sensor. To organize the camp's logistics, two perpendicular paths are paved to this supply route: one path starts at weather station $D$ and meets the supply route at a junction $H$, and another path starts at sensor $G$ and meets the supply route at a junction $I$.

To optimize the camp for the winter, the commander orders the relocation of three specific zones: the trapezoidal plot $ECGI$, the triangular plot $FGI$, and the quadrilateral plot $BFHD$. These zones are disassembled and perfectly repositioned as new sectors $EANL$, $MNK$, and $AMJD$, respectively. When these three new sectors are combined with the remaining central plots, they form a single, seamless rectangular logistics hub designated $HLKJ$.

Calculate the total area of the resulting rectangular hub $HLKJ$.

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
