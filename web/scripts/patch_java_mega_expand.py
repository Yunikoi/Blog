# -*- coding: utf-8 -*-
"""Mega expand Java guide: 简答必考专题 + 读程加题 + 编程题库."""
from pathlib import Path

MD = Path(__file__).resolve().parents[2] / "content/posts/Java期末复习满分攻略.md"
text = MD.read_text(encoding="utf-8")

# ── 1. 更新文首 ──
text = text.replace(
    "> **本文档**：在原有提纲基础上扩充为 **详讲版**——每章有概念解释 + 代码示例 + 考场陷阱；简答附 **22 题完整详答**；读程附 **30 题逐题手算解析**。",
    "> **本文档**：简答 **多线程 + GUI 必考各 1 道**（含上机重点）；读程 **40 题**；编程 **官方样例 + 10 道练习题 + 全能手册**。",
    1,
)

text = text.replace(
    "- [简答题题库（详答版 22 题）](#简答题题库详答版--共-22-题)\n"
    "- [读程题库（25 题 · 只写输出）](#二读程题57-道--题库-25-题)",
    "- [★ 简答必考：多线程 + GUI（上机重点）](#-简答题必考专题多线程--gui--上机作业重点)\n"
    "- [简答题题库（详答版 22 题）](#简答题题库详答版--共-22-题)\n"
    "- [读程题库（40 题 · 只写输出）](#二读程题57-道--题库-40-题)\n"
    "- [编程练习题库（10 道）](#编程题练习题库10-道--按条写)",
    1,
)

SHORT_MEGA = r'''
## ★ 简答题必考专题：多线程 + GUI · 上机作业重点

> **老师明确**：简答题 **4～5 道**，**只考概念**（不写完整程序）。  
> **必出**：**至少 1 道多线程** + **至少 1 道 GUI**（题目出现「用户界面 / Swing / AWT / 事件」即 GUI 题）。  
> **上机作业 / 大作业（FarmGUI、AutoSaveThread、练习一至四）** 是笔考简答、编程的重要来源——**务必独立思考、自己手写过**，不要照搬 AI 答案（阅卷能看出「背模板但不会变式」）。

---

### 专题 A · 多线程（整道大题 · 默写版）

> 考场可能拆成 1～2 小题，下面 **整段背熟**，按题目问什么摘相应段落写满即可。

**答：**

**（1）进程和线程的区别**

| 对比 | 进程 | 线程 |
|------|------|------|
| 定义 | 操作系统 **资源分配与调度** 的基本单位 | **CPU 调度** 的基本单位，进程内的执行路径 |
| 资源 | **独立地址空间**，互不直接访问内存 | **共享** 所属进程的内存、文件等资源 |
| 开销 | 创建、切换 **大** | 相对 **小** |
| 通信 | 需 IPC 等机制，较复杂 | 共享变量即可（需同步） |
| 崩溃 | 一般不影响其他进程 | 可能影响同进程其他线程 |

**（2）多线程的概念**

- 在一个进程内 **同时**（或交替）运行 **多条执行流**，每条流是一个 **线程**。
- Java 在语言层面支持多线程：`Thread` 类、`Runnable` 接口、`synchronized` 等。
- 线程映射到 OS 线程，对程序员 **透明**；调度基于 `Thread` 类机制。

**（3）多线程的好处**

- **提高 CPU 利用率**：一线程等待 I/O 时，CPU 可执行其他线程。
- **改善响应速度**：GUI 中耗时操作放 **后台线程**，**EDT** 仍可响应用户（不卡界面）。
- **简化并发建模**：服务器同时处理多请求、多任务并行等。

**（4）多线程的问题**

- **线程安全 / 竞态条件**：多线程同时读写共享数据，结果依赖 **调度顺序**，不可预测。
- **调试困难**：错误难稳定复现。
- **同步开销**：加锁、切换有性能成本。
- **死锁**：多个线程 **互相等待** 对方持有的锁，全部阻塞。

**（5）线程如何同步**

- **`synchronized`**：给方法或代码块加 **对象锁**，同一时刻只有一个线程进入 **临界区**，保证 **互斥**。
- **`wait()` / `notify()`**：在 **synchronized** 内使用，实现线程 **协作**（如生产者-消费者）；`wait()` **释放锁** 并等待；`notify()` 唤醒等待线程。
- **原则**：对 **共享可变数据** 的访问要 **保护**；锁对象要 **一致**。

**（6）线程同步「不好」会怎样？怎么办？**

- **同步不足**：数据错乱、丢失更新、脏读（**线程安全问题**）。
- **同步过度**：性能差、容易 **死锁**。
- **死锁的产生**（四个必要条件）：① 互斥 ② 持有并等待 ③ 不可剥夺 ④ **循环等待**（如线程1持锁A等锁B，线程2持锁B等锁A）。
- **死锁的预防和解除**：
  - **预防**：**统一加锁顺序**（所有线程按相同顺序申请多把锁）；**避免嵌套持锁**；使用 **超时**（了解）。
  - **解除**：破坏循环等待——释放已占锁、按序重试；实际开发还可 **检测死锁** 并重启线程（了解）。
- **其他**：不要用已废弃的 `stop()`/`suspend()`；用 **`volatile`** 仅保证可见性，**不能** 代替互斥。

**（7）补充常考点（上机/读程也会问）**

- **`start()` vs `run()`**：必须 **`start()`** 才创建新线程执行 `run()`；直接调 `run()` 只是普通方法调用。
- **线程状态**：new → Runnable → Running → Blocked → Dead；`sleep`、`join`、等锁、`wait` 会 **阻塞**。
- **创建方式**：`implements Runnable` + `new Thread(r).start()`（推荐）；或 `extends Thread` 重写 `run()`。

**一句话总结**：进程管资源、线程管执行；多线程提效率但要 **synchronized** 同步；死锁靠 **统一加锁顺序** 预防。

---

### 专题 B · GUI / 用户界面（整道大题 · 默写版）

> 题目出现 **用户界面、Swing、AWT、事件、监听器、FarmGUI** 等，按下面写。

**答：**

**（1）AWT 和 Swing 的区别**

| 对比 | AWT | Swing |
|------|-----|-------|
| 全称/年代 | Abstract Window Toolkit，Java 早期 | 在 AWT 之上扩展，** javax.swing ** |
| 实现方式 | 依赖 **操作系统原生控件**（**重量级**） | **纯 Java** 绘制（**轻量级**） |
| 外观 | 随 OS 变化 | 可 **统一** 跨平台外观（Pluggable L&F） |
| 组件命名 | `Frame`、`Button` | **`J` 前缀**：`JFrame`、`JButton` |
| 关系 | 基础 | **构建在 AWT 之上**（如 `JFrame` 继承 `Frame`） |
| 本课 | 了解 | **主要用 Swing** |

**（2）GUI 组件层次结构（必会画简图 · 简答常考）**

```
Component（所有组件根类）
└── Container（容器，可包含其他组件）
    ├── Window（顶层窗口）
    │   └── Frame → JFrame（常用主窗口）
    └── Panel → JPanel（面板，布局用）
        └── 具体组件：JButton、JTextField、JTextArea、JLabel …
```

- **Component**：GUI 组件 **共性**——大小、位置、可见性、绘制等。
- **Container**：可 **添加** 子组件（`add`）；`JFrame` 的内容区实际通过 **`contentPane`**（JPanel）添加组件。
- **Window / Frame / JFrame**：**顶层** 可独立显示窗口。

**（3）共性部分（Component / Container 简答要点）**

- 组件有 **位置、大小**（`setBounds` / 布局管理器）、**可见性**（`setVisible`）。
- **Container** 用 **LayoutManager**（如 BorderLayout、FlowLayout）管理子组件；`add(组件, 位置)`。
- Swing 遵循 **单线程规则**：UI 更新在 **EDT（事件派发线程）** 上。

**（4）事件处理机制（必考 · 结合上机 FarmGUI）**

Java GUI 是 **事件驱动** 模型，三步：

1. **事件源（Event Source）**：如 `JButton`、窗口  
2. **事件对象（Event Object）**：如 `ActionEvent`、`WindowEvent`  
3. **事件监听器（Listener）**：实现接口，如 `ActionListener.actionPerformed`

**注册**：`button.addActionListener(监听器);`

**常见写法（上机必会 · 笔考可能让补全）**：

```java
button.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        // 题目要求的动作，如 area.append(text);
    }
});
```

**Adapter 适配器**：`MouseListener` 有 5 个方法，全写太烦 → 继承 **`MouseAdapter`** 只重写需要的；**`WindowAdapter`** 常只重写 **`windowClosing`** 处理关闭窗口。

**（5）EDT 与多线程的关系（简答常和多线程一起考）**

- Swing **只允许 EDT** 创建和更新 UI。
- **耗时操作**（读文件、网络、定时保存如 `AutoSaveThread`）必须在 **后台线程**。
- 后台完成后更新界面：用 **`SwingUtilities.invokeLater(() -> { 更新UI; })`** 回到 EDT。

**（6）上机作业 ↔ 简答考点对照（重点复习）**

| 上机内容 | 简答可能问 |
|----------|------------|
| **FarmGUI** | AWT/Swing 区别、Listener、Adapter、事件三步、EDT |
| **AutoSaveThread** | 为何 GUI 要另开线程、start/run、线程与界面分离 |
| **练习一 CalendarApp** | Scanner、String（读程为主） |
| **练习二 农场数组** | 继承、OOP（编程为主） |
| **练习三 ArrayList/HashMap** | 集合概念、List/Set/Map（简答+编程） |
| **练习四 FarmStorage** | 字节流/字符流、BufferedReader（简答+编程） |

**一句话总结**：Swing 轻量跨平台；**Component→Container→Window/JFrame**；**事件源+事件+Listener**；耗时放 **后台线程**，改 UI 回 **EDT**。

---

### 专题 C · 其他简答高频（剩 2～3 道从这里出）

| 考点 | 要点 |
|------|------|
| `==` vs `equals` | 官方样例；String 用 equals |
| List / Set / Map | 有序重复 / 不重复 / 键值对 |
| 抽象类 vs 接口 | 单继承 vs 多实现 |
| 受检 vs 非受检异常 | IOException 必须处理 |
| 字节流 vs 字符流 | 文本用 Reader/Writer |

---

### 简答考场策略

1. **先扫全卷**：找到多线程题、GUI 题，优先写满（各约 5～8 分）。  
2. **只写概念**：定义 + 3～5 分点 + 一句总结；**不要写 main、不要写完整类**。  
3. **用上机自己的话**：结合 FarmGUI「按钮点击后追加文本」等 **你写过的逻辑** 举例，比空背模板得分高。  
4. **独立作答**：简答换说法、换例子也能写——这才是会了。

---

'''

READ_EXTRA = r'''
## I 组 · 继承综合加难（5 题）

### 读程 I1

**📖 相关知识点**

- 三层继承构造顺序；子类构造 **super** 调父类。
- 实例初始化顺序：父 static → 子 static → 父实例 → 父构造 → 子实例 → 子构造。

**问：写出运行结果**

```java
class A {
    A() { System.out.print("A"); }
}
class B extends A {
    B() { System.out.print("B"); }
}
class C extends B {
    C() { System.out.print("C"); }
}
public class TestI1 {
    public static void main(String[] args) {
        new C();
    }
}
```

**输出结果**：`ABC`

---

### 读程 I2

**📖 相关知识点**

- 子类 **不能** 缩小重写方法的访问权限（public 不能变 private）。
- 本题能编译；动态绑定调子类 f。

**问：写出运行结果**

```java
class Base {
    void f() { System.out.print("B"); }
}
class Sub extends Base {
    public void f() { System.out.print("S"); }
}
public class TestI2 {
    public static void main(String[] args) {
        Base b = new Sub();
        b.f();
    }
}
```

**输出结果**：`S`

---

### 读程 I3

**📖 相关知识点**

- 数组 + 多态：元素类型是父类，存子类对象；调 **实例方法** 看 **实际类型**。

**问：写出运行结果**

```java
class Animal {
    void speak() { System.out.print("A"); }
}
class Dog extends Animal {
    void speak() { System.out.print("D"); }
}
public class TestI3 {
    public static void main(String[] args) {
        Animal[] arr = { new Dog(), new Animal() };
        for (Animal a : arr) a.speak();
    }
}
```

**输出结果**：`DA`

---

### 读程 I4

**📖 相关知识点**

- **接口 default** 了解即可；本题普通 implements。
- 类实现两个接口，各方法都要能调。

**问：写出运行结果**

```java
interface I1 { void f(); }
interface I2 { void g(); }
class C implements I1, I2 {
    public void f() { System.out.print("1"); }
    public void g() { System.out.print("2"); }
}
public class TestI4 {
    public static void main(String[] args) {
        C c = new C();
        c.f();
        c.g();
    }
}
```

**输出结果**：`12`

---

### 读程 I5

**📖 相关知识点**

- 课件 **Sandwich** 简化：成员对象初始化在 **构造之前**（实例变量初始化）。

**问：写出运行结果**

```java
class X {
    X() { System.out.print("X"); }
}
class Y extends X {
    Y() { System.out.print("Y"); }
    int n = init();
    int init() { System.out.print("I"); return 1; }
}
public class TestI5 {
    public static void main(String[] args) {
        new Y();
    }
}
```

**输出结果**：`XIY`

**分析**：先父构造 X → 子类字段 init 打印 I → 子构造 Y。

---

## J 组 · 多线程读程（5 题 · 配合简答）

### 读程 J1

**📖 相关知识点**

- **两次 start()** 同一 Thread → 第二次 **IllegalThreadStateException**（了解）；若题目只问第一次输出则 `TM`。
- 本题只 start 一次。

**问：写出运行结果**

```java
public class TestJ1 {
    public static void main(String[] args) throws Exception {
        Thread t = new Thread(() -> System.out.print("T"));
        t.start();
        t.join();
        System.out.print("M");
    }
}
```

**输出结果**：`TM`

**分析**：`join()` 等子线程结束再打印 M，顺序 **确定**。

---

### 读程 J2

**📖 相关知识点**

- **join** 保证子线程先结束；与简答「线程控制方法」对应。

**问：写出运行结果**

```java
public class TestJ2 {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception {
        Thread t1 = new Thread(() -> sb.append("1"));
        Thread t2 = new Thread(() -> sb.append("2"));
        t1.start();
        t1.join();
        t2.start();
        t2.join();
        System.out.println(sb.toString());
    }
}
```

**输出结果**：`12`

---

### 读程 J3

**📖 相关知识点**

- **synchronized** 方法：两线程各 add 10000 次，理论 **20000**（笔考理想模型）。

**问：写出运行结果**

```java
public class TestJ3 {
    static int n = 0;
    static synchronized void add() { n++; }
    public static void main(String[] args) throws Exception {
        Thread t1 = new Thread(() -> { for (int i = 0; i < 1000; i++) add(); });
        Thread t2 = new Thread(() -> { for (int i = 0; i < 1000; i++) add(); });
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println(n);
    }
}
```

**输出结果**：`2000`

---

### 读程 J4

**📖 相关知识点**

- **无 synchronized** 时多次 `n++` 可能 **丢失更新**，结果 **≤ 2000** 且不固定。
- 与 J3 对照：有 synchronized 才 **确定 2000**。

**问：写出运行结果**（下列代码 **没有** synchronized）

```java
public class TestJ4 {
    static int n = 0;
    static void add() { n++; }
    public static void main(String[] args) throws Exception {
        Thread t1 = new Thread(() -> { for (int i = 0; i < 1000; i++) add(); });
        Thread t2 = new Thread(() -> { for (int i = 0; i < 1000; i++) add(); });
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println(n);
    }
}
```

**输出结果**：**≤ 2000 的不确定值**（竞态；笔考若未强调同步，可写「可能小于 2000」；若题目明确要求 synchronized 则用 J3）

---

### 读程 J5

**📖 相关知识点**

- **Runnable** 与 Thread；`new Thread(r).start()`。

**问：写出运行结果**

```java
public class TestJ5 {
    public static void main(String[] args) throws Exception {
        Runnable r = () -> System.out.print("R");
        Thread t = new Thread(r);
        t.start();
        t.join();
        System.out.print("M");
    }
}
```

**输出结果**：`RM`

---

## K 组 · 集合 / String 加难（5 题）

### 读程 K1

**📖 相关知识点**

- **Iterator** 遍历；`remove` 需先 `next`（本题只读）。

**问：写出运行结果**

```java
import java.util.*;
public class TestK1 {
    public static void main(String[] args) {
        List<Integer> L = Arrays.asList(3, 1, 2);
        Collections.sort(L);
        System.out.println(L);
    }
}
```

**输出结果**：`[1, 2, 3]`

---

### 读程 K2

**📖 相关知识点**

- **TreeSet** 有序；自然排序 String 字典序。

**问：写出运行结果**

```java
import java.util.*;
public class TestK2 {
    public static void main(String[] args) {
        Set<String> s = new TreeSet<>();
        s.add("banana");
        s.add("apple");
        s.add("cherry");
        System.out.println(s);
    }
}
```

**输出结果**：`[apple, banana, cherry]`

---

### 读程 K3

**📖 相关知识点**

- **StringBuilder** 可变；与 String 循环对比。

**问：写出运行结果**

```java
public class TestK3 {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 3; i++) sb.append(i);
        System.out.println(sb.toString());
        System.out.println(sb.length());
    }
}
```

**输出结果**：
```
012
3
```

---

### 读程 K4

**📖 相关知识点**

- **Autoboxing**；`==` 比较 Integer 127 内缓存。

**问：写出运行结果**

```java
public class TestK4 {
    public static void main(String[] args) {
        Integer a = 100, b = 100, c = 200, d = 200;
        System.out.println(a == b);
        System.out.println(c == d);
    }
}
```

**输出结果**：
```
true
false
```

---

### 读程 K5

**📖 相关知识点**

- **Map keySet** 遍历；HashMap **无序**（输出顺序可能变，考试常只问 get）。

**问：写出运行结果**

```java
import java.util.*;
public class TestK5 {
    public static void main(String[] args) {
        Map<String, Integer> m = new HashMap<>();
        m.put("a", 1);
        m.put("b", 2);
        System.out.println(m.get("a") + m.get("b"));
        System.out.println(m.containsKey("c"));
    }
}
```

**输出结果**：
```
3
false
```

---

'''

READ_INDEX = r'''## 读程题自测索引（40 题 · 只写输出）

| 编号 | 难度 | 核心考点 |
|------|------|----------|
| 官方 Test2 | ★★ | 遮蔽、this、toString |
| A1-A4 | ★★ | 参数遮蔽、UnmaskField、static 共享、重载 |
| B1-B4 | ★★★ | String 循环、常量池、混合运算、包装类 |
| C1-C5 | ★★★★ | static/实例绑定、PrivOverride、构造+多态、static 块、引用 |
| D1-D3 | ★★ | static 计数、final 引用、重写 |
| E1-E4 | ★★★ | ArrayList 课件、remove 陷阱、HashMap、HashSet |
| F1-F3 | ★★★ | 异常链、循环+finally、return+finally |
| G1-G3 | ★★★ | run/start、join、synchronized |
| H1-H4 | ★★★ | switch 贯穿、二维数组、短路、嵌套循环 |
| **I1-I5** | ★★★ | 多层继承、数组+多态、双接口、初始化顺序 |
| **J1-J5** | ★★★★ | 线程顺序、join、synchronized、Runnable |
| **K1-K5** | ★★★ | 排序、TreeSet、StringBuilder、Integer 缓存、Map |

> **冲刺建议**：每天 **手算 10 道**（含 I/J/K）；考场 5～7 道，难度 **C/E/F/J** 居多。  
> **配合简答**：读程 J 组与 [多线程专题](#专题-a--多线程整道大题--默写版) 一起复习。

'''

PROG_BANK = r'''
## 编程题练习题库（10 道 · 按条写）

> 每道按 **题目要求格式** 列出，附 **参考答案骨架**。  
> 用法：**遮住答案** → 按 [全能考点手册](#第三步编程题全能考点手册按课件--按题目用语) 逐条写 → 再对照。

---

### 练习 1 · EmpInfo（PPT 原题 · 普通类）

**要求**

1. 类 `EmpInfo`：字段 `name`、`designation`、`department`（均为 String）。  
2. 非缺省构造方法，初始化三字段。  
3. 方法 `print()` 输出三字段。

<details><summary>参考答案骨架</summary>

```java
class EmpInfo {
    private String name, designation, department;
    public EmpInfo(String name, String designation, String department) {
        this.name = name;
        this.designation = designation;
        this.department = department;
    }
    public void print() {
        System.out.println(name + ", " + designation + ", " + department);
    }
}
```

</details>

---

### 练习 2 · Rectangle + Point（PPT 几何题）

**要求**

1. `Point`：double `x,y`；无参构造置 0；两参构造；`distance(Point p)` 返回距离。  
2. `Rectangle`：double `width`,`height`；无参构造；两参构造；`getArea()`、`getPerimeter()`。

<details><summary>参考答案骨架</summary>

```java
class Point {
    private double x, y;
    public Point() { x = y = 0; }
    public Point(double x, double y) { this.x = x; this.y = y; }
    public double distance(Point p) {
        return Math.sqrt((x-p.x)*(x-p.x) + (y-p.y)*(y-p.y));
    }
}
class Rectangle {
    private double width, height;
    public Rectangle() { width = height = 0; }
    public Rectangle(double w, double h) { width = w; height = h; }
    public double getArea() { return width * height; }
    public double getPerimeter() { return 2 * (width + height); }
}
```

</details>

---

### 练习 3 · Animal 继承链（练习二农场）

**要求**

1. 类 `Animal`：字段 `name`；构造；方法 `speak()` 输出 `"animal"`。  
2. 类 `Cow extends Animal`：重写 `speak()` 输出 `"moo"`。  
3. 类 `Sheep extends Animal`：重写 `speak()` 输出 `"baa"`。

<details><summary>参考答案骨架</summary>

```java
class Animal {
    protected String name;
    public Animal(String name) { this.name = name; }
    public void speak() { System.out.println("animal"); }
}
class Cow extends Animal {
    public Cow(String name) { super(name); }
    @Override public void speak() { System.out.println("moo"); }
}
class Sheep extends Animal {
    public Sheep(String name) { super(name); }
    @Override public void speak() { System.out.println("baa"); }
}
```

</details>

---

### 练习 4 · 抽象类 + 抽象方法

**要求**

1. 抽象类 `Shape`：抽象方法 `double area()`。  
2. 类 `Circle extends Shape`：字段 `radius`；构造；实现 `area()` 返回 πr²。  
3. 类 `Rect extends Shape`：字段 `w,h`；实现 `area()` 返回 w×h。

<details><summary>参考答案骨架</summary>

```java
abstract class Shape {
    abstract double area();
}
class Circle extends Shape {
    private double radius;
    Circle(double r) { radius = r; }
    public double area() { return Math.PI * radius * radius; }
}
class Rect extends Shape {
    private double w, h;
    Rect(double w, double h) { this.w = w; this.h = h; }
    public double area() { return w * h; }
}
```

</details>

---

### 练习 5 · 双接口 Flyable + Swimmable

**要求**

1. 接口 `Flyable { void fly(); }`，`Swimmable { void swim(); }`。  
2. 类 `Duck extends Animal implements Flyable, Swimmable`：实现 `fly()` 打印 `"fly"`，`swim()` 打印 `"swim"`。

<details><summary>参考答案骨架</summary>

```java
interface Flyable { void fly(); }
interface Swimmable { void swim(); }
class Duck extends Animal implements Flyable, Swimmable {
    public Duck(String name) { super(name); }
    public void fly() { System.out.println("fly"); }
    public void swim() { System.out.println("swim"); }
}
```

</details>

---

### 练习 6 · HashMap 统计单词（练习三）

**要求**

写静态方法 `countWords(String[] words)`：返回 `Map<String,Integer>`，统计每个单词出现次数（忽略大小写）。

<details><summary>参考答案骨架</summary>

```java
static Map<String, Integer> countWords(String[] words) {
    Map<String, Integer> map = new HashMap<>();
    for (String w : words) {
        w = w.trim().toLowerCase();
        map.put(w, map.getOrDefault(w, 0) + 1);
    }
    return map;
}
```

</details>

---

### 练习 7 · 文件去空行（练习四 FarmStorage）

**要求**

写方法 `copyNonEmpty(String in, String out) throws IOException`：按行读入，**跳过空行**，写入 out。

<details><summary>参考答案骨架</summary>

```java
static void copyNonEmpty(String in, String out) throws IOException {
    try (BufferedReader br = new BufferedReader(new FileReader(in));
         BufferedWriter bw = new BufferedWriter(new FileWriter(out))) {
        String line;
        while ((line = br.readLine()) != null) {
            if (line.trim().isEmpty()) continue;
            bw.write(line);
            bw.newLine();
        }
    }
}
```

</details>

---

### 练习 8 · ActionListener 补全（FarmGUI 型）

**要求**

已有 `JButton saveBtn`、`JTextArea logArea`、`JTextField input`。为 `saveBtn` 添加监听器：点击时将 `input` 文本追加到 `logArea` 并换行。

<details><summary>参考答案骨架</summary>

```java
saveBtn.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        logArea.append(input.getText() + "\n");
    }
});
```

</details>

---

### 练习 9 · AutoSaveThread（上机大作业型）

**要求**

1. 类 `AutoSave extends Thread`。  
2. 字段 `volatile boolean running = true`。  
3. `run()`：while(running) { sleep(1000); System.out.println("saving..."); }  
4. 方法 `stopSave()`：设 running=false 并 interrupt。

<details><summary>参考答案骨架</summary>

```java
class AutoSave extends Thread {
    private volatile boolean running = true;
    public void stopSave() { running = false; interrupt(); }
    @Override
    public void run() {
        while (running) {
            try {
                Thread.sleep(1000);
                System.out.println("saving...");
            } catch (InterruptedException e) {
                if (!running) break;
            }
        }
    }
}
```

</details>

---

### 练习 10 · Person/Student 变式（官方样例变体）

**要求**

在官方 Person/Job/Life/Student 基础上：  
1. 抽象类 `Person` 增加 **抽象方法** `abstract void introduce();`  
2. `Student` 实现 `introduce()` 输出 `"我是学生"`  
3. 其余同官方（super、living、setJob、toString）

<details><summary>参考答案骨架</summary>

在 Student 中增加：
```java
@Override
public void introduce() {
    System.out.println("我是学生");
}
```
Person 中增加：`abstract void introduce();`

</details>

---

### 练习 11 · 官方样例完整默写（第 0 题 · 必做）

见 [官方样例题 · 满分骨架](#满分骨架默写) —— **闭卷 12 分钟**。

---

'''

# Insert SHORT_MEGA after 简答题 intro
anchor = "# 一、简答题（4～5 道）\n\n> **只考概念**"
if SHORT_MEGA.strip() not in text:
    i = text.index(anchor) + len(anchor)
    # skip to after first --- block following 官方样例题 section... insert before ## 官方样例题
    insert_at = text.index("## 官方样例题\n\n![简答题样例", text.index("# 一、简答题"))
    text = text[:insert_at] + SHORT_MEGA + text[insert_at:]

# Replace read index section and insert extra questions before it
old_idx = "## 读程题自测索引（25 题 · 只写输出）"
if old_idx in text:
    i = text.index(old_idx)
    text = text[:i] + READ_EXTRA + READ_INDEX + text[i + len(old_idx):]
    # remove old table until next ---
    # already replaced by READ_INDEX; need to delete old table content
    old_tail = text.index("> **冲刺建议**：考场 **5～7 道** 读程，难度接近 C/E/F 组")
    old_end = text.index("\n\n---\n\n# ★ 期末抢分秘籍", old_tail)
    text = text[:text.index("> **冲刺建议**：考场 **5～7 道** 读程，难度接近 C/E/F 组")] + text[old_end:]

# Update read section title count
text = text.replace(
    "# 二、读程题（5～7 道 · 题库 25 题）",
    "# 二、读程题（5～7 道 · 题库 40 题）",
    1,
)
text = text.replace(
    "> 下面 **25 道** 偏 **综合、多步手算**",
    "> 下面 **40 道** 偏 **综合、多步手算**",
    1,
)

# Insert programming bank
bank_anchor = "## 编程题自测（按全能手册）"
if bank_anchor in text and "## 编程题练习题库" not in text:
    i = text.index(bank_anchor)
    text = text[:i] + PROG_BANK + text[i:]

# Update checklist
text = text.replace(
    "**简答（4～5）**\n\n- [ ] 多线程全套",
    "**简答（4～5）**\n\n- [ ] [多线程专题 A](#专题-a--多线程整道大题--默写版) + [GUI 专题 B](#专题-b--gui--用户界面整道大题--默写版) **闭卷默写**\n- [ ] 对照 [上机作业表](#专题-b--gui--用户界面整道大题--默写版) 回忆 FarmGUI / FarmStorage\n- [ ] 多线程全套",
    1,
)
text = text.replace(
    "- [ ] String / 集合 / 线程 各练 2 道",
    "- [ ] 读程 **I/J/K 组** 各练 2 道 + C/E 组各 2 道",
    1,
)
text = text.replace(
    "- [ ] `BufferedReader` 按行读方法",
    "- [ ] [编程练习题库](#编程题练习题库10-道--按条写) 至少练 **1、6、7、8、11**",
    1,
)

MD.write_text(text, encoding="utf-8")
print("OK lines", text.count("\n"))
