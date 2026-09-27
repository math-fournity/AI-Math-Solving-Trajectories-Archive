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

In a specialized digital security lab, a random sequence generator is used to create a three-tier encryption key consisting of three digits: $A, B$, and $C$. Each digit is independently chosen at random (with replacement) from the set of possible values $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$.

The lab's system processes these digits to form a "Power Signature" calculated by the nested exponentiation $A^{B^{C}}$. For the encryption to be validated as a "Type-6" security protocol, the last digit (the units digit) of the resulting Power Signature must be exactly $6$. 

It is noted that the system cannot process a null state where $0^0$ occurs; therefore, if the values of $A, B$, and $C$ would result in such an undefined mathematical operation, that specific combination is considered invalid and does not count toward a successful "Type-6" validation.

Calculate the probability that a randomly generated sequence $(A, B, C)$ results in a "Type-6" validation. Express this probability as an irreducible fraction $\frac{a}{b}$. Your final task is to determine the sum of the numerator and the denominator, $a + b$.

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
