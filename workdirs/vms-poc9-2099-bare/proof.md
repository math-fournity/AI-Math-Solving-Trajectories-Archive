# 求解 $\angle BAC$ 的所有可能值

## 题目

设 $ABC$ 为等腰三角形，$AB = AC$。$A$ 的角平分线交 $BC$ 于 $D$，$B$ 的角平分线交 $AC$ 于 $E$。设 $K$ 为三角形 $ADC$ 的内心。已知 $\angle BEK = 45°$，求 $\angle BAC$ 的所有可能值。

## 答案

$$\angle BAC \in \{60°, \; 90°\}$$

---

## 证明

### 第一步：建立坐标系

设 $\angle BAC = 2\alpha$（$0 < \alpha < 90°$）。因 $AB = AC$，底角为

$$\angle ABC = \angle ACB = 90° - \alpha.$$

$A$ 的角平分线即等腰三角形的对称轴，故 $D$ 为 $BC$ 中点且 $AD \perp BC$。

建立坐标系：令 $D = (0,0)$，$BC$ 沿 $x$ 轴，$AD$ 沿 $y$ 轴。取 $AD = 1$，则

$$A = (0,\, 1), \quad B = (-t,\, 0), \quad C = (t,\, 0), \quad D = (0,\, 0),$$

其中 $t = \tan\alpha > 0$，并记 $s = \sec\alpha = \sqrt{1 + t^2}$。

此时 $AB = AC = s$，$BC = 2t$。

### 第二步：求内心 $K$ 的坐标

三角形 $ADC$ 是直角三角形（直角在 $D$），两直角边 $AD = 1$（沿 $y$ 轴）、$DC = t$（沿 $x$ 轴），斜边 $AC = s$。

直角三角形的内心到两直角边的距离均等于内切圆半径 $r$，故 $K = (r,\, r)$，其中

$$r = \frac{\text{面积}}{\text{半周长}} = \frac{\frac{1}{2} \cdot 1 \cdot t}{\frac{1 + t + s}{2}} = \frac{t}{1 + t + s}.$$

因此

$$K = \left(\frac{t}{1+t+s},\; \frac{t}{1+t+s}\right).$$

### 第三步：求 $E$ 的坐标

$B$ 的角平分线交 $AC$ 于 $E$。由角平分线定理，

$$\frac{AE}{EC} = \frac{AB}{BC} = \frac{s}{2t}.$$

用定比分点公式（$E$ 分 $AC$，$AE:EC = s:2t$，故 $E = \frac{2t \cdot A + s \cdot C}{2t + s}$）：

$$E = \left(\frac{st}{2t+s},\; \frac{2t}{2t+s}\right).$$

### 第四步：计算 $\angle BEK$

计算两个方向向量（提取正标量因子后）：

**向量 $\vec{EB}$：**

$$\vec{EB} = B - E = \frac{-2t}{2t+s}\,(t+s,\; 1).$$

记 $\vec{u} = (t+s,\; 1)$，则 $\vec{EB}$ 沿 $-\vec{u}$ 方向。

**向量 $\vec{EK}$：**

$$\vec{EK} = K - E = \frac{t}{(1+t+s)(2t+s)}\,\big(2t - st - s^2,\; -(s+2)\big).$$

记 $\vec{v} = (2t - st - s^2,\; -(s+2))$，则 $\vec{EK}$ 沿 $\vec{v}$ 方向（标量因子为正）。

因此 $\angle BEK$ 等于 $-\vec{u}$ 与 $\vec{v}$ 之间的夹角 $\theta$。

### 第五步：利用 $\tan\theta = 1$ 建立方程

计算叉积与点积：

**叉积：**

$$\vec{u} \times \vec{v} = (t+s)\bigl(-(s+2)\bigr) - 1 \cdot (2t - st - s^2)$$
$$= -(ts + 2t + s^2 + 2s) - 2t + st + s^2 = -4t - 2s = -2(2t + s).$$

故 $|\vec{u} \times \vec{v}| = 2(2t + s)$。

**点积：**

$$\vec{u} \cdot \vec{v} = (t+s)(2t - st - s^2) - (s+2).$$

展开 $(t+s)(2t - st - s^2) = 2t^2 - st^2 - 2s^2 t + 2st - s^3$，并利用 $s^2 = 1+t^2$ 化简 $-2s^2 t = -2t - 2t^3$、$-s^3 = -s - st^2$，得

$$\vec{u} \cdot \vec{v} = -2\big(t^3 - t^2 + t + 1 + s(t^2 - t + 1)\big).$$

于是

$$-\vec{u} \cdot \vec{v} = 2\big(t^3 - t^2 + t + 1 + s(t^2 - t + 1)\big).$$

**$\theta = 45°$ 的条件**为 $\tan\theta = 1$，即

$$|\vec{u} \times \vec{v}| = -\vec{u} \cdot \vec{v}, \qquad -\vec{u}\cdot\vec{v} > 0.$$

代入得方程：

$$2(2t + s) = 2\big(t^3 - t^2 + t + 1 + s(t^2 - t + 1)\big),$$

化简：

$$2t + s = t^3 - t^2 + t + 1 + s(t^2 - t + 1).$$

将含 $s$ 的项移到一边：

$$2t + s - s = t^3 - t^2 + t + 1 + st^2 - st,$$
$$t = t^3 - t^2 + 1 + st(t - 1),$$
$$t = t^2(t-1) + 1 + st(t-1),$$
$$t - 1 = (t-1)\,t\,(t + s).$$

### 第六步：求解方程

$$\boxed{(t - 1)\big(1 - t(t+s)\big) = 0.}$$

**情形一：$t = 1$。**

此时 $\tan\alpha = 1$，$\alpha = 45°$，$\angle BAC = 90°$。

验证 $-\vec{u}\cdot\vec{v} > 0$：当 $t=1$, $s=\sqrt{2}$ 时，

$$-\vec{u}\cdot\vec{v} = 2(1 - 1 + 1 + 1 + \sqrt{2}\cdot 1) = 2(2 + \sqrt{2}) > 0. \quad \checkmark$$

**情形二：$t \neq 1$，则 $1 = t(t+s) = t^2 + ts$。**

$$ts = 1 - t^2.$$

因 $s > 0$，需 $1 - t^2 > 0$，即 $t < 1$。两边平方（$s = \sqrt{1+t^2}$）：

$$t^2(1 + t^2) = (1 - t^2)^2,$$
$$t^2 + t^4 = 1 - 2t^2 + t^4,$$
$$3t^2 = 1,$$
$$t = \frac{1}{\sqrt{3}} \quad (t > 0).$$

此时 $\tan\alpha = \frac{1}{\sqrt{3}}$，$\alpha = 30°$，$\angle BAC = 60°$。

验证 $s = \sqrt{1 + \frac{1}{3}} = \frac{2}{\sqrt{3}}$，$ts = \frac{1}{\sqrt{3}} \cdot \frac{2}{\sqrt{3}} = \frac{2}{3} = 1 - \frac{1}{3} = 1 - t^2$。$\checkmark$

验证 $-\vec{u}\cdot\vec{v} > 0$：

$$t^3 - t^2 + t + 1 + s(t^2 - t + 1) = \frac{1}{3\sqrt{3}} - \frac{1}{3} + \frac{1}{\sqrt{3}} + 1 + \frac{2}{\sqrt{3}}\!\left(\frac{1}{3} - \frac{1}{\sqrt{3}} + 1\right)$$
$$= \frac{4}{3\sqrt{3}} + \frac{2}{3} + \frac{8}{3\sqrt{3}} - \frac{2}{3} = \frac{12}{3\sqrt{3}} = \frac{4}{\sqrt{3}} > 0. \quad \checkmark$$

### 第七步：无遗漏性

方程 $(t-1)(1 - t(t+s)) = 0$ 给出且仅给出上述两个解。情形二的平方步骤产生的唯一正解 $t = 1/\sqrt{3}$ 满足 $t < 1$ 的约束，无增根。因此不存在其他解。

### 数值验证

对 $\angle BAC = 60°$ 和 $90°$ 分别用坐标法数值计算 $\angle BEK$，均精确等于 $45.000°$，确认两个解的正确性。

---

## 结论

$$\boxed{\angle BAC = 60° \quad \text{或} \quad \angle BAC = 90°.}$$

**证毕。**
