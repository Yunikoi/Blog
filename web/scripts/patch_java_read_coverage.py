# -*- coding: utf-8 -*-
"""Add 读程 coverage audit + L group to fill gaps."""
from pathlib import Path

MD = Path(__file__).resolve().parents[2] / "content/posts/Java期末复习满分攻略.md"
text = MD.read_text(encoding="utf-8")

COVERAGE = r'''
## 读程考点覆盖对照（诚实版）

> **结论**：40 题 **不能** 保证 100% 覆盖全部课件，但 **覆盖期末读程 5～7 道的高频坑**（OOP、String、集合、异常、线程、switch/数组）。  
> 下面按 **PPT 章节** 标注：**✅ 题库有** / **⚠️ 部分** / **❌ 读程极少考** / **➕ L 组已补**。

| 课件章 | 读程常考考点 | 覆盖 | 对应题 |
|--------|--------------|:----:|--------|
| 第三章 基础 | 变量遮蔽、this | ✅ | 官方 Test2、A1-A2 |
| | String 不可变、+、substring | ✅ | B1-B3 |
| | == / equals、Integer 缓存 | ✅ | B2、B4、K4 |
| | NaN / Infinity | ✅ | B4 |
| | **i++ / ++i 混合** | ➕ | **L1** |
| | **强制类型转换 (int)(double)** | ➕ | **L2** |
| | **自定义类 equals 陷阱** | ➕ | **L3** |
| | **值传递 int vs 数组元素** | ➕ | **L4** |
| | switch 贯穿 | ✅ | H1 |
| | 二维数组 | ✅ | H2 |
| | 短路 && \|\| | ✅ | H3 |
| | char / println(char[]) | ➕ | **L5** |
| 第四章 OOP | 继承、多态、super | ✅ | C1-C5、I1-I3 |
| | static 绑定 vs 实例绑定 | ✅ | C1、C4 |
| | PrivOverride private | ✅ | C2 |
| | static/final 块与构造顺序 | ✅ | C4、I5 |
| | **instanceof + 向下转型** | ➕ | **L6** |
| | 包/访问权限 | ❌ | 读程几乎不考，简答了解 |
| 第五章 高级 | static 计数、final 引用 | ✅ | D1-D2 |
| | 抽象/接口（能运行的题） | ✅ | I4 |
| | **enum ordinal/name** | ⚠️→➕ | G3、**L7** |
| | ArrayList remove 陷阱 | ✅ | E1-E2 |
| | HashMap / HashSet | ✅ | E3-E4、K5 |
| | TreeSet 有序 | ✅ | K2 |
| | **LinkedList 作为 List** | ➕ | **L8** |
| | equals/hashCode + Set | ⚠️ | 简答为主，读程偶考 |
| 第六章 异常 | try-catch-finally 顺序 | ✅ | F1-F3 |
| | **循环 + catch + finally（课件 greetings 型）** | ➕ | **L9** |
| | 受检异常 throws | ❌ | 编程题为主 |
| 第七章 I/O | FileReader / 读写文件 | ❌ | **笔考读程基本不出**（编程题考） |
| 第九章 线程 | start/run、join | ✅ | G1-G2、J1-J2 |
| | synchronized | ✅ | G3、J3 |
| | 无同步竞态 | ✅ | J4 |
| | Runnable | ✅ | J5 |
| | **sleep 阻塞** | ➕ | **L10** |
| | wait/notify | ⚠️ | 简答必背，读程极少 |
| GUI | 事件、Swing | ❌ | **简答 + 编程**；读程 ★ 文档已说明 |

**仍建议从详讲章节的 PPT 例题手算**：`Sandwich` 构造顺序、`BreakAndContinueWithLabel`（标号 continue）——出现频率低于上表 ✅ 项，时间紧可后补。

---

## L 组 · 补漏（8 题 · 第三章/课件经典）

### 读程 L1

**📖 相关知识点**

- PPT 经典：`int j = (i++) + (i++);` **后置 ++** 先用后加；同一表达式中 **从左到右** 用旧值。

**问：写出运行结果**

```java
public class TestL1 {
    public static void main(String[] args) {
        int i = 5;
        int j = (i++) + (i++);
        System.out.println(i + " " + j);
    }
}
```

**输出结果**：
```
7 11
```

**分析**：第一个 i++ 用 5 再变 6；第二个用 6 再变 7；j=5+6=11。

---

### 读程 L2

**📖 相关知识点**

- **强制转换**截断小数：`(int) double` 向零取整，**不是**四舍五入。
- `Math.round` 才是四舍五入到 long。

**问：写出运行结果**

```java
public class TestL2 {
    public static void main(String[] args) {
        double d = 9.7;
        System.out.println((int) d);
        System.out.println(Math.round(d));
    }
}
```

**输出结果**：
```
9
10
```

---

### 读程 L3

**📖 相关知识点**

- PPT `Equivalence`：**自定义 equals 参数必须是 Object 才算重写**。
- `equals(Value v)` 是 **重载**，不是重写；`Object.equals` 仍比地址。

**问：写出运行结果**

```java
class Value {
    int i;
    Value(int i) { this.i = i; }
    public boolean equals(Value v) { return this.i == v.i; }
}
public class TestL3 {
    public static void main(String[] args) {
        Value a = new Value(10), b = new Value(10);
        System.out.println(a == b);
        System.out.println(a.equals(b));
    }
}
```

**输出结果**：
```
false
true
```

---

### 读程 L4

**📖 相关知识点**

- PPT `PassTest`：**基本类型** 传参改形参 **不影响** 实参；**数组元素** 改内容 **影响**。

**问：写出运行结果**

```java
public class TestL4 {
    static void change(int x, int[] arr) {
        x = 100;
        arr[0] = 100;
    }
    public static void main(String[] args) {
        int n = 1;
        int[] a = { 1, 2 };
        change(n, a);
        System.out.println(n + " " + a[0]);
    }
}
```

**输出结果**：
```
1 100
```

---

### 读程 L5

**📖 相关知识点**

- `char` 与 int 可运算提升为 int；`println(char[])` 打印 **数组内容** 而非地址。

**问：写出运行结果**

```java
public class TestL5 {
    public static void main(String[] args) {
        char c = 'A';
        System.out.println(c + 1);
        char[] arr = { 'a', 'b' };
        System.out.println(arr);
    }
}
```

**输出结果**：
```
66
ab
```

（'A'+1 → 66；println(char[]) 输出字符序列。）

---

### 读程 L6

**📖 相关知识点**

- **instanceof** 判断类型；**向下转型** 后可调子类独有方法。
- 编译类型决定 **能调哪些方法**；`x[1].u()` 需转型。

**问：写出运行结果**

```java
class Useful { void f() { System.out.print("F"); } }
class More extends Useful { void u() { System.out.print("U"); } }
public class TestL6 {
    public static void main(String[] args) {
        Useful[] x = { new Useful(), new More() };
        x[0].f();
        x[1].f();
        ((More) x[1]).u();
        System.out.println();
    }
}
```

**输出结果**：
```
FFU
```

---

### 读程 L7

**📖 相关知识点**

- **enum**：`ordinal()` 声明顺序；`name()` 常量名；可用 `==` 比较同一常量。

**问：写出运行结果**

```java
enum Color { RED, GREEN, BLUE }
public class TestL7 {
    public static void main(String[] args) {
        Color c = Color.GREEN;
        System.out.println(c.ordinal());
        System.out.println(c.name());
        System.out.println(c == Color.GREEN);
    }
}
```

**输出结果**：
```
1
GREEN
true
```

---

### 读程 L8

**📖 相关知识点**

- **LinkedList** 也实现 `List`；`addFirst` / 作为队列了解；本题用 List 接口 + 下标 insert。

**问：写出运行结果**

```java
import java.util.*;
public class TestL8 {
    public static void main(String[] args) {
        List<String> L = new LinkedList<>();
        L.add("A");
        L.add("C");
        L.add(1, "B");
        System.out.println(L);
    }
}
```

**输出结果**：
```
[A, B, C]
```

---

### 读程 L9

**📖 相关知识点**

- PPT **greetings 循环** 简化：越界进 catch，**finally 每轮都执行**。

**问：写出运行结果**

```java
public class TestL9 {
    public static void main(String[] args) {
        String[] g = { "X", "Y" };
        for (int i = 0; i < 3; i++) {
            try {
                System.out.print(g[i]);
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.print("E");
            } finally {
                System.out.print("F");
            }
        }
    }
}
```

**输出结果**：
```
XFYFE
```

**分析**：i=0 XF；i=1 YF；i=2 越界 EF。

---

### 读程 L10

**📖 相关知识点**

- **sleep** 阻塞当前线程；本题 main 里 sleep 再打印，**顺序确定**。

**问：写出运行结果**

```java
public class TestL10 {
    public static void main(String[] args) throws Exception {
        System.out.print("A");
        Thread.sleep(10);
        System.out.print("B");
    }
}
```

**输出结果**：
```
AB
```

---

'''

NEW_INDEX = r'''## 读程题自测索引（48 题 · 只写输出）

| 编号 | 难度 | 核心考点 |
|------|------|----------|
| 官方 Test2 | ★★ | 遮蔽、this、toString |
| A1-A4 | ★★ | 参数遮蔽、UnmaskField、static 共享、重载 |
| B1-B4 | ★★★ | String 循环、常量池、混合运算、包装类 |
| C1-C5 | ★★★★ | static/实例绑定、PrivOverride、构造+多态、static 块、引用 |
| D1-D3 | ★★ | static 计数、final 引用、重写 |
| E1-E4 | ★★★ | ArrayList 课件、remove 陷阱、HashMap、HashSet |
| F1-F3 | ★★★ | 异常链、循环+finally、return+finally |
| G1-G3 | ★★★ | run/start、join、synchronized、enum |
| H1-H4 | ★★★ | switch 贯穿、二维数组、短路、嵌套循环 |
| I1-I5 | ★★★ | 多层继承、数组+多态、双接口、初始化顺序 |
| J1-J5 | ★★★★ | 线程 join、synchronized、Runnable、竞态 |
| K1-K5 | ★★★ | 排序、TreeSet、StringBuilder、Integer 缓存、Map |
| **L1-L10** | ★★★ | i++、类型转换、equals 陷阱、值传递、char[]、instanceof、enum、LinkedList、greetings 异常、sleep |

> **冲刺建议**：先保证 **A～F + L1-L4** 无盲区，再攻 **C/J** 难题；每天手算 **10 道**。  
> **不考读程的**：File I/O、GUI 界面代码——见简答/编程章。

'''

# Insert L group + coverage before index
anchor = "## 读程题自测索引（40 题 · 只写输出）"
if "读程考点覆盖对照" not in text:
    i = text.index(anchor)
    text = text[:i] + COVERAGE + NEW_INDEX + text[i + len(anchor):]
    # remove old index body until sprint line
    old_body_start = text.index("| 编号 | 难度 | 核心考点 |", text.index("## 读程题自测索引（48 题"))
    # find second occurrence of table header after our new index - delete duplicate old table
    first_table = text.index("| 编号 | 难度 | 核心考点 |", text.index("## 读程题自测索引（48 题"))
    second = text.find("| 编号 | 难度 | 核心考点 |", first_table + 10)
    if second != -1 and second < text.find("# ★ 期末抢分秘籍", first_table):
        end_sprint = text.index("> **冲刺建议**", second)
        end_dash = text.index("\n\n---\n\n# ★ 期末抢分秘籍", end_sprint)
        text = text[:second] + text[end_dash:]

text = text.replace("# 二、读程题（5～7 道 · 题库 40 题）", "# 二、读程题（5～7 道 · 题库 48 题）", 1)
text = text.replace("下面 **40 道**", "下面 **48 道**", 1)
text = text.replace(
    "- [读程题库（40 题 · 只写输出）](#二读程题57-道--题库-40-题)",
    "- [读程考点覆盖对照](#读程考点覆盖对照诚实版)\n- [读程题库（48 题 · 只写输出）](#二读程题57-道--题库-48-题)",
    1,
)
text = text.replace(
    "读程 **40 题**",
    "读程 **48 题**",
    1,
)

MD.write_text(text, encoding="utf-8")
print("OK lines", text.count("\n"))
