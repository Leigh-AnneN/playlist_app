from app import app
from models import db, Playlist, Song

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        p1 = Playlist(
            name="Slow Beats",
            description="Music to chill with"
        )

        s1 = Song(
            title="Affections",
            artist="The Sugarlumps",
            rating=3
        )

        # Add songs to playlist
        p1.songs.append(s1)

        # Add playlist and song to session and commit
        db.session.add(p1)
        db.session.commit()

if __name__ == '__main__':
    seed_database()
