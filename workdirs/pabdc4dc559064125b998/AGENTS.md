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

In a remote industrial outpost, there are 20 specialized technicians and one central supervisor. Currently, the supervisor's fuel reservoir is completely empty. Each technician carries a portable fuel canister that contains either exactly 2 liters or exactly 5 liters of high-grade propellant. 

To activate their workstations for the day, every technician must contribute exactly 1 liter of propellant to the supervisor’s reservoir. If a technician presents a 2-liter or 5-liter canister to the supervisor to pay this 1-liter requirement, the supervisor must immediately dispense the remaining balance (either 1 liter or 4 liters) back to that technician from the fuel currently held in the central reservoir. If the reservoir does not contain enough fuel to provide the exact change required, the technician cannot activate their station at 그 moment.

The technicians approach the supervisor one by one in an order of your choosing. Determine the minimum possible total volume of propellant (in liters) that the 20 technicians could have possessed collectively at the start to ensure that every technician is successfully able to pay their 1-liter requirement and receive their necessary change.

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
