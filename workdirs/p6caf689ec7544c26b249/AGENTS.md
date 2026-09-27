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

In the coastal logistics hub of Port Quadrant, two parallel shipping lanes, North Lane (Segment $AB$) and South Lane (Segment $CD$), are being monitored. The length of North Lane is exactly 4 nautical miles, while South Lane stretches for 10 nautical miles. 

An automated survey drone is programmed to travel along two diagonal patrol paths: one connecting the start of North Lane to the end of South Lane (Path $AC$), and another connecting the end of North Lane to the start of South Lane (Path $BD$). These two patrol paths intersect at a central lighthouse, Point $P$, at a perfect $90^\circ$ angle. 

The boundaries of the shipping zone are defined by two lateral safety corridors. The first corridor (Line $AD$) and the second corridor (Line $BC$) are projected outward until they meet at a deep-sea observation buoy, Point $Q$. The radar at the buoy confirms that the angle of intersection between these two boundary lines ($\angle AQD$) is exactly $45^\circ$.

The Port Authority needs to calculate the total surface area of the trapezoidal region $ABCD$ enclosed by the shipping lanes and the safety corridors. If this area is expressed as a simplified fraction $\frac{a}{b}$ (where $a$ and $b$ are coprime positive integers), find the value of $a + b$.

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
