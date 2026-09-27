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

Given the commutative diagram with exact rows: $$\begin{matrix} 0 & \to & M_1 & \xrightarrow{\phi_1} & M_2 & \xrightarrow{\phi_2} & M_3 & \to & 0 \\ & & \downarrow^{\alpha_1} & & \downarrow^{\alpha_2} & & \downarrow^{\alpha_3} \\ 0 & \to & N_1 & \xrightarrow{\tau_1} & N_2 & \xrightarrow{\tau_2} & N_3 & \to & 0 \end{matrix}$$ where $M_i$ and $N_i$ are modules, $\phi_i$ and $\tau_i$ are homomorphisms, $\alpha_1$ and $\alpha_3$ are isomorphisms, $\phi_1$ and $\tau_1$ are injections, and $\phi_2$ and $\tau_2$ are surjections. This leads to exact sequences $$0 \to M_1 \xrightarrow{\phi_1} M_2 \xrightarrow{\phi_2} N_3 \to 0$$ and $$0 \to M_1 \xrightarrow{\tau_1 \circ \alpha_1} N_2 \xrightarrow{\tau_2} N_3 \to 0$$ which imply $M_2/M_1 \cong N_3$ and $N_2/M_1 \cong N_3$. Determine if $N_2 \cong M_2$. Provide a justification for your conclusion.

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
