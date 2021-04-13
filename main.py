import keyboard
import random
from playsound import playsound

keypress_generic_sounds = [
    'sounds/Keystroke1.mp3',
    'sounds/Keystroke2.mp3',
    'sounds/Keystroke3.mp3',
]


def main():
    print('ClicKeys clackering');

    keyboard.on_press(key_pressed);
    keyboard.wait();


def key_pressed(key):
    print('key pressed: {0}'.format(key.name));
    playsound(random.choice(keypress_generic_sounds), False);


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main();

