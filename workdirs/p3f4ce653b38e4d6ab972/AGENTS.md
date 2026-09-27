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

In a specialized logistics hub, a manager is organizing a sequence of 5 numbered crates, labeled 0 through 4, into a single row. A "smooth sequence" is defined as any arrangement $(a_0, a_1, a_2, a_3, a_4)$ of these crates such that no crate is immediately followed by its natural successor (for example, crate 1 cannot be placed immediately to the right of crate 0, crate 2 cannot be placed immediately to the right of crate 1, and so on). Let $f(4)$ represent the total number of unique smooth sequences that can be formed using these 5 crates.

Meanwhile, in a separate digital archive, a technician is managing 3 distinct data files labeled 1, 2, and 3. The technician must generate an ordered pair of security protocols $(B, C)$. Each protocol, $B$ and $C$, is a way to reorder (permute) the 3 files. These protocols must follow a specific "mutual stability" rule: for every file position $x \in \{1, 2, 3\}$, if protocol $B$ moves file $x$ to a different position, then protocol $C$ must leave file $x$ in its original position. Let $g(3)$ represent the total number of such ordered pairs of protocols $(B, C)$ possible for these 3 files.

Find the value of the ratio $\frac{f(4)}{g(3)}$.

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
