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

A specialized urban park is designed in the shape of a right-angled triangle $ABC$, where the corner $B$ is a perfect 90-degree bend. The longest boundary of the park is the path $AC$, and at the exact center of this boundary sits a circular fountain $O$.

The side of the park $AB$ is divided into two sections by a gate $E$, such that the distance from $A$ to $E$ is 9 meters and from $E$ to $B$ is 3 meters. The side $BC$ is similarly divided by a bench $F$, where the distance from $B$ to $F$ is 6 meters and from $F$ to $C$ is 2 meters.

Four maintenance sensors—$W, X, Y$, and $Z$—are installed at the following locations:
- $W$ is located at the exact midpoint of the path between gate $E$ and corner $B$.
- $X$ is located at the exact midpoint of the path between corner $B$ and bench $F$.
- $Y$ is located at the exact midpoint of the straight line connecting bench $F$ to the fountain $O$.
- $Z$ is located at the exact midpoint of the straight line connecting the fountain $O$ to gate $E$.

A technician needs to calculate the surface area of the quadrilateral zone $WXYZ$ formed by these four sensors. Compute the area of quadrilateral $WXYZ$.

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
