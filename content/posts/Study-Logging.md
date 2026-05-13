# 🧠 核心策略（你一定要理解）

这14天只做一件事：

> **证明：加入心率（HR）比只用IMU更好**

所有动作都围绕这个展开，其他全部砍掉。

---

# 📅 14天执行计划（最稳版本）

---

## 🟢 Phase 1：搭建“能跑的最小实验”（Day 1–4）

---

## ✅ Day 1：研究问题 + Introduction（最关键）

你完成：

* 确定一句话问题：

  > “Does heart rate improve IMU-based activity recognition?”

* 写 Introduction（英文 200–300词）

结构：

1. 老龄化背景（日本）👉 Japan
2. 问题：IMU 不够
3. gap：缺少生理信号
4. 你的方法：IMU + HR

👉 **产出：可发教授第一段**

---

## ✅ Day 2：数据采集（简单但真实）

设备：

* iPhone（加速度）
* Apple Watch（心率）

你只采这 4 类行为：

* walking
* sitting
* lying
* “abnormal stillness”（模拟异常静止）

👉 每类 3–5 分钟即可

👉 **产出：一个CSV数据文件**

---

## ✅ Day 3：数据对齐（论文关键点）

你做：

* 时间戳对齐（interpolation）
* 统一采样率

你论文可以写：

> “We applied timestamp synchronization and interpolation to align heterogeneous sensor data.”

👉 **产出：clean dataset**

---

## ✅ Day 4：特征提取（不要复杂）

你只提这些：

* IMU：mean, std
* HR：avg, variance

👉 不要 FFT、不用深度学习

👉 **产出：feature table**

---

# 🟡 Phase 2：核心实验（决定成败）（Day 5–9）

---

## ✅ Day 5：Baseline 模型（IMU only）

模型用：

* Random Forest（最稳）

👉 **产出：Accuracy + F1**

---

## ✅ Day 6：融合模型（IMU + HR）

同一个模型：

* 只加 HR 特征

👉 **产出：第二组结果**

---

## ✅ Day 7：结果对比（最关键一天）

你必须得到：

| 模型   | F1-score |
| ------ | -------- |
| IMU    | 0.xx     |
| IMU+HR | 0.xx     |

👉 哪怕 +3% 都可以写

👉 **产出：核心表格（论文灵魂）**

---

## ✅ Day 8：结果可视化

画：

* 柱状图（Accuracy / F1）

👉 **产出：一张“论文级图”**

---

## ✅ Day 9：写 Results（英文 150词）

模板核心：

* describe setup
* compare results
* state improvement

👉 **产出：论文最重要一段**

---

# 🔵 Phase 3：论文成型（Day 10–14）

---

## ✅ Day 10：Method 写作

你写三点：

1. Data collection
2. Synchronization
3. Feature extraction

👉 用术语，但不复杂

---

## ✅ Day 11：Discussion（拉高度）

你只写一个 insight：

> HR provides physiological context beyond motion signals.

👉 这句话非常关键（可以背）

---

## ✅ Day 12：Related Work（简单版）

你不用读很多论文，只写：

* IMU-based methods
* limitations
* multimodal trend

👉 写 5–6 句话即可

---

## ✅ Day 13：整合 Research Plan

你把：

* Introduction
* Method
* Result
* Discussion

拼成一份：

👉 **MEXT用研究计划**

---

## ✅ Day 14：GitHub + 教授邮件准备

你整理：

* 一个简单 repo（代码 + 图）
* 一段总结：

> “I conducted a preliminary study on multi-modal sensing…”

👉 这就是你“敲门砖”

---

