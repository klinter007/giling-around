class concat_klinter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_a": ("STRING", {"forceInput":True, "default":"", "multiline": True}),
                "string_b": ("STRING", {"forceInput":True, "default":"", "multiline": True}),
            },
            "optional": {
                "string_c": ("STRING", {"default":"", "multiline": True}),  # Made optional
            }
        }
    RETURN_TYPES = ("STRING", )
    FUNCTION = "concat"

    CATEGORY = "klinter"

    def concat(self, string_a, string_b, string_c=None):
        if string_c is None:
            string_c = ""
        d = string_a + string_b + string_c
        return (d,)


NODE_CLASS_MAPPINGS = {
    "concat_klinter": concat_klinter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "concat_klinter": "concat string (klitner)",
}
