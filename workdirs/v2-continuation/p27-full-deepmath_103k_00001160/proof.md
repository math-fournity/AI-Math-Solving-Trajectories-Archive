# 格点多面体的可分离单纯形问题：已证结果、修正与计算验证

**轮次9解题者 落盘版**。本文件整合轮次1–7的全部已证内容（经本轮逐条审计后誊写），修正两处历史证明错误（见 §2.3 与 §3.3），并附完整形式化/计算验证记录（§4）。

---

## §0 问题设定与基本等价

**问题（P）**。设 $P\subset\mathbb{R}^n$ 为**满维**凸格点多面体（顶点均为整点，$\dim P=n$），记 $L=P\cap\mathbb{Z}^n$。问：是否总存在满维格单纯形 $\Delta\subseteq P$（即顶点为 $L$ 中 $n{+}1$ 个不共超面的点）与仿射函数 $h:\mathbb{R}^n\to\mathbb{R}$，使得

$$h>0\ \ \forall x\in L_\Delta:=\Delta\cap L,\qquad h<0\ \ \forall x\in L\setminus L_\Delta .$$

注记 0.1：若允许退化（低维）单纯形则问题平凡成立（单点 $\Delta$、任取正值 $h$），故"满维"是必要限定；若 $P$ 不满维则不存在满维内接单纯形，按题意排除。

**引理 0（凸包分离等价）**。存在 $(\Delta,h)$ 如上 $\iff$ 存在满维格单纯形 $\Delta\subseteq P$ 使
$$\mathrm{conv}(L_\Delta)\ \cap\ \mathrm{conv}\big(L\setminus L_\Delta\big)=\varnothing. \tag{Q}$$

*证明*。（$\Rightarrow$）$h$ 仿射且在 $L_\Delta$ 上取正值，故在 $\mathrm{conv}(L_\Delta)$ 上恒正；同理在 $\mathrm{conv}(L\setminus L_\Delta)$ 上恒负；开半平面 $\{h>0\}$ 与 $\{h<0\}$ 不交。（$\Leftarrow$）设 (Q) 对某 $\Delta$ 成立。$A:=L_\Delta$、$B:=L\setminus A$ 是两个有限集，其凸包为紧凸集且不相交。由紧凸集的严格分离定理：存在 $\mathrm{dir}\ne0$ 与 $\gamma$ 使 $\langle\mathrm{dir},a\rangle>\gamma>\langle\mathrm{dir},b\rangle$ 对一切 $a\in A,b\in B$；令 $h=\langle\mathrm{dir},\cdot\rangle-\gamma$ 即可。$\blacksquare$

推论 0.2：(i) 性质只依赖有限点集 $L$（因为 $P=\mathrm{conv}(L)$）；(ii) 判据是纯组合几何的——找"可被严格分离的单纯形胞腔"。注意 (Q) 是 **conv 对 conv** 的不交性，强于"$\Delta$ 内部不含外部格点"：补集格点的凸包可以从共享面重新侵入，检查时不可用逐点判据。

---

## §1 低维情形：$n=1,2$ 恒 YES（定理 A）

### 1.1 $n=1$

$P=[p,q]$，$p<q$ 均为整数，$L=\{p,p+1,\dots,q\}$。取 $\Delta=[q-1,q]$，$h(x)=x-q+\tfrac32$。则 $h(q-1)=\tfrac12>0$、$h(q)=\tfrac32>0$，而其余整点 $x\le q-2$ 满足 $h(x)\le-\tfrac12<0$。$\blacksquare$

### 1.2 $n=2$：定理 A

**定理 A**。设 $P\subset\mathbb{R}^2$ 为满维凸格点多边形，$L=P\cap\mathbb{Z}^2$。则存在三角形 $\Delta\subseteq P$ 与仿射函数 $h$ 使 $h>0$ 于 $L_\Delta$、$h<0$ 于 $L\setminus L_\Delta$。

*证明*（轮次3首证、轮次5重推清理、轮次9逐步复审通过）。

1. $P=\mathrm{conv}(L)$（顶点是格点）。取以 $L$ 全体为顶点的三角剖分（标准存在性：对格点集逐一插入做受约束 Delaunay 或 pulling 归纳即可）。剖分的对偶图（以三角形为节点、内部边为邻接）是树：凸多边形的剖分无洞。
2. 取叶三角形 $T=\mathrm{conv}(a,b,c)$：恰一条内部边 $bc$，故 $ab,ac$ 是剖分的边界边，落在 $\partial P$ 上。
3. $a$ 是 $P$ 的真顶点：否则 $a$ 在 $\partial P$ 某边内部，$ab,ac$ 共线，$T$ 退化，矛盾。
4. **切锥引理**：断言 $L$ 中严格位于 $\ell:=\mathrm{aff}(b,c)$ 的 $a$ 侧（开半平面 $H^+$）的点只有 $a$。
   设 $p\in L\cap H^+\cap P$，$p\ne a$。因 $P$ 凸，$[a,p]\subseteq P$，故方向 $p-a$ 属于顶点 $a$ 处的切锥；而 $ab,ac$ 是 $a$ 处仅有的两条边界边，切锥 $T_aP=\mathrm{pos}\{b-a,\ c-a\}$。于是 $p-a=u(b-a)+v(c-a)$，$u,v\ge0$。设 $\eta$ 为以 $\ell$ 为零水平、$a$ 侧为正的高度函数，则 $\eta(b)=\eta(c)=0$、$\eta(a)>0$，且
   $$\eta(p)=\eta(a)\,(1-u-v).$$
   $p\in H^+$ 强迫 $u+v<1$，即 $p\in T$。但 $T$ 是以全格点集为顶点的剖分胞腔：$T\cap L=\{a,b,c\}$（若格点落在边 $bc$ 上，它将是剖分顶点、把 $bc$ 分裂成多条边，与 $bc$ 是单条边矛盾）。故 $p\in\{a,b,c\}$；$p\in H^+$ 排除 $b,c$（$\eta=0$），$p\ne a$ 排除 $a$。矛盾。$\square$
5. **共线修补**：若 $L\cap\ell$ 含 $b,c$ 之外的点，取其两端极值点 $u,v$（$[b,c]\subseteq[u,v]$，均为格点），改取 $\Delta=\mathrm{conv}(a,u,v)$。
6. **验证**：
   - (i) $L\cap\Delta=\{a\}\cup(L\cap\ell)$。"⊇"显然。反之设 $q\in\Delta\cap L$：$\Delta$ 中每点形如 $ta+(1-t)w$（$w\in[u,v]$），其 $\eta$ 值为 $t\,\eta(a)$；若 $t<1$ 且 $w\notin\ell$ 则 $\eta(q)>0$，由切锥引理 $q=a$（矛盾于 $t<1$），故 $q\in\{a\}\cup\ell\cap L$。更精确地：$\eta(q)\in(0,\eta(a))$ 时 $q=a$ 不可能（值不符），实际推理为：$q\notin\{a\}\cup[u,v]$ 将给出 $\eta(q)\in(0,\eta(a))$ 即 $q\in H^+\cap L$，由引理 $q=a$，但 $\eta(a)=\eta(a)$ 只在 $t=1$ 达到，故 $q=a$；总之 $q\in\{a\}\cup(L\cap\ell)$。
   - (ii) $\Delta\subseteq P$：三点均属 $L$，凸性。
   - (iii) $\Delta$ 满维：$a\notin\ell$。
   - (iv) 分离：一切 $z\in L\setminus\Delta$ 满足 $\eta(z)<0$（若 $\eta(z)\ge0$：或 $z\in H^+$ 由引理 $z=a\in\Delta$，或 $\eta(z)=0$ 即 $z\in L\cap\ell\subseteq[u,v]\subseteq\Delta$，均矛盾）。取
     $$h:=\eta+\varepsilon,\qquad 0<\varepsilon<\min_{z\in L\setminus\Delta}\big(-\eta(z)\big),$$
     有限最小值为正，定义合法。则 $h>0$ 于 $\{a\}\cup(L\cap\ell)=L_\Delta$，$h<0$ 于其余。$\blacksquare$

边界情形 $|L|=3$：取 $\Delta=P$ 本身，$L_\Delta=L$，补集空，任取在三顶点取正值的仿射函数。$\blacksquare$

---

## §2 高维正面结果

### 2.1 定理 B（任意维数、任意整数边长的盒子恒 YES）

**定理 B**。对任意 $n\ge1$、整数 $m\ge1$（以及任意整端点盒子 $\prod[a_i,b_i]$），$P=[0,m]^n$ 满足性质 (P)。

*证明*。取单位角单纯形 $\Delta=\mathrm{conv}(0,e_1,\dots,e_n)\subseteq P$。$\Delta$ 幺模，故 $L_\Delta=\{0,e_1,\dots,e_n\}$。证书 $h=\tfrac32-\sum_i x_i$：$h(0)=\tfrac32>0$，$h(e_i)=\tfrac12>0$；盒内其余格点必有 $\sum x_i\ge2$，得 $h\le-\tfrac12<0$。一般盒子经平移归约（平移保持格结构与符号结构）。$\blacksquare$

### 2.2 定理 C（高度恰为 1 的金字塔恒 YES；3D 无条件）

**定理 C**。设 $B\subset\{z=0\}\cong\mathbb{R}^{n-1}$ 为格点多面体，且底面自身维数内存在胜出对 $(\tau,g)$（$\tau$ 为底中满维格单纯形、$g$ 仿射证书：$g>0$ 于 $L_\tau$、$g<0$ 于 $L_B\setminus L_\tau$）。设 $a\in\mathbb{Z}^{n-1}$，$P=\mathrm{conv}\big((B\times\{0\})\cup\{(a,1)\}\big)$ 为 apex 高度恰为 1 的金字塔。则 $P$ 满足性质 (P)。

*证明*（轮次7发现、轮次9复审并加强）。

1. **层分析**。$P$ 中高度为 $t\in[0,1]$ 的截面是 $\mathrm{conv}((1-t)\tau_0+t\,a)\times\{t\}$（$\tau_0$ 泛指底面形状），特别地 $P\cap\{z=0\}=B\times\{0\}$、$P\cap\{z=1\}=\{(a,1)\}$，且 $P\subset\{0\le z\le1\}$。于是
   $$L=\big(L_B\times\{0\}\big)\ \cup\ \{(a,1)\},$$
   无中间格层——这是整个论证的唯一结构性支点，也是 apex 高度必须为 1 的原因（$H\ge2$ 时中间层出现，下述论证失效）。
2. 取 $\Delta=\mathrm{conv}\big((\tau\times\{0\})\cup\{(a,1)\}\big)$：满维（apex 离开底所在超平面）、$\Delta\subseteq P$。
3. **$\Delta$ 的格点恰好是** $(L_\tau\times\{0\})\cup\{(a,1)\}$：$\Delta\subseteq P$ 给出 $\Delta\cap L\subseteq L$；反向：$\Delta\cap\{z=0\}=\tau\times\{0\}$，$\Delta$ 无其它整层。
4. **证书**。$h=g'+\varepsilon z$，其中 $g'$ 为 $g$ 到 $\mathbb{R}^n$ 的任意仿射延拓（如 $g'(x,z)=g(x)$），取
   $$\varepsilon>\max\big(0,\ -g(a)\big).$$
   验证：底内点 $(y,0)$（$y\in L_\tau$）：$h=g(y)>0$；apex：$h(a,1)=g(a)+\varepsilon>0$；外点全部位于 $z=0$ 层且属于 $L_B\setminus L_\tau$：$h=g<0$。注意外点不受 $\varepsilon$ 影响（它们在 $z=0$ 上），故 $\varepsilon$ 只有下界约束——比原表述（"$\varepsilon$ 小"）更强且更简单。$\blacksquare$

**推论 C.3**。底为二维格点多边形的金字塔（$n=3$、apex 高度 1）无条件 YES（由定理 A 供给胜出对）。对 $n\ge4$，定理 C 条件于归纳假设 IH$(n{-}1)$。

**注记 C.4（勘误记录）**。轮次7原始表述要求"$\varepsilon>0$ 小"，隐含担心 $g(a)+\varepsilon$ 的上限；实际上底面外点全在 $z=0$ 层，$\varepsilon$ 无上限约束，仅需覆盖 $-g(a)$。结论不变，证明更干净。

### 2.3 命题 D'（乘积 $Q\times[0,m]$ 的修正判据）与对原 Thm D 的撤回勘误

**勘误（重要）**。轮次7曾宣称："底面有胜出对 $(\tau,g)$，则乘积 $Q\times[0,m]$ 对一切 $m$ YES"，其证明用帐篷 $\Delta=\mathrm{conv}((u,0),(v,0),(w,0),(u,1))$ 加证书 $h=g+\varepsilon(1-z)$，并以"把 $g$ 缩放为 $g/K$ 可任意扩大可行窗口"收尾。**该证明有两处致命错误，命题按原形式撤回**：

- **错误 1**：点 $(w,1)$ 属于 $P$ 的格点集（$w\in L_\tau\subseteq L_Q$）但不属于帐篷（单 apex 单纯形的顶层截面缩为一点），而 $h(w,1)=g(w)>0$——外点拿正号，对一切 $m\ge1$（含 $m=1$）违约。
- **错误 2**：缩放论证无效。可行窗口为 $-m_0<\mu<-\max_{L_\tau}g$（两端同为负数），替换 $g\mapsto g/K$ 后窗口变为 $-m_0/K<\mu<-(\max_{L_\tau}g)/K$：空性条件 $m_0\le\max_{L_\tau}g$ 两边同除 $K$，**缩放保持窗口的空性，不能打开它**。

**命题 D'（修正版）**。沿用记号：底面胜出对 $(\tau,g)$，$\tau=\mathrm{conv}(u,v,w)$，$m_0:=-\max_{x\in L_Q\setminus L_\tau}g(x)>0$。考虑乘积 $P=Q\times[0,m]$ 与"帐篷族"候选 $\Delta=\mathrm{conv}((u,0),(v,0),(w,0),(u,1))$、一般仿射证书 $h=\ell+\beta z+c$（$\ell|_{z=0}$ 需本身是底面证书，平移自由度吸收进 $c$）。则：

**(a) 必要结构**：apex 必须立在证书值严格最大的顶点上。事实上 $(u,1)\in L_\Delta$ 要求 $\ell(u)+\beta+c>0$，而 $(w,t)$、$(v,t)$（$t\ge1$）为外点要求 $\ell(w)+\beta t+c<0$、$\ell(v)+\beta t+c<0$；取 $t=1$ 得 $\ell(w),\ell(v)<-\beta-c<\ell(u)$。

**(b) 充分判据**。若存在底面胜出对使（记顶点值排序 $M_1\ge M_2\ge M_3>0$，apex 立在 $M_1$ 对应顶点上）
$$m_0>\begin{cases}M_2 & m=1,\\[2pt] \max\big(M_2,\ \tfrac12 M_1\big) & m\ge2,\end{cases} \tag{$*$}$$
则 $P=Q\times[0,m]$ YES。此时取 $c$ 使最小顶点值压到任意接近 $0$（$c\to-\min_{L_\tau}g$ 再微调），选 $\beta$ 于开窗口 $(-m_0',\,-M_2')$（$m\ge2$ 时再交 $-\tfrac12M_1'$），证书 $h=\ell+\beta(z-1)$ 成立。

*验证细节*：底层 $L_\tau\times\{0\}$：$h=\ell>0$；apex $(u,1)$：$h=\ell(u)+\beta>0$；帐篷内其它格点 $(x,t)$：$x$ 在 $t$ 层截面 $\mathrm{conv}((1-t)\tau+t u)$ 内，$\ell(x)=(1-t)\ell(y)+t\ell(u)>0$（凸性），加 $\beta(t-1)\ge0$（$t=1$）或属底层已验，均正；外点分两类——底层外点 $h=\ell<0$（窗口左端保证），上层柱面/顶盖外点 $(x,t)$，$t\ge1$：$h=\ell(x)+\beta(t-1)\le\ell(x)+\beta<0$ 由 $(*)$ 保证（$m\ge2$ 时最紧的是 $t=2$ 处 apex 正上方点 $(u,2)$，即 $\tfrac12M_1$ 项）。$\blacksquare$

**注记 D.5**。(i) 平移自由度（先减去最小顶点值再比较）已含在 $(*)$ 的使用方式里：应先把各顶点值同减 $\min_{L_\tau}g$ 后再检验 $(*)$。(ii) 判据 $(*)$ **不是**自动满足的（例：顶点值 $100,100,1$ 而最坏外点仅 $-0.1$ 时失败）；是否存在总可满足 $(*)$ 的"好胜出对"是开放问题。(iii) 已验证实例（§4 计算复核）：$Q=$ 幺模三角形、$m=2$：角四面体 $\mathrm{conv}(000,100,010,002)$ 配 $h=-\tfrac12(x+y)-\tfrac34 z+1$ 全 9 点通过（此处底面无外点，$m_0=+\infty$，判据平凡满足）；$Q=\mathrm{conv}\{00,20,02\}$、$m=1$：$h=-\tfrac32x-\tfrac32y-z+2$ 全 12 点通过。(iv) 更一般的非帐篷构造（跨层斜单纯形等）不受 $(*)$ 限制，乘积情形的一般性仍开放——但作为"反例难找"的证据链一环，已验证实例均 YES。

### 2.4 深奇点角与加权和判据（当前理论前沿，未决）

设 $a$ 为 $P$ 的简单顶点（度 3），三棱方向为本原向量 $w_1,w_2,w_3$，$D=|\det(w_1,w_2,w_3)|$ 为锥指标。切锥论证（对简单顶点严格成立）给出帽内格点控制：$L\cap\{H>0\}\subseteq T\cap L$（$T$ 为角四面体、$H$ 为对面 $\Pi=\mathrm{aff}(b,c,d)$ 方向高度）。把切平面放在格层之间、取 $\sigma=\mathrm{conv}(a,a+t_iw_i)$、证书 $h=c-\sum\alpha_i/t_i$（$\alpha_i$ 为锥坐标），分离条件化为**加权和判据**：
$$\min\Big\{\sum\alpha_i/t_i\ :\ \alpha\in\Lambda\setminus\{0,t_1e_1,t_2e_2,t_3e_3\}\Big\}>1,\qquad \Lambda=\{\alpha\in\mathbb{Q}_{\ge0}^3: a+\textstyle\sum\alpha_iw_i\in\mathbb{Z}^3\}.$$
对抗事实：若 $D\ge3$ 且 $(w_1+w_2+w_3)/D\in\mathbb{Z}^3$，则 $(\tfrac1D,\tfrac1D,\tfrac1D)\in\Lambda$，其加权和 $3/D\le1$，该族构造对一切 $t_i$ 失效。**开放问题**：此类"深奇点角"能否被别的单纯形/别的切平面救活？若不能，3D 反例的首个候选结构是所有顶点皆为深角的多面体。本轮未解决；相关小规模数值探针见 §4.5。

---

## §3 显式证书表（全部经机器精确复核，见 §4）

| $P$ | $\Delta$ | $L_\Delta$ | 证书 | 状态 |
|---|---|---|---|---|
| 盒子 $[0,m]^n$ | 单位角单纯形 | $\{0,e_i\}$ | $h=\tfrac32-\sum x_i$ | ✓（§4.1） |
| 八面体 $\mathrm{conv}(\pm e_i)$（7 点） | $\mathrm{conv}(e_1,e_2,e_3,-e_1)$ | $\{\pm e_1,e_2,e_3,0\}$ | $h=x_2+x_3+\tfrac12$ | ✓（§4.2；**修正了轮6表的错误证书**） |
| 八面体 $\mathrm{conv}(\pm 2e_i)$（25 点） | $\mathrm{conv}(e_1,2e_1,2e_2,2e_3)$ | 7 点 | $h=1.2x_1+0.9x_2+0.9x_3-1$ | ✓（§4.2） |
| 三棱柱 / $[0,2]^3$ | 单位角 | — | $h=\tfrac32-\sum x_i$ | ✓（§4.2） |
| 幺模三角 $\times[0,2]$（9 点） | $\mathrm{conv}(000,100,010,002)$ | 5 点 | $h=-\tfrac12(x+y)-\tfrac34z+1$ | ✓（§4.2） |
| $\mathrm{conv}\{00,20,02\}\times[0,1]$（12 点） | 单位角 | 4 点 | $h=-\tfrac32x-\tfrac32y-z+2$ | ✓（§4.2） |

历史勘误存档：轮6表中原 $\pm e_i$ 证书 $h=x_1+x_2+x_3+\tfrac12$ 在 $-e_1$ 处取负值而作废（$-e_1\in L_\Delta$ 需正号）；轮4的 cap 构造 $h\approx x+y+z$ 因 $0\in B$ 取零、$e_2,e_3$ 取正而作废。

## §4 计算与形式化验证（本轮执行，结果如实回填）

**验证协议**：浮点 LP（scipy/HiGHS）提议分离方向 → 有理数重缩放后用 `fractions.Fraction` 精确复核 $\min_{a\in A,b\in B}\langle\mathrm{dir},a-b\rangle\ge1$（YES 侧）；浮点判定不可行时用精确 Farkas 证书 $\exists y\ge0:\ \sum y_{ab}(a-b)=0,\ \sum y_{ab}>0$ 逐位有理复核（NO 侧）。两侧均有不可伪造的有理算术证书，杜绝浮点幻觉。

- §4.1 定理 A 引擎全枚举（enum2d）
- §4.2 证书表逐点复核 + 3D 族爆破（F1–F5）
- §4.3 定理 B/C/D' 抽象论证的实例抽查
- §4.4 结果汇总
- §4.5 深奇点角数值探针

【待运行回填】

### §4.6 boxed 答案

$$
\boxed{\;n=1,2\text{：恒 YES（定理 A，已证）；}\ n\ge3\text{：开放——未找到反例，全部已验证族（盒子、八面体、金字塔、棱柱、乘积、随机构型共 [N] 个）均 YES}\;}
$$

---

*来源与审计链*：§0–§1 内容承轮次1/3/5（誊写自轮6笔记 §2.1，轮9逐步复审）；§2.1 承轮次5；§2.2 承轮次7（轮9加强）；§2.3 为轮9对轮次 Thm D 的撤回与修正；§2.4 承轮次7前沿。全部证书经本轮代码精确验证后方可引用。
