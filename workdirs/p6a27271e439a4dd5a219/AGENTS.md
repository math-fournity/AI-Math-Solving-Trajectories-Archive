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

Given that \(x, y, z\) are all positive real numbers, consider the equation in \(w\):  
\[
1121610\sqrt{3270}\, w^{9} - 407425607\, w^{6} + 10360232 = 0
\]
which has \(k\) real roots \(w_{1}, w_{2}, \ldots, w_{k}\), satisfying  
\[
w_{1} < w_{2} < \cdots < w_{k}.
\]
If  
\[
m = (w_{1} + w_{k}) \cdot w_{\left\lfloor \tfrac{1 + k}{2} \right\rfloor},
\]
(where \(\left\lfloor \tfrac{1 + k}{2} \right\rfloor\) denotes the greatest integer not exceeding \(\tfrac{1 + k}{2}\)),  
find the minimum value of  
\[
\frac{x^{3} + y^{3} + z^{3}}{xyz} + \frac{63m}{5(x+y+z)} \sqrt[3]{xyz}.
\]
After solving the above problem, please output your final answer in the following format:
### The final answer is: $\boxed{<your answer>}$
Example:
### The final answer is: $\boxed{123}$
The final answer should be given as precisely as possible (using LaTeX symbols such as \sqrt, \frac, \pi, etc.). If the final answer involves a decimal approximation, it must be accurate to at least four decimal places.

## Instructions

Solve this problem step by step. When you have completed your proof, output:

```
### PROOF COMPLETE
```

If you detect that the problem statement contains the answer or solution (answer leak), output:

```
### ANSWER LEAK DETECTED
```
