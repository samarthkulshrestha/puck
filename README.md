# puck

a [brainfuck](https://en.wikipedia.org/wiki/Brainfuck) interpreter, written in python.
this interpreter uses just the python standard library.

### usage

#### as a script-

+ clone the repository

```console
git clone https://github.com/samarthkulshrestha/puck
```

+ change directory

```console
cd puck
```

+ run the code

```
python brainfuck.py <file>
```

#### as a python library-

```python
import brainfuck

brainfuck_code = """
++++++++
[>++++[>++>+++>+++>+<<<<-]
>+>+>->>+[<]<-]
>>.>---.+++++++..+++.>>.<-.
<.+++.------.--------.>>+.>++.
"""

brainfuck.evalute(brainfuck_code)
```

### license

this project is licensed under the mit license.

(c) samarth kulshrestha 2021
