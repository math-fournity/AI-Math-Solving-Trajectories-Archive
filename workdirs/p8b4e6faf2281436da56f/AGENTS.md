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

Consider the unit box $Q_1=[0,1]^3$ and the network of size $\epsilon$: $\epsilon \mathbb{Z}^3 \cap Q_1$. Let $W_\epsilon$ be the set of functions $v : \mathbb{R}^3 \rightarrow \mathbb{R}$ such that for every $i \in \mathbb{Z}^3$, there exists $v_i \in \mathbb{R}$ with $v(i \epsilon +y \epsilon)= v_i$ for all $y \in \mathring{Q_1}$. Define $V_\epsilon=\{ v|_{Q_1}, \ v \in W_\epsilon\}$. Consider the sequence $(u_\epsilon)_\epsilon$ such that $u_\epsilon \in V_\epsilon$ for all $\epsilon > 0$ and $u_\epsilon$ converges toward a linear profile $x \mapsto \xi \cdot x$ in $L^2(Q_1)$ as $\epsilon$ goes to zero, where $\xi$ is a given vector in $\mathbb{R}^3$. Compute the limit: $$\underset{\epsilon \rightarrow 0}{\lim} \ \epsilon \sum_{(x,y)\ \in (\epsilon \mathbb{Z}^3 \cap Q_1)^2 \\ \quad |x-y|=\epsilon} |u_\epsilon(x)-u_\epsilon(y)|^2$$

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
