# -*- coding: utf-8 -*-
"""Patch Java期末复习满分攻略.md: expand 简答题 + 读程题库.

After running this script, also run patch_java_read_knowledge.py to insert
📖 相关知识点 before each 读程题.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "content/posts/Java期末复习满分攻略.md"
text = MD.read_text(encoding="utf-8")

SHORT_START = "## ★ 必考专题 A：多线程（至少 1 道）"
SHORT_END = "# 二、读程题（5～7 道）"

SHORT_ANSWERS = r'''## 简答题题库（详答版 · 共 22 题）

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

- `Object` 类中 `equals` 的默认实现与 `==` 相同，也是比较引用。
- 许多 Java 类库类 **重写** 了 `equals`，改为比较 **对象内容** 是否相等。例如 `String`、`Integer` 的 `equals` 比较字符序列或数值。
- 自定义类若要用 `equals` 比较字段，必须 **正确重写** `equals(Object o)`（参数类型是 `Object`，不是本类）。

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

'''

READ_SECTION = r'''# 二、读程题（5～7 道 · 题库 30 题）

> 考场给代码 → 写 **运行结果** 或 **能否编译**。  
> 下面 **30 道** 按类型分组，每题含 **题目 → 代码 → 答案 → 逐行分析**。建议 **先遮住答案自己做**，再对照。

## 解题五步法（每题都用）

1. **先判编译**：类名、抽象方法、接口实现、访问权限  
2. **圈作用域**：成员 / 局部 / 参数；有没有 **`this.`**  
3. **盯修改**：String 是否新对象、`remove` 是下标还是值、`start()` 调了没  
4. **手算输出**：`substring` 左闭右开；`==` vs `equals`  
5. **多线程/异常**：输出顺序是否确定；异常后哪句不执行  

---

## 官方样例题（必做）

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

| 问 | 答 |
|----|-----|
| 能否编译？ | **不能**，`Test3` 不存在 |
| 若改为 `Test2 t2 = new Test2();` | 输出三行：`x = 1; y = 1` → `x=10; y=9` → `x = 10; y = 8` |

---

## A 组 · 编译与作用域（6 题）

### 读程 A1

```java
public class Scope1 {
    int x = 1;
    void f() {
        int x = 2;
        System.out.println(x);
        System.out.println(this.x);
    }
    public static void main(String[] args) {
        new Scope1().f();
    }
}
```

**问**：输出什么？

**答**：
```
2
1
```

**分析**：局部 `x=2` 遮蔽成员；`this.x` 访问成员 `1`。

---

### 读程 A2

```java
abstract class Base {}
public class TestA2 {
    public static void main(String[] args) {
        Base b = new Base();
    }
}
```

**问**：能否编译？

**答**：**不能**。抽象类 **不能实例化**。

---

### 读程 A3

```java
interface I { void f(); }
class C implements I {}
public class TestA3 {
    public static void main(String[] args) {
        new C().f();
    }
}
```

**问**：能否编译？

**答**：**不能**。`C` 未实现 `I.f()`。

---

### 读程 A4

```java
public class TestA4 {
    public static void main(String[] args) {
        int x;
        System.out.println(x);
    }
}
```

**问**：能否编译？

**答**：**不能**。局部变量 **使用前必须赋值**。

---

### 读程 A5

```java
public class TestA5 {
    static int x = 1;
    void print() { System.out.println(x); }
    public static void main(String[] args) {
        TestA5 t = new TestA5();
        t.print();
        System.out.println(x);
    }
}
```

**问**：输出什么？

**答**：
```
1
1
```

**分析**：静态变量 `x` 属于类，实例和类名访问都是 `1`。

---

### 读程 A6（PPT UnmaskField 原版）

```java
public class UnmaskField {
    private int x = 1, y = 1;
    public void changeFields(int a, int b) {
        x = a;
        int y = b;
        this.y = 8;
        System.out.println("x=" + x + "; y=" + y);
    }
    public void printFields() {
        System.out.println("x=" + x + "; y=" + y);
    }
    public static void main(String[] args) {
        UnmaskField uf = new UnmaskField();
        uf.printFields();
        uf.changeFields(10, 9);
        uf.printFields();
    }
}
```

**答**：
```
x=1; y=1
x=10; y=9
x=10; y=8
```

---

## B 组 · String / 包装类（6 题）

### 读程 B1

```java
public class TestB1 {
    public static void main(String[] args) {
        String s = "Hi";
        s.concat("!");
        System.out.println(s);
    }
}
```

**答**：`Hi`（concat 返回新串，s 未改）

---

### 读程 B2

```java
public class TestB2 {
    public static void main(String[] args) {
        String a = "ab";
        String b = "a" + "b";
        String c = new String("ab");
        System.out.println(a == b);
        System.out.println(a == c);
        System.out.println(a.equals(c));
    }
}
```

**答**：
```
true
false
true
```

---

### 读程 B3

```java
public class TestB3 {
    public static void main(String[] args) {
        System.out.println("Java".substring(1, 3));
        System.out.println("Hello".indexOf('l'));
        System.out.println("  abc  ".trim().length());
    }
}
```

**答**：
```
av
2
3
```

**分析**：substring [1,3) → `av`；indexOf 第一个 l 下标 2；trim 去空格后 `abc` 长度 3。

---

### 读程 B4

```java
public class TestB4 {
    public static void main(String[] args) {
        Integer a = 127, b = 127;
        Integer c = 128, d = 128;
        System.out.println(a == b);
        System.out.println(c == d);
        System.out.println(c.equals(d));
    }
}
```

**答**：
```
true
false
true
```

**分析**：-128~127 整数缓存；128 两个对象 == 为 false，equals 为 true。

---

### 读程 B5

```java
public class TestB5 {
    public static void main(String[] args) {
        System.out.println("" + 1 + 2);
        System.out.println(1 + 2 + "");
    }
}
```

**答**：
```
12
3
```

**分析**：字符串连接从左到右；`""+1` 得 `"1"` 再 `+"2"`；`1+2` 先算 3 再拼串。

---

### 读程 B6

```java
public class TestB6 {
    public static void main(String[] args) {
        System.out.println(0.0/0.0 == 0.0/0.0);
        System.out.println(Double.isNaN(0.0/0.0));
        System.out.println(1.0/0.0 > 0);
    }
}
```

**答**：
```
false
true
true
```

---

## C 组 · 继承与多态（5 题）

### 读程 C1

```java
class A { void show() { System.out.print("A"); } }
class B extends A { void show() { System.out.print("B"); } }
public class TestC1 {
    public static void main(String[] args) {
        A ref = new B();
        ref.show();
    }
}
```

**答**：`B`（运行时绑定）

---

### 读程 C2

```java
class A {
    static void f() { System.out.print("Sa"); }
    void g() { System.out.print("Ia"); }
}
class B extends A {
    static void f() { System.out.print("Sb"); }
    void g() { System.out.print("Ib"); }
}
public class TestC2 {
    public static void main(String[] args) {
        A ref = new B();
        ref.f();
        ref.g();
    }
}
```

**答**：`SaIb`（static 看引用类型 A；实例方法 g 动态绑定 B）

---

### 读程 C3

```java
class Parent {
    Parent() { System.out.print("P"); }
}
class Child extends Parent {
    Child() { System.out.print("C"); }
}
public class TestC3 {
    public static void main(String[] args) {
        new Child();
    }
}
```

**答**：`PC`（先父构造再子构造）

---

### 读程 C4

```java
class Animal {
    Animal(String s) { System.out.print("A"); }
}
class Dog extends Animal {
    Dog() { super("d"); System.out.print("D"); }
}
public class TestC4 {
    public static void main(String[] args) {
        new Dog();
    }
}
```

**答**：`AD`

---

### 读程 C5

```java
public class TestC5 {
    public static void main(String[] args) {
        int[] a = {1, 2, 3};
        int[] b = a;
        b[0] = 99;
        System.out.println(a[0]);
    }
}
```

**答**：`99`（引用复制，同一数组）

---

## D 组 · static / final（3 题）

### 读程 D1

```java
public class TestD1 {
    static int count = 0;
    TestD1() { count++; }
    public static void main(String[] args) {
        new TestD1();
        new TestD1();
        System.out.println(count);
    }
}
```

**答**：`2`

---

### 读程 D2

```java
public class TestD2 {
    final int x;
    TestD2(int v) { x = v; }
    public static void main(String[] args) {
        TestD2 t = new TestD2(5);
        t.x = 10;
    }
}
```

**问**：能否编译？

**答**：**不能**。final 字段 **只能赋一次值**，构造已赋，不能再改。

---

### 读程 D3

```java
public class TestD3 {
    static void f() { System.out.print("S"); }
    void f() { System.out.print("I"); }
    public static void main(String[] args) {
        new TestD3().f();
    }
}
```

**问**：能否编译？

**答**：**不能**。static 与非 static 方法 **不能仅返回值不同而重载同名**——这里参数相同，冲突（实际上同类不能 static/non-static 同名同参）。

---

## E 组 · 集合（5 题）

### 读程 E1

```java
import java.util.*;
public class TestE1 {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(1); list.add(2); list.add(3);
        list.remove(1);
        System.out.println(list);
    }
}
```

**答**：`[1, 3]`（remove(1) 删 **下标** 1 的元素 2）

---

### 读程 E2

```java
import java.util.*;
public class TestE2 {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(10); list.add(20);
        list.remove(Integer.valueOf(10));
        System.out.println(list);
    }
}
```

**答**：`[20]`（删 **值** 10）

---

### 读程 E3

```java
import java.util.*;
public class TestE3 {
    public static void main(String[] args) {
        Map<String, Integer> m = new HashMap<>();
        m.put("a", 1);
        m.put("a", 2);
        System.out.println(m.get("a"));
        System.out.println(m.size());
    }
}
```

**答**：
```
2
1
```

（同 key 覆盖 value）

---

### 读程 E4

```java
import java.util.*;
public class TestE4 {
    public static void main(String[] args) {
        List<String> a = new ArrayList<>();
        List<String> b = a;
        a.add("x");
        System.out.println(b.size());
    }
}
```

**答**：`1`（同一列表）

---

### 读程 E5

```java
import java.util.*;
public class TestE5 {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>();
        set.add("A");
        set.add("A");
        set.add("B");
        System.out.println(set.size());
    }
}
```

**答**：`2`（Set 不重复）

---

## F 组 · 异常（3 题）

### 读程 F1

```java
public class TestF1 {
    public static void main(String[] args) {
        System.out.print("A");
        try {
            System.out.print("B");
            int x = 1 / 0;
            System.out.print("C");
        } catch (ArithmeticException e) {
            System.out.print("D");
        } finally {
            System.out.print("E");
        }
        System.out.print("F");
    }
}
```

**答**：`ABDEF`

---

### 读程 F2

```java
public class TestF2 {
    public static void main(String[] args) {
        try {
            return;
        } finally {
            System.out.print("F");
        }
    }
}
```

**答**：`F`（finally 在 return 前执行）

---

### 读程 F3

```java
public class TestF3 {
    static void f() { throw new RuntimeException(); }
    public static void main(String[] args) {
        System.out.print("1");
        f();
        System.out.print("2");
    }
}
```

**答**：只输出 `1`，然后未捕获异常终止（**2 不输出**）

---

## G 组 · 多线程（3 题）

### 读程 G1

```java
public class TestG1 {
    public static void main(String[] args) {
        Thread t = new Thread(() -> System.out.print("T"));
        t.run();
        System.out.print("M");
    }
}
```

**答**：`TM`（run 不启新线程）

---

### 读程 G2

```java
public class TestG2 {
    static int x = 0;
    public static void main(String[] args) throws Exception {
        Thread t = new Thread(() -> x++);
        t.start();
        t.join();
        System.out.println(x);
    }
}
```

**答**：`1`（join 等待子线程结束）

---

### 读程 G3

```java
enum Color { RED, GREEN, BLUE }
public class TestG3 {
    public static void main(String[] args) {
        System.out.println(Color.RED.ordinal());
        System.out.println(Color.RED == Color.RED);
    }
}
```

**答**：
```
0
true
```

---

## H 组 · switch / 数组 / 其他（4 题）

### 读程 H1

```java
public class TestH1 {
    public static void main(String[] args) {
        int n = 2;
        switch (n) {
            case 1: System.out.print("1");
            case 2: System.out.print("2");
            case 3: System.out.print("3"); break;
            default: System.out.print("d");
        }
    }
}
```

**答**：`23`（case 2 无 break，**贯穿** 到 case 3 才 break）

---

### 读程 H2

```java
public class TestH2 {
    public static void main(String[] args) {
        int[][] a = {{1, 2}, {3}};
        System.out.println(a.length);
        System.out.println(a[1][0]);
    }
}
```

**答**：
```
2
3
```

---

### 读程 H3

```java
public class TestH3 {
    public static void main(String[] args) {
        boolean b = false;
        if (b = true) {
            System.out.print("T");
        }
        System.out.print(b);
    }
}
```

**答**：`Ttrue`（赋值表达式值为 true；注意 `b=true` 是赋值不是 `==`）

---

### 读程 H4

```java
public class TestH4 {
    public static void main(String[] args) {
        String[] arr = {"a", "b", "c"};
        for (String s : arr) {
            if (s.equals("b")) continue;
            System.out.print(s);
        }
    }
}
```

**答**：`ac`

---

## 读程题自测索引（30 题）

| 编号 | 类型 | 核心考点 |
|------|------|----------|
| 官方 Test2 | 编译+遮蔽 | Test3、this.y |
| A1-A6 | 作用域 | 局部遮蔽、抽象类、接口、static |
| B1-B6 | String | 不可变、==、substring、NaN |
| C1-C5 | 多态 | 动态绑定、static、构造、数组引用 |
| D1-D3 | static/final | 计数、final 赋值、重载冲突 |
| E1-E5 | 集合 | remove、HashMap、Set |
| F1-F3 | 异常 | finally、未捕获终止 |
| G1-G3 | 线程/enum | run/start、join、ordinal |
| H1-H4 | 其他 | switch 贯穿、二维数组、赋值 |

> **自测建议**：每天做 **10 道**，5 天刷完一轮；错题标号回到 [按课件详讲](#按课件逐章要点详讲) 复习。

---

'''

# Apply patches
i0 = text.index(SHORT_START)
i1 = text.index(SHORT_END)
text = text[:i0] + SHORT_ANSWERS + text[i1:]

i2 = text.index("# 二、读程题")
i3 = text.index("# 三、编程题")
text = text[:i2] + READ_SECTION + "\n" + text[i3:]

MD.write_text(text, encoding="utf-8")
print("OK", MD, "lines", text.count("\n"))
