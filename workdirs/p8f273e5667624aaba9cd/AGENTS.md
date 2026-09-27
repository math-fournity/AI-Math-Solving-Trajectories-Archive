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

A specialized irrigation system is designed within a triangular agricultural plot $ABC$. The plot's boundary lengths satisfy the condition that the combined length of fences $CA$ and $AB$ is exactly triple the length of the southern boundary $BC$. The length of this southern boundary $BC$ is $\sqrt{133}$ meters.

A circular walking path $\omega$, which serves as the plot's internal irrigation hub, touches the side fences $CA$ and $AB$ at points $E$ and $F$, respectively. The radius of this circular path is $\sqrt{14}$ meters. Two vertical sensor towers, $P$ and $Q$, are positioned such that the segments $PE$ and $QF$ form diameters of the circular path $\omega$.

For any location $K$ on the farm, we define a signal metric $\mathcal{D}(K)$ as the sum of the direct line-of-sight distances from $K$ to tower $P$ and from $K$ to tower $Q$ (specifically, $\mathcal{D}(K) = KP + KQ$).

Four maintenance robots—$W, X, Y,$ and $Z$—are stationed along different straight-line service tracks:
- Robot $W$ is located on the infinite line extending through the southern boundary $BC$.
- Robot $X$ is located on the infinite line extending through the fence $CE$.
- Robot $Y$ is located on the infinite line extending through the segment $EF$.
- Robot $Z$ is located on the infinite line extending through the fence $FB$.

Calculate the minimum possible value of the combined signal metrics for all four robots, expressed as $\mathcal{D}(W) + \mathcal{D}(X) + \mathcal{D}(Y) + \mathcal{D}(Z)$.

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
