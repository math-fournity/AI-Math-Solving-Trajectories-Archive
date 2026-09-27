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

Consider the vectors in \( \mathbb{R}^2 \):\n\n\[\nx^1 \equiv \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad x^2 \equiv \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad x^3 \equiv \begin{pmatrix} 1 \\ 2 \end{pmatrix},\n\]\n\n\[\nx^4 \equiv \begin{pmatrix} 1 \\ 3 \end{pmatrix}, \quad x^5 \equiv \begin{pmatrix} 1 \\ 4 \end{pmatrix}, \quad x^6 \equiv \begin{pmatrix} 0 \\ 1 \end{pmatrix}\n\]\n\nand\n\n\[\ny^1 \equiv \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad y^2 \equiv \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \quad y^3 \equiv \begin{pmatrix} -1 \\ 0 \end{pmatrix},\n\]\n\n\[\ny^4 \equiv \begin{pmatrix} 0 \\ -1 \end{pmatrix}, \quad y^5 \equiv \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad y^6 \equiv \begin{pmatrix} 0 \\ 1 \end{pmatrix}.\n\]\n\nDefine the PL function \( f : \mathbb{R}^2 \to \mathbb{R}^2 \), which coincides with the linear mapping that carries \( x^i \) onto \( y^i \) on the cone \( \text{pos}(x^i, x^{i+1}) \), for \( i = 1, \ldots, 5 \), and which is the identity outside the union of these 5 cones. The linear pieces of \( f \) are defined by the following six matrices:\n\n\[\nA^1 \equiv \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \quad\nA^2 \equiv \begin{pmatrix} 1 & -1 \\ 2 & -1 \end{pmatrix} \quad\nA^3 \equiv \begin{pmatrix} -3 & 1 \\ 2 & -1 \end{pmatrix} \n\]\n\n\[\nA^4 \equiv \begin{pmatrix} -3 & 1 \\ -4 & 1 \end{pmatrix} \quad\nA^5 \equiv \begin{pmatrix} 1 & 0 \\ -4 & 1 \end{pmatrix} \quad\nA^6 \equiv \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \n\]\n\nIt is trivial to verify that all these matrices have determinants equal to one. Thus \( f \) is coherently oriented. Yet \( f \) is not injective because every nonzero vector in \( \mathbb{R}^2 \) has exactly two preimages.

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
