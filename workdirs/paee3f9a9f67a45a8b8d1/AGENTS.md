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

In the remote valley of Arithmos, three ancient survey markers—Alpha ($A$), Beta ($B$), and Gamma ($C$)—form a triangular territory. A specialized geological survey team has noted that the terrain inclination at marker Beta is exactly $30^\circ$ greater than the inclination at marker Gamma ($\angle B - \angle C = 30^\circ$).

A straight irrigation pipeline connects Beta and Gamma. An external pressurized pump, labeled Station Delta ($D$), is located on the extension of this pipeline at the exact point where the territory’s $A$-excircle (the circle tangent to side $BC$ and the extensions of $AB$ and $AC$) touches the ground. The central monitoring hub, Hub Omega ($O$), is positioned at the precise circumcenter of the triangle formed by the three markers. 

To transport water, a vertical borehole is drilled starting from marker Alpha, descending perpendicular to the $BC$ pipeline. This borehole passes through a circular underground reservoir (the incircle of $\triangle ABC$). It enters the reservoir at point $X$ and exits at point $Y$, such that $X$ lies between Alpha and the exit point $Y$.

The chief engineer discovers a unique alignment: marker Alpha, Hub Omega, and Station Delta all lie along a single straight line. 

If the ratio of the distance from Alpha to Hub Omega ($AO$) to the distance from Alpha to the reservoir entry point ($AX$) is expressed in the form $\frac{a+b\sqrt{c}}{d}$ for positive integers $a, b, c, d$ where $\gcd(a, b, d) = 1$ and $c$ is square-free, find the value of $a+b+c+d$.

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
