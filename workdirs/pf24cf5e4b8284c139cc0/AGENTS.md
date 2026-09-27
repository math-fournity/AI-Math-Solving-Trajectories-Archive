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

Find the rank of the matrix:
[[-283, 106, 424, -640, 846, 1527, 382, 714, -87, -800, 296, 870],
 [184, 584, -1459, 373, -428, 180, -970, 1006, 732, -800, 1080, 405],
 [944, 167, -157, 350, -1257, -1255, -756, -1440, 693, 110, 62, -1703],
 [348, 397, 340, 560, 133, -684, -1259, -602, -223, -2372, -219, 1274],
 [19, 672, -182, 318, -1143, 310, -1395, -44, 83, -1414, -249, 101],
 [353, -1338, 495, -41, 1386, -187, 295, 138, -730, -419, -627, 1200],
 [-229, -42, 199, 197, -219, -1497, -651, -668, -690, 799, -1128, -679],
 [-43, -874, 885, 465, -944, -957, -960, 111, -270, 386, -1960, -611],
 [-852, 1134, 140, -14, -281, -1206, 135, -1619, -949, 1035, -78, -1117],
 [-355, 475, -405, -375, -569, 897, 213, 876, 581, 926, 187, -600],
 [746, -606, -390, -630, -628, 188, -216, -388, -239, 1132, -918, -271],
 [253, -310, 116, 425, -1043, -833, -108, 371, 963, 1196, -750, -1076]]

Present the answer in LaTex format: \boxed{Your answer}

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
