#!/usr/bin/python3
class MiError(Exception):
    def __init__(self, natural: int, error="El número debe pertenecer al conjunto de los naturales") -> None:
        self.error = error
        self.natural = natural
        super().__init__(self.error)
