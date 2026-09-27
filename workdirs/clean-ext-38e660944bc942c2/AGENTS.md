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

# Cleaning Task

以下是原始文本，可能包含题目和答案混合的内容：

3.4. A transgalactic ship has encountered an amazing meteorite stream. Some of the meteorites are flying along a straight line, one after another, at equal speeds and at equal distances from each other. Another part is flying the same way but along another straight line parallel to the first, at the same speeds but in the opposite direction, and at the same distance from each other. The ship is flying parallel to these lines. Astronaut Gavrila noted that the ship meets meteorites flying towards the ship every 7 s, and meteorites flying in the same direction as the ship every 13 s. He wondered how often meteorites would fly past him if the ship were to stand still. It seemed to him that he should take the arithmetic mean of the two given times. Is Gavrila right? If yes, write down this arithmetic mean in the answer. If not, specify the correct time in seconds, rounded to tenths.

## 清洗约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页。
   你只需要在TUI中用thinking来分析文本。

2. **从上面的文本中提取出纯净的题目和答案**：
   - 题目部分：去除答案/solution后的纯题目文本
   - 答案部分：从文本中提取出的答案

3. **直接在TUI中输出提取结果**，用XML标签包裹（内容保持原文语言）：

   <extracted-problem>
   [纯净的题目文本]
   </extracted-problem>

   <extracted-answer>
   [提取出的答案]
   </extracted-answer>

4. **如果无法提取**（文本不是题目、无法区分题目和答案等），输出：

   <extraction-failed>
   [说明为什么无法提取]
   </extraction-failed>

以上是全部约束。现在请提取。
