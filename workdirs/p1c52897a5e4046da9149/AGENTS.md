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

In a remote industrial complex, an automated climate control system manages a series of 401 thermal sensors, indexed from $k=0$ to $k=400$. Each sensor records a specific temperature differential, denoted by $a_k$. Due to the facility's insulation requirements, the sensors at both boundaries are fixed at a neutral state, such that $a_0 = a_{400} = 0$.

The internal mechanics of the system are governed by a feedback equilibrium. For every intermediate sensor $k$ (where $1 \leq k \leq 399$), the temperature differential $a_k$ is determined by a baseline calibration constant $c$ added to a cumulative interference value. This interference is calculated by summing the products of the differential at a shifted index $i-k$ and the sum of the differentials at two consecutive indices $i$ and $i+1$, as $i$ ranges from $k$ to $399$. Specifically, the equilibrium follows the rule:
\[ a_k = c + \sum_{i=k}^{399} a_{i-k}(a_i + a_{i+1}). \]

The system remains stable only for certain values of the calibration constant $c$. To ensure the facility operates at peak efficiency, the chief engineer needs to determine the upper limit of this constant.

Find the maximum possible value of the real constant $c$ that allows such a set of temperature differentials $\{a_0, a_1, \ldots, a_{400}\}$ to exist.

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
