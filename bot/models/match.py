from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Match:
    date: datetime
    place_name: str
    max_players: int
    pitch_type: str
    players: List[str] = field(default_factory=list)
    price: float = 0.0

    def __post_init__(self):
        # Validate the pitch type when creating a match.
        if self.pitch_type is None or self.pitch_type not in ["Sala Indoor", "Césped", "Sala Outdoor"]:
            # If the pitch type is not specified, cancel the match creation.
            raise ValueError("Selecciona bien el tipo de cancha: Sala Indoor, Césped, Sala Outdoor")

    # The price per player is calculated based on the total price and the number of players.
    def get_price_per_player(self):
        if len(self.players) == 0:
            return 0.0
        return self.price / len(self.players)
