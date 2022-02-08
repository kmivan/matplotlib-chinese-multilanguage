class LocaleNotSupported(Exception):
    def __init__(self, lc) -> None:
        super().__init__(f"Locale {lc} is not configured\n")


class FontNotFoundError(Exception):
    def __init__(self, filename) -> None:
        super().__init__(f"{filename} is not found in 'matplotlib_multilanguage/fonts'")
