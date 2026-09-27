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

An experimental desalination plant uses a specialized filtration chamber shaped like a triangular prism. The chamber has a height of $3 \text{ cm}$ and equilateral triangular bases with side lengths of $4 \text{ cm}$. A vertical piston, initially positioned at the edge of the prism opposite one of its rectangular lateral faces, moves inward toward that face, staying parallel to it. The "width" $w$ is defined as the distance between the piston and that parallel lateral face.

As the piston moves, it displaces saltwater into a secondary storage tank. This tank is shaped like an inverted square pyramid (apex at the bottom) with a height of $3\sqrt{3} \text{ cm}$ and a square top opening with side lengths of $4 \text{ cm}$. The saltwater fills the pyramid from the vertex upward.

At a specific moment, the width of the prism $w$ is exactly $2\sqrt{3} - \sqrt{2} \text{ cm}$. At this instant, the piston is closing the gap, causing the width $w$ to decrease at a constant rate of $1 \text{ cm/s}$. This displacement causes the water level in the pyramid to rise. Let $d$ be the rate in $\text{cm/s}$ at which the height of the water in the pyramid is increasing at this exact moment.

Compute $d$.

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
