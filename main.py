import keyboard
import random
from playsound import playsound

# used to track keypress states
key_state = {}

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
    print('ClicKeys clackering')

    while True:
        key = keyboard.read_event()
        # print('{0}: {1}'.format(key.event_type, key.name))
        key_pressed(key)


def key_pressed(key):
    print('{0}: {1}'.format(key.event_type, key.name))

    # on keypress if press state for key is false or it does not exist in state dict
    if key.event_type == 'down' and (key.name not in key_state or not key_state[key.name]):
        # if special key was pressed
        if key.name in keypress_special_sounds:
            # play random sound from key's sound list
            playsound(random.choice(keypress_special_sounds[key.name]), False)
        else:
            # else play generic keystroke sound
            playsound(random.choice(keypress_generic_sounds), False);

        # set key state to pressed
        key_state[key.name] = True

    # set key state to released on key up
    if key.event_type == 'up':
        key_state[key.name] = False


if __name__ == '__main__':
    main()

