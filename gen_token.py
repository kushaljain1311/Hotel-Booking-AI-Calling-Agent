# from livekit import api

# API_KEY = "devkey"         # Your LiveKit API key
# API_SECRET = "supersecret" # Your LiveKit API secret

# token = api.AccessToken(api_key=API_KEY, api_secret=API_SECRET) \
#     .with_identity("user1") \
#     .with_name("HotelGuest") \
#     .with_grants(api.VideoGrants(room_join=True, room="hotel_room")) \
#     .to_jwt()

# print(token)


from livekit import api

API_KEY = "devkey"         # Your LiveKit API key
API_SECRET = "supersecret" # Your LiveKit API secret

token = api.AccessToken(api_key=API_KEY, api_secret=API_SECRET) \
    .with_identity("user1") \
    .with_name("HotelGuest") \
    .with_grants(api.VideoGrants(
        room_join=True, 
        room="hotel_room",
        can_publish=True,      # Allow publishing audio/video
        can_subscribe=True,    # Allow receiving audio/video
        can_publish_data=True  # Allow sending data messages (needed for transcriptions)
    )) \
    .to_jwt()

print(f"URL: ws://localhost:7880")
print(f"Token: {token}")
