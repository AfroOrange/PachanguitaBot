from bot.models.match import Match
from db.models.matchDB import match_to_dict, dict_to_match
from dataclasses import dataclass

@dataclass
class firebase_controller:
  db: object 
     
  def save_match_to_firestore(self, chat_id, match: Match):
    self.db.collection("matches").document(str(chat_id)).set(match_to_dict(match))

  def load_match_from_firestore(self, chat_id):
    doc = self.db.collection("matches").document(str(chat_id)).get()
    if doc.exists:
      return dict_to_match(doc.to_dict())
    else:
      return None
    
'''
USE EXAMPLE
from firebase_admin import credentials, firestore
from db.services.firebase_controller import firebase_controller
from datetime import datetime

match = Match(
    date=datetime(2025, 7, 15, 18, 30),  # 15 de julio de 2025 a las 18:30
    place_name="Polideportivo Municipal",
    max_players=10,
    pitch_type="Césped",
    price=50.0
)

match.players.append("user1")
match.players.append("user2")
db = firestore.client()

db_controller = FirebaseController(db)
db_controller.save_match_to_firestore(chat_id="12345", match=match)

'''