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

In a specialized data-archiving facility, the storage cost of a data cluster is determined by a specific efficiency formula. For any set of three data partitions of sizes $p$, $q$, and $r$ (where $p, q, r$ are non-negative integers), the complexity index is calculated as:
\[f(p, q, r) = (p!)^p (q!)^q (r!)^r\]

The facility currently manages "Type-A" archives. Every Type-A archive consists of three partitions $(a, b, c)$ such that the total data volume $a + b + c$ is exactly $2020$ units.

The facility is now designing "Type-X" archives. A Type-X archive consists of three partitions $(x, y, z)$ such that the total data volume $x + y + z$ is exactly $n$ units. 

The security protocol requires that for every possible configuration of a Type-A archive and every possible configuration of a Type-X archive, the complexity index of the Type-X archive, $f(x, y, z)$, must be an integer multiple of the complexity index of the Type-A archive, $f(a, b, c)$.

Compute the smallest positive integer $n$ that ensures this requirement is satisfied for all possible valid triples $(a, b, c)$ and $(x, y, z)$.

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
