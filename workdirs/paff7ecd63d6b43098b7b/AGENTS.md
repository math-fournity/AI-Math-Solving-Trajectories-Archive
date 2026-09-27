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

A high-security data vault contains $n$ independent biometric sensors, labeled $\{1, 2, \ldots, n\}$. To access different levels of the facility, the security system generates various "Access Keys," where each key is a unique subset of these sensors.

A security audit is conducted on a specific configuration of $2k$ distinct Access Keys, denoted as $S_1, S_2, \ldots, S_{2k}$. The audit focuses on two specific clusters of keys: the "Primary Cluster" $(S_1, \ldots, S_k)$ and the "Secondary Cluster" $(S_{k+1}, \ldots, S_{2k})$. 

The system's integrity relies on a "Redundancy Overlap" rule. For this configuration to be valid, every key in the Primary Cluster must share at least one common sensor with every other key in the Primary Cluster. Furthermore, every key in the Primary Cluster must share at least one common sensor with every key in the Secondary Cluster. Mathematically, $S_i \cap S_j \neq \varnothing$ and $S_i \cap S_{j+k} \neq \varnothing$ for all $1 \leq i, j \leq k$.

The Chief Security Officer determines that for any such configuration to exist, the total number of keys in the Primary Cluster, multiplied by a weight of $1000$, can never exceed a specific threshold. This threshold is defined as the product of a constant $c$ and the total number of all possible unique subsets of sensors ($2^n$).

Find the smallest positive integer $c$ such that the inequality $1000k \leq c \cdot 2^n$ is guaranteed to hold for all possible positive integers $k$ and $n$ that allow for such a configuration.

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
