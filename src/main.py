"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Taste profile: target values for each scored feature
    user_prefs = {
        "genre": "lofi",       # preferred genre — used as a categorical match
        "mood": "chill",       # preferred mood — used as a categorical match
        "target_energy": 0.40, # preferred energy level on a 0.0–1.0 scale
        "likes_acoustic": True # whether the user prefers acoustic-sounding tracks
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
