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

(a) A circular plate of radius \( c \) has insulated faces and heat capacity \( s \) calories per degree per square centimeter. Find \( u(r,t) \) given \( u(c,t) = 0 \) and \n\n   \[\n   u(r, 0) = \n   \begin{cases} \n   \frac{q_0}{\pi s \epsilon^2} & \text{if } 0 \leq r \leq \epsilon, \\\n   0 & \text{if } \epsilon < r \leq c.\n   \end{cases} \n   \]\n\n   (b) Take the limit as \( \epsilon \to 0 \) of the result in part (a) to obtain\n  \n   \[\n   u(r,t) = \frac{q_0}{\pi s c^2} \sum_{n=1}^{\infty} \frac{1}{J_1(y_n)^2} \exp\left(-\frac{y_n^2 k t}{c^2}\right) J_0\left(\frac{y_n r}{c}\right),\n   \]\n\n   (where \( \{y_n\}_{1}^{\infty} \) are the positive roots of \( J_0(x) = 0 \)) for the temperature resulting from an injection of \( q_0 \) calories of heat at the center of the plate.

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
