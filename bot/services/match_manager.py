from ..models.match import Match

matches = {} # Dictionary to hold Match objects by chat_id

def create_match(chat_id, date, place_name, max_players, pitch_type, price=0.0):
    """Create a new match for the given chat_id"""
    try:
        match = Match(
            date=date,
            place_name=place_name,
            max_players=max_players,
            pitch_type=pitch_type,
            price=price
        )
        matches[chat_id] = match
        return match
    except ValueError as e:
        raise e

def join_match(chat_id, user):
    """Add a user to an existing match"""
    if chat_id in matches:
        match = matches[chat_id]
        if len(match.players) < match.max_players:
            if user not in match.players:
                match.players.append(user)
                return True
            else:
                raise ValueError("User is already in the match")
        else:
            raise ValueError("Match is full")
    else:
        raise ValueError("No match found for this chat")

def get_match(chat_id):
    """Get the match for a given chat_id"""
    return matches.get(chat_id)

def remove_player(chat_id, user):
    """Remove a player from a match"""
    if chat_id in matches:
        match = matches[chat_id]
        if user in match.players:
            match.players.remove(user)
            return True
        else:
            raise ValueError("User is not in the match")
    else:
        raise ValueError("No match found for this chat")

def delete_match(chat_id):
    """Delete a match for a given chat_id"""
    if chat_id in matches:
        del matches[chat_id]
        return True
    return False

def get_available_spots(chat_id):
    """Get the number of available spots in a match"""
    if chat_id in matches:
        match = matches[chat_id]
        return match.max_players - len(match.players)
    return 0

def is_match_full(chat_id):
    """Check if a match is full"""
    return get_available_spots(chat_id) == 0
