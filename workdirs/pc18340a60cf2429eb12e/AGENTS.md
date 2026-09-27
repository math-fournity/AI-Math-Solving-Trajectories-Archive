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

In a digital simulation of a galactic trade network, a central hub manages resources using a square grid of $n \times n$ sectors, where $n \geq 2$. Each sector's state is represented by an integer-valued data matrix $M$, which is invertible. The system evolves over time according to a specific transmission protocol: if the current state is $M_i$, the next state $M_{i+1}$ is calculated by taking the inverse of the transpose of the current state and multiplying it by the current state, such that $M_{i+1} = (M_i^T)^{-1} M_i$. The initial state is $M_0 = M$.

The network engineers categorize certain hubs as "balanced" if their initial data matrix is normal (meaning the matrix commutes with its own transpose, $M^T M = M M^T$). 

The engineers are searching for the smallest possible grid size $n$ that allows for a balanced hub where the sequence of data states $\{M_i\}$ is not constant (i.e., $M_1 \neq M_0$), yet the sequence is periodic with a period of exactly $P=7$, such that $M_{i+7} = M_i$ for all $i \geq 0$.

Find this smallest integer $n$.

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
