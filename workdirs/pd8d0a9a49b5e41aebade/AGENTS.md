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

Return your final response within \boxed{}. For an ordered pair  $(m,n)$  of distinct positive integers, suppose, for some nonempty subset  $S$  of  $\mathbb R$ , that a function  $f:S \rightarrow S$  satisfies the property that  $f^m(x) + f^n(y) = x+y$  for all  $x,y\in S$ . (Here  $f^k(z)$  means the result when  $f$  is applied  $k$  times to  $z$ ; for example,  $f^1(z)=f(z)$  and  $f^3(z)=f(f(f(z)))$ .) Then  $f$  is called \emph{ $(m,n)$ -splendid}. Furthermore,  $f$  is called \emph{ $(m,n)$ -primitive} if  $f$  is  $(m,n)$ -splendid and there do not exist positive integers  $a\le m$  and  $b\le n$  with  $(a,b)\neq (m,n)$  and  $a \neq b$  such that  $f$  is also  $(a,b)$ -splendid. Compute the number of ordered pairs  $(m,n)$  of distinct positive integers less than  $10000$  such that there exists a nonempty subset  $S$  of  $\mathbb R$  such that there exists an  $(m,n)$ -primitive function  $f: S \rightarrow S$ .

*Proposed by Vincent Huang*

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
