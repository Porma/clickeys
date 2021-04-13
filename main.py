import keyboard
import random
from playsound import playsound

keypress_special_sounds = {
    'space': ['sounds/SpaceBar1.mp3', 'sounds/SpaceBar2.mp3'],
    'backspace': ['sounds/Backspace_Enter1.mp3', 'sounds/Backspace_Enter2.mp3'],
    'enter': ['sounds/Backspace_Enter1.mp3', 'sounds/Backspace_Enter2.mp3']
}

keypress_generic_sounds = [
    'sounds/Keystroke1.mp3',
    'sounds/Keystroke2.mp3',
    'sounds/Keystroke3.mp3',
]


def main():
    print('ClicKeys clackering');

    # listen for key press
    keyboard.on_press(key_pressed);
    # blocking listener for endless loop kinda thing
    keyboard.wait();


def key_pressed(key):
    print('key pressed: {0}'.format(key.name));

    # if special key was press
    if key.name in keypress_special_sounds:
        # play random sound from key's sound list
        playsound(random.choice(keypress_special_sounds[key.name]), False)
    else:
        # else play generic keystroke sound
        playsound(random.choice(keypress_generic_sounds), False);


if __name__ == '__main__':
    main();