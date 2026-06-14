# -*- coding: utf-8 -*-
"""Replace 读程 section: output-only, harder questions (exam-realistic)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "content/posts/Java期末复习满分攻略.md"

READ_START = "# 二、读程题"
READ_END = "# 三、编程题"

READ_SECTION = r'''# 二、读程题（5～7 道 · 题库 25 题）

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

'''

text = MD.read_text(encoding="utf-8")
i0 = text.index(READ_START)
i1 = text.index(READ_END)
text = text[:i0] + READ_SECTION + text[i1:]

# 更新文首题型表
text = text.replace(
    "| **读程题** | **5～7 道** | 写运行结果 / 判断能否编译 |",
    "| **读程题** | **5～7 道** | **只写运行结果**（代码保证能运行） |",
    1,
)

# 更新冲刺 checklist 里读程相关（若存在）
text = text.replace(
    "- [ ] 官方 **Test2** 编译判断 + 三行输出",
    "- [ ] 官方 **Test2** 三行输出（遮蔽 + this.y）",
    1,
)

MD.write_text(text, encoding="utf-8")
print("OK: output-only 读程题库, lines", text.count("\n"))
