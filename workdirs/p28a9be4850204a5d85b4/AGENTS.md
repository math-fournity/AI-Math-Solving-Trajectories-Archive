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

In a futuristic data-management center, two security protocols, Aino and Väinö, are competing to purge corrupted files from each other’s storage partitions. Each protocol controls a local server containing a specific number of files.

The power of a protocol is determined by the function $f(n)$: if a server contains $n$ files, and $n=1$, the power is $1$; if $n > 1$, the power is equal to the largest prime factor of $n$.

On a given turn, the active protocol checks the number of files $m$ currently in its own server. It must then delete at least one file, but no more than $f(m)$ files, from the opponent’s server. The number of files in the active protocol’s own server never changes during its own turn. 

The protocols take turns, with Aino performing the first deletion. The winner is the protocol that successfully deletes the last remaining file from the opponent's server.

Assuming both Aino and Väinö utilize optimal logic to win, find the smallest positive integer $n$ such that if both protocols begin with exactly $n$ files in their respective servers, Aino is guaranteed to lose.

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
