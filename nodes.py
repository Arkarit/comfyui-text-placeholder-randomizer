import random


class TextPlaceholderRandomizer:
    """Replaces 5 sequential placeholders (search_string + index) in a text
    with a random term picked from a per-placeholder, comma-separated list
    of candidates (any number of terms). start_index lets you chain several
    of these nodes: e.g. one node covering $1-$5, a second with
    start_index=6 covering $6-$10. Same seed + same terms always picks the
    same term. A placeholder with an empty terms list is left unchanged."""

    NUM_PLACEHOLDERS = 5
    DESCRIPTION = (
        "Replaces 5 sequential placeholders (search_string + index, e.g. "
        "$1-$5) in a text with a random term picked from a per-placeholder, "
        "comma-separated list of candidates (any number of terms). "
        "start_index lets you chain several of these nodes: e.g. one node "
        "covering $1-$5, a second with start_index=6 covering $6-$10. Same "
        "seed + same terms always picks the same term. A placeholder with "
        "an empty terms list is left unchanged. Shows the result in a "
        "read-only preview widget on the node itself."
    )
    OUTPUT_NODE = True

    @classmethod
    def INPUT_TYPES(cls):
        term_tooltip = "Comma-separated candidate terms for this placeholder. Any number of terms; one is picked at random."
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "A $1 riding a $2 through $3.",
                    "tooltip": "Text containing the placeholders to be replaced.",
                }),
                "search_string": ("STRING", {
                    "multiline": False, "default": "$",
                    "tooltip": 'Prefix before the placeholder index, e.g. "$" makes placeholders $1, $2, ...',
                }),
                "start_index": ("INT", {
                    "default": 1, "min": 0, "max": 0xFFFFFFFFFFFFFFFF,
                    "tooltip": "First placeholder index. Chain multiple nodes by offsetting this, e.g. 1 then 6 for $1-$5 and $6-$10.",
                }),
                "terms_1": ("STRING", {"multiline": False, "default": "", "tooltip": term_tooltip}),
                "terms_2": ("STRING", {"multiline": False, "default": "", "tooltip": term_tooltip}),
                "terms_3": ("STRING", {"multiline": False, "default": "", "tooltip": term_tooltip}),
                "terms_4": ("STRING", {"multiline": False, "default": "", "tooltip": term_tooltip}),
                "terms_5": ("STRING", {"multiline": False, "default": "", "tooltip": term_tooltip}),
                "seed": ("INT", {
                    "default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF,
                    "tooltip": "Controls which term is picked. Same seed + same terms always gives the same result.",
                }),
            },
            "optional": {
                "preview": ("STRING", {
                    "multiline": True, "default": "",
                    "tooltip": "Read-only preview of the last result. Not an input; updates after each run.",
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "replace"
    CATEGORY = "text"

    def replace(self, text, search_string, start_index, terms_1, terms_2, terms_3, terms_4, terms_5, seed, preview=""):
        rng = random.Random(seed)
        result = text
        terms_fields = (terms_1, terms_2, terms_3, terms_4, terms_5)
        for offset, terms_field in enumerate(terms_fields):
            placeholder = f"{search_string}{start_index + offset}"
            terms = [t.strip() for t in terms_field.split(",") if t.strip()]
            if terms:
                result = result.replace(placeholder, rng.choice(terms))
        return {"ui": {"text": [result]}, "result": (result,)}


NODE_CLASS_MAPPINGS = {
    "TextPlaceholderRandomizer": TextPlaceholderRandomizer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextPlaceholderRandomizer": "Random Term Replace (5x, Chainable)",
}
