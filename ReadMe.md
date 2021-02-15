I am going through an online self study thing for Python. I needed to write a shell script to find shell scripts in a folder, determine if the first line indicates it is a shell script and then run shellcheck against the file if true.

> Note that the code has a Linux/macOS `#!/usr/bin/python3` directive at line 1. If on Windows, replace `./go.sh` below with `python go.sh`.

Scan the current directory. Expects `shellcheck` to be in your path.
```
./go.py
```
Scan `/tmp` directory. Expects `shellcheck` to be in your path.
```
./go.py /tmp
```
Scan `/tmp` directory using `shellcheck` located in `/usr/bin/shellcheck`.
```
./go.py /tmp /usr/bin/shellcheck
```

Source:
[code.txt](https://github.com/mtlynch/tinypilot/files/5979065/code.txt)

> Updated: Added a line to close the file after reading the first line `f.close()`

