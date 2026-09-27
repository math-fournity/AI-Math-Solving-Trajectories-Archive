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

In the competitive world of data encryption, a "Code-Breaker" is an integer $n > 2$ that defines a specific security protocol. Within this protocol, we test "Key-Signals," which are integers $a$ such that $0 < a < n$ and $\gcd(a, n) = 1$.

A Key-Signal $a$ is classified as "Sync-Stable" if there exists a positive integer duration $d$ such that:
1. The signal strength $a^d$ leaves a remainder of 1 when processed by the protocol $n$ (i.e., $n \mid a^d - 1$).
2. The cumulative resonance sum $a^{d-1} + a^{d-2} + \dots + a + 1$ is **not** divisible by $n$.

For any Code-Breaker $n$, the "Security Gap" is defined as the number of available Key-Signals $a$ that are **not** Sync-Stable. 

Let $M$ be the minimum possible Security Gap value that can be achieved by any Code-Breaker $n > 2$. 

Let $S$ be the set of all Code-Breakers $n$ (where $n > 2$) whose Security Gap is exactly equal to $M$. Calculate the sum of all elements in $S$ that are less than or equal to 100.

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
