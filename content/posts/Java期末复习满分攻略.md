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
> **本文档**：在原有提纲基础上扩充为 **详讲版**——每章有概念解释 + 代码示例 + 考场陷阱；简答附 **22 题完整详答**；读程附 **30 题逐题手算解析**。

![期末考试题型说明](/java-exam/exam-structure.png)

| 题型 | 题量 | 核心要求 |
|------|------|----------|
| **简答题** | **4～5 道** | **只考概念**，不写完整程序；**必考多线程 + GUI** 各至少 1 道 |
| **读程题** | **5～7 道** | **只写运行结果**（代码保证能运行） |
| **编程题** | **2 道** | 纸笔写类、接口、方法（常考 OOP 建模） |

**复习顺序**：简答背概念 → 读程手算 → 编程默写骨架。

---

## 目录

- [PPT 章节 ↔ 题型对照](#ppt-章节--题型对照摘自-javacourse)
- [按课件逐章要点（详讲）](#按课件逐章要点详讲)
- [简答题题库（详答版 22 题）](#简答题题库详答版--共-22-题)
- [读程题库（25 题 · 只写输出）](#二读程题57-道--题库-25-题)
- [★ 期末抢分秘籍](#-期末抢分秘籍)
- [三、编程题（2 道）](#三编程题2-道)
  - [按题目要求写 · 知识点保基本分](#编程题--按题目要求写知识点--保基本分)
  - [编程全能考点手册（按课件）](#第三步编程题全能考点手册按课件--按题目用语)
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

## 按课件逐章要点（详讲）

> 下表是 **速查提纲**；每节后附 **详讲**：把 PPT 里容易只背标题、不懂原理的部分写透。

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

#### 第一章详讲

**1. Java 既是语言又是平台**

- **语言**：你写的 `.java` 源码，语法、关键字、类库 API。
- **平台**：JVM + Java API。不同操作系统装不同 JVM，但跑的是同一份 **字节码**（`.class`），所以叫「Write Once, Run Anywhere」。

**2. Java SE / EE / ME 怎么记**

| 版本 | 面向 | 本课 |
|------|------|------|
| **SE** | PC 桌面、标准库 | ✅ 期末只考这个 |
| **EE** | 企业 Web、Servlet、EJB | 了解即可 |
| **ME** | 手机、嵌入式 | 了解即可 |

**3. Java 十大特征（简答可逐条展开）**

PPT Slide 30 原文框架，每条要能 **用一句话解释**：

1. **简单性**：去掉 C++ 的指针、多重继承、goto；有 GC。
2. **面向对象**：封装、继承、多态（第二章展开）。
3. **分布式**：URL 访问网络资源；Applet 曾用于浏览器（了解）。
4. **解释型**：字节码半编译半解释，跨平台。
5. **可移植性**：体系结构中立，靠 JVM。
6. **健壮性**：强类型、异常机制、GC。
7. **安全性**：无指针、字节码验证器、类装载器。
8. **高性能**：JIT 即时编译热点代码。
9. **多线程**：语言级支持，第九章重点。
10. **动态性**：运行时动态装载类，不必像 C++ 改库就全量重编译。

**4. JVM 运行过程（读程/简答都可能问）**

```
.java  --javac-->  .class（字节码）
                      ↓
              类装载器 → 字节码验证器 → 解释器 / JIT → 本地机器码执行
```

**5. 主类与 main 的硬性规则（读程常考编译错误）**

| 规则 | 错例 | 后果 |
|------|------|------|
| 文件名 = public 类名 | `Hello.java` 里 `public class Hi` | 编译失败 |
| 入口必须是 `main` 小写 | `public static void Main(...)` | 运行找不到入口 |
| `main` 必须 `static` | 非 static main | 无法直接启动 |
| 参数类型 | `String args` 可以；`String[] args` 标准写法 | — |

```java
// PPT Slide 56 改错题：Main 大写、中文引号
public class HelloWorld {
    public static void main(String[] args) {  // Main → main；英文引号
        System.out.println("Hello World!");
    }
}
```

---

### 第二章 `2_面向对象程序设计概念.ppt`

| 概念 | 简答一句话 + 要点 |
|------|-------------------|
| **抽象** | 说明本质、忽略非本质；OOP 基础 |
| **对象** | 状态（成员变量）+ 行为（方法）+ 标识；**消息 = 方法调用** |
| **类** | 同种对象的集合与抽象；**实例化 → 对象** |
| **封装** | 数据+方法包装进类；`public/protected/private/默认` 隐藏实现 |
| **继承** | is-a；子类继承父类变量方法；可增新成员、**重写**；Java **单继承** |
| **多态** | 编译时：**重载**；运行时：**重写 + 向上转型 + 动态绑定** |

#### 第二章详讲：六个概念怎么答才满分

**抽象（Abstraction）**  
从具体事物中抽出 **共性**，忽略与当前问题无关的细节。例如「学生」类只关心学号、姓名，不关心身高、爱好是否与本题有关。

**对象（Object）**  
程序运行时的 **实体**，有：

- **状态**：成员变量的当前值；
- **行为**：方法；
- **标识**：内存中唯一，引用变量存的是地址。

向对象 **发消息** = 调用它的方法：`stu.study()`。

**类（Class）**  
对象的 **模板/图纸**。`Student s = new Student();` 中，`Student` 是类，`s` 是对象（实例）。

**封装（Encapsulation）**  
把数据和方法绑在类里，用 **访问控制** 隐藏内部：

| 修饰符 | 同类 | 同包 | 子类 | 任意 |
|--------|:----:|:----:|:----:|:----:|
| private | ✅ | ❌ | ❌ | ❌ |
| 默认 | ✅ | ✅ | ❌ | ❌ |
| protected | ✅ | ✅ | ✅ | ❌ |
| public | ✅ | ✅ | ✅ | ✅ |

对外只暴露必要接口（如 getter/setter），内部实现可改而不影响调用方。

**继承（Inheritance）**  
表达 **is-a**：`Dog extends Animal`。子类 **拥有** 父类非 private 成员，可 **扩展** 新字段/方法，可 **重写** 父类方法。Java **只允许单继承**一个类，多继承效果靠 **接口**。

**多态（Polymorphism）**  
同一操作作用于不同对象，表现不同行为。

- **编译时多态**：**重载**——同名方法，参数列表不同；编译期确定调哪个。
- **运行时多态**：**重写**——子类改父类方法；父类引用指向子类对象时，**运行时** 调子类版本（动态绑定）。  
  `Animal a = new Dog(); a.speak();` → 执行 `Dog.speak()`。

**static / final 方法不参与动态绑定**（第五章会再考）。

---

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

#### 第三章详讲

**基本类型 8 种**

| 类型 | 字节 | 默认值（成员变量） | 备注 |
|------|:----:|-------------------|------|
| byte, short, int, long | 1/2/4/8 | 0 | long 字面量加 `L` |
| float, double | 4/8 | 0.0 | float 字面量加 `f` |
| char | 2 | `\u0000` | Unicode |
| boolean | — | false | **不能与 int 互转** |

**引用类型**：类、接口、数组、`String`、`enum`。声明 `String s;` 只产生引用，默认 `null`；使用前通常要 `new` 或赋值。

**String 不可变——读程必考**

```java
String s = "Hi";
s.concat("!");       // 返回新串 "Hi!"，s 仍是 "Hi"
s = s + "!";         // s 指向新对象
```

循环拼接用 `StringBuilder`（单线程）或 `StringBuffer`（多线程同步）。

**== 与 equals（PPT `Equivalence` 例题）**

```java
Integer n1 = new Integer(47), n2 = new Integer(47);
System.out.println(n1 == n2);        // false，两个不同对象
System.out.println(n1.equals(n2));   // true，Integer 重写了 equals

// 陷阱：自定义 equals 签名错误
class Value {
    int i;
    public boolean equals(Value v) {  // × 不是重写 Object.equals(Object o)
        return this.i == v.i;
    }
}
// 调用 v1.equals(v2) 能编译，但 Object.equals 仍是比较引用
```

**NaN / Infinity**

```java
double a = 0.0 / 0.0;   // NaN
double b = 1.0 / 0.0;   // Infinity
System.out.println(a == a);              // false
System.out.println(Double.isNaN(a));     // true
```

**数组是引用类型**

```java
int[] a = {1, 2}, b = a;
b[0] = 99;
System.out.println(a[0]);  // 99，a 与 b 指向同一数组
```

**switch 与 break**：没有 `break` 会 **贯穿** 到下一个 case（读程要数执行了几条 `println`）。

---

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

#### 第四章详讲

**类体执行顺序（读程偶尔考）**

1. 静态初始化块 / 静态变量（类加载时，只一次）  
2. 实例初始化块 / 实例变量  
3. 构造方法  

**参数传递：Java 只有值传递**

```java
void f(int x) { x = 10; }           // 改的是副本
void g(int[] arr) { arr[0] = 10; }  // 副本指向同一数组，内容会变
```

**PPT 原版 `UnmaskField`（= 官方 Test2 同类）**

```java
public class UnmaskField {
    private int x = 1, y = 1;

    public void changeFields(int a, int b) {
        x = a;           // 成员 x → 10
        int y = b;       // 局部 y 遮蔽成员 y
        this.y = 8;      // 成员 y → 8
        System.out.println("x=" + x + "; y=" + y);  // 局部 y=9
    }

    public void printFields() {
        System.out.println("x=" + x + "; y=" + y);
    }

    public static void main(String[] args) {
        UnmaskField uf = new UnmaskField();
        uf.printFields();           // x=1; y=1
        uf.changeFields(10, 9);     // x=10; y=9（println 里 y 是局部）
        uf.printFields();           // x=10; y=8
    }
}
```

**继承构造**：子类构造 **第一行** 必须是 `super(...)` 或 `this(...)`，否则编译器自动插入 `super()`。父类无无参构造时，子类必须显式调 `super(参数)`。

**重写规则速记**

- 方法名、参数列表 **相同**（重载是参数不同）。
- 返回类型兼容；访问权限 **不能更严**。
- 不能抛出 **更多/更新** 的受检异常。
- `@Override` 建议写上，编译器帮你查。

---

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

#### 第五章详讲

**static**

- 属于 **类**，不属于某个对象；所有实例共享一份静态变量。
- 静态方法里 **不能** 直接用实例成员（没有 `this`），只能调其他静态成员或通过对象访问实例成员。
- **静态方法不参与重写**：`Father.f()` 与 `Son.f()` 是隐藏（hide），不是多态。

**final**

```java
final int x = 1;      // x 不能重新赋值
final int[] arr = {1, 2};
arr[0] = 99;          // ✅ 数组内容可变
arr = new int[3];     // ❌ 不能让 arr 指向新数组
```

**抽象类 vs 接口（简答高频）**

| 对比项 | 抽象类 | 接口 |
|--------|--------|------|
| 关键字 | `abstract class` | `interface` |
| 继承/实现 | `extends` 单继承 | `implements` 可多接口 |
| 构造方法 | 可以有 | 不能有 |
| 成员变量 | 任意 | 默认 `public static final` 常量 |
| 方法 | 可有抽象+具体 | 传统全抽象；Java 8+ 可有 default/static |
| 实例化 | 不能直接 `new` | 不能直接 `new` |

**HashSet 与 hashCode**

- `equals` 相等 → `hashCode` **必须** 相等。
- 放入 `HashSet` 的对象应 **同时重写** `equals` 和 `hashCode`。
- 只重写 `equals` 不重写 `hashCode` → Set 可能认为两个「相等」对象是两个元素。

**Iterator 删除（PPT `TestIterator`）**

```java
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    if (it.next().equals("I"))
        it.remove();   // 必须用迭代器的 remove，不能 list.remove(i) 在 for-each 里
}
```

**enum**

```java
public enum Season { SPRING, SUMMER, AUTUMN, WINTER; }
Season.SPRING.ordinal();  // 0
Season.SPRING.name();     // "SPRING"
Season.values();          // 所有常量数组
// 枚举比较用 == 即可（单例）
```

---

### 第六章 `6_异常处理.ppt`

| 要点 | 说明 |
|------|------|
| Error vs Exception | Error 严重不可恢复；Exception 可捕获 |
| 受检 vs 非受检 | `IOException` 等**必检**须处理；`RuntimeException` **免检** |
| try-catch-finally | 未捕获则终止；**finally 常执行**（关流） |
| throws / throw | 方法声明 `throws`；`throw` 抛给调用者 |
| 读程 | 未捕获异常 → **后续语句不执行** |

#### 第六章详讲

**异常层次（简答可画简图）**

```
Throwable
├── Error（OutOfMemoryError…）— 一般不 catch
└── Exception
    ├── RuntimeException 及其子类 — 非受检（NullPointerException, ArrayIndexOutOfBounds…）
    └── 其他（IOException…）— 受检，必须 try-catch 或 throws
```

**try-catch-finally 执行顺序**

1. try 正常结束 → catch 跳过 → **finally 执行**  
2. try 抛异常且 catch 匹配 → catch 执行 → **finally 执行**  
3. try 抛异常且无 catch → **finally 仍执行** → 异常继续向上抛  
4. `System.exit(0)` 时 finally **不** 执行（了解）

**throws vs throw**

- `throws`：写在 **方法签名**，声明可能抛出的受检异常，交给调用者处理。
- `throw`：在方法 **体内** 主动 `throw new IOException("msg");`

---

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

#### 第七章详讲

**怎么选流**

| 场景 | 推荐 |
|------|------|
| 读 `.txt` 文本 | `BufferedReader` + `FileReader` |
| 读图片/二进制 | `BufferedInputStream` + `FileInputStream` |
| 写文本按行 | `BufferedWriter.newLine()` |
| 控制台输入 | `Scanner` 或 `BufferedReader(System.in)` |

**标准读法模板（编程题默写）**

```java
try (BufferedReader br = new BufferedReader(new FileReader(path))) {
    String line;
    while ((line = br.readLine()) != null) {
        // 处理 line
    }
}  // try-with-resources 自动 close
```

**Scanner 陷阱**：`nextInt()` 后接 `nextLine()` 会读到换行符——读程/上机常考，中间加一次 `nextLine()` 吃掉换行。

---

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

#### 第九章详讲

**创建线程两种方式**

```java
// 方式 1：推荐，任务与 Thread 解耦
Runnable task = () -> System.out.println("run");
new Thread(task).start();

// 方式 2：继承 Thread
class MyThread extends Thread {
    public void run() { System.out.println("run"); }
}
new MyThread().start();
```

**PPT `CountDown2` 读程要点**

- `t1.start(); t2.start();` 后 main 可能先打印 `waiting for run...`，再与子线程输出 **交错**。
- 每个线程 `sleep(1000)` 一秒打印一次，输出顺序 **不保证**（除非 `join`）。

**synchronized 两种写法等价**

```java
public synchronized void mtd() { /* 方法体 */ }
// 等价于
public void mtd() { synchronized(this) { /* 方法体 */ } }
```

**可重入锁（PPT `Reentrant`）**：同一线程对已持有锁的对象再次进入 `synchronized`，允许（否则 `a()` 调 `b()` 会死锁）。

**wait / notify 必须在 synchronized 块内**，且调用对象是 **锁对象**。`wait()` 释放锁并等待；`notify()` 唤醒 wait pool 中一个线程。

**死锁预防**：对多个锁 **按固定全局顺序** 加锁；避免嵌套持锁。

---

### GUI（课程大纲有，课件文件夹无独立 `.ppt`）

结合大作业 `FarmGUI.java` + 自学：**AWT 重量级 vs Swing 轻量级**、组件层次、`ActionListener` / `WindowAdapter`、**匿名内部类**、**EDT**（耗时操作放后台线程）。

#### GUI 详讲

**AWT vs Swing**

| | AWT | Swing |
|---|-----|-------|
| 实现 | 依赖操作系统原生控件（**重量级**） | 纯 Java 绘制（**轻量级**） |
| 包 | `java.awt.*` | `javax.swing.*`，前缀 `J` |
| 组件 | `Frame`, `Button` | `JFrame`, `JButton` |

**事件处理三步**

1. **事件源**：按钮 `JButton`  
2. **事件对象**：`ActionEvent`  
3. **监听器**：实现 `ActionListener`，在 `actionPerformed` 里写逻辑  

```java
button.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        // 处理点击
    }
});
// Java 8+ 可写 lambda：button.addActionListener(e -> { ... });
```

**Adapter 模式**：`MouseListener` 有 5 个方法，全写太烦 → 用 `MouseAdapter` 只重写需要的。`WindowAdapter` 同理，常重写 `windowClosing`。

**EDT（Event Dispatch Thread）**：Swing **单线程** 更新 UI。耗时任务（读大文件、网络）放 **后台线程**，完成后用 `SwingUtilities.invokeLater(() -> updateUI())` 回 EDT 改界面，否则界面 **卡死**。

**层次结构（简答可画图）**

```
Component
└── Container
    ├── Window → Frame / JFrame
    └── Panel / JPanel
        └── JButton、JTextField、JTextArea …
```

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

## 简答题题库（详答版 · 共 22 题）

> **用法**：每题按 **定义 → 原理/分点 → 对比或例子 → 考场一句话总结** 默写。  
> 下面不是提纲，是 **可直接照着练的完整答案**；背熟要点后用自己的话写满即可。

---

### 题 1　`==` 和 `equals` 有什么区别？（官方样例）

**答：**

`==` 是 Java 的 **相等运算符**，`equals` 是定义在 `Object` 类中的 **实例方法**。二者比较的对象不同，不能混用。

**（1）`==` 的含义**

- 对于 **基本类型**（`int`、`double`、`boolean` 等），`==` 比较的是 **数值是否相等**。
- 对于 **引用类型**（类、数组、接口等），`==` 比较的是 **两个引用是否指向内存中的同一个对象**，即比较 **地址**，而不是对象内部字段的值。

**（2）`equals` 的含义**

- `Object` 类中 `equals` 的 **默认实现** 与 `==` 相同，也是比较引用（地址）。
- **关键区别**：`==` **永远** 只比地址（引用类型）或数值（基本类型），**不能改**；`equals` **可以被重写**，重写后就按 **对象内容** 来比。
- 许多 Java 类库类 **重写** 了 `equals`，改为比较 **对象内容** 是否相等。例如 `String`、`Integer` 的 `equals` 比较字符序列或数值。
- 自定义类若要用 `equals` 比较字段，必须 **正确重写** `equals(Object o)`（参数类型是 `Object`，不是本类）。

> **常见误区**：「默认一样，所以没区别？」—— **错**。默认确实一样，但考试和写代码考的是 **String 等已重写 equals 的类**。那时 `==` 仍比地址，`equals` 比内容，**结果可以不同**。

**（2.1）一眼看懂：什么时候相同、什么时候不同**

```java
String a = new String("hi");
String b = new String("hi");

a == b;       // false —— 两个不同对象，地址不同
a.equals(b);  // true  —— String 重写了 equals，比字符 "hi" 是否相同
```

| 情况 | `==` | `equals` |
|------|------|----------|
| 两个引用指向 **同一个对象** | true | true（默认或重写后一般都 true） |
| 两个 **不同对象**，内容相同（如两个 `new String("hi")`） | **false** | **true**（若类重写了 equals） |
| 自定义类 **没重写** equals | 比地址 | 比地址（与 == 结果相同） |
| 自定义类 **重写了** equals | 仍比地址 | 比字段内容 |

**（3）String 的特殊情况**

- 字符串 **字面量** 可能进入字符串常量池，两个相同字面量用 `==` 可能为 `true`。
- 用 `new String("abc")` 创建的对象在堆上，`==` 与字面量比较通常为 **false**，但 `equals` 为 **true**。

**（4）规范**

比较字符串、包装类内容时，应使用 **`equals`**；只有明确要判断「是否为同一对象」时才用 `==`。

**一句话总结**：`==` 比地址（或基本类型比値）；`equals` 默认也比地址，重写后比内容。

---

### 题 2　进程和线程有什么区别？多线程有什么好处和问题？

**答：**

**（1）进程（Process）**

进程是操作系统进行 **资源分配和调度** 的基本单位。每个进程拥有 **独立的地址空间**、文件描述符、堆栈等，进程之间 **不能直接访问** 对方的内存，需要通过 IPC 等机制通信。创建一个进程的开销较大。

**（2）线程（Thread）**

线程是 **CPU 调度** 的基本单位，是进程内的 **一条执行路径**。同一进程内的多个线程 **共享** 该进程的内存空间和资源（如打开的文件），因此线程间通信比进程间容易，但共享也带来了 **同步** 问题。

**（3）区别对照**

| 对比项 | 进程 | 线程 |
|--------|------|------|
| 资源 | 独立地址空间 | 共享进程资源 |
| 开销 | 创建/切换大 | 相对小 |
| 通信 | 较复杂 | 共享变量即可（需同步） |
| 崩溃影响 | 一般不影响其他进程 | 可能影响同进程其他线程 |

**（4）多线程的好处**

- **提高 CPU 利用率**：一个线程等待 I/O 时，CPU 可切换执行其他线程。
- **改善响应**：GUI 程序中，耗时操作放后台线程，界面线程（EDT）仍可响应用户。
- **简化建模**：某些问题天然有多条并发活动（如服务器同时处理多个请求）。

**（5）多线程的问题**

- **线程安全**：多线程同时读写共享数据可能产生 **竞态条件**，结果依赖调度顺序。
- **调试困难**：错误难以稳定复现。
- **开销**：线程切换、同步机制有成本。
- **死锁**：多个线程互相等待对方持有的锁。

**一句话总结**：进程管资源、线程管执行；多线程提高效率但需同步。

---

### 题 3　线程如何同步？`synchronized` 的作用是什么？

**答：**

**（1）为什么需要同步**

当多个线程访问 **同一共享可变数据** 时，若至少有一个线程在 **写**，就必须保证操作 **互斥**，否则会出现「丢失更新」「读到脏数据」等问题。同步就是为了 **同一时刻只有一个线程** 进入临界区访问共享资源。

**（2）`synchronized` 的用法**

- **同步实例方法**：锁对象是 **当前实例** `this`。
- **同步静态方法**：锁对象是 **类的 Class 对象**。
- **同步块**：`synchronized(对象) { ... }`，显式指定锁对象。

**（3）工作原理（PPT 第九章）**

Java 中每个对象都可以作为 **锁（monitor）**。线程进入 `synchronized` 标记的代码前，必须 **获得该对象的排他锁**；若锁已被其他线程持有，当前线程进入 **lock pool** 阻塞等待，直到锁被释放。

**（4）其他手段（了解）**

- `java.util.concurrent.locks.Lock`：显式加锁解锁，功能更灵活。
- `volatile`：保证 **可见性**，**不能** 代替互斥；适合一个线程写、多线程读且语义简单的场景。

**（5）注意**

- 同步范围 **越小越好**，减少阻塞时间。
- 所有访问共享数据的代码路径都必须受 **同一把锁** 保护，不能遗漏。

**一句话总结**：`synchronized` 用对象锁保证临界区互斥，未获锁的线程等待。

---

### 题 4　什么是死锁？如何产生？如何预防或解除？

**答：**

**（1）定义**

**死锁** 是指两个或多个线程各自持有部分资源，又 **互相等待** 对方释放资源，导致所有相关线程 **永久阻塞**，程序无法继续执行。

**（2）典型产生条件（需同时满足）**

- 互斥：资源一次只能被一个线程占用。
- 持有并等待：线程持有至少一个资源，又等待其他资源。
- 不可剥夺：已获得的锁不能强行夺走。
- 循环等待：存在线程等待链形成环，如 A 等 B 的锁，B 等 A 的锁。

**（3）例子**

线程 1：`synchronized(lockA) { synchronized(lockB) { ... } }`  
线程 2：`synchronized(lockB) { synchronized(lockA) { ... } }`  
若交替获得第一把锁，可能永远等第二把锁。

**（4）预防（PPT 强调「资源排序」）**

- **统一加锁顺序**：所有线程按 **相同全局顺序** 获取多把锁（如始终先 A 后 B）。
- **减少嵌套锁**：尽量只持有一把锁。
- **缩短持锁时间**：临界区只放必要代码。
- **不要使用** 已废止的 `stop()`、`suspend()`、`resume()`。

**（5）解除**

死锁一旦发生，通常需重启或中断线程；代价大，因此 **重点在预防**。

**一句话总结**：死锁是互相等锁；预防靠固定加锁顺序、少嵌套。

---

### 题 5　`start()` 和 `run()` 有什么区别？

**答：**

**（1）`run()` 方法**

- 定义在 `Thread` 类或 `Runnable` 接口中，包含线程要执行的 **任务逻辑**。
- 若直接调用 `t.run()`，只是在 **当前线程**（通常是 main 线程）中 **普通地执行** 这段方法，**不会创建新线程**，程序仍是单线程执行。

**（2）`start()` 方法**

- `Thread` 类的方法，**不能重写**。
- 调用 `t.start()` 后，JVM 会 **创建新的执行线程**，在新线程中 **自动调用** `run()`。
- 线程进入 **Runnable** 状态，由调度器分配 CPU 时间片后进入 **Running**。

**（3）读程/考场陷阱**

- 题目写 `t.run()` 却问「启动几个线程」→ 答案是 **0 个新线程**。
- 只有 `start()` 才表示 **多线程**。

**（4）注意**

- 对同一线程对象 **不能重复** `start()`，第二次会抛 `IllegalThreadStateException`。

**一句话总结**：`run()` 是普通方法调用；`start()` 才真正启动新线程。

---

### 题 6　简述 Java 线程有哪些状态？哪些操作会导致阻塞？

**答：**

**（1）主要状态（PPT 第九章）**

- **New（新建）**：创建了 `Thread` 对象，尚未 `start()`。
- **Runnable（可运行）**：调用了 `start()`，等待或正在获得 CPU。
- **Running（运行）**：正在执行（教材中常与 Runnable 合并讨论）。
- **Blocked（阻塞）**：暂时无法继续执行，等待某种条件。
- **Dead（终止）**：`run()` 执行完毕或异常退出。

**（2）进入 Blocked 的常见原因**

- 调用 `Thread.sleep(ms)`：主动睡眠，不释放对象锁（sleep 不在 synchronized 内时）。
- 调用 `t.join()`：等待另一线程结束。
- 试图进入 `synchronized` 块但锁被占用：在 **lock pool** 等待。
- 在 `synchronized` 内调用 `wait()`：释放锁，进入 **wait pool**，等待 `notify()`。

**（3）`sleep` vs `wait`**

- `sleep` 是 `Thread` 的静态方法，**不释放** 已持有的锁。
- `wait` 是 `Object` 的方法，必须在 synchronized 内，**释放** 锁并等待唤醒。

**一句话总结**：new→Runnable→Running↔Blocked→Dead；sleep/join/等锁/wait 会阻塞。

---

### 题 7　`wait()` 和 `notify()` 有什么作用？使用时要注意什么？

**答：**

**（1）作用**

用于多线程 **协作**（典型：生产者-消费者）。当线程发现条件不满足（如缓冲区空），可在 **持有对象锁** 的情况下调用 `wait()`， **释放锁** 并进入该对象的 **wait pool** 等待；其他线程在条件满足时调用 `notify()` 或 `notifyAll()`，唤醒 wait pool 中的线程，被唤醒的线程重新竞争锁。

**（2）使用前提**

- 必须在 **synchronized(同一对象)** 块或方法内调用，否则抛 `IllegalMonitorStateException`。
- `wait()`/`notify()` 的接收者是 **锁对象**，不是 Thread 对象。

**（3）与 `sleep` 的区别**

- `wait` 释放锁；`sleep` 不释放锁。
- `wait` 需要 notify 唤醒；`sleep` 时间到自动醒。

**（4）PPT 例子**

`SyncStack` 的 `pop()` 在 buffer 空时 `wait()`；`push()` 在放入数据后 `notify()`。

**一句话总结**：wait/notify 在 synchronized 内协作；wait 释放锁，notify 唤醒等待线程。

---

### 题 8　AWT 和 Swing 有什么区别？

**答：**

**（1）AWT（Abstract Window Toolkit）**

- Java 早期 GUI 工具包，组件依赖 **底层操作系统** 的原生窗口控件绘制。
- 称为 **重量级（Heavyweight）** 组件，外观随操作系统变化。
- 主要类：`Frame`、`Button`、`Panel` 等，在 `java.awt` 包。

**（2）Swing**

- 在 AWT 之上构建，`javax.swing` 包，组件名多带 **J** 前缀：`JFrame`、`JButton`。
- 大多 **轻量级（Lightweight）**，由 Java 自己绘制，跨平台外观更一致，组件更丰富（如 `JTable`、`JTree`）。

**（3）关系**

- Swing 基于 AWT（顶层窗口仍可能用到 AWT 容器），但日常开发 **优先用 Swing**。
- 二者都使用 **事件驱动** 模型处理用户交互。

**（4）简答可补充**

- 布局管理器：`FlowLayout`、`BorderLayout`、`GridLayout` 等自动排布组件，不用手写坐标。

**一句话总结**：AWT 重量级依赖本地控件；Swing 轻量级纯 Java 绘制，功能更强。

---

### 题 9　什么是 Listener？什么是 Adapter？GUI 中为什么要用 Adapter？

**答：**

**（1）事件处理模型**

GUI 采用 **事件驱动**：用户操作（点击、关闭窗口等）产生 **事件对象**，发送给已注册的 **监听器（Listener）** 处理。

**（2）Listener（监听器）**

- 通常是 **接口**，定义一个或多个回调方法。
- 例如 `ActionListener` 有 `actionPerformed(ActionEvent e)`，处理按钮点击。
- 使用步骤：① 实现接口 ② 创建监听器对象 ③ `组件.addXxxListener(监听器)` 注册。

**（3）Adapter（适配器）**

- 某些 Listener 接口方法很多（如 `MouseListener` 有 5 个方法、`WindowListener` 有 7 个）。
- **适配器类**（如 `MouseAdapter`、`WindowAdapter`） **空实现** 所有方法，程序员 **继承适配器** 后 **只重写需要的方法**，避免写一堆空方法。

**（4）匿名内部类**

- GUI 中常写：`button.addActionListener(new ActionListener() { public void actionPerformed(ActionEvent e) { ... } });`
- 无类名，代码紧凑，可访问外部 **effectively final** 变量。

**一句话总结**：Listener 处理事件；Adapter 空实现接口，只写需要的方法。

---

### 题 10　什么是 EDT？为什么 GUI 中耗时操作要放在新线程？

**答：**

**（1）EDT（Event Dispatch Thread）**

Swing 规定 **所有 UI 的创建、更新、绘制** 都应在 **事件派发线程（EDT）** 上执行。这是 Swing 的 **单线程规则**：避免多线程同时改界面导致不一致或崩溃。

**（2）问题**

若在 EDT 上执行 **耗时操作**（读大文件、复杂计算、网络请求），EDT 被阻塞，界面 **无法重绘、无法响应点击**，用户感觉程序 **卡死**。

**（3）正确做法**

- 耗时任务在 **后台工作线程** 执行。
- 需要更新界面时，用 `SwingUtilities.invokeLater(() -> { /* 更新 UI */ })` 把代码 **提交回 EDT** 执行。

**（4）与大作业联系**

`FarmGUI` + `AutoSaveThread`：自动保存在后台线程定时运行，保存完成后若需提示用户，应回到 EDT 更新。

**一句话总结**：Swing 单线程更新 UI；耗时放后台，改界面用 invokeLater。

---

### 题 11　什么是封装、继承、多态？各举一例说明。

**答：**

**（1）封装（Encapsulation）**

将 **数据（成员变量）** 和 **操作数据的方法** 包装在类中，并通过 **访问控制**（`private`、`public` 等） **隐藏内部实现细节**，只对外提供必要接口。  
**例**：`private int age` + `public int getAge()` / `setAge()`，外部不能直接改 age 的非法值。

**（2）继承（Inheritance）**

子类通过 `extends` **获得** 父类的非 private 成员，表示 **is-a** 关系，并可 **扩展** 新成员或 **重写** 父类方法。Java **单继承** 一个类。  
**例**：`class Dog extends Animal`，Dog 拥有 Animal 的 `speak()` 并可重写为「汪汪」。

**（3）多态（Polymorphism）**

同一 **父类引用** 可以指向 **不同子类对象**，调用 **被重写的方法** 时，在 **运行时** 根据 **实际对象类型** 绑定具体方法（ **动态绑定**）。  
**例**：`Animal a = new Dog(); a.speak();` 输出狗叫声而非动物默认声。

**（4）补充**

- **重载**（编译时多态）：同名方法，参数列表不同。
- **static 方法不参与** 重写意义上的多态。

**一句话总结**：封装隐藏细节；继承复用 is-a；多态父类引用调子类重写方法。

---

### 题 12　抽象类和接口有什么区别？分别适用于什么场景？

**答：**

**（1）抽象类 `abstract class`**

- 用 `abstract` 修饰，**不能** 用 `new` 直接实例化。
- 可以包含 **抽象方法**（无方法体）和 **普通方法**、成员变量、构造方法。
- 子类用 `extends` **单继承**，必须实现全部抽象方法（除非子类也是抽象类）才能实例化。
- 适合：**is-a 关系** 且多个子类 **共享大量相同代码** 时使用。

**（2）接口 `interface`**

- 用 `interface` 定义，传统上方法 public abstract，常量是 public static final。
- 类用 `implements` 实现，Java 支持 **多接口实现**，弥补单继承不足。
- 适合：定义 **能力契约**（能做什么），如 `Life` 接口的 `living()`。

**（3）对比表**

| 项目 | 抽象类 | 接口 |
|------|--------|------|
| 继承/实现 | extends，单继承 | implements，可多实现 |
| 构造方法 | 可以有 | 不能有 |
| 成员变量 | 任意 | 默认 public static final |
| 实例化 | 不能直接 new | 不能直接 new |

**（4）编程题例子**

官方样例：`Person` 抽象类存 name/age；`Life` 接口定义 `living()`；`Student extends Person implements Life`。

**一句话总结**：抽象类共享代码+单继承；接口定义能力+多实现。

---

### 题 13　`static` 和 `final` 关键字分别有什么作用？

**答：**

**（1）`static`（静态）**

- 修饰成员变量：属于 **类**，所有实例 **共享一份**，通过 `类名.变量` 访问。
- 修饰方法：属于 **类**，**没有 `this`**，不能直接用实例成员；常作工具方法。
- 静态方法 **不参与** 重写意义上的运行时多态（子类 static 方法 **隐藏** 父类 static 方法，看引用类型）。
- 静态块：类加载时执行一次，用于静态资源初始化。

**（2）`final`（最终）**

- 修饰类：类 **不能被继承**（如 `String`）。
- 修饰方法：方法 **不能被重写**。
- 修饰变量：变量 **只能赋一次值**；对引用类型，引用不能改指向，但 **对象内容可变**（如 final 数组仍可改元素）。

**（3）组合**

- `static final` 常表示 **类常量**，如 `Math.PI`。

**一句话总结**：static 属类共享；final 禁止改继承/重写/重新赋值。

---

### 题 14　String 为什么说是不可变的？和 StringBuilder 有什么区别？

**答：**

**（1）String 不可变**

- `String` 内部字符数组（早期实现）在创建后 **不能修改**；`concat`、`+`、`replace` 等都 **返回新 String 对象**，原对象不变。
- 好处：**线程安全**（只读）、可安全共享、适合常量池。
- 读程陷阱：`s = s + "!"` 产生新对象；`s.concat("x")` 若不赋值，`s` 不变。

**（2）StringBuilder**

- **可变** 字符序列，`append`、`insert` 在 **同一对象** 上修改，适合 **循环拼接** 字符串，效率高于反复 `+` 产生大量临时 String。

**（3）StringBuffer**

- 与 StringBuilder 类似，但方法 **synchronized**，**线程安全**，单线程下 StringBuilder 更快。

**（4）比较**

| | String | StringBuilder |
|---|--------|---------------|
| 可变性 | 不可变 | 可变 |
| 线程安全 | 安全 | 不安全 |
| 适用 | 少量固定文本 | 大量拼接 |

**一句话总结**：String 改操作产生新对象；StringBuilder 原地拼接。

---

### 题 15　List、Set、Map 有什么区别？ArrayList 和 LinkedList 呢？

**答：（完整版见前文范文 4，此处扩展）**

**（1）Collection 体系**

- **List**：元素 **有序**、**可重复**，有索引。如 `ArrayList`、`LinkedList`。
- **Set**：元素 **不重复**，无索引概念。如 `HashSet`（无序）、`TreeSet`（有序）。
- **Map**：**键值对**，**key 不重复**，一个 key 对应一个 value。如 `HashMap`。Map **不是** Collection 子接口。

**（2）ArrayList**

- 底层 **动态数组**，`get(i)` 随机访问 **O(1)**，中间插入删除需移动元素 **O(n)**。

**（3）LinkedList**

- 底层 **双向链表**，头尾插删 **O(1)**，按索引访问需遍历 **O(n)**。

**（4）选用**

- 频繁按下标查改 → ArrayList；频繁在头尾增删 → LinkedList。
- 去重 → HashSet；键值查找 → HashMap。

**（5）HashMap 注意**

- `put(k, v)` 若 key 已存在，**覆盖** 旧 value。

**一句话总结**：List 有序可重复；Set 不重复；Map 键值对；ArrayList 查快，LinkedList 插删快。

---

### 题 16　放入 HashSet 的对象为什么要同时重写 `equals` 和 `hashCode`？

**答：**

**（1）HashSet 原理**

`HashSet` 基于 `HashMap`，通过对象的 **hashCode** 定位桶，再通过 **equals** 判断是否与桶内元素相同。

**（2）Java 约定**

- 若两个对象 `equals` 为 true，则 **hashCode 必须相等**。
- 若 hashCode 相等，equals 可以为 false（哈希冲突，需 equals 再判）。

**（3）只重写 equals 不重写 hashCode 的后果**

两个「逻辑相等」的对象 hashCode 可能不同，会被放进 **不同桶**，Set 中会出现 **重复元素**，违反 Set 语义。

**（4）重写要点**

- `equals`：先 `==`，再 `instanceof`，再比字段。
- `hashCode`：用相同字段计算，保证 equals 相等则 hashCode 相等。

**一句话总结**：HashSet 先比 hashCode 再 equals；equals 相等必须 hashCode 相等。

---

### 题 17　字节流和字符流有什么区别？读文本文件按行读怎么写？

**答：（完整版见范文 5）**

**（1）字节流** `InputStream`/`OutputStream`：按 **字节** 读写，适合图片、音频、任意二进制。

**（2）字符流** `Reader`/`Writer`：按 **字符** 读写，内部处理 **字符编码**，适合 `.txt` 等文本。

**（3）节点流与过滤流**

- `FileReader`：节点流，直接连文件。
- `BufferedReader`：过滤流，包装 Reader，提供 **缓冲** 和 **`readLine()`**。

**（4）按行读模板**

```java
try (BufferedReader br = new BufferedReader(new FileReader(path))) {
    String line;
    while ((line = br.readLine()) != null) {
        // 处理 line
    }
}
```

**（5）写出**

`BufferedWriter` + `write(line)` + **`newLine()`**。

**（6）try-with-resources**

JDK 7+ 自动关闭实现了 `AutoCloseable` 的资源，防止忘关流。

**一句话总结**：文本用字符流+BufferedReader.readLine()；二进制用字节流。

---

### 题 18　受检异常和非受检异常有什么区别？`throws` 和 `throw` 呢？

**答：**

**（1）Exception 分类**

- **受检异常（Checked）**：除 `RuntimeException` 及其子类外的 Exception，编译器 **强制** 处理——要么 `try-catch`，要么方法声明 **`throws`**。如 `IOException`。
- **非受检异常（Unchecked）**：`RuntimeException` 子类（如 `NullPointerException`、`ArrayIndexOutOfBoundsException`）和 `Error`，编译器 **不强制** catch。

**（2）Error vs Exception**

- **Error**：严重错误（如 `OutOfMemoryError`），一般 **不捕获**。
- **Exception**：程序可处理的异常。

**（3）`throw` vs `throws`**

- **`throw`**：在方法 **体内** 主动抛出异常对象，如 `throw new IOException("msg");`
- **`throws`**：在方法 **签名** 上声明可能抛出的受检异常，交给 **调用者** 处理。

**（4）finally**

无论是否发生异常，`finally` 块 **通常** 都会执行，常用于 **关闭资源**。

**（5）读程**

未捕获的运行时异常 → try 内 **后续语句不执行**，程序终止（除非被 catch）。

**一句话总结**：受检异常必须 catch 或 throws；throw 抛出，throws 声明。

---

### 题 19　什么是 NaN 和 Infinity？如何正确判断 NaN？

**答：**

**（1）Infinity（无穷大）**

浮点运算中，如 `1.0 / 0.0` 得到 **正无穷** `Double.POSITIVE_INFINITY`；`-1.0 / 0.0` 为负无穷。

**（2）NaN（Not a Number）**

如 `0.0 / 0.0`、无效的浮点运算结果，表示 **非数值**。

**（3）陷阱**

- **`NaN == NaN` 结果为 false**（NaN 与任何值包括自己比较相等都为 false）。
- 不能用 `x == NaN` 判断，应使用 **`Double.isNaN(x)`** 或 **`Float.isNaN(x)`**。
- 无穷大可用 `Double.isInfinite(x)`。

**（4）读程常考**

`System.out.println(0.0/0.0 == 0.0/0.0);` → **false**。

**一句话总结**：NaN 不等于自身；用 Double.isNaN() 判断。

---

### 题 20　Java 枚举类型 enum 如何定义和使用？有什么优点？

**答：**

**（1）定义**

```java
public enum Season { SPRING, SUMMER, AUTUMN, WINTER; }
```

每个枚举常量本质是 **public static final** 的枚举实例。

**（2）常用方法**

- `Season.SPRING`：引用常量。
- `values()`：返回所有常量的数组。
- `ordinal()`：返回声明顺序，从 0 开始。
- `name()`：返回常量名字符串。
- 可用于 **`switch`**。

**（3）特点**

- **类型安全**：编译期检查，比 int 常量不易写错。
- 可有 **构造方法**（默认 **private**）、字段、普通方法。
- 枚举比较可用 **`==`**（单例）。

**（4）读程**

`Season.SPRING.ordinal()` → **0**。

**一句话总结**：enum 类型安全常量；values/ordinal/name；比较用==。

---

### 题 21　Java 是值传递还是引用传递？请举例说明。

**答：**

**Java 只有值传递（pass by value）**。

**（1）基本类型**

方法参数收到的是 **值的副本**，方法内改参数 **不影响** 实参。

**（2）引用类型**

传递的是 **引用的副本**（地址值的复制），不是对象本身。因此：

- 通过副本 **修改对象内部状态**（如 `arr[0]=10`），**会影响** 实参所指向的对象。
- 若让参数 **指向新对象**（`param = new Xxx()`），**不会** 改变实参的引用。

**（3）例子**

```java
void f(int x) { x = 10; }           // 实参 int 不变
void g(int[] a) { a[0] = 10; }     // 实参数组内容变
void h(int[] a) { a = new int[3]; } // 实参引用不变
```

**一句话总结**：Java 永远传值的拷贝；引用拷贝可改对象内容，不能改引用本身。

---

### 题 22　什么是方法重载和方法重写？有什么区别？

**答：**

**（1）重载（Overload）**

- **同一类** 中，方法名相同，**参数列表不同**（类型、个数、顺序）。
- 与返回值无关；编译期根据实参 **静态绑定** 决定调哪个方法。

**（2）重写（Override）**

- **子类** 对 **父类** 实例方法重新实现，方法名、参数列表 **相同**。
- 运行时根据 **实际对象类型** **动态绑定**（多态）。
- 访问权限不能更严；受检异常不能更多；`@Override` 注解辅助检查。
- **static、final、private** 方法不能重写（static 是隐藏，不是重写）。

**（3）对比**

| | 重载 | 重写 |
|---|------|------|
| 位置 | 同类 | 子类对父类 |
| 参数 | 必须不同 | 必须相同 |
| 绑定 | 编译时 | 运行时 |
| 多态 | 编译时多态 | 运行时多态 |

**一句话总结**：重载同名不同参；重写子类改父类同名同参方法。

---

## 简答题自测清单（闭卷 22 题）

1. `==` 和 `equals` 的区别？（官方样例）
2. 进程和线程的区别？多线程的好处和问题？
3. 线程如何同步？`synchronized` 作用？
4. 什么是死锁？如何产生和预防？
5. `start()` 和 `run()` 的区别？
6. 线程有哪些状态？哪些操作会阻塞？
7. `wait()` 和 `notify()` 的作用？
8. AWT 和 Swing 的区别？
9. Listener 和 Adapter 是什么？
10. 什么是 EDT？GUI 为何要用新线程？
11. 封装、继承、多态各是什么？
12. 抽象类和接口的区别？
13. `static` 和 `final` 的作用？
14. String 为何不可变？与 StringBuilder 区别？
15. List、Set、Map 区别？ArrayList vs LinkedList？
16. HashSet 为何要重写 equals 和 hashCode？
17. 字节流和字符流区别？如何按行读 txt？
18. 受检/非受检异常？`throw` vs `throws`？
19. NaN 和 Infinity？如何判断 NaN？
20. enum 如何定义使用？
21. Java 值传递？举例。
22. 重载和重写的区别？

---

# 二、读程题（5～7 道 · 题库 25 题）

> **考场真实形式**：给一段 **能编译、能运行** 的 Java 代码，只要求 **写出运行结果**（控制台输出）。  
> **不考**「能否编译」——那种题出现在练习里，期末读程 **只填输出**。  
> 下面 **25 道** 偏 **综合、多步手算**；每题：**📖 知识点 → 代码 → 输出结果 → 逐步分析**。

## 解题四步法（只算输出）

1. **圈调用链**：main 里调了谁？构造顺序？父类/子类谁先执行？  
2. **圈作用域**：成员 / 局部 / 参数；`this.`；static 看 **声明类型** 还是 **实际对象**  
3. **盯修改**：String 是否新对象、集合 `remove` 下标还是值、异常后哪句跳过  
4. **按顺序写输出**：`print` 不换行、`println` 换行；try-catch-finally 每轮各输出什么  

---

## 官方样例题（必做 · 只写输出）

![读程题样例：Test2](/java-exam/sample-read-code.png)

**📖 相关知识点**

- 考场代码 **一定能运行**；样例 PDF 里若写了 `Test3` 是印刷笔误，按 **`Test2`** 理解。
- **变量遮蔽**：方法里 `int y = b` 是 **局部 y**，与成员 y 同名；裸写 `y` 指局部，`this.y` 指成员。
- **toString()**：`println(对象)` 会自动调 `toString()`。

**问：写出运行结果（每行一条输出）**

```java
public class Test2 {
    private int x = 1;
    private int y = 1;

    public void changeState(int a, int b) {
        x = a;
        int y = b;
        this.y = 8;
        System.out.println("x=" + x + "; y=" + y);
    }

    public String toString() {
        return "x = " + x + "; y = " + y;
    }

    public static void main(String[] args) {
        Test2 t2 = new Test2();
        System.out.println(t2);
        t2.changeState(10, 9);
        System.out.println(t2);
    }
}
```

**输出结果**：
```
x = 1; y = 1
x=10; y=9
x = 10; y = 8
```

**逐步分析**：
1. `println(t2)` → toString → `x = 1; y = 1`  
2. `changeState(10,9)`：成员 x→10；局部 y=9 打印 `x=10; y=9`；**this.y**→8  
3. 再 println(t2) → 成员 x=10, y=8  

---

## A 组 · 作用域与成员（4 题 · 综合）

### 读程 A1

**📖 相关知识点**

- 参数也是 **局部变量**，与成员同名时 **遮蔽成员**。
- 无 `this.` 时改的是 **局部/参数**；`this.n` 改 **成员**。
- 多个方法连续改同一成员，要 **按调用顺序累加**。

**问：写出运行结果**

```java
public class Mask1 {
    int n = 0;
    void bump() { n++; }
    void f(int n) {
        n = 10;
        bump();
        System.out.println(n);
        System.out.println(this.n);
    }
    public static void main(String[] args) {
        Mask1 o = new Mask1();
        o.f(5);
        o.bump();
        System.out.println(o.n);
    }
}
```

**输出结果**：
```
10
1
2
```

**分析**：`f(5)` 里局部 n=10 打印；`bump()` 使成员 n=1；`this.n` 打印 1；main 里再 bump → n=2。

---

### 读程 A2

**📖 相关知识点**

- 课件 **UnmaskField** 加长版：两次改字段 + 中间 print。
- 每次进方法都要 **分开看** 局部变量与 `this.`。

**问：写出运行结果**

```java
public class Mask2 {
    private int x = 1, y = 1;
    public void change(int a, int b) {
        x = a;
        int y = b;
        this.y = 8;
        System.out.println("x=" + x + "; y=" + y);
    }
    public void show() {
        System.out.println("x=" + x + "; y=" + y);
    }
    public static void main(String[] args) {
        Mask2 m = new Mask2();
        m.show();
        m.change(10, 9);
        m.show();
        m.change(3, 4);
        m.show();
    }
}
```

**输出结果**：
```
x=1; y=1
x=10; y=9
x=10; y=8
x=3; y=4
x=3; y=8
```

**分析**：每次 `change` 第三行 print 的是 **局部 y**；`show()` 打印 **成员**；第二次 change 后成员 x=3, y=8。

---

### 读程 A3

**📖 相关知识点**

- **static 变量** 全类共享；**实例变量** 每个对象一份。
- 通过对象访问 static 字段合法，但改的是 **同一份** static。

**问：写出运行结果**

```java
public class StaticInst {
    static int sx = 1;
    int ix = 10;
    public static void main(String[] args) {
        StaticInst a = new StaticInst();
        StaticInst b = new StaticInst();
        a.sx = 2;
        b.ix = 20;
        a.ix = 15;
        System.out.println(a.sx + " " + b.sx);
        System.out.println(a.ix + " " + b.ix);
        System.out.println(StaticInst.sx);
    }
}
```

**输出结果**：
```
2 2
15 20
2
```

---

### 读程 A4

**📖 相关知识点**

- 方法 **重载**：根据 **实参类型** 选方法。
- 重载与成员变量无关，别被同名变量干扰。

**问：写出运行结果**

```java
public class OverPrint {
    int v = 1;
    void p(int x) { System.out.print("A" + x); }
    void p(long x) { System.out.print("B" + x); }
    void p(Integer x) { System.out.print("C" + x); }
    public static void main(String[] args) {
        OverPrint o = new OverPrint();
        o.p(1);
        o.p(1L);
        o.p(Integer.valueOf(1));
        System.out.println();
        System.out.println(o.v);
    }
}
```

**输出结果**：
```
A1B1C1
1
```

**分析**：`1`→int→A；`1L`→long→B；`Integer.valueOf(1)`→C。

---

## B 组 · String / 包装类（4 题 · 综合）

### 读程 B1

**📖 相关知识点**

- String **不可变**；`+` 在循环里每次产生 **新对象**。
- `equals` 比内容；`==` 比是否为 **同一对象**。

**问：写出运行结果**

```java
public class StrLoop {
    public static void main(String[] args) {
        String s = "";
        for (int i = 0; i < 3; i++) {
            s = s + i;
        }
        String t = "012";
        System.out.println(s.equals(t));
        System.out.println(s == t);
        System.out.println(s);
    }
}
```

**输出结果**：
```
true
false
012
```

---

### 读程 B2

**📖 相关知识点**

- 字面量、`+` 常量折叠、**new String** 与常量池。
- 先 `==` 再 `equals`，顺序别漏。

**问：写出运行结果**

```java
public class StrPool {
    public static void main(String[] args) {
        String a = "java";
        String b = "ja" + "va";
        String c = new String("java");
        String d = c.intern();
        System.out.println(a == b);
        System.out.println(a == c);
        System.out.println(a == d);
        System.out.println(c == d);
    }
}
```

**输出结果**：
```
true
false
true
false
```

**分析**：`intern()` 把 c 的内容放入/指向常量池，d 与 a 同一对象；c 仍是堆上原对象。

---

### 读程 B3

**📖 相关知识点**

- `substring(begin,end)` **左闭右开**；`indexOf` 返回首次下标。
- **`+` 结合性**：从左到右，遇 String 变连接。

**问：写出运行结果**

```java
public class StrMix {
    public static void main(String[] args) {
        String s = "abcdef";
        System.out.println(s.substring(1, 4));
        System.out.println(s.indexOf("cd"));
        System.out.println("" + 1 + 2 + 3);
        System.out.println(1 + 2 + 3 + "");
        System.out.println("Java".replace('a', 'o'));
    }
}
```

**输出结果**：
```
bcd
2
123
6
Jovo
```

---

### 读程 B4

**📖 相关知识点**

- **Integer 缓存** -128～127；超出则新对象。
- **自动拆箱** 参与 `+` 时按 int 算。

**问：写出运行结果**

```java
public class Wrap {
    public static void main(String[] args) {
        Integer a = 127, b = 127;
        Integer c = 128, d = 128;
        System.out.println(a == b);
        System.out.println(c == d);
        System.out.println(c.equals(d));
        System.out.println(a + b);
        System.out.println(Double.isNaN(0.0 / 0.0));
    }
}
```

**输出结果**：
```
true
false
true
254
true
```

---

## C 组 · 继承与多态（5 题 · 高频难点）

### 读程 C1

**📖 相关知识点**

- **实例方法**：运行时 **动态绑定**，看 **实际对象类型**。
- **static 方法**：看 **引用声明类型**，没有多态。

**问：写出运行结果**

```java
class Base {
    static void sf() { System.out.print("Sb"); }
    void im() { System.out.print("Ib"); }
}
class Derived extends Base {
    static void sf() { System.out.print("Sd"); }
    void im() { System.out.print("Id"); }
}
public class Poly1 {
    public static void main(String[] args) {
        Base r = new Derived();
        r.sf();
        r.im();
        System.out.println();
        r = new Base();
        r.sf();
        r.im();
    }
}
```

**输出结果**：
```
SbId
SbIb
```

---

### 读程 C2

**📖 相关知识点**

- 课件 **PrivOverride**：子类 **不能** 用 public 方法「覆盖」父类 **private** 方法；父类 private 方法不参与多态。
- 引用类型为父类时，调 private 方法 **编译通过**，执行 **父类版本**。

**问：写出运行结果**

```java
public class PrivOverride {
    private void f() { System.out.println("parent"); }
    public static void main(String[] args) {
        PrivOverride p = new PrivChild();
        p.f();
        new PrivChild().f();
    }
}
class PrivChild extends PrivOverride {
    public void f() { System.out.println("child"); }
}
```

**输出结果**：
```
parent
child
```

**分析**：`main` 在 **声明 private f 的类内部**，`p.f()` 调的是 **父类 private 方法**（子类 public f **不算重写**）；`new PrivChild().f()` 在子类上下文中调 **子类自己的 f**。

---

### 读程 C3

**📖 相关知识点**

- **构造顺序**：创建子类 → 父类构造 → 子类构造。
- 父类构造里若调 **可被重写** 的实例方法，可能跑到 **子类尚未初始化完** 的版本（读程常考 print 顺序）。

**问：写出运行结果**

```java
class Animal {
    Animal() {
        System.out.print("A");
        show();
    }
    void show() { System.out.print("a"); }
}
class Dog extends Animal {
    int age = 10;
    Dog() { System.out.print("D"); }
    void show() { System.out.print("d" + age); }
}
public class InitOrder {
    public static void main(String[] args) {
        new Dog();
        System.out.println();
    }
}
```

**输出结果**：
```
Ad0D
```

**分析**：父构造调 `show()` 时已动态绑定到 Dog，但 **age 尚未初始化**（默认 0）→ `d0`；再 D。

---

### 读程 C4

**📖 相关知识点**

- 课件 **static 初始化块 + 继承**：先父 static → 子 static → 父构造 → 子构造。
- **static 块** 在类 **首次加载** 时执行一次。

**问：写出运行结果**

```java
class T1 {
    static int s1 = 1;
    static { System.out.print("T1s"); }
    T1() { System.out.print("T1c"); }
}
class T2 extends T1 {
    static int s2 = 2;
    static { System.out.print("T2s"); }
    T2() { System.out.print("T2c"); }
}
public class StaticInit {
    public static void main(String[] args) {
        new T2();
        new T2();
    }
}
```

**输出结果**：
```
T1sT2sT1cT2cT1cT2c
```

**分析**：static 块 **只执行一次**；第二次 new 只有构造 `T1cT2c`。

---

### 读程 C5

**📖 相关知识点**

- 数组、引用 **赋值共享**；通过任一引用改元素，另一引用可见。
- **值传递**：传引用副本，改元素有效，换引用无效。

**问：写出运行结果**

```java
public class ArrRef {
    static void change(int[] a, int x) {
        a[0] = 99;
        a = new int[] { 1 };
        x = 100;
    }
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 };
        int k = 5;
        change(arr, k);
        System.out.println(arr[0] + " " + arr.length);
        System.out.println(k);
    }
}
```

**输出结果**：
```
99 3
5
```

---

## D 组 · static / final / 重载（3 题）

### 读程 D1

**📖 相关知识点**

- **static 计数**：构造每执行一次 count++。
- static 属于类，不随对象销毁。

**问：写出运行结果**

```java
public class Count {
    static int n = 0;
    Count() { n++; }
    static void reset() { n = 0; }
    public static void main(String[] args) {
        new Count();
        new Count();
        System.out.println(n);
        reset();
        new Count();
        System.out.println(n);
    }
}
```

**输出结果**：
```
2
1
```

---

### 读程 D2

**📖 相关知识点**

- **final 引用**：不能改 **指向**；但引用指向的 **对象内容** 仍可改（如数组元素、StringBuilder）。

**问：写出运行结果**

```java
public class FinalRef {
    public static void main(String[] args) {
        final int[] a = { 1, 2 };
        a[0] = 9;
        final StringBuilder sb = new StringBuilder("Hi");
        sb.append("!");
        System.out.println(a[0] + " " + a[1]);
        System.out.println(sb);
    }
}
```

**输出结果**：
```
9 2
Hi!
```

---

### 读程 D3

**📖 相关知识点**

- **重写** 要求签名相同；子类返回类型可以是 **协变** 类型（本题不涉及）。
- 多态调用 **实际对象** 的重写方法。

**问：写出运行结果**

```java
class Shape {
    void draw() { System.out.print("S"); }
}
class Circle extends Shape {
    void draw() { System.out.print("C"); }
    void radius() { System.out.print("r"); }
}
public class ShapeTest {
    public static void main(String[] args) {
        Shape s = new Circle();
        s.draw();
        Circle c = (Circle) s;
        c.draw();
        c.radius();
    }
}
```

**输出结果**：
```
CCr
```

---

## E 组 · 集合（4 题 · 课件风格）

### 读程 E1

**📖 相关知识点**

- 课件 **UseArrayList**：add、**insert**、set、remove 混合。
- `remove(int)` 是 **下标**；删后 size 变，下标要重新想。

**问：写出运行结果**

```java
import java.util.*;
public class ListOps {
    public static void main(String[] args) {
        List<String> L = new ArrayList<>();
        L.add("86");
        L.add("98");
        L.add(1, "99");
        for (int i = 0; i < L.size(); i++) {
            System.out.print(L.get(i) + " ");
        }
        L.set(1, "77");
        L.remove(0);
        System.out.println();
        System.out.println(L);
    }
}
```

**输出结果**：
```
86 99 98 
[77, 98]
```

**分析**：插入后 [86,99,98]；set(1,"77")→[86,77,98]；remove(0) 删 86→[77,98]。

---

### 读程 E2

**📖 相关知识点**

- `remove(1)` → 下标 1；`remove(Integer.valueOf(1))` → 删 **值为 1** 的元素。
- 两种 remove **结果完全不同**，读程必考。

**问：写出运行结果**

```java
import java.util.*;
public class RemoveTrap {
    public static void main(String[] args) {
        List<Integer> L = new ArrayList<>(Arrays.asList(1, 2, 3, 2));
        L.remove(1);
        System.out.println(L);
        L.remove(Integer.valueOf(2));
        System.out.println(L);
    }
}
```

**输出结果**：
```
[1, 3, 2]
[1, 3]
```

---

### 读程 E3

**📖 相关知识点**

- **HashMap**：同 key 的 put **覆盖** value；size 不变。
- `get` 不存在返回 **null**（本题都有 key）。

**问：写出运行结果**

```java
import java.util.*;
public class MapOps {
    public static void main(String[] args) {
        Map<String, Integer> m = new HashMap<>();
        m.put("a", 1);
        m.put("b", 2);
        m.put("a", 3);
        System.out.println(m.get("a"));
        System.out.println(m.get("c"));
        System.out.println(m.size());
        m.remove("b");
        System.out.println(m.containsKey("b"));
        System.out.println(m);
    }
}
```

**输出结果**：
```
3
null
2
false
{a=3}
```

---

### 读程 E4

**📖 相关知识点**

- **HashSet** 不重复；`add` 返回 boolean 表示是否 **新加进**。
- 课件 **FindDups** 思路：重复 add 失败。

**问：写出运行结果**

```java
import java.util.*;
public class SetOps {
    public static void main(String[] args) {
        Set<String> s = new HashSet<>();
        System.out.print(s.add("A") + " ");
        System.out.print(s.add("A") + " ");
        System.out.print(s.add("B") + " ");
        System.out.println(s.size());
        System.out.println(s);
    }
}
```

**输出结果**：
```
true false true 2
[A, B]
```

（Set 的 toString 顺序 **不保证**，考场一般只考 size 或 true/false 行。）

---

## F 组 · 异常（3 题 · 课件风格）

### 读程 F1

**📖 相关知识点**

- try 里 **异常点之后** 的语句 **不执行**；进 catch；**finally 几乎总执行**。
- 课件常见：`1/0` 跳过中间 print。

**问：写出运行结果**

```java
public class Ex1 {
    public static void main(String[] args) {
        System.out.print("1");
        try {
            System.out.print("2");
            int x = 10 / 0;
            System.out.print("3");
        } catch (ArithmeticException e) {
            System.out.print("4");
        } finally {
            System.out.print("5");
        }
        System.out.print("6");
    }
}
```

**输出结果**：
```
12456
```

---

### 读程 F2

**📖 相关知识点**

- 课件 **greetings 循环** 简化版：catch 住 **数组越界** 后 break，避免死循环。
- 每轮 **finally 都执行**。

**问：写出运行结果**

```java
public class ExLoop {
    public static void main(String[] args) {
        String[] g = { "A", "B", "C" };
        int i = 0;
        while (i < 4) {
            try {
                System.out.print(g[i]);
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.print("X");
                break;
            } finally {
                System.out.print("F");
            }
            i++;
        }
        System.out.print("E");
    }
}
```

**输出结果**：
```
AFBFCFXFE
```

**逐步分析**：
- i=0：`A` + finally `F` → `AF`  
- i=1：`B` + `F` → `BF`  
- i=2：`C` + `F` → `CF`  
- i=3：越界 → `X` + finally `F` → `XF`；break  
- 最后 `E`  

---

### 读程 F3

**📖 相关知识点**

- **return 之前** 仍执行 finally。
- finally 里若有 return 会覆盖 try 的 return（本题 finally 只 print）。

**问：写出运行结果**

```java
public class ExFinally {
    static int f() {
        try {
            return 1;
        } finally {
            System.out.print("F");
        }
    }
    public static void main(String[] args) {
        System.out.print(f());
        System.out.print(f());
    }
}
```

**输出结果**：
```
F1F1
```

---

## G 组 · 多线程（3 题）

### 读程 G1

**📖 相关知识点**

- **`run()`** 普通调用，**不启新线程**；**`start()`** 才新线程。
- 本题全在 main 线程，顺序确定。

**问：写出运行结果**

```java
public class ThreadRun {
    public static void main(String[] args) {
        Thread t = new Thread(() -> System.out.print("T"));
        t.run();
        t.run();
        System.out.print("M");
    }
}
```

**输出结果**：
```
TTM
```

---

### 读程 G2

**📖 相关知识点**

- **`start()` + `join()`**：main 等子线程 **跑完** 再往下。
- 无 join 时，打印顺序可能 **不确定**（考场若给了 join 就 **确定**）。

**问：写出运行结果**

```java
public class ThreadJoin {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception {
        Thread t = new Thread(() -> sb.append("B"));
        t.start();
        t.join();
        sb.append("A");
        System.out.println(sb);
    }
}
```

**输出结果**：
```
BA
```

---

### 读程 G3

**📖 相关知识点**

- **synchronized**：同一把锁 **互斥**；本题顺序固定因 main 等 t1、t2 都 join。

**问：写出运行结果**

```java
public class SyncDemo {
    static int n = 0;
    static final Object lock = new Object();
    static void add() {
        synchronized (lock) {
            n++;
        }
    }
    public static void main(String[] args) throws Exception {
        Thread t1 = new Thread(() -> { add(); add(); });
        Thread t2 = new Thread(() -> { add(); });
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println(n);
    }
}
```

**输出结果**：
```
3
```

---

## H 组 · switch / 数组 / 循环（4 题）

### 读程 H1

**📖 相关知识点**

- **switch 贯穿**：case 无 **break** 则 **继续执行** 下一 case。
- 考场常考 **故意不写 break**。

**问：写出运行结果**

```java
public class Sw {
    public static void main(String[] args) {
        int n = 2;
        switch (n) {
            case 1: System.out.print("1");
            case 2: System.out.print("2");
            case 3: System.out.print("3"); break;
            default: System.out.print("d");
        }
        System.out.print("!");
    }
}
```

**输出结果**：
```
23!
```

---

### 读程 H2

**📖 相关知识点**

- **二维数组**：`length` 是 **行数**；每行是 **一维数组**，长度可不同。
- `a[i][j]` 先选行再选列。

**问：写出运行结果**

```java
public class Arr2D {
    public static void main(String[] args) {
        int[][] a = { { 1, 2 }, { 3 }, { 4, 5, 6 } };
        System.out.print(a.length + " ");
        System.out.print(a[1].length + " ");
        System.out.print(a[2][1] + " ");
        int sum = 0;
        for (int[] row : a) {
            sum += row[0];
        }
        System.out.print(sum);
    }
}
```

**输出结果**：
```
3 1 5 8
```

**分析**：三行；第二行长 1；a[2][1]=5；各行第 0 列 1+3+4=8。

---

### 读程 H3

**📖 相关知识点**

- **`if (b = true)`** 是 **赋值**，不是 `==`；条件为 true。
- **短路运算** `&&` / `||`：左侧能定结果则 **不评估** 右侧。

**问：写出运行结果**

```java
public class Logic {
    public static void main(String[] args) {
        int x = 0;
        if (x++ == 0) System.out.print("A");
        System.out.print(x + " ");
        boolean ok = false;
        if (ok = true) System.out.print("B");
        if (false && (++x > 0)) System.out.print("C");
        System.out.print(x);
    }
}
```

**输出结果**：
```
A1 B1
```

---

### 读程 H4

**📖 相关知识点**

- **for 循环 + continue/break**；嵌套 loop 要 **分层手算**。
- `print` 无换行，一行粘在一起。

**问：写出运行结果**

```java
public class LoopNest {
    public static void main(String[] args) {
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == j) continue;
                System.out.print(i + "" + j + " ");
            }
        }
    }
}
```

**输出结果**：
```
12 13 21 23 31 32 
```

（末尾空格可有可无，看阅卷是否抠格式。）

---

## 读程题自测索引（25 题 · 只写输出）

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

> **冲刺建议**：考场 **5～7 道** 读程，难度接近 C/E/F 组；每天 **手算 8 道** 不看书，错题回到 [按课件详讲](#按课件逐章要点详讲)。

---

# ★ 期末抢分秘籍

> 老师原话：**只有三种题型**——简答 4～5、读程 5～7、编程 2；**要用库会给方法声明**，不用背 API 签名。  
> 编程题就是 **[官方样例截图](/java-exam/sample-programming.png)** 那种：**抽象类 + 普通类 + 接口 + 子类**，纸笔写完整类定义。

## 考场时间怎么切（90 分钟卷参考）

| 阶段 | 时间 | 做什么 |
|------|------|--------|
| ① 编程题 | **25～30 min** | 先拿大分；Person/Student 型 **默写骨架** |
| ② 读程题 | **25 min** | 只写输出；每题 3～4 min，不确定也写一版 |
| ③ 简答题 | **25 min** | 概念分点写满；**多线程 + GUI 各至少 1 道** |
| ④ 检查 | **10 min** | 编程：`super`、接口、`living()` 标点；读程：漏行 |

**原则**：编程 **先写**——会就是 15～20 分一道，不会后面慌；简答 **写满** 就有分，空着必 0。

---

## 简答题 · 3 条抢分口诀

1. **分点 + 关键词**：阅卷按点给分。看到「线程同步」必写 **`synchronized`、对象锁、临界区**；看到 GUI 必写 **AWT/Swing、Listener/Adapter、EDT**。
2. **对比题用表格思维**：`==` vs `equals`、List/Set/Map、受检/非受检异常——写 **3 行对比** 比一大段废话得分高。
3. **最后一行总结句**：例如「Java 只有值传递，引用传的是地址的副本」。一句话 1 分，不亏。

---

## 读程题 · 3 条抢分口诀

1. **只填输出**——代码一定能跑；别在卷子上写「不能编译」。
2. **`print` vs `println`**：粘在一起还是换行，占一半错题；写完 **数行数** 是否和 `println` 次数一致。
3. **拿不准也写**：多线程无 `join` 时顺序可能乱，但 **有 join / synchronized** 的题顺序 **确定**，必须算准；实在不会写「输出顺序不确定」比空白强（本题若确定则别写这句）。

---

## 编程题 · 抢分核心（Person / Job / Life / Student 型）

![编程题样例：Person / Job / Life / Student](/java-exam/sample-programming.png)

老师这种题 **20 分一道、考 2 道**，本质是 **OOP 建模默写**：照着题目 **逐条翻译** 成 Java，不需要算法、不需要 main。

### 第一步：30 秒圈得分点（写在草稿角）

拿到题先在边上打勾，**写一条算一条**：

| 题目里的词 | 你要写的 Java | 几分级 |
|------------|---------------|--------|
| 抽象类 X | `abstract class X { ... }` | 必写 |
| 成员变量 | `private/protected 类型 名;` | 每个字段 1 分 |
| 构造方法 | `public X(参数) { this.x = x; }` | 2～3 分 |
| `toString()` | `return "name=" + name + ...` | 2 分 |
| 接口 Y | `interface Y { void method(); }` **无方法体** | 2 分 |
| 继承 + 实现 | `class Z extends X implements Y` | **先 extends 后 implements** |
| 调用父构造 | `super(...)` 在子类构造 **第一行** | 漏了整题构造 0 分 |
| 组合（has-a） | `private Job job;` + `setJob(Job job)` | 常漏 setJob |
| 接口方法实现 | `public void living() { System.out.println("…"); }` | 字符串 **一字不差** |
| 重写 toString | `super.toString() + ", school=" + ...` | 要含 **全部** 字段含 job |

### 第二步：默写顺序（固定 4 步，闭卷练到 12 分钟内）

```
1. abstract class Person     ← 最简单，先写稳
2. class Job                 ← 独立类，复制 Person 改字段
3. interface Life            ← 两行搞定
4. class Student             ← 分值最高，留最多时间
```

**Student 内部顺序（别乱）**：

```
extends Person implements Life
→ 字段 school, id, job
→ 构造 + super(name, age)
→ living() 固定句
→ setJob()
→ toString() 含 super.toString()
```

### 第三步：最小保分版（时间不够 / 某块忘了）

即使写不完，按下面写也能 **拿到 60%～70%**：

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
        return accountabilities;   // 忘了字段名至少 return 参数
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
        System.out.println("好好学习、天天向上！");
    }

    public void setJob(Job job) { this.job = job; }

    public String toString() {
        return super.toString() + ", school=" + school + ", id=" + id + ", job=" + job;
    }
}
```

### 第四步：致命扣分 · 考前红笔标

| 错误 | 后果 |
|------|------|
| `implements extends` 顺序反了 | 语法错，Student 整段 0 分 |
| 子类构造 **没有** `super(name, age)` | 父类字段未初始化，构造 0 分 |
| 接口里写了 `{ System.out... }` | 接口不能带实现（除非 default，本课一般不考） |
| `living()` 字符串和题目 **差一个标点** | 该方法 0 分（全角 `！` 看清楚） |
| 有 `Job job` 但 **没写 setJob** | 组合关系不完整，扣 2～4 分 |
| `toString` 只写字类字段，**没 super** | 父类 name/age 缺失，扣一半 |
| 把 `Job` 写成 `extends Job` | 组合变继承，概念错 |

### 第五步：`living()` 和 toString 格式 · 一字抄题

**官方固定句（截图原文）**：

```java
System.out.println("好好学习、天天向上！");
```

- 用的是 **中文顿号 `、`** 和 **全角叹号 `！`**
- 建议考前 **手抄三遍**，别用英文 `!`

**toString 推荐格式**（字段全、阅卷好认）：

```java
return super.toString() + ", school=" + school + ", id=" + id + ", job=" + job;
```

`job` 会自动调 `Job.toString()`，不用手动拼 `accountabilities`。

### 第六步：第二道编程题可能考什么

第一道往往是 **Person/Student 型**；第二道常见变式（仍纸笔写类/方法）：

| 变式 | 抢分写法 |
|------|----------|
| 抽象类加 `abstract void study();` | Student 里 **必须** `public void study() { ... }` |
| `Job` 改成接口 `Workable` | `implements Life, Workable`（逗号分隔，**先 extends 后 implements**） |
| 加 `equals` 只比 `id` | `if (!(o instanceof Student)) return false;` + `(Student)o` + `return id == s.id;` |
| 文件方法「去空行复制」 | 直接默写 [类型 3 骨架](#类型-3文件读写方法ppt-第三章--练习四) |
| 集合「统计单词频次」 | 默写 [类型 4 骨架](#类型-4集合方法ppt-第三章--练习三) |
| GUI 补监听器 | 默写 [类型 5 骨架](#类型-5gui-监听器补全ppt-gui-章) |
| 线程类 `extends Thread` | 默写 [类型 6 骨架](#类型-6线程类ppt-多线程章) |

**第二道若是方法题**：题目会给 `FileReader` / `HashMap` 等声明 → **只写方法体 + throws**，别纠结 import。

### 编程题 · 纸笔书写技巧

- **类与类之间空一行**，阅卷一眼四个类齐不齐。
- 字段先 **竖着写全**，再写构造，避免漏 `id` 或 `job`。
- 接口方法、实现类 public 方法：行首 **`public`** 别漏（实现接口时 public 可省略但写上更稳）。
- 写错一行 **划单线改**，别涂黑团；构造参数名和字段同名时用 **`this.`**。
- **不需要写 `main`**，除非题目明确要求。

### 编程题 · 15 分钟倒计时演练

| 分钟 | 任务 |
|------|------|
| 0～1 | 圈 Person/Job/Life/Student 得分点 |
| 1～4 | 写完 Person + Job + Life |
| 4～12 | 写 Student（super、living、setJob、toString） |
| 12～14 | 对照题目逐条打勾 |
| 14～15 | 补漏的 `@Override` 或分号 |

---

## 一页纸速记卡（进考场前背）

```
简答：多线程 + GUI 必考；分点写；对比题三行表
读程：只写输出；println 数行数；String/集合/多态手算
编程：Person→Job→Life→Student
      extends 在前 implements 在后
      super 第一行
      living 全角：好好学习、天天向上！
      toString 要 super + job + setJob
      组合不是 extends
```

---

# 三、编程题（2 道）

> 纸笔写 **类 / 接口 / 方法**；`import` 可省略；需用库时考场给 **方法声明**。  
> **老师出题方式**：要求写得很细（第 1 点、第 2 点……），你要做的是 **把每一条要求翻译成 Java**，不用自己设计程序。

---

## 编程题 · 按题目要求写（知识点 + 保基本分）

### 先建立正确心态

编程题 **不是** 让你从零想逻辑，而是 **照着说明书拼代码**：

```
题目第 N 条要求  →  对应一种 Java 写法  →  写对一条得一条的分
```

基本分策略：**题目有几条，就写几个类 / 几个方法**；即使某个方法体写不完美，**类名、字段、构造、继承关系** 写对也能拿大部分分。

---

### 第一步：读题——把要求拆成四类

拿到题先 **用铅笔在题目旁标号**，通常就这四类（官方样例全覆盖）：

| 题目怎么说 | 你要写什么 | 例子 |
|------------|------------|------|
| **抽象类** X | `abstract class X { ... }` | `abstract class Person` |
| **类** X（没写抽象） | `class X { ... }` | `class Job` |
| **接口** X | `interface X { 方法声明; }` | `interface Life` |
| **类** Y **继承** X **实现** 接口 Z | `class Y extends X implements Z` | `class Student extends Person implements Life` |

另外常见 **附加要求**（出现在某一条里）：

| 题目怎么说 | 含义 | 怎么写 |
|------------|------|--------|
| 成员变量 / 字段 | 类里存数据的变量 | `private 类型 名;` |
| 构造方法 | `new` 时初始化字段 | `public 类名(参数) { this.字段 = 参数; }` |
| `toString()` | 把对象转成字符串 | `public String toString() { return "..."; }` |
| 方法 **输出** xxx | 打印固定内容 | `System.out.println("题目原文");` |
| **重写** toString | 子类重新写 toString | 加 `@Override`，用 `super.toString()` 带上父类信息 |
| **引用** 某类对象 | **组合**（has-a），不是继承 | `private Job job;` + `setJob(Job j)` |
| `abstract` 方法 | 子类 **必须实现** | 子类里写 `public void 方法名() { ... }` |

---

### 第二步：逐条知识点——官方样例怎么写

下面按 **截图题目顺序**，讲 **每条要求考什么、基本分怎么拿**。

![编程题样例：Person / Job / Life / Student](/java-exam/sample-programming.png)

---

#### 要求 1：抽象类 `Person`

> 成员变量 `String name`、`int age`；构造方法；`toString()` 返回姓名年龄信息。

**① 为什么是「抽象类」？**

- 题目写 **抽象类** → 关键字必须是 **`abstract class`**。
- 抽象类 **不能** `new Person()`，但 **可以** 被继承；适合当「人的公共模板」，具体学生由 `Student` 实现。
- **基本分**：写出 `abstract class Person` 就有结构分。

**② 成员变量怎么写？**

```java
protected String name;
protected int age;
```

- 题目给什么类型就写什么类型：`String name`、`int age`。
- 用 **`protected`** 最常见：子类 `Student` 能直接访问，又比 `public` 规范（写 `private` + getter 也行，但纸笔考试 **题目没要求就别多写**）。
- **基本分**：两个字段 **类型 + 名字** 和题目一致。

**③ 构造方法怎么写？**

```java
public Person(String name, int age) {
    this.name = name;
    this.age = age;
}
```

- 构造方法 **名字必须和类名相同**：`Person`。
- 参数列表 **和题目一致**：`(String name, int age)`。
- 参数名和字段名相同时，左边用 **`this.name`** 表示 **成员变量**，右边 `name` 是 **参数**。
- **基本分**：有构造 + 两个赋值语句。

**④ `toString()` 怎么写？**

```java
public String toString() {
    return "name=" + name + ", age=" + age;
}
```

- 返回类型 **`String`**；方法名 **`toString`**（和 Object 类一致，属于 **重写**）。
- 题目说「返回姓名年龄信息」→ 用字符串拼：`"name=" + name + ", age=" + age`。
- **不要求** 和标准库格式一模一样，**能看出 name、age 就行**。
- **基本分**：`return` 里 **同时出现 name 和 age**。

---

#### 要求 2：类 `Job`

> 成员变量 `String accountabilities`（职责描述）；构造方法；`toString()` 输出职责描述。

**① 普通类 vs 抽象类**

- 题目只写 **类**，没写抽象 → 用 **`class Job`**，**不要** 加 `abstract`。
- `Job` 和 `Person` **没有继承关系**，是 **两个独立的类**。

**② 和 Person 写法一样，换字段名即可**

```java
class Job {
    private String accountabilities;

    public Job(String accountabilities) {
        this.accountabilities = accountabilities;
    }

    public String toString() {
        return "accountabilities=" + accountabilities;
        // 或 return accountabilities;  也能拿 toString 基本分
    }
}
```

- **基本分**：字段 + 构造 + toString 三段都有。
- 题目若写「输出职责描述」，toString 的 return 里 **带上 accountabilities** 即可。

---

#### 要求 3：接口 `Life`

> 包含方法 `living()`。

**① 接口是什么？**

- 接口 = **只规定「能做什么」**，不管 **怎么做**。
- 写法：**只有方法声明，没有方法体**（没有 `{ ... }` 实现）。

```java
interface Life {
    void living();
}
```

**② 常见错误**

```java
// ❌ 错：接口里不能写实现
interface Life {
    void living() {
        System.out.println("...");
    }
}

// ❌ 错：漏写 void
interface Life {
    living();
}
```

- **基本分**：`interface Life` + `void living();` 两行。

---

#### 要求 4：类 `Student`（分值最高，分条拆）

> 继承 `Person`、实现 `Life`；`living()` 输出「好好学习、天天向上！」；字段 `school`、`id`、`Job job`；构造；重写 `toString` 含 **全部** 成员；`setJob(Job job)`。

**① 继承 + 实现——类头怎么写？**

```java
class Student extends Person implements Life {
```

| 关键字 | 含义 |
|--------|------|
| `extends Person` | **is-a**：学生 **是一种** 人，继承 name、age |
| `implements Life` | **can-do**：学生 **具备** 生活能力，必须写 `living()` |

- **顺序固定**：`extends` 在前，`implements` 在后。
- Java **单继承**：只能 `extends` 一个类；接口可以 **多个**：`implements A, B`。

**② 子类自己的字段**

```java
private String school;
private long id;
private Job job;
```

- 题目说 **long id** → 类型写 **`long`**，不要写成 `int`。
- **`Job job`**：表示学生 **有一个** 工作对象 → 这叫 **组合（has-a）**。
  - ✅ `private Job job;` —— 学生 **持有** Job
  - ❌ `class Student extends Job` —— 错，学生不是 Job 的子类

**③ 构造方法 + `super`（必考）**

```java
public Student(String name, int age, String school, long id) {
    super(name, age);
    this.school = school;
    this.id = id;
}
```

**为什么要有 `super(name, age)`？**

- 父类 `Person` **没有无参构造**，只有 `Person(String name, int age)`。
- 创建 `Student` 时，必须先 **帮父类初始化 name、age** → 子类构造 **第一行** 写 `super(name, age)`。
- `school`、`id` 是子类自己的，用 `this.school = school` 赋值。
- **基本分**：有 `super(name, age)` 且参数和父类构造 **一致**。

**④ 实现接口方法 `living()`**

```java
@Override
public void living() {
    System.out.println("好好学习、天天向上！");
}
```

- **实现接口** = 给出方法 **具体 body**。
- 题目写 **输出** → 用 **`System.out.println`**。
- 字符串 **从题目原样抄写**（全角 **`！`**、顿号 **`、`**）。
- **基本分**：方法名 `living`、无参、`void`、println 里字符串对。

**⑤ `setJob(Job job)`——题目明确要求就要写**

```java
public void setJob(Job job) {
    this.job = job;
}
```

- 题目说「为 job 赋值」→ 提供 **setter** 即可，**不要求** getter。
- 参数类型 **`Job`** 和字段类型一致。
- **基本分**：方法名 `setJob`、参数 `Job job`、给 `this.job` 赋值。

**⑥ 重写 `toString()`——含「全部成员变量」**

```java
@Override
public String toString() {
    return super.toString() + ", school=" + school + ", id=" + id + ", job=" + job;
}
```

**「全部成员」包括什么？**

- **继承来的**：name、age → 用 **`super.toString()`** 带上（不要重复写 name、age 赋值逻辑）。
- **自己的**：school、id、job → 字符串里都要有。
- `job` 是对象，拼接时会自动调 **`Job.toString()`**。

**基本分**：return 里 **school、id、job 三个都出现** + 用了 `super.toString()`。

---

### 第三步：编程题全能考点手册（按课件 · 按题目用语）

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

---

## 官方样例题（必做 · 只写输出）

![读程题样例：Test2](/java-exam/sample-read-code.png)

**📖 相关知识点**

- 考场代码 **一定能运行**；样例 PDF 里若写了 `Test3` 是印刷笔误，按 **`Test2`** 理解。
- **变量遮蔽**：方法里 `int y = b` 是 **局部 y**，与成员 y 同名；裸写 `y` 指局部，`this.y` 指成员。
- **toString()**：`println(对象)` 会自动调 `toString()`。

**问：写出运行结果（每行一条输出）**

```java
public class Test2 {
    private int x = 1;
    private int y = 1;

    public void changeState(int a, int b) {
        x = a;
        int y = b;
        this.y = 8;
        System.out.println("x=" + x + "; y=" + y);
    }

    public String toString() {
        return "x = " + x + "; y = " + y;
    }

    public static void main(String[] args) {
        Test2 t2 = new Test2();
        System.out.println(t2);
        t2.changeState(10, 9);
        System.out.println(t2);
    }
}
```

**输出结果**：
```
x = 1; y = 1
x=10; y=9
x = 10; y = 8
```

**逐步分析**：
1. `println(t2)` → toString → `x = 1; y = 1`  
2. `changeState(10,9)`：成员 x→10；局部 y=9 打印 `x=10; y=9`；**this.y**→8  
3. 再 println(t2) → 成员 x=10, y=8  

---

## A 组 · 作用域与成员（4 题 · 综合）

### 读程 A1

**📖 相关知识点**

- 参数也是 **局部变量**，与成员同名时 **遮蔽成员**。
- 无 `this.` 时改的是 **局部/参数**；`this.n` 改 **成员**。
- 多个方法连续改同一成员，要 **按调用顺序累加**。

**问：写出运行结果**

```java
public class Mask1 {
    int n = 0;
    void bump() { n++; }
    void f(int n) {
        n = 10;
        bump();
        System.out.println(n);
        System.out.println(this.n);
    }
    public static void main(String[] args) {
        Mask1 o = new Mask1();
        o.f(5);
        o.bump();
        System.out.println(o.n);
    }
}
```

**输出结果**：
```
10
1
2
```

**分析**：`f(5)` 里局部 n=10 打印；`bump()` 使成员 n=1；`this.n` 打印 1；main 里再 bump → n=2。

---

### 读程 A2

**📖 相关知识点**

- 课件 **UnmaskField** 加长版：两次改字段 + 中间 print。
- 每次进方法都要 **分开看** 局部变量与 `this.`。

**问：写出运行结果**

```java
public class Mask2 {
    private int x = 1, y = 1;
    public void change(int a, int b) {
        x = a;
        int y = b;
        this.y = 8;
        System.out.println("x=" + x + "; y=" + y);
    }
    public void show() {
        System.out.println("x=" + x + "; y=" + y);
    }
    public static void main(String[] args) {
        Mask2 m = new Mask2();
        m.show();
        m.change(10, 9);
        m.show();
        m.change(3, 4);
        m.show();
    }
}
```

**输出结果**：
```
x=1; y=1
x=10; y=9
x=10; y=8
x=3; y=4
x=3; y=8
```

**分析**：每次 `change` 第三行 print 的是 **局部 y**；`show()` 打印 **成员**；第二次 change 后成员 x=3, y=8。

---

### 读程 A3

**📖 相关知识点**

- **static 变量** 全类共享；**实例变量** 每个对象一份。
- 通过对象访问 static 字段合法，但改的是 **同一份** static。

**问：写出运行结果**

```java
public class StaticInst {
    static int sx = 1;
    int ix = 10;
    public static void main(String[] args) {
        StaticInst a = new StaticInst();
        StaticInst b = new StaticInst();
        a.sx = 2;
        b.ix = 20;
        a.ix = 15;
        System.out.println(a.sx + " " + b.sx);
        System.out.println(a.ix + " " + b.ix);
        System.out.println(StaticInst.sx);
    }
}
```

**输出结果**：
```
2 2
15 20
2
```

---

### 读程 A4

**📖 相关知识点**

- 方法 **重载**：根据 **实参类型** 选方法。
- 重载与成员变量无关，别被同名变量干扰。

**问：写出运行结果**

```java
public class OverPrint {
    int v = 1;
    void p(int x) { System.out.print("A" + x); }
    void p(long x) { System.out.print("B" + x); }
    void p(Integer x) { System.out.print("C" + x); }
    public static void main(String[] args) {
        OverPrint o = new OverPrint();
        o.p(1);
        o.p(1L);
        o.p(Integer.valueOf(1));
        System.out.println();
        System.out.println(o.v);
    }
}
```

**输出结果**：
```
A1B1C1
1
```

**分析**：`1`→int→A；`1L`→long→B；`Integer.valueOf(1)`→C。

---

## B 组 · String / 包装类（4 题 · 综合）

### 读程 B1

**📖 相关知识点**

- String **不可变**；`+` 在循环里每次产生 **新对象**。
- `equals` 比内容；`==` 比是否为 **同一对象**。

**问：写出运行结果**

```java
public class StrLoop {
    public static void main(String[] args) {
        String s = "";
        for (int i = 0; i < 3; i++) {
            s = s + i;
        }
        String t = "012";
        System.out.println(s.equals(t));
        System.out.println(s == t);
        System.out.println(s);
    }
}
```

**输出结果**：
```
true
false
012
```

---

### 读程 B2

**📖 相关知识点**

- 字面量、`+` 常量折叠、**new String** 与常量池。
- 先 `==` 再 `equals`，顺序别漏。

**问：写出运行结果**

```java
public class StrPool {
    public static void main(String[] args) {
        String a = "java";
        String b = "ja" + "va";
        String c = new String("java");
        String d = c.intern();
        System.out.println(a == b);
        System.out.println(a == c);
        System.out.println(a == d);
        System.out.println(c == d);
    }
}
```

**输出结果**：
```
true
false
true
false
```

**分析**：`intern()` 把 c 的内容放入/指向常量池，d 与 a 同一对象；c 仍是堆上原对象。

---

### 读程 B3

**📖 相关知识点**

- `substring(begin,end)` **左闭右开**；`indexOf` 返回首次下标。
- **`+` 结合性**：从左到右，遇 String 变连接。

**问：写出运行结果**

```java
public class StrMix {
    public static void main(String[] args) {
        String s = "abcdef";
        System.out.println(s.substring(1, 4));
        System.out.println(s.indexOf("cd"));
        System.out.println("" + 1 + 2 + 3);
        System.out.println(1 + 2 + 3 + "");
        System.out.println("Java".replace('a', 'o'));
    }
}
```

**输出结果**：
```
bcd
2
123
6
Jovo
```

---

### 读程 B4

**📖 相关知识点**

- **Integer 缓存** -128～127；超出则新对象。
- **自动拆箱** 参与 `+` 时按 int 算。

**问：写出运行结果**

```java
public class Wrap {
    public static void main(String[] args) {
        Integer a = 127, b = 127;
        Integer c = 128, d = 128;
        System.out.println(a == b);
        System.out.println(c == d);
        System.out.println(c.equals(d));
        System.out.println(a + b);
        System.out.println(Double.isNaN(0.0 / 0.0));
    }
}
```

**输出结果**：
```
true
false
true
254
true
```

---

## C 组 · 继承与多态（5 题 · 高频难点）

### 读程 C1

**📖 相关知识点**

- **实例方法**：运行时 **动态绑定**，看 **实际对象类型**。
- **static 方法**：看 **引用声明类型**，没有多态。

**问：写出运行结果**

```java
class Base {
    static void sf() { System.out.print("Sb"); }
    void im() { System.out.print("Ib"); }
}
class Derived extends Base {
    static void sf() { System.out.print("Sd"); }
    void im() { System.out.print("Id"); }
}
public class Poly1 {
    public static void main(String[] args) {
        Base r = new Derived();
        r.sf();
        r.im();
        System.out.println();
        r = new Base();
        r.sf();
        r.im();
    }
}
```

**输出结果**：
```
SbId
SbIb
```

---

### 读程 C2

**📖 相关知识点**

- 课件 **PrivOverride**：子类 **不能** 用 public 方法「覆盖」父类 **private** 方法；父类 private 方法不参与多态。
- 引用类型为父类时，调 private 方法 **编译通过**，执行 **父类版本**。

**问：写出运行结果**

```java
public class PrivOverride {
    private void f() { System.out.println("parent"); }
    public static void main(String[] args) {
        PrivOverride p = new PrivChild();
        p.f();
        new PrivChild().f();
    }
}
class PrivChild extends PrivOverride {
    public void f() { System.out.println("child"); }
}
```

**输出结果**：
```
parent
child
```

**分析**：`main` 在 **声明 private f 的类内部**，`p.f()` 调的是 **父类 private 方法**（子类 public f **不算重写**）；`new PrivChild().f()` 在子类上下文中调 **子类自己的 f**。

---

### 读程 C3

**📖 相关知识点**

- **构造顺序**：创建子类 → 父类构造 → 子类构造。
- 父类构造里若调 **可被重写** 的实例方法，可能跑到 **子类尚未初始化完** 的版本（读程常考 print 顺序）。

**问：写出运行结果**

```java
class Animal {
    Animal() {
        System.out.print("A");
        show();
    }
    void show() { System.out.print("a"); }
}
class Dog extends Animal {
    int age = 10;
    Dog() { System.out.print("D"); }
    void show() { System.out.print("d" + age); }
}
public class InitOrder {
    public static void main(String[] args) {
        new Dog();
        System.out.println();
    }
}
```

**输出结果**：
```
Ad0D
```

**分析**：父构造调 `show()` 时已动态绑定到 Dog，但 **age 尚未初始化**（默认 0）→ `d0`；再 D。

---

### 读程 C4

**📖 相关知识点**

- 课件 **static 初始化块 + 继承**：先父 static → 子 static → 父构造 → 子构造。
- **static 块** 在类 **首次加载** 时执行一次。

**问：写出运行结果**

```java
class T1 {
    static int s1 = 1;
    static { System.out.print("T1s"); }
    T1() { System.out.print("T1c"); }
}
class T2 extends T1 {
    static int s2 = 2;
    static { System.out.print("T2s"); }
    T2() { System.out.print("T2c"); }
}
public class StaticInit {
    public static void main(String[] args) {
        new T2();
        new T2();
    }
}
```

**输出结果**：
```
T1sT2sT1cT2cT1cT2c
```

**分析**：static 块 **只执行一次**；第二次 new 只有构造 `T1cT2c`。

---

### 读程 C5

**📖 相关知识点**

- 数组、引用 **赋值共享**；通过任一引用改元素，另一引用可见。
- **值传递**：传引用副本，改元素有效，换引用无效。

**问：写出运行结果**

```java
public class ArrRef {
    static void change(int[] a, int x) {
        a[0] = 99;
        a = new int[] { 1 };
        x = 100;
    }
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 };
        int k = 5;
        change(arr, k);
        System.out.println(arr[0] + " " + arr.length);
        System.out.println(k);
    }
}
```

**输出结果**：
```
99 3
5
```

---

## D 组 · static / final / 重载（3 题）

### 读程 D1

**📖 相关知识点**

- **static 计数**：构造每执行一次 count++。
- static 属于类，不随对象销毁。

**问：写出运行结果**

```java
public class Count {
    static int n = 0;
    Count() { n++; }
    static void reset() { n = 0; }
    public static void main(String[] args) {
        new Count();
        new Count();
        System.out.println(n);
        reset();
        new Count();
        System.out.println(n);
    }
}
```

**输出结果**：
```
2
1
```

---

### 读程 D2

**📖 相关知识点**

- **final 引用**：不能改 **指向**；但引用指向的 **对象内容** 仍可改（如数组元素、StringBuilder）。

**问：写出运行结果**

```java
public class FinalRef {
    public static void main(String[] args) {
        final int[] a = { 1, 2 };
        a[0] = 9;
        final StringBuilder sb = new StringBuilder("Hi");
        sb.append("!");
        System.out.println(a[0] + " " + a[1]);
        System.out.println(sb);
    }
}
```

**输出结果**：
```
9 2
Hi!
```

---

### 读程 D3

**📖 相关知识点**

- **重写** 要求签名相同；子类返回类型可以是 **协变** 类型（本题不涉及）。
- 多态调用 **实际对象** 的重写方法。

**问：写出运行结果**

```java
class Shape {
    void draw() { System.out.print("S"); }
}
class Circle extends Shape {
    void draw() { System.out.print("C"); }
    void radius() { System.out.print("r"); }
}
public class ShapeTest {
    public static void main(String[] args) {
        Shape s = new Circle();
        s.draw();
        Circle c = (Circle) s;
        c.draw();
        c.radius();
    }
}
```

**输出结果**：
```
CCr
```

---

## E 组 · 集合（4 题 · 课件风格）

### 读程 E1

**📖 相关知识点**

- 课件 **UseArrayList**：add、**insert**、set、remove 混合。
- `remove(int)` 是 **下标**；删后 size 变，下标要重新想。

**问：写出运行结果**

```java
import java.util.*;
public class ListOps {
    public static void main(String[] args) {
        List<String> L = new ArrayList<>();
        L.add("86");
        L.add("98");
        L.add(1, "99");
        for (int i = 0; i < L.size(); i++) {
            System.out.print(L.get(i) + " ");
        }
        L.set(1, "77");
        L.remove(0);
        System.out.println();
        System.out.println(L);
    }
}
```

**输出结果**：
```
86 99 98 
[77, 98]
```

**分析**：插入后 [86,99,98]；set(1,"77")→[86,77,98]；remove(0) 删 86→[77,98]。

---

### 读程 E2

**📖 相关知识点**

- `remove(1)` → 下标 1；`remove(Integer.valueOf(1))` → 删 **值为 1** 的元素。
- 两种 remove **结果完全不同**，读程必考。

**问：写出运行结果**

```java
import java.util.*;
public class RemoveTrap {
    public static void main(String[] args) {
        List<Integer> L = new ArrayList<>(Arrays.asList(1, 2, 3, 2));
        L.remove(1);
        System.out.println(L);
        L.remove(Integer.valueOf(2));
        System.out.println(L);
    }
}
```

**输出结果**：
```
[1, 3, 2]
[1, 3]
```

---

### 读程 E3

**📖 相关知识点**

- **HashMap**：同 key 的 put **覆盖** value；size 不变。
- `get` 不存在返回 **null**（本题都有 key）。

**问：写出运行结果**

```java
import java.util.*;
public class MapOps {
    public static void main(String[] args) {
        Map<String, Integer> m = new HashMap<>();
        m.put("a", 1);
        m.put("b", 2);
        m.put("a", 3);
        System.out.println(m.get("a"));
        System.out.println(m.get("c"));
        System.out.println(m.size());
        m.remove("b");
        System.out.println(m.containsKey("b"));
        System.out.println(m);
    }
}
```

**输出结果**：
```
3
null
2
false
{a=3}
```

---

### 读程 E4

**📖 相关知识点**

- **HashSet** 不重复；`add` 返回 boolean 表示是否 **新加进**。
- 课件 **FindDups** 思路：重复 add 失败。

**问：写出运行结果**

```java
import java.util.*;
public class SetOps {
    public static void main(String[] args) {
        Set<String> s = new HashSet<>();
        System.out.print(s.add("A") + " ");
        System.out.print(s.add("A") + " ");
        System.out.print(s.add("B") + " ");
        System.out.println(s.size());
        System.out.println(s);
    }
}
```

**输出结果**：
```
true false true 2
[A, B]
```

（Set 的 toString 顺序 **不保证**，考场一般只考 size 或 true/false 行。）

---

## F 组 · 异常（3 题 · 课件风格）

### 读程 F1

**📖 相关知识点**

- try 里 **异常点之后** 的语句 **不执行**；进 catch；**finally 几乎总执行**。
- 课件常见：`1/0` 跳过中间 print。

**问：写出运行结果**

```java
public class Ex1 {
    public static void main(String[] args) {
        System.out.print("1");
        try {
            System.out.print("2");
            int x = 10 / 0;
            System.out.print("3");
        } catch (ArithmeticException e) {
            System.out.print("4");
        } finally {
            System.out.print("5");
        }
        System.out.print("6");
    }
}
```

**输出结果**：
```
12456
```

---

### 读程 F2

**📖 相关知识点**

- 课件 **greetings 循环** 简化版：catch 住 **数组越界** 后 break，避免死循环。
- 每轮 **finally 都执行**。

**问：写出运行结果**

```java
public class ExLoop {
    public static void main(String[] args) {
        String[] g = { "A", "B", "C" };
        int i = 0;
        while (i < 4) {
            try {
                System.out.print(g[i]);
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.print("X");
                break;
            } finally {
                System.out.print("F");
            }
            i++;
        }
        System.out.print("E");
    }
}
```

**输出结果**：
```
AFBFCFXFE
```

**逐步分析**：
- i=0：`A` + finally `F` → `AF`  
- i=1：`B` + `F` → `BF`  
- i=2：`C` + `F` → `CF`  
- i=3：越界 → `X` + finally `F` → `XF`；break  
- 最后 `E`  

---

### 读程 F3

**📖 相关知识点**

- **return 之前** 仍执行 finally。
- finally 里若有 return 会覆盖 try 的 return（本题 finally 只 print）。

**问：写出运行结果**

```java
public class ExFinally {
    static int f() {
        try {
            return 1;
        } finally {
            System.out.print("F");
        }
    }
    public static void main(String[] args) {
        System.out.print(f());
        System.out.print(f());
    }
}
```

**输出结果**：
```
F1F1
```

---

## G 组 · 多线程（3 题）

### 读程 G1

**📖 相关知识点**

- **`run()`** 普通调用，**不启新线程**；**`start()`** 才新线程。
- 本题全在 main 线程，顺序确定。

**问：写出运行结果**

```java
public class ThreadRun {
    public static void main(String[] args) {
        Thread t = new Thread(() -> System.out.print("T"));
        t.run();
        t.run();
        System.out.print("M");
    }
}
```

**输出结果**：
```
TTM
```

---

### 读程 G2

**📖 相关知识点**

- **`start()` + `join()`**：main 等子线程 **跑完** 再往下。
- 无 join 时，打印顺序可能 **不确定**（考场若给了 join 就 **确定**）。

**问：写出运行结果**

```java
public class ThreadJoin {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception {
        Thread t = new Thread(() -> sb.append("B"));
        t.start();
        t.join();
        sb.append("A");
        System.out.println(sb);
    }
}
```

**输出结果**：
```
BA
```

---

### 读程 G3

**📖 相关知识点**

- **synchronized**：同一把锁 **互斥**；本题顺序固定因 main 等 t1、t2 都 join。

**问：写出运行结果**

```java
public class SyncDemo {
    static int n = 0;
    static final Object lock = new Object();
    static void add() {
        synchronized (lock) {
            n++;
        }
    }
    public static void main(String[] args) throws Exception {
        Thread t1 = new Thread(() -> { add(); add(); });
        Thread t2 = new Thread(() -> { add(); });
        t1.start(); t2.start();
        t1.join(); t2.join();
        System.out.println(n);
    }
}
```

**输出结果**：
```
3
```

---

## H 组 · switch / 数组 / 循环（4 题）

### 读程 H1

**📖 相关知识点**

- **switch 贯穿**：case 无 **break** 则 **继续执行** 下一 case。
- 考场常考 **故意不写 break**。

**问：写出运行结果**

```java
public class Sw {
    public static void main(String[] args) {
        int n = 2;
        switch (n) {
            case 1: System.out.print("1");
            case 2: System.out.print("2");
            case 3: System.out.print("3"); break;
            default: System.out.print("d");
        }
        System.out.print("!");
    }
}
```

**输出结果**：
```
23!
```

---

### 读程 H2

**📖 相关知识点**

- **二维数组**：`length` 是 **行数**；每行是 **一维数组**，长度可不同。
- `a[i][j]` 先选行再选列。

**问：写出运行结果**

```java
public class Arr2D {
    public static void main(String[] args) {
        int[][] a = { { 1, 2 }, { 3 }, { 4, 5, 6 } };
        System.out.print(a.length + " ");
        System.out.print(a[1].length + " ");
        System.out.print(a[2][1] + " ");
        int sum = 0;
        for (int[] row : a) {
            sum += row[0];
        }
        System.out.print(sum);
    }
}
```

**输出结果**：
```
3 1 5 8
```

**分析**：三行；第二行长 1；a[2][1]=5；各行第 0 列 1+3+4=8。

---

### 读程 H3

**📖 相关知识点**

- **`if (b = true)`** 是 **赋值**，不是 `==`；条件为 true。
- **短路运算** `&&` / `||`：左侧能定结果则 **不评估** 右侧。

**问：写出运行结果**

```java
public class Logic {
    public static void main(String[] args) {
        int x = 0;
        if (x++ == 0) System.out.print("A");
        System.out.print(x + " ");
        boolean ok = false;
        if (ok = true) System.out.print("B");
        if (false && (++x > 0)) System.out.print("C");
        System.out.print(x);
    }
}
```

**输出结果**：
```
A1 B1
```

---

### 读程 H4

**📖 相关知识点**

- **for 循环 + continue/break**；嵌套 loop 要 **分层手算**。
- `print` 无换行，一行粘在一起。

**问：写出运行结果**

```java
public class LoopNest {
    public static void main(String[] args) {
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == j) continue;
                System.out.print(i + "" + j + " ");
            }
        }
    }
}
```

**输出结果**：
```
12 13 21 23 31 32 
```

（末尾空格可有可无，看阅卷是否抠格式。）

---

## 读程题自测索引（25 题 · 只写输出）

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

> **冲刺建议**：考场 **5～7 道** 读程，难度接近 C/E/F 组；每天 **手算 8 道** 不看书，错题回到 [按课件详讲](#按课件逐章要点详讲)。

---

# ★ 期末抢分秘籍

> 老师原话：**只有三种题型**——简答 4～5、读程 5～7、编程 2；**要用库会给方法声明**，不用背 API 签名。  
> 编程题就是 **[官方样例截图](/java-exam/sample-programming.png)** 那种：**抽象类 + 普通类 + 接口 + 子类**，纸笔写完整类定义。

## 考场时间怎么切（90 分钟卷参考）

| 阶段 | 时间 | 做什么 |
|------|------|--------|
| ① 编程题 | **25～30 min** | 先拿大分；Person/Student 型 **默写骨架** |
| ② 读程题 | **25 min** | 只写输出；每题 3～4 min，不确定也写一版 |
| ③ 简答题 | **25 min** | 概念分点写满；**多线程 + GUI 各至少 1 道** |
| ④ 检查 | **10 min** | 编程：`super`、接口、`living()` 标点；读程：漏行 |

**原则**：编程 **先写**——会就是 15～20 分一道，不会后面慌；简答 **写满** 就有分，空着必 0。

---

## 简答题 · 3 条抢分口诀

1. **分点 + 关键词**：阅卷按点给分。看到「线程同步」必写 **`synchronized`、对象锁、临界区**；看到 GUI 必写 **AWT/Swing、Listener/Adapter、EDT**。
2. **对比题用表格思维**：`==` vs `equals`、List/Set/Map、受检/非受检异常——写 **3 行对比** 比一大段废话得分高。
3. **最后一行总结句**：例如「Java 只有值传递，引用传的是地址的副本」。一句话 1 分，不亏。

---

## 读程题 · 3 条抢分口诀

1. **只填输出**——代码一定能跑；别在卷子上写「不能编译」。
2. **`print` vs `println`**：粘在一起还是换行，占一半错题；写完 **数行数** 是否和 `println` 次数一致。
3. **拿不准也写**：多线程无 `join` 时顺序可能乱，但 **有 join / synchronized** 的题顺序 **确定**，必须算准；实在不会写「输出顺序不确定」比空白强（本题若确定则别写这句）。

---

## 编程题 · 抢分核心（Person / Job / Life / Student 型）

![编程题样例：Person / Job / Life / Student](/java-exam/sample-programming.png)

老师这种题 **20 分一道、考 2 道**，本质是 **OOP 建模默写**：照着题目 **逐条翻译** 成 Java，不需要算法、不需要 main。

### 第一步：30 秒圈得分点（写在草稿角）

拿到题先在边上打勾，**写一条算一条**：

| 题目里的词 | 你要写的 Java | 几分级 |
|------------|---------------|--------|
| 抽象类 X | `abstract class X { ... }` | 必写 |
| 成员变量 | `private/protected 类型 名;` | 每个字段 1 分 |
| 构造方法 | `public X(参数) { this.x = x; }` | 2～3 分 |
| `toString()` | `return "name=" + name + ...` | 2 分 |
| 接口 Y | `interface Y { void method(); }` **无方法体** | 2 分 |
| 继承 + 实现 | `class Z extends X implements Y` | **先 extends 后 implements** |
| 调用父构造 | `super(...)` 在子类构造 **第一行** | 漏了整题构造 0 分 |
| 组合（has-a） | `private Job job;` + `setJob(Job job)` | 常漏 setJob |
| 接口方法实现 | `public void living() { System.out.println("…"); }` | 字符串 **一字不差** |
| 重写 toString | `super.toString() + ", school=" + ...` | 要含 **全部** 字段含 job |

### 第二步：默写顺序（固定 4 步，闭卷练到 12 分钟内）

```
1. abstract class Person     ← 最简单，先写稳
2. class Job                 ← 独立类，复制 Person 改字段
3. interface Life            ← 两行搞定
4. class Student             ← 分值最高，留最多时间
```

**Student 内部顺序（别乱）**：

```
extends Person implements Life
→ 字段 school, id, job
→ 构造 + super(name, age)
→ living() 固定句
→ setJob()
→ toString() 含 super.toString()
```

### 第三步：最小保分版（时间不够 / 某块忘了）

即使写不完，按下面写也能 **拿到 60%～70%**：

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
        return accountabilities;   // 忘了字段名至少 return 参数
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
        System.out.println("好好学习、天天向上！");
    }

    public void setJob(Job job) { this.job = job; }

    public String toString() {
        return super.toString() + ", school=" + school + ", id=" + id + ", job=" + job;
    }
}
```

### 第四步：致命扣分 · 考前红笔标

| 错误 | 后果 |
|------|------|
| `implements extends` 顺序反了 | 语法错，Student 整段 0 分 |
| 子类构造 **没有** `super(name, age)` | 父类字段未初始化，构造 0 分 |
| 接口里写了 `{ System.out... }` | 接口不能带实现（除非 default，本课一般不考） |
| `living()` 字符串和题目 **差一个标点** | 该方法 0 分（全角 `！` 看清楚） |
| 有 `Job job` 但 **没写 setJob** | 组合关系不完整，扣 2～4 分 |
| `toString` 只写字类字段，**没 super** | 父类 name/age 缺失，扣一半 |
| 把 `Job` 写成 `extends Job` | 组合变继承，概念错 |

### 第五步：`living()` 和 toString 格式 · 一字抄题

**官方固定句（截图原文）**：

```java
System.out.println("好好学习、天天向上！");
```

- 用的是 **中文顿号 `、`** 和 **全角叹号 `！`**
- 建议考前 **手抄三遍**，别用英文 `!`

**toString 推荐格式**（字段全、阅卷好认）：

```java
return super.toString() + ", school=" + school + ", id=" + id + ", job=" + job;
```

`job` 会自动调 `Job.toString()`，不用手动拼 `accountabilities`。

### 第六步：第二道编程题可能考什么

第一道往往是 **Person/Student 型**；第二道常见变式（仍纸笔写类/方法）：

| 变式 | 抢分写法 |
|------|----------|
| 抽象类加 `abstract void study();` | Student 里 **必须** `public void study() { ... }` |
| `Job` 改成接口 `Workable` | `implements Life, Workable`（逗号分隔，**先 extends 后 implements**） |
| 加 `equals` 只比 `id` | `if (!(o instanceof Student)) return false;` + `(Student)o` + `return id == s.id;` |
| 文件方法「去空行复制」 | 直接默写 [类型 3 骨架](#类型-3文件读写方法ppt-第三章--练习四) |
| 集合「统计单词频次」 | 默写 [类型 4 骨架](#类型-4集合方法ppt-第三章--练习三) |
| GUI 补监听器 | 默写 [类型 5 骨架](#类型-5gui-监听器补全ppt-gui-章) |
| 线程类 `extends Thread` | 默写 [类型 6 骨架](#类型-6线程类ppt-多线程章) |

**第二道若是方法题**：题目会给 `FileReader` / `HashMap` 等声明 → **只写方法体 + throws**，别纠结 import。

### 编程题 · 纸笔书写技巧

- **类与类之间空一行**，阅卷一眼四个类齐不齐。
- 字段先 **竖着写全**，再写构造，避免漏 `id` 或 `job`。
- 接口方法、实现类 public 方法：行首 **`public`** 别漏（实现接口时 public 可省略但写上更稳）。
- 写错一行 **划单线改**，别涂黑团；构造参数名和字段同名时用 **`this.`**。
- **不需要写 `main`**，除非题目明确要求。

### 编程题 · 15 分钟倒计时演练

| 分钟 | 任务 |
|------|------|
| 0～1 | 圈 Person/Job/Life/Student 得分点 |
| 1～4 | 写完 Person + Job + Life |
| 4～12 | 写 Student（super、living、setJob、toString） |
| 12～14 | 对照题目逐条打勾 |
| 14～15 | 补漏的 `@Override` 或分号 |

---

## 一页纸速记卡（进考场前背）

```
简答：多线程 + GUI 必考；分点写；对比题三行表
读程：只写输出；println 数行数；String/集合/多态手算
编程：Person→Job→Life→Student
      extends 在前 implements 在后
      super 第一行
      living 全角：好好学习、天天向上！
      toString 要 super + job + setJob
      组合不是 extends
```

---

# 三、编程题（2 道）

> 纸笔写 **类 / 接口 / 方法**；`import` 可省略；需用库时考场给 **方法声明**。  
> **老师出题方式**：要求写得很细（第 1 点、第 2 点……），你要做的是 **把每一条要求翻译成 Java**，不用自己设计程序。

---

## 编程题 · 按题目要求写（知识点 + 保基本分）

### 先建立正确心态

编程题 **不是** 让你从零想逻辑，而是 **照着说明书拼代码**：

```
题目第 N 条要求  →  对应一种 Java 写法  →  写对一条得一条的分
```

基本分策略：**题目有几条，就写几个类 / 几个方法**；即使某个方法体写不完美，**类名、字段、构造、继承关系** 写对也能拿大部分分。

---

### 第一步：读题——把要求拆成四类

拿到题先 **用铅笔在题目旁标号**，通常就这四类（官方样例全覆盖）：

| 题目怎么说 | 你要写什么 | 例子 |
|------------|------------|------|
| **抽象类** X | `abstract class X { ... }` | `abstract class Person` |
| **类** X（没写抽象） | `class X { ... }` | `class Job` |
| **接口** X | `interface X { 方法声明; }` | `interface Life` |
| **类** Y **继承** X **实现** 接口 Z | `class Y extends X implements Z` | `class Student extends Person implements Life` |

另外常见 **附加要求**（出现在某一条里）：

| 题目怎么说 | 含义 | 怎么写 |
|------------|------|--------|
| 成员变量 / 字段 | 类里存数据的变量 | `private 类型 名;` |
| 构造方法 | `new` 时初始化字段 | `public 类名(参数) { this.字段 = 参数; }` |
| `toString()` | 把对象转成字符串 | `public String toString() { return "..."; }` |
| 方法 **输出** xxx | 打印固定内容 | `System.out.println("题目原文");` |
| **重写** toString | 子类重新写 toString | 加 `@Override`，用 `super.toString()` 带上父类信息 |
| **引用** 某类对象 | **组合**（has-a），不是继承 | `private Job job;` + `setJob(Job j)` |
| `abstract` 方法 | 子类 **必须实现** | 子类里写 `public void 方法名() { ... }` |

---

### 第二步：逐条知识点——官方样例怎么写

下面按 **截图题目顺序**，讲 **每条要求考什么、基本分怎么拿**。

![编程题样例：Person / Job / Life / Student](/java-exam/sample-programming.png)

---

#### 要求 1：抽象类 `Person`

> 成员变量 `String name`、`int age`；构造方法；`toString()` 返回姓名年龄信息。

**① 为什么是「抽象类」？**

- 题目写 **抽象类** → 关键字必须是 **`abstract class`**。
- 抽象类 **不能** `new Person()`，但 **可以** 被继承；适合当「人的公共模板」，具体学生由 `Student` 实现。
- **基本分**：写出 `abstract class Person` 就有结构分。

**② 成员变量怎么写？**

```java
protected String name;
protected int age;
```

- 题目给什么类型就写什么类型：`String name`、`int age`。
- 用 **`protected`** 最常见：子类 `Student` 能直接访问，又比 `public` 规范（写 `private` + getter 也行，但纸笔考试 **题目没要求就别多写**）。
- **基本分**：两个字段 **类型 + 名字** 和题目一致。

**③ 构造方法怎么写？**

```java
public Person(String name, int age) {
    this.name = name;
    this.age = age;
}
```

- 构造方法 **名字必须和类名相同**：`Person`。
- 参数列表 **和题目一致**：`(String name, int age)`。
- 参数名和字段名相同时，左边用 **`this.name`** 表示 **成员变量**，右边 `name` 是 **参数**。
- **基本分**：有构造 + 两个赋值语句。

**④ `toString()` 怎么写？**

```java
public String toString() {
    return "name=" + name + ", age=" + age;
}
```

- 返回类型 **`String`**；方法名 **`toString`**（和 Object 类一致，属于 **重写**）。
- 题目说「返回姓名年龄信息」→ 用字符串拼：`"name=" + name + ", age=" + age`。
- **不要求** 和标准库格式一模一样，**能看出 name、age 就行**。
- **基本分**：`return` 里 **同时出现 name 和 age**。

---

#### 要求 2：类 `Job`

> 成员变量 `String accountabilities`（职责描述）；构造方法；`toString()` 输出职责描述。

**① 普通类 vs 抽象类**

- 题目只写 **类**，没写抽象 → 用 **`class Job`**，**不要** 加 `abstract`。
- `Job` 和 `Person` **没有继承关系**，是 **两个独立的类**。

**② 和 Person 写法一样，换字段名即可**

```java
class Job {
    private String accountabilities;

    public Job(String accountabilities) {
        this.accountabilities = accountabilities;
    }

    public String toString() {
        return "accountabilities=" + accountabilities;
        // 或 return accountabilities;  也能拿 toString 基本分
    }
}
```

- **基本分**：字段 + 构造 + toString 三段都有。
- 题目若写「输出职责描述」，toString 的 return 里 **带上 accountabilities** 即可。

---

#### 要求 3：接口 `Life`

> 包含方法 `living()`。

**① 接口是什么？**

- 接口 = **只规定「能做什么」**，不管 **怎么做**。
- 写法：**只有方法声明，没有方法体**（没有 `{ ... }` 实现）。

```java
interface Life {
    void living();
}
```

**② 常见错误**

```java
// ❌ 错：接口里不能写实现
interface Life {
    void living() {
        System.out.println("...");
    }
}

// ❌ 错：漏写 void
interface Life {
    living();
}
```

- **基本分**：`interface Life` + `void living();` 两行。

---

#### 要求 4：类 `Student`（分值最高，分条拆）

> 继承 `Person`、实现 `Life`；`living()` 输出「好好学习、天天向上！」；字段 `school`、`id`、`Job job`；构造；重写 `toString` 含 **全部** 成员；`setJob(Job job)`。

**① 继承 + 实现——类头怎么写？**

```java
class Student extends Person implements Life {
```

| 关键字 | 含义 |
|--------|------|
| `extends Person` | **is-a**：学生 **是一种** 人，继承 name、age |
| `implements Life` | **can-do**：学生 **具备** 生活能力，必须写 `living()` |

- **顺序固定**：`extends` 在前，`implements` 在后。
- Java **单继承**：只能 `extends` 一个类；接口可以 **多个**：`implements A, B`。

**② 子类自己的字段**

```java
private String school;
private long id;
private Job job;
```

- 题目说 **long id** → 类型写 **`long`**，不要写成 `int`。
- **`Job job`**：表示学生 **有一个** 工作对象 → 这叫 **组合（has-a）**。
  - ✅ `private Job job;` —— 学生 **持有** Job
  - ❌ `class Student extends Job` —— 错，学生不是 Job 的子类

**③ 构造方法 + `super`（必考）**

```java
public Student(String name, int age, String school, long id) {
    super(name, age);
    this.school = school;
    this.id = id;
}
```

**为什么要有 `super(name, age)`？**

- 父类 `Person` **没有无参构造**，只有 `Person(String name, int age)`。
- 创建 `Student` 时，必须先 **帮父类初始化 name、age** → 子类构造 **第一行** 写 `super(name, age)`。
- `school`、`id` 是子类自己的，用 `this.school = school` 赋值。
- **基本分**：有 `super(name, age)` 且参数和父类构造 **一致**。

**④ 实现接口方法 `living()`**

```java
@Override
public void living() {
    System.out.println("好好学习、天天向上！");
}
```

- **实现接口** = 给出方法 **具体 body**。
- 题目写 **输出** → 用 **`System.out.println`**。
- 字符串 **从题目原样抄写**（全角 **`！`**、顿号 **`、`**）。
- **基本分**：方法名 `living`、无参、`void`、println 里字符串对。

**⑤ `setJob(Job job)`——题目明确要求就要写**

```java
public void setJob(Job job) {
    this.job = job;
}
```

- 题目说「为 job 赋值」→ 提供 **setter** 即可，**不要求** getter。
- 参数类型 **`Job`** 和字段类型一致。
- **基本分**：方法名 `setJob`、参数 `Job job`、给 `this.job` 赋值。

**⑥ 重写 `toString()`——含「全部成员变量」**

```java
@Override
public String toString() {
    return super.toString() + ", school=" + school + ", id=" + id + ", job=" + job;
}
```

**「全部成员」包括什么？**

- **继承来的**：name、age → 用 **`super.toString()`** 带上（不要重复写 name、age 赋值逻辑）。
- **自己的**：school、id、job → 字符串里都要有。
- `job` 是对象，拼接时会自动调 **`Job.toString()`**。

**基本分**：return 里 **school、id、job 三个都出现** + 用了 `super.toString()`。

---

### 第三步：题目里其他常见要求（第二道编程题）

第一道多是 **Person/Student 型**；第二道仍是 **按条写**，常见如下：

#### 要求：「抽象方法 xxx，由子类实现」

```java
// 抽象类里
abstract void study();

// 子类里
@Override
public void study() {
    System.out.println("正在学习");
}
```

- 父类 **只声明**（无方法体）；子类 **必须写 public 实现**，否则子类也要标 abstract。

#### 要求：「重写 equals，仅比较 id」

```java
@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Student)) return false;
    Student s = (Student) o;
    return this.id == s.id;
}
```

- 参数类型 **必须是 `Object`**；先 `instanceof` 再 **强转**。

#### 要求：「读文件 / 写文件 / 去空行」

题目会给 `FileReader`、`BufferedReader` 等声明 → 你写 **方法体**：

```java
try (BufferedReader br = new BufferedReader(new FileReader(路径))) {
    String line;
    while ((line = br.readLine()) != null) {
        // 按题目处理 line
    }
}
```

- **基本分**：`try-with-resources` + `readLine` 循环 + 题目要求的 if/write。

#### 要求：「用 HashMap / ArrayList 统计 / 存储」

```java
Map<String, Integer> map = new HashMap<>();
for (String w : 数组) {
    map.put(w, map.getOrDefault(w, 0) + 1);
}
```

- **基本分**：声明集合 + 循环 + `put`/`get`。

#### 要求：「为按钮添加 ActionListener」

```java
button.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        // 题目要求的动作
    }
});
```

- **基本分**：匿名内部类结构 + `@Override` + 题目里的那一行操作。

#### 要求：「定义线程类，重写 run」

```java
class MyTask extends Thread {
    @Override
    public void run() {
        // 题目要求循环 / sleep / 打印
    }
}
```

- **基本分**：`extends Thread` + `public void run()` 有方法体。

---

### 第四步：写代码的固定顺序（保基本分版）

不管题目多细，**按这个顺序写就不会漏大项**：

```
1. 读完全题，数有几个类 / 接口
2. 每个类：先字段 → 再构造 → 再其他方法
3. 有父类：子类构造第一行 super(...)
4. 有接口：实现类里每个接口方法都写 public 实现
5. 题目说 toString / equals / setXxx：单独写一个方法，别漏
6. 对照题目逐条打勾
```

**不需要写 `main`**，除非题目明确要求。

---

### 第五步：官方样例 · 对照表（写完打勾）

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
| 4 | toString 含 **全部** 成员（super + school + id + job） | ☐ |

**10 项里对 8 项 ≈ 基本分稳了**；全对 ≈ 满分。

---

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
        System.out.println("好好学习、天天向上！");
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
- [ ] `living()` 输出 **一字不错**（全角 **`！`**，顿号 **`、`**）
- [ ] `toString` 用 `super.toString()` 带父类字段  

**逐行得分说明（编程题阅卷视角）**

| 代码块 | 分值关注点 | 常见扣分 |
|--------|------------|----------|
| `abstract class Person` | 字段 protected、构造赋值 | 写成 public 字段、漏构造 |
| `class Job` | 独立类、toString | 误写成 static 内部类 |
| `interface Life` | 只有方法声明，无方法体 | 写了 `{}` 实现 |
| `Student extends Person implements Life` | 顺序：先 extends 后 implements | 反写、漏 implements |
| `super(name, age)` | 必须是构造第一行有效语句 | 用 this.name 重复赋值代替 super |
| `private Job job` + `setJob` | **组合** 关系，非继承 | 漏 setJob 导致 job 永远 null |
| `living()` | 字符串与题目 **完全一致** | 标点、空格错误 |
| `toString()` | `super.toString()` + 本类字段 + job | 漏 job 或 id |

**变式题可能改什么**

- 把 `Job` 改成接口 `Workable`，`Student implements Life, Workable`
- 增加 `equals`/`hashCode` 只比 `id`
- 增加 `abstract void study()` 由 Student 实现

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

抽象类 + 接口 + 继承 + 组合 → 见 [全能考点手册 A 组](#a-组--第四章面向对象特性编程--最高频) + [满分骨架](#满分骨架默写)

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

## 编程题自测（按全能手册）

1. **A2 官方样例**：Person / Job / Life / Student 四类（12 分钟）。  
2. **A1**：EmpInfo 或 Rectangle 普通类（字段+构造+方法）。  
3. **A3**：Shape/Rectangle 继承 + override + super。  
4. **A5**：构造重载 + this() 链。  
5. **A8**：equals 只比 id + toString。  
6. **B5～B7**：ArrayList 增删改查；HashMap 覆盖与统计；HashSet 去重。  
7. **D2**：BufferedReader 读文件去空行写出。  
8. **E1**：extends Thread + run + sleep。  
9. **F1～F2**：ActionListener 与 WindowAdapter 各默写一遍。  
10. 随机抽一道：**圈题目用语 → 查总索引表 → 写代码**。

---

# 冲刺 Checklist

**简答（4～5）**

- [ ] 多线程全套（进程/线程、同步、死锁、start vs run）
- [ ] GUI 全套（AWT/Swing、层次、Listener/Adapter、匿名内部类）
- [ ] 官方样例 `==` vs `equals`
- [ ] Infinity/NaN、enum、List/Set/Map、字节流/字符流

**读程（5～7）**

- [ ] 官方 **Test2** 三行输出（遮蔽 + this.y）
- [ ] String / 集合 / 线程 各练 2 道
- [ ] NaN、enum.ordinal()

**编程（2）**

- [ ] [抢分秘籍](#-期末抢分秘籍) 过一遍：15 分钟默写顺序 + 致命扣分表
- [ ] 官方 **Person/Job/Life/Student** 四类骨架 **12 分钟内**闭卷默写
- [ ] `living()` 手抄三遍：`好好学习、天天向上！`
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

*最后更新：2026-06-12 · **详讲版** · 笔考专版 · 课件摘自 `JAVA\课件\` 共 8 个 PPT（无 GUI 课件）· 已移除机考*
