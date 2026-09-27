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

Under the assumptions in Section 5.3, derive the maximum principle for the following problem:\n\nMaximize \n\n\[ \int_{\Omega} [y_1^u(x, T) + y_2^u(x, T)] dx, \]\n\nsubject to \( u \in L^2(\Omega \times (0, T)) \), \( 0 \leq u(x, t) \leq 1 \) a.e. \( t \in (0, T) \), where \((y_1^u, y_2^u)\) is the solution to the\n\n\[\n\begin{aligned}\n  \frac{\partial y_1}{\partial t} - d_1 \Delta y_1 &= r_1 y_1 - \mu_1 u(x, t) y_1 y_2, \quad (x, t) \in \Omega \times (0, T) \\\n  \frac{\partial y_2}{\partial t} - d_2 \Delta y_2 &= -r_2 y_2 + \mu_2 u(x, t) y_1 y_2, \quad (x, t) \in \Omega \times (0, T) \\\n  \frac{\partial y_1}{\partial \nu}(x, t) &= \frac{\partial y_2}{\partial \nu}(x, t) = 0, \quad (x, t) \in \partial \Omega \times (0, T) \\\n  y_1(x, 0) &= y_{01}(x), \quad y_2(x) = y_{02}(x), \quad x \in \Omega.\n\end{aligned}\n\]\n\n*Hint.* \((y_1^u, y_2^u)\) is the solution of the following initial-value problem (in \(L^2(\Omega) \times L^2(\Omega)\)).\n\n\[\n\begin{aligned}\n  y'(t) &= f(t, u(t), y(t)), \quad t \in (0, T) \\\n  y(0) &= y_0,\n\end{aligned}\n\]\n\nwhere\n\n\[\ny_0 = \n\begin{pmatrix}\n  y_{01} \\\n  y_{02}\n\end{pmatrix},\n\]\n\nand\n\n\[\nf(t, u, y) = Ay + \n\begin{pmatrix}\n  r_1 y_1 - \mu_1 u y_1 y_2 \\\n  -r_2 y_2 + \mu_2 u y_1 y_2\n\end{pmatrix}.\n\]\n\nHere \n\n\[\ny = \n\begin{pmatrix}\n  y_1 \\\n  y_2\n\end{pmatrix},\n\]\n\nand \(A\) is a linear unbounded operator. In fact, \(A\) is defined by\n\n\[\n\begin{aligned}\nD(A) &= \{ w = (w_1, w_2) \in H^2(\Omega) \times H^2(\Omega); \, \frac{\partial w_1}{\partial \nu} = \frac{\partial w_2}{\partial \nu} = 0 \text{ on } \partial \Omega \}, \n\end{aligned}\n\]\n\n\[\nAy = \n\begin{pmatrix}\n  d_1 \Delta y_1 \\\n  d_2 \Delta y_2\n\end{pmatrix},\n\quad y \in D(A).\n\]

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
