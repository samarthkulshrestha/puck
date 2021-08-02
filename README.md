# Introducing **PUCK**

---

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

```
import brainfuck

brainfuck_code = """
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
"""

brainfuck.evalute(brainfuck_code)
```

---

## License

This project is licensed under the **DO WHATEVER THE FUCK YOU WANNA DO PUBLIC LICENSE**.
(c) Samarth Kulshrestha 2021
