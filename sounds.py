from pathlib import Path
import winsound

SOUNDS_DIR = Path(__file__).parent / "assets"

def play(sound_name, meme_label):
    sound_file = SOUNDS_DIR / f"{sound_name}.wav"

    if not sound_file.exists():
        print(f"Sound '{sound_name}' not found at {sound_file.resolve()}!")
        return

    print(f"Now Playing: {meme_label}")
    # SND_FILENAME: Tells it to look for a file
    # SND_ASYNC: Plays the sound in the background so the script doesn't freeze
    winsound.PlaySound(str(sound_file), winsound.SND_FILENAME | winsound.SND_ASYNC)

# --- Meme Functions ---

def fart():
    play("fart", "Fart Meme")

def bone_crack():
    play("bone_crack", "Bone_crack Meme")

def oppa():
    play("oppa", "Oopa Neymar Meme")

def six_seven():
    play("67", "67 Meme")

def siren():
    play("siren", "-999 Social Credit Siren Meme") 

def wow():
    play("WOW", "WoW Meme")    

def baby():
    play("baby", "Baby_cry Meme")