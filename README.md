pyexp
--------

A tiny python expression level script engine.

&nbsp;

## 关于 pyexp 微脚本引擎

pyexp 是一种运行于 python v3+ 环境的微型 python 脚本引擎，它取 python 语法规则的一个子集实现，所以很容易学习，很容上手定制开发。

&nbsp;

## 为什么需要 pyexp ？

当您的基于 python 开发的产品在部署运行中，需要某种动态解析执行的机制时，您可能希望在产品内嵌入一个微型 python 解释器，这种解释器应该是高度安全的，具备沙盒特性，它有预设的功能边界，没有安全泄露问题，同时它还是资源消耗（内存占用、CPU 占用）受控的系统，不会因为在产品中引入客户化定制能力后，不恰当脚本导致资源过重占用，导至系统崩溃或假死现象。

使用 pyexp 引擎还有一个好处，很容易借助现成 python 模块，实施功能扩展。

&nbsp;

## 安装与使用

``` bash
git clone https://github.com/fn-share/pyexp.git
cd pyexp

python3 -i cli.py   # input 'break' to quit
```

启动交互式命令行界面后，输入类似如下脚本将得到相应运行结果：

``` bash
> 3 + 5
8
> uses(basetypes)
None
> "abcd".upper()
'ABCD'
```

&nbsp;

## 举例说明 pyexp 语法规则

### 1) 使用字面文法描述常量

``` python
3
3.5
None
True
"example"
'for example'
b'for example'
```

&nbsp;

### 2) 使用复合数据

``` python
(3,4)
[3,4]
[3,4,"ab"]
{"ab",5}
{'name':'wayne','age':20}
```

&nbsp;

### 3) 运算

``` python
3 + 4
-(3 + 4)
not (3 > 4)
3 // 4
0x01 | 0x02
(0x01 | 0x02) == 0x03

"please introduce " + 'yourself.'

3 in [3,4] and True
"cd" not in [3,4,"ab"]
'OK' if 3 in [3,4] else 'FAILED'
```

&nbsp;

### 4) 使用变量

``` python
var(info,{"age":20})
var(info.age)
var(info.age,21)
var(info.age) == 21
```

&nbsp;

### 5) 逗号表达式与循环语句

``` python
comma(3,4)
comma(log('line1'),log('line2'),3+4)

loop(2,log("in loop"))

var(count,0)
loop(var(count) < 5,var(count,var(count)+1),log("in loop",var(count)))
```

&nbsp;

### 6) 用支持短路判断的 or 或 and 表达 if_else 处理

``` python
var(count,0)
comma(log('same to: if count == 0: ...'),var(count) == 0 and log('count is 0'))
comma(log('same to: if count != 1: ...'),var(count) == 1 or log('count is not 1'))
comma(log('is 0') if var(count) == 0 else log('not 0'))
```

&nbsp;

## 扩展模块

请参考 `dapp_lib/pyexp_libs` 之下各个源码模块，如：`bytes.py, dict.py` 等。

&nbsp;

## 设置脚本引擎配置常量

用户定制 pyexp 脚本引擎时，可按如下方法指定若干配置常量，如字串最大长度、复合变量最大成员数、循环体最大循环次数。

``` python
from dapp_lib import pyexp

pyexp.PYEXP_STR_MAX  = 262144   # 256K
pyexp.PYEXP_LIST_MAX = 4096     #   4K
pyexp.PYEXP_LOOP_MAX = 4096     #   4K
```

&nbsp;
