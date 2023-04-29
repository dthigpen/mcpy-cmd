# mcpy-cmd

A Python wrapper for writing Minecraft commands.

## Usage

Use with any Python datapack generator such as [mcpy](https://github.com/dthigpen/mcpy) or directly in a `.mcfunction` with [cog](https://nedbatchelder.com/code/cog/).

```python
# mcpy
foo = Scoreboard.Player("$foo", "obj")
item = Data.Storage('item','dt.example')
yield foo.set(5)
yield item.modify().set_from(Data.Entity('@s','SelectedItem'))
```

## Installation

1. Install the repository as a Python package

    ```bash
    > python -m pip install git+https://github.com/dthigpen/mcpy-cmd
    ```
