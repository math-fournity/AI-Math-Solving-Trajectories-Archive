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

In a specialized rail terminal, a technician is tasked with arranging six unique cargo containers labeled "1", "2", "3", "4", "5", and "6". The containers must be processed in their natural numerical order: container "1" first, then "2", and so on, ending with "6".

The terminal utilizes a single linear track that extends infinitely to the right. There is a mobile crane that can pick up a container and place it at its current position on the track. If there are already containers on the track at or to the right of the crane's position, they are all shifted exactly one slot to the right to make space for the new arrival. After placing a container, the crane’s default behavior is to move one slot to the right, positioning itself to the immediate right of the container it just placed.

However, the technician has a "Step Back" command. Each time this command is issued, the crane moves its placement position exactly one slot to the left. The technician can issue this command any number of times between the placement of containers, provided the crane does not move further left than the very first slot on the track.

A configuration is deemed "Valid" if it is a permutation of "123456" that can be formed on the track after all six containers have been placed using some sequence of "Step Back" commands. Find the total number of distinct "Valid" configurations possible.

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
