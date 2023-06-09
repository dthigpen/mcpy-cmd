# mcpy-cmd

A Python wrapper for writing Minecraft commands.

## Usage

Use with any Python datapack generator such as [mcpy](https://github.com/dthigpen/mcpy) or directly in a `.mcfunction` with [cog](https://nedbatchelder.com/code/cog/).

```python
# mcpy
foo = Score("$foo", "obj")
block_items = BlockPath('~1 ~2 ~3', 'Items')
items = StoragePath('items','dt.example')
yield from modify_set(items, block_items)
```

## Installation

1. Install the repository as a Python package

    ```bash
    > python -m pip install git+https://github.com/dthigpen/mcpy-cmd
    ```
