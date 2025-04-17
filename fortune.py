# fortune.py

import random

def get_fortune(mood):
    fortunes = {
        "happy": [
            "🌈 Bright days are ahead, keep shining!",
            "✨ Your joy is contagious, Indranil!",
        ],
        "sad": [
            "💖 It's okay to feel down. Better days are coming.",
            "🌧️ Even storms pass. You're stronger than you know.",
        ],
        "neutral": [
            "🌟 A surprise is around the corner, stay curious!",
            "💫 Balance brings clarity. Trust yourself.",
        ]
        
    }
    if mood in fortunes:
        return random.choice(fortunes[mood])
    else:
        return "🤔 I can't predict that mood. Try happy, sad, neutral"

def main():
    print("🔮 Welcome to Indranil Sen's Fortune Teller (21JE0413) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()
    print(f"\n✨ Your fortune: {get_fortune(mood)} ✨")

if __name__ == "__main__":
    main()
