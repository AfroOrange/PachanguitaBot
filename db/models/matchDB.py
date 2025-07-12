from bot.models.match import Match
from datetime import datetime

# Convert Match object to dictionary for Firestore storage
def match_to_dict(match: Match):
    return {
        "date": match.date.isoformat(),  # Serialize datetime as ISO string
        "place_name": match.place_name,
        "max_players": match.max_players,
        "pitch_type": match.pitch_type,
        "players": match.players,
        "price": match.price
    }

# Convert dictionary from Firestore to Match object
def dict_to_match(data: dict) -> Match:
    return Match(
        date=datetime.fromisoformat(data["date"]),
        place_name=data["place_name"],
        max_players=data["max_players"],
        pitch_type=data["pitch_type"],
        players=data.get("players", []),
        price=data.get("price", 0.0)
    )