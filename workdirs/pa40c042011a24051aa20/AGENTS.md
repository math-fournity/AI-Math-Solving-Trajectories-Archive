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

In the coastal territory of Aethelgard, four watchtowers—Alpha ($A$), Bravo ($B$), Charlie ($C$), and Delta ($D$)—form a quadrilateral boundary where the inland angles at $C$ and $D$ are perfectly equal ($\angle BCD = \angle CDA$). The northern walls, if extended from $D$ through $A$ and from $C$ through $B$, meet at a central Command Post ($E$). 

A massive circular defensive shield, $\Gamma$, is generated to perfectly enclose the triangular region formed by towers $A$ and $B$ and the Command Post $E$. Within this defense system, two specialized drone hubs, $\Gamma_1$ and $\Gamma_2$, are deployed:

*   **Hub $\Gamma_1$** is a circular zone tangent to the extension of the southern wall $CD$ (at a point $W$ beyond $D$), tangent to the wall segment $AD$ at point $X$, and touches the outer shield $\Gamma$ from the inside.
*   **Hub $\Gamma_2$** is a circular zone tangent to the extension of the southern wall $DC$ (at a point $Y$ beyond $C$), tangent to the wall segment $BC$ at point $Z$, and also touches the outer shield $\Gamma$ from the inside.

A logistics point $P$ is established at the intersection of the two signal lines $WX$ and $YZ$. Surveys confirm that this point $P$ lies exactly on the perimeter of the primary shield $\Gamma$. 

Deep in the territory, the High Command designates a Strategic Point $F$, defined as the $E$-excenter of the triangle formed by $A$, $B$, and $E$. 

The surveyors provide the following distances between the towers and the command post:
*   The distance between Alpha and Bravo ($AB$) is $544$ units.
*   The distance from Alpha to the Command Post ($AE$) is $2197$ units.
*   The distance from Bravo to the Command Post ($BE$) is $2299$ units.

Engineers must calculate the precise distance between the Strategic Point $F$ and the logistics point $P$. If this distance is expressed as a reduced fraction $\frac{m}{n}$ where $m$ and $n$ are relatively prime positive integers, find the value of $m+n$.

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
