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

In a tech hub, there are $n$ distinct specialized servers, forming a network $S = \{1, 2, \dots, n\}$. A "Project" is defined as a subset of these servers. 

Two Projects, $A$ and $B$, are said to be "Interdependent" if they share at least one common server ($A \cap B \neq \emptyset$) but each also possesses at least one server not utilized by the other ($A \setminus B \neq \emptyset$ and $B \setminus A \neq \emptyset$). However, for the purposes of this specific organizational constraint, we use a directional rule: Project $A$ "extends" Project $B$ if and only if they share a server ($A \cap B \neq \emptyset$) and Project $A$ contains at least one server that is not in Project $B$ ($A \setminus B \neq \emptyset$).

A consultancy firm establishes a portfolio $\mathcal{F}$ consisting of various Projects (subsets of $S$). To prevent logistical deadlocks, the portfolio must satisfy the following "Chain Constraint": For any three Projects $A, B, C$ in the portfolio $\mathcal{F}$, if Project $A$ extends Project $B$ and Project $B$ extends Project $C$, then Project $A$ and Project $C$ must be completely disjoint ($A \cap C = \emptyset$).

Let $M(n)$ represent the maximum possible number of Projects that can be included in such a portfolio $\mathcal{F}$ for a network of $n$ servers.

Calculate the value of $\sum_{n=1}^{10} M(n)$.

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
