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

In a remote territory, three survey outposts—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a large triangular perimeter. A straight transmission line connects Bravo ($B$) and Charlie ($C$), and another connects Alpha ($A$) and Bravo ($B$). 

An engineer establishes a relay station, Delta ($D$), located somewhere along the line between Alpha and Bravo. From this relay station, a maintenance path is cleared directly to outpost Charlie ($C$). Along this maintenance path ($CD$), a signal booster, Foxtrot ($F$), is installed. The distance from the signal booster ($F$) to outpost Charlie ($C$) is measured to be exactly equal to the total distance between outposts Alpha ($A$) and Bravo ($B$).

The signal range of the equipment at Delta ($D$), Bravo ($B$), and Foxtrot ($F$) creates a circular coverage zone (the circumcircle of $\triangle BDF$). This coverage zone boundary crosses the transmission line between Bravo and Charlie at a specific access point, Echo ($E$).

During a site inspection, a surveyor discovers that outposts Alpha ($A$), Foxtrot ($F$), and the access point Echo ($E$) all lie on a perfectly straight line.

If the angle formed at outpost Charlie between the lines to Alpha and Bravo ($\angle ACB$) is denoted as $\gamma$, determine the measurement of the angle formed at the relay station Delta between outposts Alpha and Charlie ($\angle ADC$).

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
