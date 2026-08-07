import random


class TextPlaceholderRandomizer:
    MAX_TERMS = 5
    PLACEHOLDERS = ("$1", "$2", "$3")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "A $1 riding a $2 through $3."}),
                "terms_1": ("STRING", {"multiline": False, "default": ""}),
                "terms_2": ("STRING", {"multiline": False, "default": ""}),
                "terms_3": ("STRING", {"multiline": False, "default": ""}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "replace"
    CATEGORY = "text"

    def replace(self, text, terms_1, terms_2, terms_3, seed):
        rng = random.Random(seed)
        result = text
        for placeholder, terms_field in zip(self.PLACEHOLDERS, (terms_1, terms_2, terms_3)):
            terms = [t.strip() for t in terms_field.split(",") if t.strip()][: self.MAX_TERMS]
            if terms:
                result = result.replace(placeholder, rng.choice(terms))
        return (result,)


NODE_CLASS_MAPPINGS = {
    "TextPlaceholderRandomizer": TextPlaceholderRandomizer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextPlaceholderRandomizer": "Random Term Replace ($1 $2 $3)",
}
