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

A high-security logistics firm manages 100 unique server modules, labeled 1 through 100. To ensure redundancy, two independent engineers, Alpha and Beta, must each perform a solo maintenance check on every module over a 100-day schedule. 

Each engineer follows a schedule where they process exactly one distinct module per day. Consequently, Alpha’s schedule is an ordered sequence $(a_1, a_2, \dots, a_{100})$ and Beta’s schedule is an ordered sequence $(b_1, b_2, \dots, b_{100})$, where both sequences are permutations of the set $\{1, 2, \dots, 100\}$.

A "Security Protocol" is defined by the specific pair of schedules chosen by Alpha and Beta. Within a protocol:
- Let $x$ be the count of specific modules $p$ that are serviced by Alpha on a day strictly earlier than the day they are serviced by Beta.
- Let $y$ be the count of specific modules $p$ that are serviced by Beta on a day strictly earlier than the day they are serviced by Alpha.

A Security Protocol is classified as "Balanced" if $x$ is exactly equal to $y$. Let $N$ be the total number of possible Balanced Security Protocols. 

Given that $N \ge 100! \times C$, determine the value of $C$.

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
