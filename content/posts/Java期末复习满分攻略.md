---
title: Java 程序设计 · 期末满分攻略
date: 2026-05-22
tags: 学习/大三下学期期末考试复习/Java
column: 学习笔记
toc: true
---

# Java 程序设计 · 期末满分攻略（笔考 + 机考）

> **依据**：期末复习要求（多线程、GUI、**流**、**容器**、**String/Math/Object**、**查 API**）+ 课程上机实验（练习一至四、开心农场大作业）  
> **笔考（官方）**：仅 **3 种题型** — **问答**、**读程**、**编程**（闭卷纸笔）  
> **机考**：IDE 或 OJ 编写可运行 Java 程序，重点考 **I/O + 集合 + String 处理**，常附带 **GUI 事件** 或 **多线程**

---

## 目录

- [考点权重总览](#考点权重总览)
- [一、笔考满分攻略](#一笔考满分攻略)
  - [笔考题型总览（仅 3 种）](#笔考题型总览仅-3-种)
  - [题型1：问答](#题型1问答)
  - [题型2：读程](#题型2读程)
  - [题型3：编程](#题型3编程)
  - [模块1：String / Math / Object（★★★）](#模块1string--math--object)
  - [模块2：容器类 Collection Framework（★★★）](#模块2容器类-collection-framework)
  - [模块3：Java 流 I/O（★★★）](#模块3java-流-io)
  - [模块4：多线程（★★）](#模块4多线程)
  - [模块5：GUI 与事件（★★）](#模块5gui-与事件)
  - [模块6：查阅 API 解题（★★★）](#模块6查阅-api-解题)
  - [笔考冲刺 Checklist](#笔考冲刺-checklist)
- [二、机考满分攻略](#二机考满分攻略)
  - [机考总策略](#机考总策略)
  - [题型速查表](#题型速查表)
  - [模板1：文件读写 + String 解析](#模板1文件读写--string-解析)
  - [模板2：ArrayList / HashMap 统计](#模板2arraylist--hashmap-统计)
  - [模板3：Swing 按钮事件 + 匿名类](#模板3swing-按钮事件--匿名类)
  - [模板4：后台线程定时任务](#模板4后台线程定时任务)
  - [机考万能骨架](#机考万能骨架考前-10-分钟过一遍)
  - [机考时间分配](#机考时间分配)
- [附录：课程实验 ↔ 考点对照](#附录课程实验--考点对照)

---

## 考点权重总览

| 优先级 | 模块 | 笔考（问答/读程/编程） | 机考常见 |
|:------:|------|------------------------|----------|
| ★★★ | **String / Math / Object** | 读程输出；问答 equals/不可变；编程字符串处理 | 文本清洗、分割、大小写、substring |
| ★★★ | **容器类** | 问答 List/Set/Map；读程集合修改；编程 ArrayList/HashMap | ArrayList 增删查、HashMap 计数 |
| ★★★ | **流 I/O** | 问答类层次；编程写读文件片段 | 读文件→处理→写文件 |
| ★★★ | **查 API** | 问答「用什么类/方法」 | 现场搜 JDK 文档完成需求 |
| ★★ | **多线程** | 问答 start/run；读程线程输出 | 继承 Thread 或 Runnable 后台任务 |
| ★★ | **GUI** | 问答事件模型、匿名类；编程补监听器 | Swing 按钮 + ActionListener |

**记忆口诀**：**「串容流，查 API；线面 GUI 加分项」**

---

# 一、笔考满分攻略

> **闭卷纸笔**，官方确认 **只有 3 种题型**，无选择、无单独填空卷面。复习按「问答背概念 → 读程练输出 → 编程默写骨架」三步走。

## 笔考题型总览（仅 3 种）

| 题型 | 考什么 | 拿分关键 | 对应模块 |
|------|--------|----------|----------|
| **① 问答** | 概念、对比、流程、术语、API 选用 | 分点作答，先定义再举例 | 容器区别、I/O 类图、线程/GUI 概念、查 API |
| **② 读程** | 给一段 Java 代码，写 **运行结果** 或判断对错 | 逐行跟踪；盯 String/引用、集合修改、线程 | String/Math/Object、容器、多线程 |
| **③ 编程** | 纸笔写代码（方法/类片段，未必完整 main） | 语法正确、API 用对、边界考虑 | 流读写、集合操作、String 处理、监听器骨架 |

**记忆口诀**：**「问读编，三板斧」** — 问答背、读程算、编程写。

---

## 题型1：问答

### 答题模板

1. **一句话定义**（是什么）  
2. **2～4 个要点**（特点 / 区别 / 步骤）  
3. **一句例子或对比**（加分项）

### 高频问答清单

| 主题 | 典型问法 | 要点 |
|------|----------|------|
| String | `==` 与 `equals`？String 与 StringBuilder？ | 引用 vs 内容；不可变 vs 可变 |
| 容器 | List / Set / Map 区别？ArrayList vs LinkedList？ | 有序可重复 / 不重复 / 键值对；随机访问 vs 链表 |
| 流 | 字节流与字符流？按行读文本用什么？ | InputStream/OutputStream vs Reader/Writer；BufferedReader |
| 线程 | `start()` 与 `run()`？为何 GUI 耗时操作要新线程？ | 新线程 vs 普通调用；不阻塞 EDT |
| GUI | 事件驱动三要素？匿名内部类作用？ | 事件源、事件、监听器；简化监听器实现 |
| API | 读 txt 每行、统计词频、随机整数用什么？ | BufferedReader、HashMap、Math.random / Random |

> 下文各 **模块** 中的「易错辨析」「问答答题模板」优先用于 **问答** 题。

---

## 题型2：读程

### 解题步骤

1. **圈变量类型**：String 还是引用？集合装的是什么？  
2. **盯修改点**：`+` 拼接、`add/remove`、`start()` 是否调用  
3. **手算输出**：不要跳步；`substring` 注意左闭右开  
4. **检查陷阱**：`==` 与 `equals`、常量池、`split` 正则

### 读程高发陷阱

| 陷阱 | 示例 |
|------|------|
| String 不可变 | `s.concat("x")` 不改变 s |
| 常量池 | 字面量 `==` 可能为 true |
| 集合引用 | `list.add` 改的是同一对象 |
| 线程 | 直接 `run()` 不启动新线程 |
| 异常 | 未捕获时程序终止，后面不执行 |

> 下文 **「经典读程例题」** 专供 **读程** 训练。

---

## 题型3：编程

### 纸笔编程要求

- 常考 **一个方法** 或 **一小段类**（如读文件、遍历 ArrayList、补 `ActionListener`）  
- **import 可简写** 或只写核心类名（以课堂要求为准）  
- 必须体现：**try-with-resources**、合理 **异常处理**、正确 **API 名**

### 默写优先级（编程题）

| 优先级 | 默写内容 |
|--------|----------|
| P0 | `BufferedReader` 按行读 + `BufferedWriter` 写行 |
| P0 | `ArrayList` 增删查遍历；`HashMap` put/get/getOrDefault |
| P0 | `trim` / `split` / `substring` / `parseInt` 组合 |
| P1 | `ActionListener` 匿名类或 Lambda 骨架 |
| P1 | `extends Thread` 的 `run()` + `sleep` |
| P2 | `equals` 重写、`toString` 重写 |

> 下文 **机考模板** 与 **编程** 题同源，纸笔版去掉 `main` 或缩成单方法即可。

---


## 模块1：String / Math / Object

### 必背考点

#### String 常用方法（按考试频率）

| 方法 | 作用 | 易错点 |
|------|------|--------|
| `length()` | 字符个数 | 不是 `length`（数组才用） |
| `charAt(i)` | 取字符 | 下标从 0，越界抛异常 |
| `substring(begin, end)` | 截取 **[begin, end)** | 左闭右开 |
| `trim()` | 去首尾空白 | 中间空白不去 |
| `toUpperCase()` / `toLowerCase()` | 大小写 | 返回**新** String，原串不变 |
| `equals(s)` / `equalsIgnoreCase(s)` | 内容比较 | **比较内容用 equals，不用 ==** |
| `split(regex)` | 正则分割 | `"a.b".split("\\.")` → `["a","b"]` |
| `replace(old, new)` | 替换 | 也是新对象 |
| `indexOf` / `lastIndexOf` | 查找 | 找不到返回 -1 |
| `startsWith` / `endsWith` | 前缀后缀 | |
| `isEmpty()` / `isBlank()`(Java 11+) | 空串判断 | `"".isEmpty()` 为 true |

#### String 不可变 + 拼接

```java
String s = "ab";
s.concat("c");      // 返回 "abc"，但 s 仍是 "ab"
s = s + "c";        // s 变成 "abc"（产生新对象）
StringBuilder sb = new StringBuilder("ab");
sb.append("c");     // sb 变为 "abc"（可变，循环拼接首选）
```

#### Math 常用

| 方法 | 说明 |
|------|------|
| `Math.random()` | [0.0, 1.0)  double |
| `Math.abs(x)` | 绝对值 |
| `Math.max(a,b)` / `Math.min(a,b)` | |
| `Math.pow(a,b)` | a 的 b 次方 |
| `Math.sqrt(x)` | 平方根 |
| `(int)(Math.random() * n)` | **[0, n-1]** 随机整数 |
| `(int)(Math.random() * (max-min+1) + min)` | **[min, max]** 闭区间 |

#### Object 必会

| 方法 | 默认行为 | 重写要点 |
|------|----------|----------|
| `toString()` | 类名@哈希 | 返回可读信息 |
| `equals(Object o)` | **引用相等** == | 先 `instanceof`，再比字段 |
| `hashCode()` | 与地址相关 | **equals 相等则 hashCode 必相等** |
| `getClass()` | 运行时类型 | 很少改 |

### 经典读程例题

```java
String a = "Hello";
String b = "Hello";
String c = new String("Hello");
System.out.println(a == b);       // true（字符串常量池）
System.out.println(a == c);       // false（new 在堆上）
System.out.println(a.equals(c));  // true
System.out.println("Hi ".trim().length()); // 2
System.out.println("A,B,C".split(",")[1]); // B
System.out.println("Java".substring(1, 3)); // av
```

### 问答答题模板

> **问：String 与 StringBuilder 区别？**  
> String **不可变**，频繁 `+` 产生大量临时对象；StringBuilder **可变**，适合循环拼接。  
> **问：== 与 equals？**  
> `==` 比较引用（地址）；`equals` 比较内容（Object 默认同 ==，String 等类已重写）。

---

## 模块2：容器类 Collection Framework

### 体系结构（必画）

```
Collection
├── List（有序、可重复）
│   ├── ArrayList   — 数组实现，随机访问 O(1)，中间插入慢
│   └── LinkedList  — 双向链表，头尾操作快
├── Set（不重复）
│   ├── HashSet     — 无序，哈希表，O(1) 增删查
│   └── TreeSet     — 有序（红黑树），需 Comparable/Comparator
└── Queue / Deque

Map（键值对，不属于 Collection）
├── HashMap   — 无序，允许 null 键值（JDK8+）
├── TreeMap   — 按键排序
└── LinkedHashMap — 插入顺序
```

### 高频 API

**List（ArrayList）**

```java
List<String> list = new ArrayList<>();
list.add("a");
list.add(0, "b");           // 指定位置插入
list.get(i); list.set(i, x);
list.remove(i); list.remove(Object o);
list.size(); list.isEmpty();
list.contains(o); list.indexOf(o);
for (String s : list) { ... }
for (int i = 0; i < list.size(); i++) { list.get(i); }
```

**Map（HashMap）**

```java
Map<String, Integer> map = new HashMap<>();
map.put("key", 1);
map.get("key");             // 无则 null
map.getOrDefault("key", 0);
map.containsKey(k); map.containsValue(v);
map.remove(k);
for (String k : map.keySet()) { map.get(k); }
for (Map.Entry<String,Integer> e : map.entrySet()) {
    e.getKey(); e.getValue();
}
```

### 易错辨析（问答常客）

| 对比 | 要点 |
|------|------|
| **ArrayList vs LinkedList** | 随机访问选 ArrayList；频繁头尾插删选 LinkedList |
| **HashSet vs TreeSet** | 要去重+无序 HashSet；要排序 TreeSet |
| **HashMap vs Hashtable** | HashMap 非线程安全、效率高；Hashtable 线程安全（老类） |
| **List vs Set** | List 可重复有序；Set 元素唯一 |
| **迭代时删除** | 用 **Iterator.remove()**，不要 for-each 里直接 list.remove(i)（ConcurrentModificationException） |

### 课程实验对照

练习三 `Farm` 使用 **二维 ArrayList**：

```java
ArrayList<ArrayList<FarmObject>> rows = new ArrayList<>();
rows.add(new ArrayList<>());           // 新增一行
rows.get(i).add(j, object);            // 第 i 行第 j 列插入
rows.get(i).get(j);                    // 访问
rows.get(i).remove(j);                 // 删除
```

---

## 模块3：Java 流 I/O

### 类层次（问答必背）

```
字节流                          字符流（处理文本）
InputStream                     Reader
  ├── FileInputStream             ├── FileReader
  ├── BufferedInputStream         ├── BufferedReader  ★ 按行读
  └── ObjectInputStream           └── InputStreamReader（字节→字符桥梁）
OutputStream                    Writer
  ├── FileOutputStream            ├── FileWriter
  ├── BufferedOutputStream        ├── BufferedWriter  ★ 按行写
  └── ObjectOutputStream          └── OutputStreamReader
```

**选用原则**

| 场景 | 推荐 |
|------|------|
| 文本文件读（按行） | `BufferedReader` + `FileReader` |
| 文本文件写 | `BufferedWriter` + `FileWriter` |
| 二进制（图片等） | `FileInputStream` / `FileOutputStream` |
| 已知编码 UTF-8 | `Files.readAllLines(path, StandardCharsets.UTF_8)`（Java 7+） |

### try-with-resources（编程 / 机考必考）

```java
// 自动关闭 Closeable，比 finally 手动 close 更安全
try (BufferedReader br = new BufferedReader(new FileReader("in.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        // 处理 line
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

### 练习四标准写文件模式

```java
try (BufferedWriter w = new BufferedWriter(new FileWriter("farm.txt"))) {
    w.write("ROWS=" + rowCount);
    w.newLine();
    for (...) {
        w.write(String.format("%d,%d,%s", i, j, name));
        w.newLine();
    }
}
```

### 练习四标准读文件 + String 解析

```java
try (BufferedReader r = new BufferedReader(new FileReader("farm.txt"))) {
    String line = r.readLine();
    int rows = Integer.parseInt(line.substring(line.indexOf('=') + 1));
    while ((line = r.readLine()) != null) {
        if (line.trim().isEmpty()) continue;
        String[] parts = line.split(",", 6);  // 限制段数，防止逗号在字段内
        int row = Integer.parseInt(parts[0].trim());
        String name = parts[4].trim();
    }
}
```

### 易错点

- `readLine()` 返回 **null** 表示 EOF，不是 `""`
- `FileWriter` 默认**覆盖**；追加用 `new FileWriter(file, true)`
- 字符流 vs 字节流：**.txt 用字符流**，别用 DataInputStream 读文本
- `split(".")` 错误：`.` 是正则「任意字符」，应 `split("\\.")`

---

## 模块4：多线程

### 创建线程两种方式

```java
// 方式1：继承 Thread
class MyThread extends Thread {
    public void run() { /* 任务 */ }
}
new MyThread().start();   // 必须 start()，不能直接 run()

// 方式2：实现 Runnable（推荐，解耦）
new Thread(() -> { /* 任务 */ }).start();
new Thread(new Runnable() {
    public void run() { /* 任务 */ }
}).start();
```

### 生命周期 & 常用方法

| 方法/概念 | 说明 |
|-----------|------|
| `start()` | 启动新线程，JVM 调用 `run()` |
| `run()` | 线程体；直接调用 run() **不会**新线程 |
| `sleep(ms)` | 静态，当前线程休眠，**不释放锁** |
| `join()` | 等待该线程结束 |
| `interrupt()` / `isInterrupted()` | 中断协作式退出 |
| `setDaemon(true)` | 守护线程，JVM 退出时自动结束 |
| `synchronized` | 同步块/方法，互斥锁 |

### 课程大作业 `AutoSaveThread` 考点

```java
public class AutoSaveThread extends Thread {
    private volatile boolean running = true;

    public void shutdown() {
        running = false;
        interrupt();                    // 配合 sleep 退出
    }

    public void run() {
        while (running) {
            try {
                Thread.sleep(intervalMs);
                FarmStorage.save(farm); // I/O + 线程结合
            } catch (InterruptedException ex) {
                if (!running) break;
            } catch (IOException ex) { /* 通知 GUI */ }
        }
    }
}
```

**问答常考**：为什么 GUI 里耗时操作（读大文件）要放 **SwingWorker** 或 **新线程**？  
→ **避免阻塞 EDT（事件分发线程）**，否则界面卡死。

---

## 模块5：GUI 与事件

> GUI 框架不限 AWT/Swing/SWT；校内机考以 **Swing** 居多。核心是 **事件驱动 + 监听器 + 匿名类/内部类**。

### Swing 基本结构

```java
JFrame frame = new JFrame("标题");
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setLayout(new BorderLayout());
frame.add(panel, BorderLayout.CENTER);
frame.setSize(800, 600);
frame.setLocationRelativeTo(null);
frame.setVisible(true);
```

### 事件处理三种写法（必会）

```java
// ① 匿名内部类（笔考编程 / 机考最常见）
button.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        label.setText("clicked");
    }
});

// ② Lambda（Java 8+，机考推荐）
button.addActionListener(e -> label.setText("clicked"));

// ③ 适配器类（只重写需要的方法）
frame.addWindowListener(new WindowAdapter() {
    @Override
    public void windowClosing(WindowEvent e) {
        // 退出前保存
    }
});
resultArea.addMouseListener(new MouseAdapter() {
    @Override
    public void mouseEntered(MouseEvent e) { /* ... */ }
});
```

### 事件模型术语

| 术语 | 含义 |
|------|------|
| **事件源** | 按钮、文本框等组件 |
| **事件对象** | ActionEvent、MouseEvent… |
| **监听器** | ActionListener、MouseListener… |
| **注册** | `addXxxListener(...)` |
| **EDT** | Event Dispatch Thread，Swing 单线程画界面 |

### 读代码考点

- **匿名内部类**可以访问外部方法的 **final 或 effectively final** 局部变量
- **成员内部类**持有外部类引用：`FarmGUI.this`
- `SwingUtilities.invokeLater(() -> { ... })`：在 EDT 上更新 UI

---

## 模块6：查阅 API 解题

### 考场策略

1. **JDK 官方文档**：https://docs.oracle.com/en/java/javase/ — 搜类名 → Methods
2. **IDE 快捷键**：Ctrl+点击类名、Ctrl+Space 补全、Ctrl+Q 参数提示
3. **import 不会写**：先写类名看 IDE 自动 import，或查文档 **Package**

### 按需求查什么类（速查）

| 需求 | 查哪个 API |
|------|------------|
| 读文本文件每一行 | `BufferedReader.readLine()` |
| 写一行并换行 | `BufferedWriter.newLine()` |
| 分割 CSV | `String.split(",")` |
| 去空格 | `String.trim()` |
| 字符串转数字 | `Integer.parseInt(s)` / `Double.parseDouble(s)` |
| 动态数组 | `ArrayList` |
| 计数统计 | `HashMap<String,Integer>` + `merge` 或 `getOrDefault+1` |
| 排序列表 | `Collections.sort(list)` / `list.sort(Comparator)` |
| 当前时间格式化 | `SimpleDateFormat` 或 `DateTimeFormatter` |
| 随机整数 | `Math.random()` 或 `Random.nextInt(n)` |
| 弹窗提示 | `JOptionPane.showMessageDialog` |
| 选文件 | `JFileChooser` |

### 课程 `StringUtil` 体现的 API 组合题

```java
raw.trim().replaceAll("\\s+", " ");     // 去空白 + 合并空格
line.split(delimiter);                  // 分割
text.substring(0, maxLen);              // 截取
text.equalsIgnoreCase(other);           // 忽略大小写比较
text.toUpperCase();                     // 日志关键字
```

---

## 笔考冲刺 Checklist

**问答**

- [ ] List / Set / Map 各一句区别；ArrayList vs LinkedList
- [ ] 字节流 vs 字符流；按行读文本用什么类
- [ ] `start()` vs `run()`；GUI 为何不能阻塞 EDT
- [ ] Object 三方法：toString / equals / hashCode

**读程**

- [ ] 手算 3 道 String `==` / `equals` / `substring` / `split` 题
- [ ] 手算 1 道 ArrayList `add/remove` 后 size 与内容
- [ ] 分清 `concat` 不改变原串、`run()` 不启新线程

**编程**

- [ ] 默写 BufferedReader 按行读取（try-with-resources）
- [ ] 默写 ArrayList / HashMap 各 5 个常用方法
- [ ] 默写 ActionListener 匿名内部类或 Lambda 骨架
- [ ] 能写：读文件 → split → HashMap 计数 → 写回一行结果

---

# 二、机考满分攻略

> 机考 = **能编译运行** + **满足题目 I/O 格式** + **正确处理异常**。先拿模板跑通，再填业务逻辑。

## 机考总策略

1. **5 分钟读题**：输入输出文件？控制台？要不要 GUI？
2. **10 分钟搭骨架**：main + try-with-resources + 集合声明
3. **核心 30 分钟**：读入 → String/集合处理 → 写出
4. **10 分钟**：用小样例自测 + 边界（空文件、空行、非法数字）
5. **编译命令**：`javac *.java` → `java MainClass`（类名与文件名一致）

**抢分原则**

- 不会优雅实现，先 **暴力 AC**：`ArrayList` + `for` 循环永远可用
- 任何 I/O 都包 **try-catch IOException**，main 里 `printStackTrace` 或友好提示
- String 从文件读出来先 **`trim()`**
- 数字转换包 **NumberFormatException**

---

## 题型速查表

| 机考题型 | 核心技术 | 模板 |
|----------|----------|------|
| 读 txt/csv 统计 | BufferedReader + split + HashMap | [模板1](#模板1文件读写--string-解析) + [模板2](#模板2arraylist--hashmap-统计) |
| 写结果到文件 | BufferedWriter + String.format | 模板1 |
| 学生/农场对象管理 | ArrayList + 增删查改 | 练习三 Farm |
| 简单图形界面 | JFrame + JButton + Lambda | [模板3](#模板3swing-按钮事件--匿名类) |
| 定时保存/后台任务 | extends Thread + sleep | [模板4](#模板4后台线程定时任务) |
| 字符串批处理 | trim/split/replace/substring | StringUtil 思路 |

---

## 模板1：文件读写 + String 解析

```java
import java.io.*;
import java.util.*;

public class FileProcess {
    public static void main(String[] args) {
        List<String> lines = readLines("input.txt");
        List<String> result = new ArrayList<>();
        for (String line : lines) {
            line = line.trim();
            if (line.isEmpty()) continue;
            String[] p = line.split(",");
            // TODO: 业务逻辑
            result.add(/* 处理后的行 */);
        }
        writeLines("output.txt", result);
    }

    static List<String> readLines(String path) {
        List<String> list = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = br.readLine()) != null) {
                list.add(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return list;
    }

    static void writeLines(String path, List<String> lines) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path))) {
            for (String line : lines) {
                bw.write(line);
                bw.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**满分细节**

- 输出格式与样例 **逐字符一致**（空格、逗号、换行）
- `split(",", -1)` 保留尾部空字段（题目需要时）
- 键值行 `key=value` 用 `indexOf('=')` + `substring`

---

## 模板2：ArrayList / HashMap 统计

```java
// 词频 / 出现次数
Map<String, Integer> freq = new HashMap<>();
for (String word : words) {
    word = word.trim().toLowerCase();
    freq.put(word, freq.getOrDefault(word, 0) + 1);
}

// 按次数降序输出（查 API：Map.Entry + List.sort）
List<Map.Entry<String, Integer>> entries = new ArrayList<>(freq.entrySet());
entries.sort((a, b) -> b.getValue() - a.getValue());

// 去重保序
Set<String> seen = new HashSet<>();
List<String> unique = new ArrayList<>();
for (String s : list) {
    if (seen.add(s)) unique.add(s);
}
```

---

## 模板3：Swing 按钮事件 + 匿名类

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimpleGUI extends JFrame {
    private final JTextArea area = new JTextArea(10, 30);
    private final JTextField input = new JTextField(15);

    public SimpleGUI() {
        super("机考 GUI 模板");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout(8, 8));

        JButton btn = new JButton("提交");
        // Lambda 事件
        btn.addActionListener(e -> onSubmit());

        // 匿名内部类：窗口关闭
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                dispose();
            }
        });

        JPanel top = new JPanel();
        top.add(input);
        top.add(btn);
        add(top, BorderLayout.NORTH);
        add(new JScrollPane(area), BorderLayout.CENTER);
        pack();
        setLocationRelativeTo(null);
    }

    private void onSubmit() {
        String text = input.getText().trim();
        if (text.isEmpty()) {
            JOptionPane.showMessageDialog(this, "不能为空");
            return;
        }
        area.append(text.toUpperCase() + "\n");  // String API 演示
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new SimpleGUI().setVisible(true));
    }
}
```

---

## 模板4：后台线程定时任务

```java
public class Worker extends Thread {
    private volatile boolean running = true;

    public void stopWorker() {
        running = false;
        interrupt();
    }

    @Override
    public void run() {
        while (running) {
            try {
                Thread.sleep(3000);       // 每 3 秒
                doTask();                 // 保存/刷新
            } catch (InterruptedException e) {
                if (!running) break;
            }
        }
    }

    private void doTask() {
        // FarmStorage.save(...) 或更新 UI
    }
}

// GUI 中启动与停止
Worker w = new Worker();
w.setDaemon(true);
w.start();
// 窗口关闭：w.stopWorker();
```

**线程 + GUI 更新**：后台线程 **不要直接改 Swing 组件**，用 `SwingUtilities.invokeLater(() -> label.setText(...))`。

---

## 机考万能骨架

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        try {
            solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void solve() throws IOException {
        // 1. 读
        // 2. String / 集合 处理
        // 3. 写 / 输出
    }
}
```

**考前 10 分钟过一遍**

- `BufferedReader` / `BufferedWriter` 头尾
- `ArrayList` add/get/remove/size
- `HashMap` put/get/getOrDefault
- `String` trim/split/substring/equalsIgnoreCase
- `Integer.parseInt` 包 try-catch
- Swing：`JFrame` + `JButton` + `addActionListener(e -> {})`

---

## 机考时间分配

| 阶段 | 时间 | 动作 |
|------|------|------|
| 读题 + 样例 | 5 min | 圈出输入输出文件名、格式 |
| 搭 main + I/O | 10 min | 模板复制，能读能写 |
| 核心逻辑 | 25～35 min | 集合 + String |
| GUI/线程（若有） | 10～15 min | 套模板3/4 |
| 自测 | 10 min | 空文件、一行、非法输入 |

---

# 附录：课程实验 ↔ 考点对照

| 实验 | 路径 | 对应期末考点 |
|------|------|--------------|
| 练习一 | `CalendarApp` | Scanner、Calendar、String 格式化 |
| 练习二 | 农场数组版 | 面向对象、数组 |
| 练习三 | 农场 ArrayList | **容器 ArrayList**、二维结构 |
| 练习四 | `FarmStorage` | **流 I/O**、**String.split**、try-with-resources |
| 大作业 | `FarmGUI` + `AutoSaveThread` | **Swing 事件**、**匿名类**、**多线程**、StringUtil |

**复习建议**：把 **练习四 `FarmStorage.java`** 和 **大作业 `FarmGUI.java` 事件注册部分** 各手写一遍，期末机考极可能考「同类变形题」（读配置 → 内存集合 → 写回文件 / 简单界面操作）。

---

## 附：笔考模拟自测（按三题型）

### 问答

1. `ArrayList` 和 `LinkedList` 在 **get(i)** 上谁更快？为什么？  
2. 读文本文件按行，应选 `FileInputStream` 还是 `BufferedReader`？  
3. `t.start()` 和 `t.run()` 区别？  
4. `ActionListener` 在事件模型中是什么角色？  
5. `HashMap` 的 key 重复 `put` 会怎样？

### 读程

1. `new String("a") == new String("a")` 结果？  
2. `"1,2,3".split(",").length` 等于几？  
3. `"Java".substring(1, 3)` 输出什么？

### 编程

1. 写一个方法：从 `input.txt` 按行读取，去掉空行，写入 `output.txt`。  
2. 写一个方法：统计 `String[] words` 中各单词出现次数，返回 `HashMap<String,Integer>`。  
3. 为 `JButton btn` 添加点击后在 `JTextArea area` 追加一行文本的监听器（匿名内部类）。

> **参考答案（问答）**：1 ArrayList，数组随机访问 O(1)  2 BufferedReader  3 start 新线程，run 普通方法  4 监听器  5 覆盖旧 value  
> **读程**：1 false  2 3  3 `av`  
> **编程**：见上文 [模板1](#模板1文件读写--string-解析)、[模板2](#模板2arraylist--hashmap-统计)、[模板3](#模板3swing-按钮事件--匿名类)

---

*最后更新：2026-05-22（笔考题型：问答 / 读程 / 编程）· 标签：`学习/大三下学期期末考试复习/Java`*
