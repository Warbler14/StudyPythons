# How to Use Jupyter Notebook

## What Jupyter Notebook Is

Jupyter Notebook is an interactive environment where you can write Python code in small blocks called cells, run them one by one, and keep notes in the same document.

It is useful for:

- learning Python step by step
- testing ideas quickly
- writing explanations with code
- showing charts, tables, and results

## Install Jupyter

If you have Python installed, you can install Jupyter with:

```bash
pip install notebook
```

If you use a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install notebook
```

## Start Jupyter Notebook

Open a terminal in your project folder and run:

```bash
jupyter notebook
```

This usually opens your browser automatically. If it does not, copy the local URL shown in the terminal and open it in your browser.

## Create a Notebook

1. Open Jupyter in your browser.
2. Click `New`.
3. Choose `Python 3` or your available Python kernel.
4. A new notebook file with the `.ipynb` extension will open.

## Basic Usage

There are two main kinds of cells:

- Code cell: runs Python code
- Markdown cell: writes notes, titles, and explanations

Useful actions:

- Run current cell: `Shift + Enter`
- Add a cell below: `B` in command mode
- Add a cell above: `A` in command mode
- Delete a cell: `D` then `D` in command mode
- Change cell to code: `Y`
- Change cell to markdown: `M`

## Example

Code cell:

```python
name = "Python"
print(f"Hello, {name}!")
```

Markdown cell:

```md
# My Python Notes

This notebook is for practice.
```

## Good Study Workflow

For modern Python study, a good notebook flow is:

1. Write a short title in a markdown cell.
2. Add one concept at a time.
3. Test small code examples in code cells.
4. Write notes under the code about what happened.
5. Keep one notebook per topic, such as `lists.ipynb`, `functions.ipynb`, or `classes.ipynb`.

## Save and Export

- Jupyter saves notebooks as `.ipynb` files.
- You can rename the notebook from the top of the page.
- You can download or export notebooks from the menu.

## Helpful Tip

Use notebooks for practice and exploration, but for bigger reusable programs, move the final code into `.py` files.
