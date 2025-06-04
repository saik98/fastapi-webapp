from app.models.user import User

# Fake in-memory database for now
fake_users_db = []

def get_all_users() -> list[User]:
    return fake_users_db

def create_user(user: User) -> User:
    fake_users_db.append(user)
    return user