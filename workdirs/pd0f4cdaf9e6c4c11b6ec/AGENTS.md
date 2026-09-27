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

A specialized urban drone-delivery network is being mapped out across a circular metropolitan zone. Three major logistics hubs, labeled Alpha ($A$), Bravo ($B$), and Charlie ($C$), are positioned on the circular boundary of the city. To optimize signal coverage, the angle formed by the paths from Bravo to Alpha and Bravo to Charlie ($\angle ABC$) is exactly $20^{\circ}$, while the angle from Charlie to Alpha and Charlie to Bravo ($\angle ACB$) is $60^{\circ}$.

A central coordination tower ($I$) is located at the city's "Incenter," the unique point equidistant from the three direct flight paths connecting the hubs. A primary data trunk line begins at hub $C$ and passes through the coordination tower $I$. This line continues straight until it hits the straight-line border between hubs $A$ and $B$ at a relay station ($L$). The same data line, extending further from hub $C$, eventually reaches the city’s circular boundary at a peripheral terminal ($M$).

A secondary circular sensor field is established such that its perimeter passes through hub $B$, the coordination tower $I$, and the peripheral terminal $M$. A straight maintenance flight path connects hub $A$ to terminal $M$. This maintenance path intersects the boundary of the secondary sensor field at a specific monitoring point ($D$), which is distinct from hub $A$.

A technician at monitoring point $D$ needs to calibrate a directional antenna pointed toward the relay station $L$. Based on the geometry of the network, what is the measure of the angle formed between the maintenance path $AD$ and the line of sight $DL$ (the measure of $\angle ADL$)?

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
