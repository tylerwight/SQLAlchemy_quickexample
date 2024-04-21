import sqlalchemy as db
from sqlalchemy.orm import Session
import models

# setup engine and session
engine = db.create_engine("sqlite:///test.db")
session = Session(engine)
#create table if it doesn't exist
models.Base.metadata.create_all(engine)


new_guild = models.Guild(id=123, name='test', spotify_user='testuser', enabled=False, playlist_name="none", playlist_id='id_stuff')
new_guild2 = models.Guild(id=124, name='sample', spotify_user='sampleuser', enabled=True, playlist_name="favorites", playlist_id='id_favorites')
new_guild3 = models.Guild(id=125, name='example', spotify_user='userino', enabled=True, playlist_name="non", playlist_id='guid_things')

#example add one guild
session.add(new_guild)

#example add multiple guilds
session.add_all([new_guild2, new_guild3])

session.commit()


#get via primary id
target_guild = session.query(models.Guild).get(125)

if target_guild:
    print(f"Guild ID: {target_guild.id}, Name: {target_guild.name}, Spotify User: {target_guild.spotify_user}, Enabled: {target_guild.enabled}, Playlist Name: {target_guild.playlist_name}, Playlist ID: {target_guild.playlist_id}")
else:
    print("No guild found with ID 125")


#get via filterint for name
search_text = 'test'
target_guilds = session.query(models.Guild).filter(models.Guild.name == search_text).all()

if len(target_guilds) == 0:
    print("No guilds found with the name", search_text)
elif len(target_guilds) == 1:
    print("One guild found:", target_guilds[0].id, target_guilds[0].name, target_guilds[0].spotify_user, target_guilds[0].enabled, target_guilds[0].playlist_name, target_guilds[0].playlist_id)
else:
    print(f"Multiple guilds found with the name '{search_text}':")
    for guild in target_guilds:
        print(f"Guild ID: {guild.id}, Name: {guild.name}, Spotify User: {guild.spotify_user}, Enabled: {guild.enabled}, Playlist Name: {guild.playlist_name}, Playlist ID: {guild.playlist_id}")


#get only first match
single_guild = session.query(models.Guild).filter(models.Guild.name == search_text).first()

session.close()