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

In a futuristic research facility, engineers have developed a specialized propulsion rail for a high-speed maglev system. The rail is modeled as a perfectly horizontal surface. Resting on this rail is a long, hollow fuselage with an elliptical cross-section. The cross-section is defined by a semi-major axis of length $a$ and a semi-minor axis of length $b$, where $a > b$.

The fuselage is constructed from an advanced ultralight composite material with negligible mass. In its resting state, the fuselage touches the horizontal rail along a straight line that corresponds to the lower endpoints of the minor axes of its elliptical cross-sections. To provide stability, a dense tungsten reinforcement filament, which is extremely thin (negligible diameter) but very heavy, is fused internally along the entire length of the fuselage. This filament is positioned exactly along the upper endpoints of the minor axes of the cross-sections, directly above the line of contact with the rail.

Because the filament is located at the top of the minor axis and the contact point is at the bottom, the system is in a state of equilibrium due to vertical symmetry. This equilibrium is considered stable if, after a small lateral displacement, the system returns to its original position, and unstable if it continues to roll away. 

The stability of this configuration depends entirely on the eccentricity of the elliptical cross-section. It is observed that the equilibrium is stable when the fuselage is very flat (the ratio $b/a$ is near zero) and unstable when the fuselage is nearly circular (the ratio $b/a$ approaches 1). Determine the specific value of the ratio $b/a$ that serves as the boundary between stable and unstable equilibrium.

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
