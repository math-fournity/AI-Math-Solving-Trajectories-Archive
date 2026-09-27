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

In the coastal region of Trimetria, three guard towers—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. The distance between Alpha and Bravo is 13 miles, Alpha to Charlie is 14 miles, and Bravo to Charlie is 15 miles.

A primary supply road $AC$ connects towers Alpha and Charlie. A specialized communication beam originates at tower Bravo and hits the supply road at point $G$. This point $G$ is uniquely positioned such that if the beam $BG$ is reflected across the angle bisector of the corner at Bravo, the reflected path precisely strikes the exact midpoint of the road $AC$.

On the supply road $AC$, several logistics hubs are established:
1. Hub $Y$ is located at the midpoint of the segment between $G$ and tower Charlie.
2. Hub $X$ is located on the segment between tower Alpha and $G$ such that the distance from Alpha to $X$ is three times the distance from $X$ to $G$.

Two secondary paths are paved: path $FX$ (starting at point $F$ on the $AB$ perimeter) and path $HY$ (starting at point $H$ on the $BC$ perimeter). Both paths $FX$ and $HY$ are constructed to be perfectly parallel to the original beam $BG$.

A central command center $Z$ is built at the intersection of two direct transit lines: one connecting tower Alpha to hub $H$, and the other connecting tower Charlie to hub $F$. Finally, a surveyor marks a point $W$ on the supply road $AC$ such that the line segment $WZ$ is also perfectly parallel to the beam $BG$.

Calculate the exact length of the segment $WZ$.

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
