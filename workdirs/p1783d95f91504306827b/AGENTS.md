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

A specialized satellite network consists of 202 ground stations arranged in a perfect circle, indexed from 0 to 201. A signal transmitter is programmed with a "jump constant" $n$, where $n$ is a positive integer. Each time the transmitter sends a pulse, it moves $n$ stations forward around the circle. The relative position of the transmitter after $m$ pulses is defined by the fraction $p_m = \frac{(mn \pmod{202})}{202}$.

A network engineer is testing "balanced synchronization" for different subsystem sizes $k$, where $k$ is a positive integer less than 202. A subsystem of size $k$ is considered perfectly balanced if, for some jump constant $n$, the sum of the relative positions of the transmitter after each of its first $k$ pulses (from $m=1$ to $k$) is exactly equal to $\frac{k}{2}$. 

Mathematically, this occurs if there exists a positive integer $n$ such that:
$$ \sum_{m=1}^{k} \left\{ \frac{mn}{202} \right\} = \frac{k}{2} $$
where $\{x\}$ represents the fractional part of $x$.

Find the sum of all possible values of $k$ in the range $1 \le k < 202$ for which such a jump constant $n$ exists.

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
