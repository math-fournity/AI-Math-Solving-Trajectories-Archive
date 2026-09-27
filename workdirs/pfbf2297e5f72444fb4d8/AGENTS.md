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

In a specialized optics laboratory, a laser beam passes through a sequence of crystalline filters to produce specific light polarizations. Each filter corresponds to a fundamental transformation within the quaternion group $Q_8 = \{1, -1, i, -i, j, -j, k, -k\}$. Specifically, Yellow filters ($Y$) represent the imaginary unit $i$, Magenta filters ($M$) represent $j$, and Cyan filters ($C$) represent $k$. The final state of the light is determined by the ordered product of these transformations in the sequence they are encountered.

Engineers have determined that a sequence of filters can be reconfigured into any other sequence as long as the total product of the group elements remains identical.

The laboratory currently uses a "Primary Array" consisting of the following sequence:
**Yellow, Yellow, Magenta, Magenta, Cyan, Cyan, Cyan.**

The research team is testing whether this Primary Array can be reconfigured into any of the following four "Target Arrays":
1. **Yellow, Magenta, Yellow, Magenta, Cyan, Cyan, Cyan**
2. **Cyan, Yellow, Cyan, Magenta, Cyan**
3. **Magenta, Magenta, Cyan, Cyan, Cyan**
4. **Yellow, Cyan, Cyan, Cyan**

Let $S$ be the set of indices $n \in \{1, 2, 3, 4\}$ such that Target Array $n$ has a total product equal to the Primary Array and is therefore reachable. 

Find the sum $\sum_{n \in S} 2^n$.

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
