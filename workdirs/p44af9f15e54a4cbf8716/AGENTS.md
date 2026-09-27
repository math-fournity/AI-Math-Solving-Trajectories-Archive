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

In a remote sector of the ocean, a triangular wildlife sanctuary is defined by three research buoys: $A$, $B$, and $C$. The path from buoy $A$ to $B$ runs exactly $8$ kilometers due north. From buoy $A$, the path to buoy $C$ is exactly perpendicular to the path to $B$ (forming a $90^\circ$ angle at $A$). A scout vessel at buoy $B$ measures the angle between the lines to $A$ and $C$ as exactly $60^\circ$.

A specialized sensor, point $P$, is submerged somewhere within the triangular sanctuary. Three directional sonar beams—$\ell_A$, $\ell_B$, and $\ell_C$—are projected from the buoys. Beam $\ell_A$ perfectly bisects the angle formed between the lines $AP$ and $AB$. Beam $\ell_B$ perfectly bisects the angle formed between the lines $BP$ and $BC$. Beam $\ell_C$ perfectly bisects the angle formed between the lines $CP$ and $CA$. 

The intersection points of these sonar beams create a smaller triangular region of interest:
- Point $X$ is where beams $\ell_A$ and $\ell_B$ cross.
- Point $Y$ is where beams $\ell_B$ and $\ell_C$ cross.
- Point $Z$ is where beams $\ell_C$ and $\ell_A$ cross.

Marine biologists note that the survey triangle $XYZ$ is directly similar to the original sanctuary triangle $ABC$. The area of this inner triangle $XYZ$ can be expressed in the form $\frac{p\sqrt{q} - r\sqrt{s}}{t}$ square kilometers, where $p, q, r, s, t$ are positive integers, $q$ and $s$ are square-free, and the greatest common divisor $\gcd(p, r, t) = 1$. 

Compute the value of $p+q+r+s+t$.

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
