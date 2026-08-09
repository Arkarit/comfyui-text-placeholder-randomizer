# ComfyUI Text Placeholder Randomizer

A small ComfyUI custom node: replaces sequential placeholders in a text
string with a random term picked from a CSV candidate list, one row per
placeholder.

## Node: Random CSV Text Replace

**Inputs**

- `text` — the text containing the placeholders
- `search_string` — prefix before the placeholder index (default `$`, so
  placeholders look like `$1`, `$2`, ...)
- `start_index` — index of the first placeholder (default `1`). Also maps
  to the first row of `terms` (see below), and lets you chain multiple
  copies of this node by offsetting it: e.g. one node with `start_index=1`
  covers `$1`-`$5`, a second with `start_index=6` covers `$6`-`$10`
- `terms` — CSV text. Each row is the candidate list for one placeholder;
  row order maps to `start_index`, `start_index+1`, ... Any number of rows
  and any number of comma-separated candidates per row. Quote a field to
  include a literal comma, e.g. `"a, b",c`
- `seed` — controls which term is picked; same seed + same terms always
  produces the same result

**Output**

- `text` — the input text with each placeholder replaced by one randomly
  chosen candidate from its row. A placeholder whose row is missing or
  empty is left unchanged.
- A read-only `preview` widget on the node itself shows the last result, so
  you don't need a separate preview/text-display node downstream.

## Install

Clone into your ComfyUI `custom_nodes` directory and restart ComfyUI:

```bash
git clone https://github.com/Arkarit/comfyui-text-placeholder-randomizer.git
```
