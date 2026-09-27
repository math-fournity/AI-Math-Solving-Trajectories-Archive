# 证明：$\angle BEA_1 = 90°$ 且 $\angle AEB_1 = 90°$

## 问题陈述

在三角形 $ABC$ 中，$J$ 是 $A$-旁切圆的圆心（即对面顶点 $A$ 的旁心）。该旁切圆与边 $BC$ 相切于 $A_1$，与边 $AC$ 的延长线相切于 $B_1$，与边 $AB$ 的延长线相切于 $C_1$。已知直线 $A_1B_1$ 与 $AB$ 垂直，交点为 $D$。$E$ 是 $C_1$ 到直线 $DJ$ 的垂足。求 $\angle BEA_1$ 和 $\angle AEB_1$。

## 结论

$$\angle BEA_1 = 90°, \qquad \angle AEB_1 = 90°.$$

## 证明

### 记号与基本性质

记 $a = BC$，$b = CA$，$c = AB$，$s = \frac{a+b+c}{2}$ 为半周长，$r_A$ 为 $A$-旁切圆半径。

$A$-旁切圆与 $BC$ 相切于 $A_1$，与 $AC$ 延长线相切于 $B_1$，与 $AB$ 延长线相切于 $C_1$。由切线性质：

- **半径垂直于切线**：$JA_1 \perp BC$，$JB_1 \perp AC$，$JC_1 \perp AB$，且 $JA_1 = JB_1 = JC_1 = r_A$。
- **切线长相等**：$BA_1 = BC_1 = s - c$，$CA_1 = CB_1 = s - b$，$AC_1 = AB_1 = s$。

其中 $C_1$ 在 $AB$ 延长线上（$B$ 的外侧），$B_1$ 在 $AC$ 延长线上（$C$ 的外侧）。

### 第一步：$D$ 在以 $BA_1$ 为直径的圆上

$D$ 是 $A_1B_1$ 与 $AB$ 的交点。由题设 $A_1B_1 \perp AB$，所以 $DA_1 \perp AB$。

由于 $B$ 在直线 $AB$ 上，$DB \subset AB$，故 $DA_1 \perp DB$，即 $\angle BDA_1 = 90°$。

由 Thales 定理，$D$ 在以 $BA_1$ 为直径的圆 $\omega_1$ 上。

### 第二步：$D$ 在以 $AB_1$ 为直径的圆上

同理，$DB_1 \subset A_1B_1$，$A$ 在直线 $AB$ 上，$DA \subset AB$，故 $DB_1 \perp DA$，即 $\angle ADB_1 = 90°$。

由 Thales 定理，$D$ 在以 $AB_1$ 为直径的圆 $\omega_2$ 上。

### 第三步：$J$ 对 $\omega_1$ 的幂等于 $r_A^2$

圆 $\omega_1$ 以 $BA_1$ 为直径。点 $J$ 对 $\omega_1$ 的幂为

$$\operatorname{Pow}_{\omega_1}(J) = \vec{JB} \cdot \vec{JA_1}.$$

（这是因为对于以 $PQ$ 为直径的圆，任意点 $X$ 的幂等于 $\vec{XP} \cdot \vec{XQ}$。）

由于 $A_1$ 是 $J$ 到 $BC$ 的垂足（$JA_1 \perp BC$），而 $B$ 在 $BC$ 上，故 $\vec{A_1B}$ 沿 $BC$ 方向，与 $\vec{JA_1}$ 垂直。分解：

$$\vec{JB} = \vec{JA_1} + \vec{A_1B},$$

$$\vec{JB} \cdot \vec{JA_1} = |\vec{JA_1}|^2 + \vec{A_1B} \cdot \vec{JA_1} = r_A^2 + 0 = r_A^2.$$

因此 $\operatorname{Pow}_{\omega_1}(J) = r_A^2$。

### 第四步：$J$ 对 $\omega_2$ 的幂等于 $r_A^2$

圆 $\omega_2$ 以 $AB_1$ 为直径。同理：

$$\operatorname{Pow}_{\omega_2}(J) = \vec{JA} \cdot \vec{JB_1}.$$

由于 $B_1$ 是 $J$ 到直线 $AC$ 的垂足（$JB_1 \perp AC$），而 $A$ 在 $AC$ 上，故 $\vec{B_1A}$ 沿 $AC$ 方向，与 $\vec{JB_1}$ 垂直。分解：

$$\vec{JA} = \vec{JB_1} + \vec{B_1A},$$

$$\vec{JA} \cdot \vec{JB_1} = |\vec{JB_1}|^2 + \vec{B_1A} \cdot \vec{JB_1} = r_A^2 + 0 = r_A^2.$$

因此 $\operatorname{Pow}_{\omega_2}(J) = r_A^2$。

### 第五步：$\triangle C_1DJ$ 是直角三角形，$E$ 是高足

$C_1$ 在直线 $AB$ 上，$D$ 也在直线 $AB$ 上，所以 $C_1D \subset AB$。

由旁切圆性质 $JC_1 \perp AB$，故 $JC_1 \perp C_1D$，即 $\triangle C_1DJ$ 在 $C_1$ 处为直角，$DJ$ 为斜边。

$E$ 是 $C_1$ 到斜边 $DJ$ 的垂足。由直角三角形中高足的性质（射影定理）：

$$JD \cdot JE = JC_1^2 = r_A^2. \tag{$*$}$$

且 $E$ 在线段 $JD$ 上（高足在斜边上的两个端点之间），故 $JE < JD$。

### 第六步：$E$ 在 $\omega_1$ 上，即 $\angle BEA_1 = 90°$

$J$ 在 $\omega_1$ 外部（因为 $\operatorname{Pow}_{\omega_1}(J) = r_A^2 > 0$）。$D$ 在 $\omega_1$ 上。

直线 $JD$ 与 $\omega_1$ 相交于 $D$ 及另一点 $E'$。由于 $J$ 在圆外，$D$ 和 $E'$ 在从 $J$ 出发的同一射线上，且

$$JD \cdot JE' = \operatorname{Pow}_{\omega_1}(J) = r_A^2. \tag{$**$}$$

由 $(*)$ 和 $(**)$ 得 $JE = JE'$。由于 $E$ 和 $E'$ 都在从 $J$ 通过 $D$ 的射线上（$E$ 在 $J$ 与 $D$ 之间），且到 $J$ 的距离相等，故 $E = E'$。

因此 $E$ 在 $\omega_1$ 上。由 Thales 定理，$\angle BEA_1 = 90°$。

### 第七步：$E$ 在 $\omega_2$ 上，即 $\angle AEB_1 = 90°$

完全同理：$J$ 在 $\omega_2$ 外部，$D$ 在 $\omega_2$ 上，直线 $JD$ 与 $\omega_2$ 的另一交点 $E''$ 满足

$$JD \cdot JE'' = \operatorname{Pow}_{\omega_2}(J) = r_A^2.$$

与 $(*)$ 比较得 $JE'' = JE$，故 $E'' = E$。因此 $E$ 在 $\omega_2$ 上，由 Thales 定理，$\angle AEB_1 = 90°$。

$$\boxed{\angle BEA_1 = 90°, \qquad \angle AEB_1 = 90°.}$$

证毕。$\blacksquare$
