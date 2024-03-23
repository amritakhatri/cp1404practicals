class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Initialise a ProgrammingLanguage instance.

        name: string, name of language
        typing: string, typing of language
        reflection: boolean, indicates if language has reflection
        year: int, year language was introduced
        pointer_arithmetic: boolean, indicates if language supports pointer arithmetic
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, Year={self.year}, Pointer Arithmetic={self.pointer_arithmetic}"
