IPython
===
Python 的优点之一是其交互式解释器，也称为 shell。
IPython 集成了交互式 Python 的诸多有点。IPython 具有卓越的 Python shell，其性能
远远优于标准 Python 的 shell。IPython 同时提供了基于控制台命令环境的定制功能，
可以十分轻松地将交互式 Python shell 包含在各种 Python 应用中，甚至可以当作系统
级 shell 来使用。

### Install
    $ aptitude install ipython
    $ ipython

### 交互
    * ipython:
        In [6]: class DoubleRep(object):
        ...:     def __str__(self):
        ...:         return 'Hi, I\'m a __str__'
        ...:     def __repr__(self):
        ...:         return "Hi, I'm a __repr__"
        ...:   

        In [7]: dr = DoubleRep()

        In [8]: print dr
        Hi, I'm a __str__

        In [9]: dr
        Out[9]: Hi, I'm a __repr__

    * python:
        >>> class DoubleRep(object):
        ...   def __str__(self):
        ...     return 'hi, I a __str__'
        ...   def __repr__(self):
        ...     return 'hi, i am a __repr'
        ... 
        >>> dr =DoubleRep()
        >>> print dr
        hi, I a __str__
        >>> dr
        hi, i am a __repr
    * 当调用 str(obj) 或使用格式化字符串 "%s" % obj 时，__str__方法被调用；
        当调用 repr(obj) 或使用格式化字符串 "%r" % obj 时，__repr__ 方法被调用。
    * In & Out:
        - In -- list
            In [11]: type(In)
            Out[11]: <class 'IPython.iplib.InputList'>

        - Out -- dict
            In [12]: type(Out)
            Out[12]: <type 'dict'>
    * Tab Complete
    * Magic Edit(魔力编辑)
    * 配置 IPython:
        ~/.ipython/ipy_user_conf.py
        In [14]: %edit
    * (built-in) 魔力函数:
        以 % 开头的行，视为对魔力函数的特殊调用。
        魔力函数以 % 为前缀，参数中不带括号或者引号。
        ep: "%cd mydir"
        
        列出所以魔力函数
        In [19]: %lsmagic
        In [20]: %<TAB>

        帮助文档
        In [21]: %magic
        In [22]: %page?
        In [23]: %quickref
    * Unix Shell:
        - alias
            In [29]: %alias nss netstat -lnpt
            In [30]: nss
            In [31]: nss | grep 80
            In [32]: %alias achoo echo first: "%s", second: "%s"
            In [33]: achoo foo bar
        - store: 保留别名
            In [34]: store achoo
    * Shell 的执行: 
        - 在命令前加一个感叹号(!)
            In [34]: !netstat -lnpt
        - 通过美元符号(%)前缀，将变量传递到 shell 命令中
            In [35]: user = 'ixkungfu'
            In [36]: process = 'bash'
            In [37]: !ps aux | grep $user | grep $process

