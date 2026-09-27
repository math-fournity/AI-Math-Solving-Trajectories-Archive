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

A specialized deep-sea mining firm, "Abyssal Tech," has secured a contract to extract 3250 units of a rare isotope from the ocean floor. The deadline is strict: the operation must be completed in exactly 10 hours.

To perform the extraction, the company utilizes automated drones. There are two ways to acquire these drones on-site:
1.  **Industrial Fabricators:** The company owns an unlimited fleet of high-speed fabrication bays. Each bay can manufacture 1 drone in exactly 1 hour.
2.  **Self-Replication:** The drones are equipped with advanced nanites, allowing an active drone to construct a perfect functional replica of itself in exactly 2 hours.

The financial breakdown for the project is as follows:
*   **Production Cost:** Every drone produced carries a fixed manufacturing cost of 100 credits, regardless of whether it was built by a fabrication bay or self-replicated by another drone.
*   **Operational Fee:** For every drone produced by an industrial fabrication bay, the company incurs an additional maintenance and energy fee of 70 credits for the hour the bay is in operation. Self-replication by drones does not incur this specific maintenance fee.
*   The company starts with zero drones on-site at the beginning of the 10-hour window.

What are the minimum total costs, in credits, that the company must incur to fulfill the order of 3250 units, assuming each unit requires one drone to be produced?

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
