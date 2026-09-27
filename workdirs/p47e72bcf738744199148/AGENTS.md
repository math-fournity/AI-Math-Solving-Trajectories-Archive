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

A specialized architectural firm is designing a triangular park defined by three landmark pillars: Alpha ($A$), Bravo ($B$), and Charlie ($C$). The surveying team has confirmed that the angle at pillar Alpha ($\angle BAC$) is exactly $40^\circ$.

The project manager identifies two key internal points for the landscaping: 
1. The Irrigation Hub ($O$), located at the circumcenter of the triangle formed by the three pillars.
2. The Community Pavilion ($G$), located at the centroid of the triangle.

To expand the park's perimeter, a new boundary marker, Delta ($D$), is placed along the straight line extending from Bravo through Charlie. This marker is positioned such that the distance from Charlie to Delta ($CD$) is exactly equal to the distance from Alpha to Charlie ($AC$), with Charlie situated directly between Bravo and Delta.

During the final site inspection, the lead engineer notices a unique geometric alignment: the straight path connecting Alpha to Delta ($AD$) runs perfectly parallel to the maintenance road connecting the Irrigation Hub to the Community Pavilion ($OG$).

Based on this specific alignment and the initial measurements, what is the degree measure of the angle at pillar Charlie ($\angle ACB$)?

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
