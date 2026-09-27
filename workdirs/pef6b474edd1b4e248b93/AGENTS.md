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

In the high-stakes world of international logistics, a shipping coordinator manages a manifest of 68 shipping containers. Each container is defined by a distinct "Origin-Destination" code represented by an ordered pair of non-zero integers $(x, y)$. While some containers may share the same route codes, the manifest has a specific security restriction: for any integer $k$, it is impossible for both a $(k, k)$ container and a $(-k, -k)$ container to exist in the same manifest.

A customs auditor must now perform a "neutralization" protocol. The auditor looks at the 136 individual integers printed on the manifest (two per container). They are permitted to select a subset of these integers to flag for inspection, under one strict safety constraint: they cannot flag two integers if their sum is zero. 

The auditor earns a performance credit of 1 point for every container that has at least one of its two codes flagged. 

Regardless of the specific values of the non-zero integers present on the blackboard manifest, what is the maximum number of points the auditor can guaranteed to earn?

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
