#Ejemplo básico sobre el funcionamiento del patron de diseño "Memento"

class Editor:
    def __init__(self):
        self._content = ''
        self._memento = None

    def add_text(self, text):
        self._memento = Memento(self._content)
        self._content += text

    def undo(self):
        if self._memento:
            self._content = self._memento.get_saved_content()
            self._memento = None

    def get_content(self):
        return self._content

class Memento:
    def __init__(self, content):
        self._content = content

    def get_saved_content(self):
        return self._content

editor = Editor()
editor.add_text('Hola')
editor.add_text(' Mundo')
print(editor.get_content()) # Hola Mundo
editor.undo()
print(editor.get_content()) # Hola
