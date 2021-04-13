import keyboard
from playsound import playsound

def main():
    print('ClicKeys clackering');

    keyboard.on_press(key_pressed);
    keyboard.wait();

    # while True:
        # print('key pressed');

def key_pressed(key):
    print('key pressed: {0}'.format(key.name));
    playsound('./sounds/Keystroke1.mp3', False);


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/