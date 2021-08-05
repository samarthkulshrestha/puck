# Introducing **PUCK**

A [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) interpreter, written in python.
This interpreter uses just the python standard library.

## Usage

-   Unix (Linux/MacOS)

```
# clones the repository
git clone https://github.com/samarthkulshrestha/puck

cd puck

# runs the code
./brainfuck.py <file>
```

-   Windows

```
# clones the repository
git clone https://github.com/samarthkulshrestha/puck

cd puck

# runs the code
python brainfuck.py <file>
```

-   Or use it in python itself

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

## Licenee

This project is licenced under the **_DO WHATEVER THE FUCK YOU WANNA DO PUBLIC LICENSE_**.

(c) Samarth Kulshrestha 2021
