from contextlib import contextmanager
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, load_only

# Define the connection string
connection_string = "mysql+mysqlconnector://my_user:my_password@localhost/cshot"

# Create the engine
engine = create_engine(connection_string, echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define the Player model
class Player(Base):
    __tablename__ = "cshot"
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique ID
    name = Column(String(50), nullable=False) 
    score = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Player(name={self.name}, score={self.score})>"

# Create all tables
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Context manager for session handling
@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# Function to create a new player
def create_player(name, score):
    with session_scope() as session:
        new_player = Player(name=name, score=score)
        session.add(new_player)

# Function to fetch all players
def select_players():
    with session_scope() as session:
        players = session.query(Player).all()
        result = [{"name": player.name, "score": player.score} for player in players]
        return result

if __name__ == "__main__":

    create_player("Ali", 53)
    create_player("Ali", 43)
    create_player("Amin", 70)

    players = select_players()
    for player in players:
        print(player["name"], player["score"])
