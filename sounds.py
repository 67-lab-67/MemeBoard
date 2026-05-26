from pathlib import Path
import argparse
import random
import winsound

SOUNDS_DIR = Path(__file__).parent / "assets"

ALIASES = {
    "oppa": "oopa",
    "six_seven": "67",
}


def _sound_path(sound_name):
    sound_key = ALIASES.get(sound_name, sound_name)
    return SOUNDS_DIR / f"{sound_key}.wav"


def list_sounds():
    return sorted(sound.stem for sound in SOUNDS_DIR.glob("*.wav"))


def play_sound(sound_name):
    sound_file = _sound_path(sound_name)

    if not sound_file.exists():
        print(f"Sound '{sound_name}' not found at {sound_file.resolve()}!")
        return False

    print(f"Now Playing: {sound_file.stem}")
    winsound.PlaySound(str(sound_file), winsound.SND_FILENAME)
    return True


def random_sound():
    sounds = list_sounds()
    if not sounds:
        print(f"No sounds found in {SOUNDS_DIR.resolve()}!")
        return False

    return play_sound(random.choice(sounds))


def play(sound_name, meme_label):
    sound_file = SOUNDS_DIR / f"{sound_name}.wav"

    if not sound_file.exists():
        print(f"Sound '{sound_name}' not found at {sound_file.resolve()}!")
        return False

    print(f"Now Playing: {meme_label}")
    winsound.PlaySound(str(sound_file), winsound.SND_FILENAME)
    return True

# --- Meme Functions ---

def fart():
    play("fart", "Fart Meme")

def bone_crack():
    play("bone_crack", "Bone_crack Meme")

def oppa():
    play("oopa", "Oopa Neymar Meme")

def six_seven():
    play("67", "67 Meme")

def siren():
    play("siren", "-999 Social Credit Siren Meme") 

def wow():
    play("wow", "woooow Meme")    

def baby():
    play("baby", "Baby_laugh Meme") 

def ack ():
    play ("ack", "ack Meme")    

def cat_laugh ():
    play ("cat_laugh", "cat_laugh Meme")

def get_out ():
    play ("get_out", "get_out Meme")

def emo_damage ():
    play ("emo_damage", "emotional damage Meme")

def hell_nahh ():
    play ("hell_nahh", "Hell_nahh Meme")   

def mario_jump ():
    play ("mario_jump", "mario_jump")

def omg():
    play ("omg", "ohh my god")                     

def sad_meow ():
    play ("sad_meow", "so sad")

def so_cute ():
    play ("so_cute", "i show speed")

def womp_womp ():
    play ("womp_womp", "so sad again")

def yay ():
    play ("yay", "be happy")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="memesounds")
    parser.add_argument("sound", nargs="?", help="Sound name to play")
    parser.add_argument("--list", action="store_true", help="List available sounds")
    parser.add_argument("--random", action="store_true", help="Play a random sound")
    args = parser.parse_args(argv)

    if args.list:
        for sound in list_sounds():
            print(sound)
        return 0

    if args.random:
        return 0 if random_sound() else 1

    if args.sound:
        return 0 if play_sound(args.sound) else 1

    parser.print_help()
    return 0
