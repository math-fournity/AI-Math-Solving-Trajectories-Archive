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

In a remote desert, two experimental irrigation pipelines, **Pipe AC** and **Pipe AB**, originate from a central pumping station at **Point A**, forming an acute angle. A straight survey line, **Path $\ell$**, is drawn to perfectly bisect the angle between these two pipes. 

A maintenance road runs in a straight line between the endpoints of the pipes, **Point B** and **Point C**. At the exact midpoint of this road, **Point M**, a technician lays a specialized fiber-optic cable. This cable follows a straight path through **Point M** and is laid perfectly parallel to the survey **Path $\ell$**.

The fiber-optic cable intersects the water pipelines at two access ports: **Port E** (located on Pipe AC) and **Port F** (located on Pipe AB).

The following measurements are recorded by the engineering team:
- The distance from the pumping station **A** to **Port E** is exactly **1** kilometer.
- The length of the fiber-optic cable segment between **Port E** and **Port F** is **$\sqrt{3}$** kilometers.
- The total length of the water pipeline **AB** is **21** kilometers.

The project manager needs to determine the length of the maintenance road **BC**. The sum of all possible values for the distance **BC** is found to be in the form **$\sqrt{a} + \sqrt{b}$**, where **$a$** and **$b$** are positive integers. 

What is the value of **$a + b$**?

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
