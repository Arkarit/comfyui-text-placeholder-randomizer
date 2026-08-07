# ComfyUI Text Placeholder Randomizer

A small ComfyUI custom node: replaces `$1`, `$2`, `$3` placeholders in a text
string with a random term picked from up to 5 comma-separated candidates per
placeholder.

## Node: Random Term Replace ($1 $2 $3)

**Inputs**

- `text` — the text containing `$1`, `$2`, `$3` placeholders
- `terms_1`, `terms_2`, `terms_3` — comma-separated candidate terms for each
  placeholder (max 5 used per list; extras are ignored)
- `seed` — controls which term is picked; same seed + same terms always
  produces the same result

**Output**

- `text` — the input text with each placeholder replaced by one randomly
  chosen term from its list. A placeholder with an empty terms list is left
  unchanged.

## Install

Clone into your ComfyUI `custom_nodes` directory and restart ComfyUI:

```bash
git clone https://github.com/<your-username>/comfyui-text-placeholder-randomizer.git
```
