# -*- coding: utf-8 -*-
"""Insert comprehensive programming exam handbook into Java guide."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "content/posts/Java期末复习满分攻略.md"

START = "### 第三步：题目里其他常见要求（第二道编程题）"
END = "---\n\n## 官方样例题"

HANDBOOK = r'''### 第三步：编程题全能考点手册（按课件 · 按题目用语）

> **老师出题规律**：编程 **2 道**，要求 **逐条列出**（第 1 点、第 2 点…）。  
> **你要做的**：在题目里 **圈关键词** → 在下表 / 对应小节找到写法 → **一条要求 = 一段代码**。  
> 下面按 **PPT 章节 + 实验作业** 汇总 **所有可能考到** 的编程要求（不只官方 Person 样例）。

#### 总索引：题目里出现这些词 → 怎么写

| 题目用语 | 写什么 | 见小节 |
|----------|--------|--------|
| 定义类 X / 编写类 X | `class X { 字段; 构造; 方法 }` | [A1](#a1-普通类--字段--构造--输出) |
| **抽象类** X | `abstract class X` | [A2](#a2-官方综合题--抽象类--接口--继承--组合) |
| **接口** X | `interface X { void m(); }` 无方法体 | [A2](#a2-官方综合题--抽象类--接口--继承--组合) |
| **继承** X、**extends** | `class Y extends X` | [A3](#a3-继承--重写--super) |
| **实现** 接口 X、**implements** | `implements X` 或 `implements X, Y` | [A2](#a2)、[A10](#a10-实现多个接口) |
| 成员变量 / 字段 | `private/protected 类型 名;` | [A1](#a1-普通类--字段--构造--输出) |
| **构造方法** / 非缺省构造 | `public 类名(参数) { ... }` | [A1](#a1) |
| **默认构造** / 无参构造 | `public 类名() { 字段=默认值; }` | [A4](#a4-几何类--rectangle--point-型) |
| **构造重载** | 多个构造，用 `this(...)` 串联 | [A5](#a5-构造重载--this-链) |
| 子类构造 + 父类有参构造 | 第一行 **`super(...)`** | [A2](#a2)、[A6](#a6-多层继承--super-链) |
| **重写** / override 方法 | 同名同参 + `@Override` + 方法体 | [A3](#a3) |
| **重载** 方法 | 同名 **不同参数列表** | [A7](#a7-方法重载) |
| `toString()` | `public String toString() { return ... }` | [A1](#a1)、[A8](#a8-重写-equals--hashcode--tostring) |
| `equals()` | 参数 `Object o`，`instanceof` + 强转 | [A8](#a8) |
| `hashCode()` | 与 equals 一致，常 `return Objects.hash(...)` 或 `Long.hashCode(id)` | [A8](#a8) |
| **输出** / `print()` 方法 | `System.out.println(...)` 或题目指定格式 | [A1](#a1) |
| **引用** 某类对象 / 组合 | `private SomeClass ref;` + setter | [A2](#a2) |
| **getter/setter** | `getX()` / `setX(类型 x)` | [A9](#a9-getter--setter) |
| **static** 变量/方法 | `static int count;` / `static void f()` | [B1](#b1-static) |
| **final** 类 | `final class X` 不可继承 | [B2](#b2-final) |
| **final** 方法/字段 | 方法不可重写 / 字段只能赋一次 | [B2](#b2) |
| **abstract** 方法 | 父类声明，子类 **public** 实现 | [B3](#b3-抽象方法) |
| **enum** 枚举 | `enum Season { SPRING, SUMMER; }` | [B4](#b4-enum) |
| **ArrayList** | `List<T> list = new ArrayList<>();` add/get/remove/set | [B5](#b5-arraylist) |
| **HashMap** | put/get/remove/containsKey | [B6](#b6-hashmap) |
| **HashSet** | add，不重复 | [B7](#b7-hashset) |
| 统计频次 / 计数 | `map.getOrDefault(k,0)+1` | [B6](#b6) |
| **try-catch-finally** | 异常处理块 | [C1](#c1-try-catch-finally) |
| **throws** IOException | 方法头声明 | [C2](#c2-throws-与自定义异常) |
| 自定义异常类 | `class MyEx extends Exception` | [C2](#c2) |
| 读文件 / 按行读 | `BufferedReader` + `readLine()` | [D1](#d1-字符流按行读写) |
| 写文件 | `BufferedWriter` + `write` + `newLine()` | [D1](#d1) |
| 去空行 / 复制文件 | readLine + `trim().isEmpty()` + write | [D2](#d2-去空行复制--farmstorage-型) |
| **split** 分割 | `line.split(",")` | [D3](#d3-split-解析) |
| **extends Thread** | `class T extends Thread { public void run() }` | [E1](#e1-线程类) |
| **implements Runnable** | `class T implements Runnable { public void run() }` | [E2](#e2-runnable) |
| **synchronized** | 方法或块 | [E3](#e3-synchronized) |
| **ActionListener** | 匿名内部类 | [F1](#f1-actionlistener) |
| **WindowAdapter** | 重写 `windowClosing` | [F2](#f2-windowadapter) |
| **main** 方法 | 仅题目明确要求时写 | [G1](#g1-main-与变长参数) |

---

#### A 组 · 第四章「面向对象特性」（编程 ★★★ · 最高频）

##### A1 普通类 · 字段 · 构造 · 输出

**对应**：PPT `EmpInfo` 习题、实验农场类、任何「定义 XX 类，包含…」

**题目示例**：定义 `EmpInfo`，字段 `name, designation, department`（String），非缺省构造，`print()` 输出成员。

**知识点**：类体顺序 = **字段 → 构造 → 方法**；构造方法名 **= 类名**；`this.字段 = 参数`。

```java
class EmpInfo {
    private String name;
    private String designation;
    private String department;

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

**基本分**：3 字段 + 构造里 3 赋值 + print 里 3 字段都出现。

---

##### A2 官方综合题 · 抽象类 + 接口 + 继承 + 组合

**对应**：期末 **官方 20 分样例** Person / Job / Life / Student。

**逐条翻译**（完整讲解见上文 [要求 1～4](#第二步逐条知识点官方样例怎么写)）：

| 条 | 写法要点 |
|----|----------|
| 抽象类 Person | `abstract class` + protected 字段 + 构造 + toString |
| 类 Job | 普通 `class`，独立 |
| 接口 Life | `void living();` 无 `{}` |
| Student | `extends Person implements Life` + super + living + setJob + toString(super) |

**基本分**：四个类型都写对 + Student 里 **super + setJob + living 原句**。

---

##### A3 继承 · 重写 · super

**对应**：PPT `Shape` / `Rectangle`、农场 `Animal`/`Cow` 继承链。

**题目示例**：`Rectangle extends Shape`，重写 `draw()`，新方法里先调自己的 `draw()` 再 `super.draw()`。

**知识点**：
- **继承**：子类拥有父类非 private 成员。
- **重写**：方法名、参数、返回类型 **相同**；子类用 `@Override`。
- **super.方法()**：调用 **父类版本**。

```java
class Shape {
    public void draw() { System.out.println("Draw shape"); }
}
class Rectangle extends Shape {
    @Override
    public void draw() { System.out.println("Draw Rectangle"); }
    public void newDraw() {
        draw();        // 子类 draw
        super.draw();  // 父类 draw
    }
}
```

**基本分**：`extends` + `@Override` + 方法体 + 题目若要求 `super` 则写上。

---

##### A4 几何类 · Rectangle / Point 型

**对应**：PPT 习题「定义 Rectangle、Point」。

**题目示例**：Rectangle 有 width、height；无参构造置 0；两参构造；`getArea()`、`getPerimeter()`。

```java
class Rectangle {
    private double width, height;

    public Rectangle() {
        width = height = 0.0;
    }

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double getArea() { return width * height; }

    public double getPerimeter() { return 2 * (width + height); }
}
```

**变式**：加入 `Point` 左上角、`boolean contains(Point p)` → 用 **组合** `private Point corner;`，比较坐标。

**基本分**：题目要几个构造写几个 + 要几个方法写几个（公式别写错：面积 w×h，周长 2(w+h)）。

---

##### A5 构造重载 · this() 链

**对应**：PPT `ConstructorOverloading` / `Student` 三构造。

**知识点**：`this(实参)` 调用 **本类另一个构造**，必须放在构造 **第一行**。

```java
class Student {
    private String name, id;

    public Student(String nm, String id) {
        this.name = nm;
        this.id = id;
    }
    public Student(String nm) {
        this(nm, "00000000");
    }
    public Student() {
        this("Unknown");
    }
}
```

**基本分**：多个构造 + 至少一处 `this(...)` 调别的构造。

---

##### A6 多层继承 · super 链

**对应**：PPT `Person → Student → Undergraduate`。

**知识点**：每层子类构造 **先** `super(父类需要的参数)`，否则父类字段未初始化。

```java
class Person {
    Person() { System.out.println("Person"); }
}
class Student extends Person {
    Student(int id) { System.out.println("Student " + id); }
}
class Undergraduate extends Student {
    Undergraduate(int id) {
        super(id);
        System.out.println("Undergraduate");
    }
}
```

**基本分**：最子类构造里 **super 参数与父类构造匹配**。

---

##### A7 方法重载

**对应**：PPT `Screen.print(int/float/String)`。

**知识点**：同名，**参数类型或个数不同**；与返回值无关。

```java
void print(int i)    { System.out.println(i); }
void print(String s) { System.out.println(s); }
void print(double d) { System.out.println(d); }
```

**基本分**：至少 2 个同名方法，参数列表不同。

---

##### A8 重写 equals / hashCode / toString

**对应**：PPT 集合章要求、HashSet 存自定义对象。

**题目示例**：`equals` 仅比较 `id`；`toString` 返回所有字段。

```java
@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Student)) return false;
    Student s = (Student) o;
    return this.id == s.id;
}

@Override
public int hashCode() {
    return Long.hashCode(id);
}

@Override
public String toString() {
    return "Student{id=" + id + ", name=" + name + "}";
}
```

**基本分**：equals 参数是 **Object**；hashCode 若题目提到 HashSet **必写**。

---

##### A9 getter / setter

**题目示例**：提供 `getName()`、`setName(String name)`。

```java
public String getName() { return name; }
public void setName(String name) { this.name = name; }
```

**基本分**：get **return 字段**；set **`this.字段 = 参数`**。

---

##### A10 实现多个接口

**题目示例**：`class Duck extends Animal implements Flyable, Swimmable`

```java
interface Flyable { void fly(); }
interface Swimmable { void swim(); }

class Duck extends Animal implements Flyable, Swimmable {
    public void fly()  { System.out.println("flying"); }
    public void swim() { System.out.println("swimming"); }
}
```

**基本分**：`extends` 一个类 + `implements` 多个接口用逗号分隔；**每个接口方法都要实现**。

---

#### B 组 · 第五章「高级语言特征」（编程 ★★★）

##### B1 static

**题目示例**：统计创建了多少个对象；或 `static void main` 调 `static` 方法。

```java
class Counter {
    static int n = 0;
    Counter() { n++; }
    static int getCount() { return n; }
}
```

**知识点**：static 属于 **类**，所有对象共享；static 方法 **不能** 直接访问实例字段（无 this）。

**基本分**：`static` 关键字 + 题目要求的变量/方法。

---

##### B2 final

| 题目说 | 写法 |
|--------|------|
| final 类 | `final class X { }` 不能再 extends |
| final 方法 | `public final void f() { }` 不能重写 |
| final 字段 | 构造或声明时赋一次；引用可改对象内容 |

```java
final class Config { }  // 不可继承

class Box {
    final int id;
    final int[] data = {1, 2};
    Box(int id) { this.id = id; }
    void change() { data[0] = 9; }  // OK
}
```

---

##### B3 抽象方法

**题目示例**：抽象类 `Animal` 有 `abstract void sound();`，`Dog` 实现。

```java
abstract class Animal {
    abstract void sound();
}
class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("wang");
    }
}
```

**基本分**：抽象类里 **只有声明**；具体类 **public void** 实现。

---

##### B4 enum

**题目示例**：定义季节枚举，含 `SPRING, SUMMER` 及构造传中文名。

```java
enum Season {
    SPRING("春"), SUMMER("夏");
    private final String label;
    Season(String label) { this.label = label; }
    public String getLabel() { return label; }
}
```

**基本分**：`enum` 关键字 + 常量列表；若题目要方法则写。

---

##### B5 ArrayList

**对应**：PPT `UseArrayList`、实验 **练习三** 农场 ArrayList。

**题目示例**：创建 List，add、在指定下标 insert、set 修改、remove 删除、遍历输出。

```java
List<String> list = new ArrayList<>();
list.add("86");
list.add("98");
list.add(1, "99");           // 在下标 1 插入
for (int i = 0; i < list.size(); i++) {
    System.out.print(list.get(i) + " ");
}
list.set(1, "77");
list.remove(0);              // 下标 0
```

**基本分**：`new ArrayList<>()` + 题目点的操作各写一句。

---

##### B6 HashMap

**对应**：PPT `UseHashMap`、练习三设备表、单词统计。

**题目示例**：键值存姓名-分数；同 key 覆盖；按 key 查询。

```java
Map<String, String> map = new HashMap<>();
map.put("张一", "86");
map.put("李二", "98");
map.put("李二", "77");       // 覆盖
System.out.println(map.get("李二"));
map.remove("张一");
```

**统计词频模板**：

```java
Map<String, Integer> freq = new HashMap<>();
for (String w : words) {
    freq.put(w, freq.getOrDefault(w, 0) + 1);
}
```

**基本分**：put + get；统计题加 getOrDefault 循环。

---

##### B7 HashSet

**对应**：PPT `FindDups` 去重。

```java
Set<String> set = new HashSet<>();
for (String s : args) {
    if (!set.add(s)) {
        System.out.println("Duplicate: " + s);
    }
}
```

**基本分**：`new HashSet<>()` + add；题目若说「不重复」用 Set。

---

#### C 组 · 第六章「异常处理」（编程 ★★）

##### C1 try-catch-finally

**题目示例**：读文件时捕获 IOException；除零捕获 ArithmeticException。

```java
public void readFile(String path) {
    try {
        // 可能出错的代码
    } catch (IOException e) {
        System.out.println("读文件失败");
    } finally {
        // 可选：关闭资源（更推荐 try-with-resources）
    }
}
```

**try-with-resources（推荐写法）**：

```java
try (BufferedReader br = new BufferedReader(new FileReader(path))) {
    // 读
} catch (IOException e) {
    e.printStackTrace();
}
```

**基本分**：try + 至少一个 catch；题目说 finally 则写。

---

##### C2 throws 与自定义异常

```java
class ScoreException extends Exception {
    ScoreException(String msg) { super(msg); }
}

void check(int score) throws ScoreException {
    if (score < 0) throw new ScoreException("分数非法");
}
```

**基本分**：自定义类 **extends Exception**；throw + throws 与题目一致。

---

#### D 组 · 第七章「输入输出」（编程 ★★★ · 练习四）

##### D1 字符流按行读写

**对应**：实验 `FarmStorage`、PPT 流式 I/O。

**题目会给**：`FileReader`、`BufferedReader`、`FileWriter` 等声明。

```java
static void copyLines(String inPath, String outPath) throws IOException {
    try (BufferedReader br = new BufferedReader(new FileReader(inPath));
         BufferedWriter bw = new BufferedWriter(new FileWriter(outPath))) {
        String line;
        while ((line = br.readLine()) != null) {
            bw.write(line);
            bw.newLine();
        }
    }
}
```

**基本分**：try-with-resources + while readLine + write/newLine。

---

##### D2 去空行复制 · FarmStorage 型

**题目示例**：复制 txt，**跳过空行**（或只复制非空行）。

```java
while ((line = br.readLine()) != null) {
    if (line.trim().isEmpty()) continue;
    bw.write(line);
    bw.newLine();
}
```

**基本分**：`trim().isEmpty()` + continue。

---

##### D3 split 解析

**对应**：FarmStorage 按逗号存动物/设备。

```java
String[] parts = line.split(",");
String name = parts[0].trim();
int age = Integer.parseInt(parts[1].trim());
```

**基本分**：split + 下标取字段 + parseInt/parseDouble。

---

#### E 组 · 第九章「线程」（编程 ★★）

##### E1 线程类

**对应**：PPT `CountDown2`、`AutoSaveThread`。

```java
class AutoSave extends Thread {
    private volatile boolean running = true;

    public void shutdown() {
        running = false;
        interrupt();
    }

    @Override
    public void run() {
        while (running) {
            try {
                Thread.sleep(1000);
                // 题目要求的保存/打印
            } catch (InterruptedException e) {
                if (!running) break;
            }
        }
    }
}
```

**使用**：`AutoSave t = new AutoSave(); t.start();`（题目若要求 main 才写）

**基本分**：extends Thread + public run() + 题目要的 sleep/循环。

---

##### E2 Runnable

```java
class Task implements Runnable {
    public void run() {
        System.out.println("task");
    }
}
// 使用
new Thread(new Task()).start();
```

**基本分**：implements Runnable + run()；启动用 **start()** 不是 run()。

---

##### E3 synchronized

**题目示例**：多线程累加共享变量 count。

```java
synchronized void add() {
    count++;
}
// 或
synchronized (lock) {
    count++;
}
```

**基本分**：synchronized 关键字 + 共享变量修改在块/方法内。

---

#### F 组 · GUI（编程 ★★ · 大作业 FarmGUI）

##### F1 ActionListener

**题目示例**：按钮点击把输入框文字追加到文本区。

```java
button.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        textArea.append(inputField.getText() + "\n");
    }
});
```

**基本分**：`addActionListener` + 匿名类 + `@Override` + `actionPerformed` + 题目那一行操作。

---

##### F2 WindowAdapter

**题目示例**：关闭窗口时退出或保存。

```java
frame.addWindowListener(new WindowAdapter() {
    @Override
    public void windowClosing(WindowEvent e) {
        // 保存 / System.exit(0)
    }
});
```

**基本分**：WindowAdapter + 只重写 windowClosing。

---

##### F3 常用组件（题目若要求创建界面）

```java
JFrame frame = new JFrame("标题");
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
JPanel panel = new JPanel();
JButton btn = new JButton("确定");
JTextArea area = new JTextArea(10, 30);
panel.add(btn);
panel.add(new JScrollPane(area));
frame.add(panel);
frame.pack();
frame.setVisible(true);
```

**基本分**：题目要哪个组件写哪个；纸笔常只考 **监听器补全**，不必整窗。

---

#### G 组 · 其他可能要求

##### G1 main 与变长参数

**仅题目明确要求时写 main**：

```java
public static void main(String[] args) {
    EmpInfo e = new EmpInfo("a", "b", "c");
    e.print();
}
```

**变长参数**（PPT `VariousArgs`）：

```java
double avg(int r, int... points) {
    int sum = 0;
    for (int p : points) sum += p;
    return (double) sum / points.length * r;
}
```

---

### 第四步：两道编程题常见搭配

| 搭配 | 说明 |
|------|------|
| **① OOP 综合 + ② 文件/集合方法** | 最常见：第 1 道 Person/Student；第 2 道 HashMap 或 BufferedReader |
| **① OOP + ② GUI 监听器** | 补 ActionListener / WindowAdapter |
| **① 继承体系 + ② 线程类** | Animal 子类 + extends Thread |
| **① 多类建模 + ② enum/equals** | 加 HashSet 存对象 |

**第二道原则**：看清是 **写整个类** 还是 **只写某一个方法**；方法题 **题目给 API 声明**，你只写方法体 + throws。

---

### 第五步：按课件自查清单（编程题全能）

考前过一遍，**不会的回到对应小节**：

| 课件/实验 | 必会编程技能 | ☐ |
|-----------|--------------|---|
| 第四章 EmpInfo | 普通类 + 构造 + print/toString | ☐ |
| 第四章 Shape/Rectangle | extends + @Override + super | ☐ |
| 第四章 构造重载 | this(...) 链 | ☐ |
| **官方样例** | abstract + interface + extends + implements + 组合 | ☐ |
| 第五章 抽象/接口 | abstract 方法实现；多接口 | ☐ |
| 第五章 集合 | ArrayList / HashMap / HashSet 基本操作 | ☐ |
| 第五章 equals/hashCode | Object 参数 + instanceof | ☐ |
| 第六章 | try-catch；throws；try-with-resources | ☐ |
| 第七章 / 练习四 | readLine；去空行；split | ☐ |
| 第九章 | Thread.run；Runnable；synchronized | ☐ |
| GUI / FarmGUI | ActionListener；WindowAdapter | ☐ |

---

### 第六步：官方样例 · 对照表（写完打勾）

| 题号 | 题目要求 | 你写了吗？ |
|------|----------|------------|
| 1 | `abstract class Person` + name, age | ☐ |
| 1 | Person 构造 + toString | ☐ |
| 2 | `class Job` + accountabilities + 构造 + toString | ☐ |
| 3 | `interface Life` + `void living();` | ☐ |
| 4 | `Student extends Person implements Life` | ☐ |
| 4 | 字段 school, id, job | ☐ |
| 4 | 构造 + **super(name, age)** | ☐ |
| 4 | living() 固定输出 | ☐ |
| 4 | setJob(Job job) | ☐ |
| 4 | toString 含 **全部** 成员 | ☐ |

**10 项对 8 项 ≈ 基本分**；全对 ≈ 满分。

---

'''

text = MD.read_text(encoding="utf-8")
i0 = text.index(START)
i1 = text.index(END)
text = text[:i0] + HANDBOOK + text[i1:]

# Update intro of 编程题 section
text = text.replace(
    "下面按 **PPT 章节 + 实验作业** 汇总 **所有可能考到** 的编程要求（不只官方 Person 样例）。",
    "下面按 **PPT 章节 + 实验作业** 汇总 **所有可能考到** 的编程要求（不只官方 Person 样例）。",
)

# Update 目录 sub-item
old_toc = "  - [按题目要求写 · 知识点保基本分](#编程题--按题目要求写知识点--保基本分)"
new_toc = """  - [按题目要求写 · 知识点保基本分](#编程题--按题目要求写知识点--保基本分)
  - [编程全能考点手册（按课件）](#第三步编程题全能考点手册按课件--按题目用语)"""
if old_toc in text and new_toc not in text:
    text = text.replace(old_toc, new_toc)

# Expand 题型分类 intro - add link after 类型1
text = text.replace(
    "### 类型 1：OOP 建模（官方样例 ★★★）\n\n抽象类 + 接口 + 继承 + 组合 → 见 [满分骨架](#满分骨架默写)",
    "### 类型 1：OOP 建模（官方样例 ★★★）\n\n抽象类 + 接口 + 继承 + 组合 → 见 [全能考点手册 A 组](#a-组--第四章面向对象特性编程--最高频) + [满分骨架](#满分骨架默写)",
)

# Update 编程题自测 list
old_self = """## 编程题自测

1. 默写 **Person / Job / Life / Student** 完整四类（官方样例）。  
2. 写方法：读 `input.txt` 去空行写入 `output.txt`。  
3. 写方法：`HashMap` 统计单词频次。  
4. 为 `JButton` 写 `ActionListener` **匿名内部类**。  
5. 写 `extends Thread` 的 `run()` + `sleep` + `volatile` 退出。"""

new_self = """## 编程题自测（按全能手册）

1. **A2 官方样例**：Person / Job / Life / Student 四类（12 分钟）。  
2. **A1**：EmpInfo 或 Rectangle 普通类（字段+构造+方法）。  
3. **A3**：Shape/Rectangle 继承 + override + super。  
4. **A5**：构造重载 + this() 链。  
5. **A8**：equals 只比 id + toString。  
6. **B5～B7**：ArrayList 增删改查；HashMap 覆盖与统计；HashSet 去重。  
7. **D2**：BufferedReader 读文件去空行写出。  
8. **E1**：extends Thread + run + sleep。  
9. **F1～F2**：ActionListener 与 WindowAdapter 各默写一遍。  
10. 随机抽一道：**圈题目用语 → 查总索引表 → 写代码**。"""

if old_self in text:
    text = text.replace(old_self, new_self)

MD.write_text(text, encoding="utf-8")
print("OK lines", text.count("\n"))
