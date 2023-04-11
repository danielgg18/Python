class Editor:
    def __init__(self):
        self._content = ''
        self._memento = None
        self._states = []

    def add_text(self, text):
        self._states.append(self._content)
        self._content += text

    def undo(self):
        if len(self._states) > 0:
            self._content = self._states[-1]
            self._states.pop(-1)

    def get_content(self):
        return self._content

class Memento:
    def __init__(self, content):
        self._content = content

    def get_saved_content(self):
        return self._content

editor = Editor()
while True:
    command = int(input("Ingrese un comando (1: escribir / 2: deshacer / 3: salir): "))
    if command == 1:
        text = input("Ingrese el texto a agregar: ")
        editor.add_text(text)
        print("Contenido actual: ", editor.get_content())
    elif command == 2:
        editor.undo()
        print("Contenido actual: ", editor.get_content())
    elif command == 3:
        break
    else:
        print("Comando no reconocido, intente de nuevo.")

print("Programa terminado.")
