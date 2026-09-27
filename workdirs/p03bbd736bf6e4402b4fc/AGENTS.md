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

In a vast, automated textile mill, a single infinite conveyor belt loops through a sequence of two types of weaving patterns, denoted as Pattern A and Pattern B. This sequence, $W$, is perfectly periodic, and the shortest repeating segment of patterns has a total length of exactly $2^{2016}$.

The factory’s monitoring software tracks "sub-sequences," which are finite strings of patterns found anywhere within the infinite loop. A sub-sequence $U$ is classified as "Versatile" if the following four extensions are all found somewhere within the master sequence $W$:
1. $U$ followed by Pattern A.
2. $U$ followed by Pattern B.
3. Pattern A followed by $U$.
4. Pattern B followed by $U$.

(Note: The "null" sub-sequence, containing zero patterns, is automatically classified as Versatile.)

Quality control sensors have determined a strict physical constraint: no Versatile sub-sequence can have a length greater than $2015$ patterns.

Let $N$ be the minimum possible total number of distinct Versatile sub-sequences that can exist under these conditions. Find the remainder when $N$ is divided by $1000$.

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
