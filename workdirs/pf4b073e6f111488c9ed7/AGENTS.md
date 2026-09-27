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

In a remote sector of the ocean, a maritime surveillance network is established with four sensor buoys located at points $A, B, C$, and $D$, all positioned along a single circular patrol perimeter. Two main undersea communication cables connect buoy $A$ to $C$ and buoy $B$ to $D$, intersecting at a central relay hub $E$.

A specialized research vessel is tasked with mapping a quadrilateral zone $WXYZ$ defined by the following navigational coordinates:
- $W$ is the point on the straight-line boundary $DA$ closest to the relay hub $E$.
- $Y$ is the point on the straight-line boundary $BC$ closest to the relay hub $E$.
- $X$ is the exact midpoint of the straight-line boundary $AB$.
- $Z$ is the exact midpoint of the straight-line boundary $CD$.

The fleet's acoustic mapping sensors provide the following data regarding the triangular sectors formed by the cables:
1. The triangular region defined by the hub and the northern buoys, $\triangle AED$, covers an area of exactly $9$ square kilometers.
2. The triangular region defined by the hub and the southern buoys, $\triangle BEC$, covers an area of exactly $25$ square kilometers.
3. Sophisticated sonar readings at the southern buoys indicate that the internal angle at buoy $B$ in $\triangle BEC$ exceeds the internal angle at buoy $C$ in $\triangle BEC$ by exactly $30^\circ$.

Calculate the total area of the zone $WXYZ$ in square kilometers.

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
