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

In a remote desert, a specialized surveying team is establishing a triangular perimeter defined by three base stations: **Alpha**, **Bravo**, and **Charlie**. 

To stabilize their communications network, the team establishes three specific linear paths starting from station **Alpha** and extending to the straight pipeline connecting stations **Bravo** and **Charlie**:
1.  A maintenance road, **AM**, which reaches the exact midpoint **M** of the pipeline.
2.  A fiber-optic cable, **AL**, which follows the exact angular bisector of the corner at station **Alpha**, reaching the pipeline at point **L**. This cable has a known length of **t** units.
3.  A direct drainage line, **AH**, which is built at a perfect right angle to the pipeline. This line has a known length of **h** units.

During the final inspection, the chief engineer notes a unique symmetry: the connection point for the fiber-optic cable, **L**, sits exactly halfway between the maintenance road entrance **M** and the drainage exit **H**.

Calculate the radius of the perfect circular fence that would pass through all three base stations (**Alpha**, **Bravo**, and **Charlie**) based on the measurements **t** and **h**.

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
