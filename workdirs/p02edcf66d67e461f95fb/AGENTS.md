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

Let \( n=2017 \) and \( x_1,\dots,x_n \) be boolean variables. A \( 7 \)-CNF clause is an expression of the form \( \phi_1(x_{i_1})+\dots+\phi_7(x_{i_7}) \), where \( \phi_1,\dots,\phi_7 \) are each either the function \( f(x)=x \) or \( f(x)=1-x \), and \( i_1,i_2,\dots,i_7\in\{1,2,\dots,n\} \). For example, \( x_1+(1-x_1)+(1-x_3)+x_2+x_4+(1-x_3)+x_{12} \) is a \( 7 \)-CNF clause. Determine the smallest number \( k \) for which there exist \( 7 \)-CNF clauses \( f_1,\dots,f_k \) such that \[f(x_1,\dots,x_n):=f_1(x_1,\dots,x_n)\cdots f_k(x_1,\dots,x_n)\] is zero for all values of \((x_1,\dots,x_n)\in\{0,1\}^n\).

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
