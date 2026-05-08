class UsersHandler:
    def __init__(self, db):
        self.db = db

    async def nicks(self):
        return {'nicks': await self.db.users.nicks()}

    async def new_user(self, nick: str, user_id: int):
        await self.db.users.new(id=user_id, nick=nick)
        return {'ok': True}
