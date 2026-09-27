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

In a remote desert, a circular research outpost serves as the hub for three sensor stations: Alpha (A), Beta (B), and Gamma (C), all located on the outpost’s perimeter fence. The direct cable link between station Alpha and Gamma is exactly 40 kilometers long. Surveyors have determined that the angle formed at station Alpha by the cables connecting to Beta and Gamma is exactly 60 degrees.

A straight access road is built perfectly tangent to the circular fence at station Alpha. Meanwhile, the straight path connecting stations Gamma and Beta is extended outward until it intersects this tangent road at a communication tower, Point P (with station Beta located between Point P and station Gamma).

To provide internet to the interior of the sector, a signal beam is projected from the communication tower, perfectly bisecting the angle formed at Point P between the tangent road and the path to the stations. This signal beam crosses the cable link between Alpha and Beta at a maintenance hub, Point D, and crosses the cable link between Alpha and Gamma at another hub, Point E.

The distance from station Alpha to the maintenance hub at Point D is measured at 15 kilometers. Based on these precise geographical coordinates and measurements, calculate the straight-line distance between station Beta and station Gamma.

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
