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

In the high-stakes world of the Galactic Trading Guild, 11 elite merchants are competing for a prestigious monopoly. Among them are 10 honest traders and one Corporate Espionage Agent. The competition consists of an undisclosed, potentially infinite number of trading rounds.

In every round, a secret market opportunity is presented. The 10 honest traders must commit to a trade simultaneously. Because of his illegal surveillance tech, the Agent can see the decisions of the 10 honest traders before he submits his own trade for that round.

The scoring for each round is dictated by the Guild’s strict "Risk-Reward" protocol:
- If a trader makes the correct market call, they gain exactly 1 Prestige Point.
- If an honest trader makes the wrong call, they lose exactly 1 Prestige Point.
- If the Agent makes a wrong call, he uses his hacking skills to scrub the records, resulting in 0 Prestige Points lost (he gains 0 points).

To secure the monopoly, the Agent must be the sole winner, meaning his total Prestige Point score must be strictly greater than the score of every other individual trader when the competition concludes.

Let $K$ be the minimum point lead the Agent must establish over the current second-place trader at some point during the competition to guarantee that he possesses a mathematical strategy to remain the sole winner until the end of the competition, no matter how many rounds are played or how the honest traders perform. 

Find $K$.

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
