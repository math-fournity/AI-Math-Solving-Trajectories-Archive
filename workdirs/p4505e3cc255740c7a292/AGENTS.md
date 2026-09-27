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

A digital automated manufacturing system operates using three primary resource registers: an inventory of raw materials ($a_n$), a high-capacity power cell ($b_n$), and a secondary storage capacitor ($c_n$). At the start of the production cycle (cycle $n=0$), the power cell is charged to $4$ units ($b_0 = 4$), and the secondary capacitor contains $1$ unit of energy ($c_0 = 1$). The initial inventory of raw materials is set to a positive integer value $k$, where $k < 1995$.

The system processes these resources in discrete cycles according to the following protocol:

1. **Even-State Protocol:** If the current material inventory $a_n$ is an even number, the system undergoes a "Division Shift." In the next cycle ($n+1$), the inventory is halved ($a_{n+1} = a_n / 2$), the power cell's energy is doubled ($b_{n+1} = 2b_n$), and the secondary capacitor's charge remains unchanged ($c_{n+1} = c_n$).

2. **Odd-State Protocol:** If the current material inventory $a_n$ is an odd number, the system undergoes a "Resource Reallocation." In the next cycle ($n+1$), the inventory is reduced by an amount equal to half the current power cell's energy plus the charge in the secondary capacitor ($a_{n+1} = a_n - b_n/2 - c_n$). During this shift, the power cell's energy remains the same ($b_{n+1} = b_n$), but the secondary capacitor is recharged by adding the current power cell's energy to its existing charge ($c_{n+1} = b_n + c_n$).

The production run is considered successful if, after some number of cycles $n$, the material inventory $a_n$ reaches exactly $0$.

Find the total number of possible initial values for $k$ in the range $1 \le k < 1995$ that result in a successful production run.

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
