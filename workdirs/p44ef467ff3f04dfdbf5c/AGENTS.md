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

A network security firm has been commissioned to distribute 2,009 terabytes (TB) of encrypted data across three storage servers. The distribution process involves a Lead Architect and three Junior Engineers.

The protocol for data allocation is as follows: Each of the three Junior Engineers (Engineer 1, Engineer 2, and Engineer 3) independently submits a request for a specific amount of storage capacity, denoted as $b_1, b_2$, and $b_3$ respectively. These requests must be positive integers such that $b_1 \ge b_2 \ge b_3$ and the total sum of the requests is exactly $b_1 + b_2 + b_3 = 2,009$.

The Lead Architect, without knowing the specific values requested by the engineers, must pre-allocate the 2,009 TB of data into three discrete data packets of sizes $a_1, a_2$, and $a_3$, where $a_1 \ge a_2 \ge a_3$ and $a_1 + a_2 + a_3 = 2,009$.

The final distribution follows a strict security clearance rule: For each engineer $k$ (where $k = 1, 2, 3$), if their requested capacity $b_k$ is strictly less than the size of the corresponding packet $a_k$ (i.e., $b_k < a_k$), the engineer is granted $b_k$ terabytes of data. If $b_k \ge a_k$, that engineer receives 0 terabytes. Any data not successfully granted to the engineers is recovered by the Lead Architect for the firm's private archive.

If the Lead Architect chooses the packet sizes $a_1, a_2, a_3$ strategically to ensure they always recover at least $n$ terabytes of data regardless of which valid integers $b_1, b_2, b_3$ the engineers submit, determine the maximum possible value of $n$.

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
