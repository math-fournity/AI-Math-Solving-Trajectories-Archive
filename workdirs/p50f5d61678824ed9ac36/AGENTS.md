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

Let $X\subset\mathbb{P}^N$ be a rational smooth projective irreducible non-degenerated variety of dimension $n=\dim(X)$. Consider the linear system of hyperplane sections \(\mathcal{H}=|\mathcal{O}_X(1) \otimes\mathcal{I}_{{p_1}^2,\dots,{p_l}^2}|\) that is singular at points $p_1,\dots,p_{l}$. Assume $\dim(\mathcal{H})=n$ and that a general divisor $H\in \mathcal{H}$ is singular along a positive dimensional subvariety passing through these points. Additionally, assume the schematic intersection of all these singularities is singular only at $p_1,\dots,p_l$. Locally, near $p_1$, $H$ can be expressed as the zero locus of \(H_f=a_{i,j}x_ix_j+h(x_1,\dots,x_n)=0\), where $x_1,\dots,x_n$ are local coordinates and $h(x_1,\dots,x_n)$ is a polynomial of degree $\geq3$. The quadric \(Q_{H_f}=a_{i,j} x_ix_j=0\) generally has rank $h\leq n$. Denote by $\mathcal{A}_H$ the vertex of $Q_{H_f}$. Prove or disprove that under these assumptions, $\bigcap_{H\in \mathcal{H}} \mathcal{A}_H=p_1$. 

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
