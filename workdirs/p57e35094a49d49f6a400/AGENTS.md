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

In a specialized logistics network, an engineer is designing a filtration system for a series of $n$ high-precision sensors, where $n$ is a positive integer. The cost efficiency of the system is modeled by a monic polynomial $P(x)$ of degree $n$ with real coefficients.

The network operates across $n+1$ distinct nodes, indexed $i = 1, 2, \ldots, n+1$. At each node $i$, the resistance factor is defined by the function $Q(i) = \prod_{k=1}^{n+1} (i+k)^2$. The energy loss at each specific node is calculated as the ratio of the square of the product of the node's index and its cost efficiency, $i^2 P(i^2)^2$, to the resistance factor $Q(i)$.

The total energy loss for the entire network is the sum of these individual losses: 
$$E = \sum_{i=1}^{n+1} \frac{i^2 P(i^2)^2}{Q(i)}$$

The engineer seeks to find the minimum possible total energy loss, denoted as $m_n$, by optimizing the coefficients of the monic polynomial $P(x)$. 

Advanced theoretical analysis shows that as the number of sensors $n$ grows toward infinity, the value of $m_n$ behaves asymptotically like the expression $a^{2n} n^{2n+b} c$, for specific positive constants $a$, $b$, and $c$. That is, the ratio $\frac{m_n}{a^{2n} n^{2n+b} c}$ approaches 1 as $n \to \infty$.

Calculate the value of $\lfloor 2019 a b c^2 \rfloor$.

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
