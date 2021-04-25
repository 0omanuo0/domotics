from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}
]

# The currently active modifiers
current = set()

def execute():
    print ("Do Something")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            print('gho')
            current.remove(key)


listener = keyboard.Listener(on_press=on_press)
listener.join()