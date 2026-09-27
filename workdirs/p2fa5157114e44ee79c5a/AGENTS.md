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

In a specialized logistics simulation, a starting cargo weight $n_0$ is chosen from the set of integers $\{2, 3, \dots, 10\}$. Two controllers, Alpha and Beta, take turns modifying the cargo weight $n$ to reach their respective target quotas. Alpha always moves first, taking the current weight $n_{2k}$ and increasing it to any integer $n_{2k+1}$ such that $n_{2k} \le n_{2k+1} \le n_{2k}^2$. Beta then takes the weight $n_{2k+1}$ and reduces it to a new integer $n_{2k+2}$ such that the ratio $n_{2k+1}/n_{2k+2}$ is equal to a prime power $p^r$ (where $p$ is prime and $r \ge 1$).

Alpha’s objective is to be the one to select the specific weight of $1990$. Beta’s objective is to be the one to select the specific weight of $1$. The simulation ends as soon as either target is hit.

Let $S_A$ be the set of initial weights $n_0 \in \{2, 3, \dots, 10\}$ for which Alpha can guarantee a win regardless of Beta's choices.
Let $S_B$ be the set of initial weights $n_0 \in \{2, 3, \dots, 10\}$ for which Beta can guarantee a win regardless of Alpha's choices.
Let $S_N$ be the set of initial weights $n_0 \in \{2, 3, \dots, 10\}$ for which neither controller has a guaranteed winning strategy (the game could potentially continue indefinitely or result in a draw if both play optimally).

Calculate the value of:
$$\sum_{n \in S_A} n^2 + \sum_{n \in S_B} n + |S_N|$$

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
