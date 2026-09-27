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

In a specialized digital logistics hub, two automated sorting systems, System P and System Q, are being programmed to process data packets. Each system is defined by its "processing complexity level," denoted as $m$ for System P and $n$ for System Q. These levels are restricted to integer values between 1 and 20 inclusive ($m, n \in \{1, 2, 3, \dots, 20\}$).

The behavior of these systems is modeled by monic polynomials $P(x)$ and $Q(x)$, where the degree of $P$ is $m$ and the degree of $Q$ is $n$. The hub's efficiency depends on whether the order of operations matters. Specifically, a pair of complexity levels $(m, n)$ is classified as "Non-Commutative" if there exist specific monic polynomials $P(x)$ and $Q(x)$ of those degrees such that the composite operation $P(Q(t))$ never yields the same output as $Q(P(t))$ for any real-valued input signal $t$. 

Let $S$ be the set of all such "Non-Commutative" integer pairs $(m, n)$. Your task is to identify all pairs in $S$ and calculate the total sum of the values $m + n$ for every pair contained in the set.

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
