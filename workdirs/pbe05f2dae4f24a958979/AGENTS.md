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

In a remote industrial logistics center, a supervisor and a technician are managing a shipment of 100 high-capacity batteries. The batteries are currently organized into 10 identical racks, with each rack holding exactly 10 batteries.

The supervisor wants to extract as many batteries as possible for his department, while the technician aims to keep as many as possible for the main facility. They follow a specific redistribution protocol:

1.  **Preparation Phase:** The supervisor selects exactly 4 of the 10 racks. Next to each selected rack, he places an empty transport bin. He then removes a number of batteries from each of those 4 racks and places them into the bin sitting next to that specific rack. He must remove at least 1 battery from each selected rack, but he cannot empty a rack completely.
2.  **The Shuffle:** After the batteries are placed in the bins, the technician must rearrange the 4 bins. He must move every bin to a different rack among the 4 that the supervisor just selected (no bin can remain at its original rack).
3.  **Redistribution:** Once the technician has moved the bins, the batteries inside each bin are loaded into the rack next to which the bin now sits.
4.  **Iteration:** The supervisor may repeat this entire process (Steps 1 through 3) as many times as he wishes, choosing any 4 racks for each new round.

At any point in time, the supervisor can choose to end the process. When he does, he is allowed to take all the batteries contained in any 3 racks of his choice. All remaining batteries in the other 7 racks are claimed by the technician.

If both the supervisor and the technician employ optimal strategies to maximize their own respective totals, what is the maximum number of batteries the supervisor can guarantee he will take?

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
