import yaml
import ahk
import util
from main import a

if __name__ == '__main__':
    a.add_hotkey('!r', lambda: util.click((150, 1000)))
    a.add_hotkey('!s', lambda: util.click((1050, 50)))

    a.start_hotkeys()
    a.block_forever()
