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

In a remote geothermal research facility, two sensors, Sensor $X$ and Sensor $Y$, record independent thermal oscillations. The state of the system is governed by two fundamental equilibrium equations derived from the interaction of these oscillations.

The first equilibrium condition is defined by the ratio of the difference between the cosine of $X$'s signal and the sine of $X$'s signal to the sine of $Y$'s signal. This ratio is exactly equal to $\frac{2 \sqrt{2}}{5}$ times the tangent of half the average of the two signals:
$$\frac{\cos x-\sin x}{\sin y}=\frac{2 \sqrt{2}}{5} \tan \left(\frac{x+y}{2}\right)$$

The second equilibrium condition states that the ratio of the sum of the sine and cosine of $X$'s signal to the cosine of $Y$'s signal is equal to $-\frac{5}{\sqrt{2}}$ times the cotangent of half the average of the two signals:
$$\frac{\sin x+\cos x}{\cos y}=-\frac{5}{\sqrt{2}} \cot \left(\frac{x+y}{2}\right)$$

Engineers have determined that the combined phase shift, defined as $\tan(x+y)$, is not fixed but can result in at least three distinct numerical outcomes depending on the system's initialization. Let these possible distinct values for the phase shift be $v_1, v_2,$ and $v_3$. 

Calculate the sum of the squares of these three possible values: $v_1^2 + v_2^2 + v_3^2$.

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
