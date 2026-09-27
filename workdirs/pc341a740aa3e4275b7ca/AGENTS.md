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

A specialized manufacturing plant has a 15-meter long automated assembly line with Station A at the 0-meter mark and Station B at the 15-meter mark. Three robotic transporters—Alpha, Beta, and Gamma—are tasked with moving components. Alpha and Beta start at Station A and must reach Station B. Gamma starts at Station B and must reach Station A. All three robots begin moving simultaneously.

Each robot has two operational modes: "Low-Power Crawl" at a speed of 5 meters per hour and "High-Power Glide" at a speed of 15 meters per hour. There is only one high-power glide module available between them.

1. Alpha begins moving toward Station B in Low-Power Crawl; Beta begins toward Station B in High-Power Glide.
2. The moment Beta encounters Gamma (who is crawling toward Station A), Beta transfers the glide module to Gamma. Beta then switches to Low-Power Crawl to finish the journey to Station B.
3. Gamma uses the glide module to move toward Station A until Gamma encounters Alpha.
4. The moment they meet, Gamma transfers the glide module to Alpha. Gamma then switches back to Low-Power Crawl to finish the journey to Station A.
5. Alpha uses the glide module to complete the remaining distance to Station B.

Let $T_A, T_B, T_G$ be the total duration (in hours) each robot (Alpha, Beta, and Gamma respectively) took to reach its destination. Let $W_A, W_B, W_G$ be the total duration (in hours) each robot spent in Low-Power Crawl.

Calculate the value of $8(T_A + T_B + T_G + W_A + W_B + W_G)$.

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
