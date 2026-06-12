---
title: Java 程序设计 · 期末满分攻略
date: 2026-05-22
tags: 学习/大三下学期期末考试复习/Java
column: 学习笔记
toc: true
---

# Java 程序设计 · 期末满分攻略（笔考 · 按题型）

> **考试形式**：闭卷纸笔，**仅 3 种题型**  
> **资料**：任课教师期末说明 + 课件 `D:\Study\大三\大三下学期\JAVA\课件\`（8 个 `.ppt`）+ 上机实验源码  
> **PPT 路径**：`JAVA\课件\` — 第一章概念（**历史不看**）；**第三章起全部重要**；GUI 无独立课件，结合大作业 `FarmGUI` 自学  
> **说明**：需用库时会 **提供方法声明**；PPT **历史沿革不考**

![期末考试题型说明](/java-exam/exam-structure.png)

| 题型 | 题量 | 核心要求 |
|------|------|----------|
| **简答题** | **4～5 道** | **只考概念**，不写完整程序；**必考多线程 + GUI** 各至少 1 道 |
| **读程题** | **5～7 道** | 写运行结果 / 判断能否编译 |
| **编程题** | **2 道** | 纸笔写类、接口、方法（常考 OOP 建模） |

**复习顺序**：简答背概念 → 读程手算 → 编程默写骨架。

---

## 目录

- [PPT 章节 ↔ 题型对照](#ppt-章节--题型对照摘自-javacourse)
- [按课件逐章要点](#按课件逐章要点抄自-ppt按题型归类)
- [一、简答题（4～5 道）](#一简答题45-道)
- [二、读程题（5～7 道）](#二读程题57-道)
- [三、编程题（2 道）](#三编程题2-道)
- [冲刺 Checklist](#冲刺-checklist)
- [附录：实验代码 ↔ 考点](#附录实验代码--考点)

---

## PPT 章节 ↔ 题型对照（摘自 `JAVA\课件`）

| 课件文件 | 章节 | 复习策略 | 简答 | 读程 | 编程 |
|----------|------|----------|:----:|:----:|:----:|
| `1_JAVA程序设计.ppt` | **第一章** Java 概述 | 概念全考；**Slide 8～15 发展历史跳过** | ★★★ | ★★ | ★ |
| `2_面向对象程序设计概念.ppt` | **第二章** OOP 概念 | **六个概念必背**（见下） | ★★★ | ★★ | ★★ |
| `3_JAVA语言基础.ppt` | **第三章** 语言基础 | **第三章起全重要** | ★★★ | ★★★ | ★★ |
| `4_Java面向对象特性.ppt` | **第四章** 面向对象特性 | 类/包/继承/多态；**官方读程 Test2 同类** | ★★★ | ★★★ | ★★★ |
| `5_Java高级语言特征.ppt` | **第五章** 高级特征 | static/final/抽象接口/集合/enum | ★★★ | ★★★ | ★★★ |
| `6_异常处理.ppt` | **第六章** 异常 | 受检/非受检、try-catch-finally | ★★ | ★★★ | ★★ |
| `7_输入输出.ppt` | **第七章** I/O | File、字节/字符流、BufferedReader | ★★ | ★★ | ★★★ |
| `9_线程.ppt` | **第九章** 线程 | **简答必考**；锁、状态、同步 | ★★★ | ★★★ | ★★ |
| （无课件） | GUI 程序设计 | 课程大纲有、文件夹无 `.ppt`；**简答必考** + 大作业 | ★★★ | ★ | ★★ |

**第二章六个概念（PPT Slide 10，必背）**：① 抽象 ② 对象 ③ 类 ④ 封装 ⑤ 继承 ⑥ 多态

**课堂未讲但会考（自学 + PPT 要求手写例子）**：GUI adapter/listener/匿名内部类；线程锁与状态转换；`enum`；PPT 例题须**独立思考、勿粘贴**

---

## 按课件逐章要点（抄自 PPT，按题型归类）

### 第一章 `1_JAVA程序设计.ppt`（历史不看）

| 考点（简答/读程） | PPT 要点 |
|-------------------|----------|
| 什么是 Java | 既是**编程语言**又是**平台**；一次编写到处运行 |
| Java SE / EE / ME | SE：桌面；EE：企业；ME：嵌入式；本课指 **Java SE** |
| Java 特征（10 条） | 简单、面向对象、分布式、解释型、可移植、健壮、安全、高性能、**多线程**、动态 |
| 与 C++ 不同 | **无指针**、**单继承**（接口多实现）、**package**、**abstract/final** |
| JVM / JRE | JRE = JVM + Java API；字节码 → 类装载 → 验证 → 解释/JIT |
| 主类与 main | `public class` 与源文件同名；`public static void main(String[] args)` |
| **不考** | Gosling、JDK 版本年表、TIOBE 排名等历史 |

### 第二章 `2_面向对象程序设计概念.ppt`

| 概念 | 简答一句话 + 要点 |
|------|-------------------|
| **抽象** | 说明本质、忽略非本质；OOP 基础 |
| **对象** | 状态（成员变量）+ 行为（方法）+ 标识；**消息 = 方法调用** |
| **类** | 同种对象的集合与抽象；**实例化 → 对象** |
| **封装** | 数据+方法包装进类；`public/protected/private/默认` 隐藏实现 |
| **继承** | is-a；子类继承父类变量方法；可增新成员、**重写**；Java **单继承** |
| **多态** | 编译时：**重载**；运行时：**重写 + 向上转型 + 动态绑定** |

### 第三章 `3_JAVA语言基础.ppt`（读程高频）

| 模块 | 要点 |
|------|------|
| 数据类型 | 基本 8 种 + 引用（类、接口、数组、**enum**）；`boolean` 与整型**不能互转** |
| String | **类**，非基本类型；**不可变**；修改用 `StringBuilder`（`StringBuffer` 线程安全） |
| **NaN / Infinity** | `0.0/0.0→NaN`；`1.0/0.0→Infinity`；`NaN==NaN` 为 **false**；用 `Double.isNaN()` |
| `==` vs `equals` | `==` 比**引用**；`equals` 默认同 `==`，`String` 等重写后比**内容**（**官方简答样例**） |
| 变量 | 成员 / 局部 / 参数；引用类型声明只分配引用，须 `new` 实例化；**局部变量使用前必须赋值** |
| 运算符 | 短路 `&&` `\|\|`；`instanceof`；`>>` 带符号 / `>>>` 零填充 |
| 流控制 | `switch` 须 `break`；增强 for `for(String s: arr)` |
| 数组 | 引用类型；`length`；赋值是**引用复制**；`System.arraycopy`；多维 `int[][]` |

### 第四章 `4_Java面向对象特性.ppt`（编程 + 读程）

| 模块 | 要点 |
|------|------|
| 类体四部分 | 成员变量、构造方法、成员方法、**初始化块** |
| `this` | 区分成员与局部；`this.y`；构造中 `this(...)` 重载 | 
| 参数传递 | **值传递**；引用传的是引用的副本，改对象内容会影响实参 |
| 包与 import | `package` 第一行；`import`；访问权限 **public > protected > 默认 > private** |
| 对象生命周期 | `new` → 分配空间、默认初始化、显式初始化、构造 → 引用；**GC** 无引用可回收 |
| 继承 | `extends`；不继承 `private` 构造；隐含继承 **Object**；`super()` 第一行 |
| 多态 | 重载 vs 重写；向上转型 `Animal a=new Dog()`；**动态绑定**（非 static/final） |
| **读程必考** | 局部变量**遮蔽**成员 + `this.y`（PPT `UnmaskField` = 官方 `Test2`） |

### 第五章 `5_Java高级语言特征.ppt`

| 模块 | 要点 |
|------|------|
| static | 类变量/方法共享；**无 this**；静态方法**不重写多态** |
| final | 类不可继承、方法不可重写、变量不可改；引用 final 指向不变但对象可变 |
| 抽象类 | 可有构造；**不能 new**；子类实现全部抽象方法才可实例化 |
| 接口 | 常量 `public static final`；方法 `public abstract`；类 **implements** 可多接口 |
| 抽象 vs 接口 | 抽象类可有非抽象方法、单继承；接口全抽象、多实现 |
| 泛型集合 | `ArrayList<E>`、`HashMap<K,V>`；`Collection` / `List` / `Set` / `Map` |
| List | `ArrayList` 随机访问快；`LinkedList` 插删快 |
| Set | `HashSet` 无序；`TreeSet` 有序；放 HashSet 需 `equals`+`hashCode` |
| Map | `put` 同 key **覆盖**；`HashMap` 无序；`TreeMap` 有序 |
| Iterator | `hasNext`/`next`/`remove`（先 next 再 remove） |
| **enum** | `enum Season{...}`；`values()`、`name()`、`ordinal()`；构造 **private** |
| Wrapper | 基本类型包装；**autoboxing / autounboxing** |

### 第六章 `6_异常处理.ppt`

| 要点 | 说明 |
|------|------|
| Error vs Exception | Error 严重不可恢复；Exception 可捕获 |
| 受检 vs 非受检 | `IOException` 等**必检**须处理；`RuntimeException` **免检** |
| try-catch-finally | 未捕获则终止；**finally 常执行**（关流） |
| throws / throw | 方法声明 `throws`；`throw` 抛给调用者 |
| 读程 | 未捕获异常 → **后续语句不执行** |

### 第七章 `7_输入输出.ppt`

| 要点 | 说明 |
|------|------|
| File | 文件/目录抽象；`exists`、`length`、`list`；不读写内容 |
| 字节流 vs 字符流 | `InputStream/OutputStream` vs `Reader/Writer` |
| 节点流 vs 过滤流 | `FileReader` 节点；`BufferedReader` 过滤 |
| 文本按行 | **`BufferedReader.readLine()`** + `FileReader` |
| 文本写出 | `BufferedWriter` + **`newLine()`**；或 `PrintWriter.println` |
| Scanner | `nextInt()`、`nextLine()` 等（练习一 `CalendarApp`） |
| 对象串行化 | `implements Serializable`；`ObjectOutputStream.writeObject` |

### 第九章 `9_线程.ppt`（简答必考）

| 考点 | PPT 原文要点 |
|------|----------------|
| 进程 vs 线程 | 进程内核级；线程用户级；**同进程线程共享进程状态** |
| 创建方式 | ① `implements Runnable` + `new Thread(r).start()` ② `extends Thread` |
| `start()` vs `run()` | **必须 `start()`** 才进入 Runnable；直接 `run()` 只是普通调用 |
| 优先级 | `MIN=1, NORM=5, MAX=10`；子线程继承父线程优先级 |
| 控制方法 | `sleep`、`join`、`yield`；**不要用 stop/suspend/resume** |
| 同步 | **`synchronized`** = 对象锁；临界区互斥；**lock pool / wait pool** |
| 死锁 | 两线程互等对方锁；**统一加锁顺序**预防 |
| wait/notify | 在 synchronized 中；`wait()` 释放锁进 wait pool；`notify()` 唤醒 |
| 线程状态 | **new → Runnable → Running → Blocked → Dead**；sleep/join/等锁/wait 会阻塞 |

### GUI（课程大纲有，课件文件夹无独立 `.ppt`）

结合大作业 `FarmGUI.java` + 自学：**AWT 重量级 vs Swing 轻量级**、组件层次、`ActionListener` / `WindowAdapter`、**匿名内部类**、**EDT**（耗时操作放后台线程）。

---

# 一、简答题（4～5 道）

> **只考概念**：定义 → 分点 → 短例。不写 `main`、不写完整可运行程序。

## 官方样例题

![简答题样例：== 与 equals](/java-exam/sample-short-answer.png)

**题目**：`==` 和 `equals` 方法有什么区别？

**满分答案（分点默写）**

1. **`==`**：比较 **引用（地址）** 是否同一对象；基本类型比较 **值**。
2. **`equals`**：`Object` 的方法，默认等同 `==`；`String` 等类 **重写后比较内容**。
3. **String 特例**：字面量可能共享常量池，`==` 有时为 true；`new String("x")` 与字面量 `==` 通常为 false。
4. **规范**：比较字符串内容用 **`equals`**，不用 `==`。

---

## 答题规范

| 步骤 | 做法 |
|------|------|
| ① | 一句话 **定义** |
| ② | **2～5 个要点**（区别 / 优缺点 / 步骤） |
| ③ | 可选：一句 **例子** 或对比表 |

---

## ★ 必考专题 A：多线程（至少 1 道）

| 考点 | 参考答案要点 |
|------|----------------|
| **进程 vs 线程** | 进程：资源分配单位，独立地址空间；线程：CPU 调度单位，**共享进程资源** |
| **多线程概念** | 一进程内 **多条执行流** 并发/交替执行 |
| **多线程好处** | 提高 CPU 利用率；I/O 等待时可切换；GUI 后台任务不阻塞界面 |
| **多线程问题** | 数据竞争、线程安全；调试难；上下文切换开销 |
| **线程如何同步** | `synchronized` 同步方法/块；`Lock`；互斥访问共享资源 |
| **同步不好怎么办** | 缩小同步范围；避免嵌套锁；固定加锁顺序；`volatile` 保可见性（不代替互斥） |
| **死锁产生** | 多线程 **互相等待** 对方已持有的锁；加锁顺序不一致 |
| **死锁解除** | **预防**：统一加锁顺序、减少嵌套；**避免**：`tryLock` 超时；检测后中断（代价大） |
| **`start()` vs `run()`** | `start()` 启动 **新线程**；直接 `run()` 只是普通方法调用 |
| **线程状态**（PPT 第九章） | **new** → **Runnable** → **Running** → **Blocked** → **Dead**；`sleep`/`join`/等锁/`wait` 进入 Blocked |
| **对象锁** | 每个 `synchronized` 对象有**排他锁**；未获锁线程进 **lock pool** 等待 |
| **wait/notify** | `wait()` 释放锁、进 **wait pool**；`notify()` 唤醒一个到 lock pool |
| **GUI 为何要新线程** | Swing 在 **EDT** 绘界面；耗时操作放 EDT 会 **卡死**，应后台线程 + `invokeLater` 更新 UI |

---

## ★ 必考专题 B：GUI — Swing 与 AWT（至少 1 道）

| 考点 | 参考答案要点 |
|------|----------------|
| **AWT vs Swing** | AWT：**重量级**，依赖本地控件；Swing：**轻量级**，纯 Java 绘制，组件更丰富 |
| **层次结构（共性）** | `Component` → `Container` → `Window`/`Panel` → 具体组件；**布局管理器** 排位置 |
| **Swing 常用** | `JFrame`、`JPanel`、`JButton`、`JTextArea`；`BorderLayout`、`FlowLayout`、`GridLayout` |
| **事件处理模型** | **事件源** → **事件对象** → **监听器** 处理 |
| **Listener** | 接口，如 `ActionListener`（`actionPerformed`）、`MouseListener` |
| **Adapter** | 适配器类（`WindowAdapter`、`MouseAdapter`）**空实现**，只重写需要的方法 |
| **内部类** | 类中定义类；可访问外部类成员；GUI 中作监听器 |
| **匿名类 / 匿名内部类** | `new XxxListener() { ... }`；无类名；可访问 effectively final 局部变量 |
| **事件处理方法** | 注册：`addActionListener(...)`；处理：在回调方法中写逻辑 |
| **EDT** | Event Dispatch Thread；Swing **单线程** 更新界面 |

**层次结构（简答可画图/写）**

```
Component
└── Container
    ├── Window → Frame / JFrame
    └── Panel / JPanel
        └── JButton、JTextField、JTextArea …
```

---

## 专题 C：String / Math / Object（官方样例延伸）

| 考点 | 要点 |
|------|------|
| `==` vs `equals` | 见 [官方样例](#官方样例题) |
| String 不可变 | `concat`、`+` 产生新对象，原串不变 |
| String vs StringBuilder | String 不可变；StringBuilder **可变**，循环拼接首选 |
| Object 三方法 | `toString` 可读信息；`equals` 先 `instanceof` 再比字段；`hashCode` 与 equals 一致 |
| `hashCode` 约定 | **equals 相等 → hashCode 必须相等** |

### Infinity 与 NaN（自学必考）

| 表达式 | 结果 |
|--------|------|
| `1.0 / 0.0` | `Infinity` |
| `0.0 / 0.0` | `NaN` |
| `NaN == NaN` | **false** |
| 正确判断 | `Double.isNaN(x)`、`Double.isInfinite(x)` |

---

## 专题 D：容器 Collection Framework

| 考点 | 要点 |
|------|------|
| List / Set / Map | List **有序可重复**；Set **不重复**；Map **键值对** |
| ArrayList vs LinkedList | ArrayList **随机访问快**；LinkedList **头尾插删快** |
| HashSet vs TreeSet | HashSet 无序 O(1)；TreeSet **有序**（Comparable/Comparator） |
| HashMap | `put` 重复 key **覆盖** value；`getOrDefault` |
| 迭代删除 | 用 `Iterator.remove()`，勿在 for-each 里直接 `list.remove(i)` |

**体系简图（简答可画）**

```
Collection → List(ArrayList/LinkedList)、Set(HashSet/TreeSet)
Map → HashMap、TreeMap（不属于 Collection）
```

---

## 专题 E：流 I/O

| 考点 | 要点 |
|------|------|
| 字节流 vs 字符流 | `InputStream/OutputStream` vs `Reader/Writer` |
| 文本按行读 | **`BufferedReader.readLine()`** + `FileReader` |
| 文本按行写 | **`BufferedWriter.newLine()`** + `FileWriter` |
| try-with-resources | `try (BufferedReader br = ...) { }` 自动关闭 |
| 选用 | `.txt` 用 **字符流**；二进制用字节流 |

---

## 专题 F：枚举 enum（自学必考）

```java
public enum Season { SPRING, SUMMER, AUTUMN, WINTER; }
```

| 要点 | 说明 |
|------|------|
| 定义 | `enum` 关键字，逗号分隔常量 |
| 使用 | `Season.SPRING`、`values()`、`ordinal()`、`switch` |
| 特点 | **类型安全** 常量；可有字段、构造、方法 |
| 比较 | 枚举常量用 `==` 即可（同一实例） |

---

## 专题 G：OOP 与第二章概念

| 考点 | 要点 |
|------|------|
| 封装 | private 字段 + public getter/setter，隐藏实现 |
| 继承 | `extends`；子类拥有父类非 private 成员；`super()` 调父构造 |
| 多态 | 父类引用指向子类对象；**重写** 方法运行时绑定 |
| 抽象类 | `abstract class`；可有抽象方法；**不能 new** |
| 接口 | `interface`；实现类 `implements`；多实现 |
| 包与访问控制 | `public` > `protected` > 默认 > `private` |

---

## 专题 H：异常（PPT 第六章 `6_异常处理.ppt`）

| 考点 | 要点 |
|------|------|
| Error vs Exception | Error 虚拟机级、不可恢复；Exception 应用程序可捕获 |
| 受检 vs 非受检 | **必检**：除 `RuntimeException` 及其子类外；**免检**：`RuntimeException`、Error |
| `try-catch-finally` | 至少一个 catch；**finally 无论是否异常都执行**（关文件流） |
| `throws` / `throw` | 方法签名 `throws IOException`；`throw new XxxException()` 交给调用者 |
| 重写与异常 | 子类重写方法不能抛出**比父类更多/更新**的受检异常 |
| 读程陷阱 | 未捕获异常 → **try 内后续语句不执行**，程序终止 |

---

## 简答题自测（闭卷）

1. 线程和进程的区别？多线程的好处和问题？
2. 线程如何同步？死锁如何产生和解除？
3. Swing 和 AWT 的区别？Listener 和 Adapter 各是什么？
4. `==` 和 `equals` 的区别？（官方样例）
5. List、Set、Map 的区别？ArrayList 和 LinkedList 呢？
6. 字节流和字符流的区别？读 txt 按行用什么？
7. `Infinity`、`NaN` 是什么？如何判断 NaN？
8. Java 枚举如何定义和使用？
9. 抽象类和接口的区别？
10. 为何 GUI 耗时操作要放新线程？

---

# 二、读程题（5～7 道）

> 给一段代码 → 写 **运行结果** 或判断 **能否编译**。

## 官方样例题

![读程题样例：Test2](/java-exam/sample-read-code.png)

```java
public class Test2 {
    private int x = 1;
    private int y = 1;

    public void changeState(int a, int b) {
        x = a;
        int y = b;        // 局部 y 遮蔽成员 y
        this.y = 8;       // 修改成员 y
        System.out.println("x=" + x + "; y=" + y);  // 局部 y=9
    }

    public String toString() {
        return "x = " + x + "; y = " + y;
    }

    public static void main(String[] args) {
        Test3 t3 = new Test3();   // × 编译错误：没有 Test3
        System.out.println(t3);
        t3.changeState(10, 9);
        System.out.println(t3);
    }
}
```

**分析**

| 步骤 | 结论 |
|------|------|
| 能否编译 | **不能** — `Test3` 类不存在 |
| 若改为 `Test2 t2 = new Test2();` | 可编译，输出如下 |

**正确输出（三行）**

```
x = 1; y = 1
x=10; y=9
x = 10; y = 8
```

**考点**：① 局部变量 **遮蔽** 成员（PPT 第四章 `UnmaskField`）② `this.y` 访问成员 ③ `println` 打印 **局部 y=9** ④ `toString` 打印 **成员 y=8** ⑤ 类名错误 → 编译失败

---

## 解题五步法

1. **先判编译**：类名、接口是否实现、抽象方法、访问权限  
2. **圈作用域**：成员 / 局部 / 参数；是否 **`this.`**  
3. **盯修改**：`add/remove`、`start()` 是否调用、String 是否重新赋值  
4. **手算输出**：`substring` 左闭右开；`==` vs `equals`  
5. **多线程**：`start` 顺序、`sleep`、`synchronized` 谁先拿锁

---

## 分类训练

### ① 编译与作用域（官方样例同类）

| 陷阱 | 示例 |
|------|------|
| 类名错误 | `new Test3()` 但类是 `Test2` |
| 未实现接口 | 漏写 `implements` 的方法 |
| 变量遮蔽 | `int y = b` 遮住成员，`this.y` 才是成员 |
| 抽象类实例化 | `new AbstractClass()` 非法 |

### ② String / Math / Object

```java
String a = "Hello", b = "Hello", c = new String("Hello");
System.out.println(a == b);        // true（常量池）
System.out.println(a == c);        // false
System.out.println(a.equals(c));   // true
System.out.println("Java".substring(1, 3));  // av
System.out.println("1,2,3".split(",").length);  // 3
```

| 陷阱 | 说明 |
|------|------|
| 不可变 | `s.concat("x")` 不改变 `s` |
| `==` vs `equals` | 见简答官方样例 |
| `substring` | **[begin, end)** 左闭右开 |

### ③ Infinity / NaN / enum

```java
System.out.println(0.0/0.0 == 0.0/0.0);  // false（NaN）
System.out.println(1.0/0.0 > 0);        // true（Infinity）
System.out.println(Season.SPRING.ordinal());  // 0
```

### ④ 集合

```java
List<String> list = new ArrayList<>();
list.add("a"); list.add("b");
list.remove(0);
// size=1, 内容为 "b"
```

| 陷阱 | 说明 |
|------|------|
| `remove(int)` vs `remove(Object)` | `list.remove(1)` 删下标；`list.remove("1")` 删对象 |
| 引用 | 两个引用指向同一 `ArrayList`，`add` 都生效 |

### ⑤ 继承与多态

```java
class Animal { void speak() { System.out.print("A"); } }
class Dog extends Animal { void speak() { System.out.print("D"); } }
Animal a = new Dog();
a.speak();  // D（运行时绑定）
```

### ⑥ 多线程

```java
Thread t = new Thread(() -> System.out.print("T"));
t.run();    // 只输出 T，不启动新线程
t.start();  // 新线程执行
```

| 陷阱 | 说明 |
|------|------|
| `run()` vs `start()` | 直接 `run()` **不** 新起线程 |
| 输出顺序 | 多线程 **不确定**（除非 `join`） |

### ⑦ 异常

未捕获的运行时异常 → 程序终止，**后续语句不执行**。

---

## 读程题自测

1. 官方 **Test2**：先判能否编译，再手算三行输出。  
2. `new String("a") == new String("a")` → ?  
3. `0.0/0.0 == 0.0/0.0` → ?  
4. `"Java".substring(1, 3)` → ?  
5. `t.run()` 与 `t.start()` 输出有何不同？  
6. `ArrayList` 连续 `add` 两次后 `remove(0)`，`get(0)` 是什么？

> **参考答案**：2 false · 3 false · 4 `av` · 5 `run` 不启新线程 · 6 第二个元素

---

# 三、编程题（2 道）

> 纸笔写 **类 / 接口 / 方法**；`import` 可省略；需用库时考场给 **方法声明**。

## 官方样例题

![编程题样例：Person / Job / Life / Student](/java-exam/sample-programming.png)

**题目要求摘要**

| 类型 | 要求 |
|------|------|
| 抽象类 `Person` | 字段 `name`、`age`；构造；`toString` |
| 类 `Job` | 字段 `accountabilities`；构造；`toString` |
| 接口 `Life` | 方法 `living()` |
| 类 `Student` | **继承 Person、实现 Life**；字段 `school`、`id`、`Job job`；构造；`living()` 输出固定句；`toString` 含全部字段；`setJob(Job job)` |

**满分骨架（默写）**

```java
abstract class Person {
    protected String name;
    protected int age;
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public String toString() {
        return "name=" + name + ", age=" + age;
    }
}

class Job {
    private String accountabilities;
    public Job(String accountabilities) {
        this.accountabilities = accountabilities;
    }
    public String toString() {
        return "accountabilities=" + accountabilities;
    }
}

interface Life {
    void living();
}

class Student extends Person implements Life {
    private String school;
    private long id;
    private Job job;

    public Student(String name, int age, String school, long id) {
        super(name, age);
        this.school = school;
        this.id = id;
    }

    public void living() {
        System.out.println("好好学习、天天向上!");
    }

    public void setJob(Job job) {
        this.job = job;
    }

    public String toString() {
        return super.toString() + ", school=" + school
             + ", id=" + id + ", job=" + job;
    }
}
```

**得分点检查**

- [ ] `extends` + `implements` 写法正确  
- [ ] `super(name, age)` 调父构造  
- [ ] **组合** `Job job` + `setJob`  
- [ ] `living()` 输出 **一字不错**  
- [ ] `toString` 用 `super.toString()` 带父类字段  

---

## 答题规范

| 原则 | 说明 |
|------|------|
| 先写字段 | 类型 + 名字齐全 |
| 再写构造 | `super(...)` 若有父类 |
| 接口方法 | 实现类必须写 `public` 实现 |
| 不求花哨 | 语法正确、得分点齐全优先 |

---

## 题型分类与默写骨架

### 类型 1：OOP 建模（官方样例 ★★★）

抽象类 + 接口 + 继承 + 组合 → 见 [满分骨架](#满分骨架默写)

### 类型 2：重写 `equals` / `toString`

```java
public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Student)) return false;
    Student s = (Student) o;
    return id == s.id && name.equals(s.name);
}
public String toString() {
    return "Student{name=" + name + ", id=" + id + "}";
}
```

### 类型 3：文件读写方法（PPT 第三章 · 练习四）

```java
static void copyNoEmptyLines(String in, String out) throws IOException {
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

### 类型 4：集合方法（PPT 第三章 · 练习三）

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

### 类型 5：GUI 监听器补全（PPT GUI 章）

```java
button.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        area.append(input.getText().trim() + "\n");
    }
});

frame.addWindowListener(new WindowAdapter() {
    @Override
    public void windowClosing(WindowEvent e) {
        // 退出前保存
    }
});
```

### 类型 6：线程类（PPT 多线程章）

```java
class Worker extends Thread {
    private volatile boolean running = true;
    public void shutdown() { running = false; interrupt(); }
    public void run() {
        while (running) {
            try {
                Thread.sleep(1000);
                // 定时任务
            } catch (InterruptedException e) {
                if (!running) break;
            }
        }
    }
}
```

---

## 编程题自测

1. 默写 **Person / Job / Life / Student** 完整四类（官方样例）。  
2. 写方法：读 `input.txt` 去空行写入 `output.txt`。  
3. 写方法：`HashMap` 统计单词频次。  
4. 为 `JButton` 写 `ActionListener` **匿名内部类**。  
5. 写 `extends Thread` 的 `run()` + `sleep` + `volatile` 退出。

---

# 冲刺 Checklist

**简答（4～5）**

- [ ] 多线程全套（进程/线程、同步、死锁、start vs run）
- [ ] GUI 全套（AWT/Swing、层次、Listener/Adapter、匿名内部类）
- [ ] 官方样例 `==` vs `equals`
- [ ] Infinity/NaN、enum、List/Set/Map、字节流/字符流

**读程（5～7）**

- [ ] 官方 **Test2** 编译判断 + 三行输出
- [ ] String / 集合 / 线程 各练 2 道
- [ ] NaN、enum.ordinal()

**编程（2）**

- [ ] 官方 **Person/Student** 四类骨架闭卷默写
- [ ] `BufferedReader` 按行读方法
- [ ] `ActionListener` 或 `WindowAdapter` 匿名内部类

---

# 附录：实验代码 ↔ 考点

> 实验用于 **理解考点、练手写**，不是另一种考试形式。

| 实验 | 路径 | 对应题型 |
|------|------|----------|
| 练习一 | `CalendarApp` | 读程：String/Scanner；简答：基础语法 |
| 练习二 | 农场数组版 | 编程：OOP、继承；读程：数组 |
| 练习三 | 农场 ArrayList | 简答/读程/编程：**容器** |
| 练习四 | `FarmStorage` | 简答/编程：**流 I/O** + `split` |
| 大作业 | `FarmGUI`、`AutoSaveThread` | 简答：**GUI + 多线程**；编程：监听器、线程类 |

**建议手写一遍**：`FarmStorage.java`（I/O）、`FarmGUI` 事件注册部分、`AutoSaveThread`（线程退出）、PPT 要求自己写的小例子。

---

*最后更新：2026-05-22 · 笔考专版 · 课件摘自 `JAVA\课件\` 共 8 个 PPT（无 GUI 课件）· 已移除机考*
