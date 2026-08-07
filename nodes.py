import random


class TextPlaceholderRandomizer:
    """Replaces $1..$5 placeholders in a text with a random term picked from
    a per-placeholder, comma-separated list of candidates (any number of
    terms). Same seed + same terms always picks the same term. A placeholder
    with an empty terms list is left unchanged."""

    PLACEHOLDERS = ("$1", "$2", "$3", "$4", "$5")
    DESCRIPTION = (
        "Replaces $1..$5 placeholders in a text with a random term picked "
        "from a per-placeholder, comma-separated list of candidates (any "
        "number of terms). Same seed + same terms always picks the same "
        "term. A placeholder with an empty terms list is left unchanged."
    )

    @classmethod
    def INPUT_TYPES(cls):
        term_tooltip = "Comma-separated candidate terms for this placeholder. Any number of terms; one is picked at random."
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "A $1 riding a $2 through $3.",
                    "tooltip": "Text containing $1..$5 placeholders to be replaced.",
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
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "replace"
    CATEGORY = "text"

    def replace(self, text, terms_1, terms_2, terms_3, terms_4, terms_5, seed):
        rng = random.Random(seed)
        result = text
        terms_fields = (terms_1, terms_2, terms_3, terms_4, terms_5)
        for placeholder, terms_field in zip(self.PLACEHOLDERS, terms_fields):
            terms = [t.strip() for t in terms_field.split(",") if t.strip()]
            if terms:
                result = result.replace(placeholder, rng.choice(terms))
        return (result,)


NODE_CLASS_MAPPINGS = {
    "TextPlaceholderRandomizer": TextPlaceholderRandomizer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextPlaceholderRandomizer": "Random Term Replace ($1-$5)",
}
