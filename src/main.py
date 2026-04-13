"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    print(f"Loaded {len(songs)} songs.")

    profiles = {
        "The Ghost Genre": {
            "genre": "k-pop",
            "mood": "happy",
            "target_energy": 0.80,
            "likes_acoustic": False,
        },
        "Contradictory Energy + Mood": {
            "genre": "ambient",
            "mood": "intense",
            "target_energy": 0.95,
            "likes_acoustic": False,
        },
        "The Orphan Mood": {
            "genre": "lofi",
            "mood": "sad",
            "target_energy": 0.40,
            "likes_acoustic": True,
        },
        "Dead-Center Energy": {
            "genre": "classical",
            "mood": "peaceful",
            "target_energy": 0.50,
            "likes_acoustic": True,
        },
        "Single-Song Genre": {
            "genre": "rock",
            "mood": "happy",
            "target_energy": 0.30,
            "likes_acoustic": False,
        },
        "Everything Conflicts": {
            "genre": "jazz",
            "mood": "angry",
            "target_energy": 0.10,
            "likes_acoustic": False,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 40)
        print(f"  {profile_name}")
        print("=" * 40)
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n#{i}  {song['title']} by {song['artist']}")
            print(f"    Score  : {score:.2f} / 4.00")
            print(f"    Reasons: {explanation}")
        print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
