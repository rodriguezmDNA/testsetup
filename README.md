# testsetup
repo to test setup.py


Create a new directory and virtual environment:

```bash
python3 -m venv venv
```

Activate it with:
```bash
venv/bin/activate
```
Install the module from the GitHub repo:

```bash
pip install git+https://github.com/rodriguezmDNA/testsetup.git`
```

Start a python session, import and test the module:

```python
import helloworld
helloworld.say_hello()
> 'Hello, World'
```


---

To install a specific branch use `@branch` after the URL:

```bash
pip install git+https://github.com/rodriguezmDNA/testsetup.git@v2

```
