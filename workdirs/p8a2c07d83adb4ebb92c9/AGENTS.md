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

In a remote sector of the galaxy, the Galactic Engineering Corps is designing a high-efficiency propulsion chamber housed inside a massive, perfectly conical hull. The chamber’s core power system relies on two spherical plasma containment units, $S_1$ and $S_2$, which have different radii. These two units are positioned one above the other so that they touch at a single point, and each unit fits snugly against the interior walls of the conical hull, forming a full circular ring of contact for each sphere.

To stabilize the energy flow, engineers must install a ring of $n$ identical solid spherical shielding beads. These $n$ beads are arranged in a continuous loop around the interior of the cone. For the configuration to be stable, each individual shielding bead must simultaneously satisfy four contact points: it must touch the inner surface of the conical hull, it must touch the first containment unit $S_1$ externally, it must touch the second containment unit $S_2$ externally, and it must touch its two immediate neighbors in the ring.

Due to the geometric constraints of the conical chamber, this configuration can only exist for certain integer values of $n$. Calculate the sum of all possible values of $n$ for which such a stable arrangement can be constructed.

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
