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

In a remote research facility, a high-precision laser is programmed to fire 2012 pulses over a duration of exactly 1 second, starting at time $t=0$ and ending at $t=1$. Each pulse is fired at a random time within this interval, and the times are independent of one another. After the experiment, a computer records the 2012 timestamps and sorts them chronologically as $x_1 \le x_2 \le \cdots \le x_{2012}$.

The lead scientist is investigating "high-density bursts." She defines a successful experiment as one where the gap between any two consecutive laser pulses never exceeds the average interval size; specifically, $x_{i+1} - x_i \le \frac{1}{2011}$ for every $i=1, 2, \ldots, 2011$.

The probability that an experiment meets this condition can be expressed as a fraction $\frac{m}{n}$ in lowest terms, where $m$ and $n$ are relatively prime positive integers. Determine the remainder when $m+n$ is divided by 1000.

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
