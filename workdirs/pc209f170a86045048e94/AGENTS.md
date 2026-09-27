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

A specialized irrigation system is being designed for a triangular vineyard plot, labeled $ABC$. The plot’s layout is such that the difference between the angles at corner $B$ and corner $C$ is exactly $30^{\circ}$. 

An external water reservoir is located at point $D$, which is defined as the point where the excircle opposite to corner $A$ touches the boundary line $BC$. The central control hub of the vineyard is located at $O$, the center of a circular perimeter fence that passes through all three corners $A, B$, and $C$. A straight maintenance path connects the main gate at $A$ to the reservoir at $D$. On this path, the control hub $O$ is situated exactly midway between the gate and the reservoir (in other words, points $A, O,$ and $D$ are collinear).

A vertical drainage pipe runs from corner $A$ perpendicular to the side $BC$. This pipe passes through a circular garden (the incircle of the vineyard). The pipe intersects the garden’s boundary at two specific valves, $X$ and $Y$, where $X$ is positioned closer to the gate $A$ than $Y$ is.

The head engineer needs to determine the ratio of the distance between the gate and the control hub ($AO$) to the distance between the gate and the first valve ($AX$). This ratio can be expressed in the form $\frac{a+b\sqrt{c}}{d}$ for positive integers $a,b,c,d$ where $\gcd(a,b,d)=1$ and $c$ is square-free. 

Find the value of $a+b+c+d$.

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
