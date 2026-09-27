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

Let the polynomial $f(x)=x^6 - 11x^5 + 28x^4 + 2x^3 + 57x^2 + 13x + 30$, and let $\alpha$ be the smallest positive real root of the equation $f(x)=0$. Set $N$ as the remainder of the closest integer to $\alpha^{35}$ divided by 1498. 
A logistics company warehouses pallets with serial numbers $m=1,2,\dots, M$. To simplify the ``sampling-judgment'' process, three quality inspectors use their respective ``cyclic-power residue'' rules: 
Inspector A uses a ``cycle of $7$ pallets'' rule to record the remainder of serial number $m$ divided by $7$. If this remainder is a non-zero quadratic residue of modulo $7$ (there exists an $r$ coprime to $7$ such that $r^2\equiv m\pmod7$), it is marked as ``passed''; 
Inspector B uses a ``cycle of $11$ pallets'' rule to record the remainder of serial number $m$ divided by $11$. If this remainder is a non-zero cubic residue of modulo $11$ (there exists an $r$ coprime to $11$ such that $r^3\equiv m\pmod{11}$), it is marked as ``passed''; 
Inspector C uses a ``cycle of $13$ pallets'' rule to record the remainder of serial number $m$ divided by $13$. If this remainder is a non-zero quartic residue of modulo $13$ (there exists an $r$ coprime to $13$ such that $r^4\equiv m\pmod{13}$), it is marked as ``passed''. 
A serial number $m$ is marked as ``qualified'' if and only if all three inspectors mark it as ``passed''. Let the total number of qualified serial numbers be counted within the range $1 \le m \le M$, where the integer $M$ satisfies $M-724=N$. How many ``qualified'' serial numbers are there in total?
After solving the above problem, please output your final answer in the following format:
### The final answer is: $\boxed{<your answer>}$
Example:
### The final answer is: $\boxed{123}$
The final answer should be given as precisely as possible (using LaTeX symbols such as \sqrt, \frac, \pi, etc.). If the final answer involves a decimal approximation, it must be accurate to at least four decimal places.

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
