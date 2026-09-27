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

In the city of Modulo-Prime, there are exactly $n = 15$ distinct communication towers, numbered $1$ through $15$. The Department of Networking is working on two separate infrastructure projects involving these towers.

**Project 1: The Maximum Network (M)**
The engineers want to create a collection of signal "triads." Each triad must connect exactly $3$ different towers. To prevent signal interference, the engineers follow a strict rule: any two distinct triads in the network can share at most one common tower. Find the maximum possible number of triads that can be formed under these constraints. Let this maximum number be $M$.

**Project 2: The Harmonic Network (K)**
A specialized group of technicians is setting up a specific frequency-balanced network. They define a "balanced triple" as a set of three distinct towers $\{a, b, c\}$, where each tower ID is between $1$ and $15$ inclusive, such that the sum of their IDs is a multiple of the total number of towers ($a + b + c \equiv 0 \pmod{15}$). Find the total number of such balanced triples that exist. Let this number be $K$.

Calculate the total value of $M + K$.

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
