from members.model import MemberDao

class MemberController:
    def __init__(self):
        self.dao = MemberDao()

    def create_table(self):
        self.dao.create()
        # self.dao.insert_many()
        self.dao.fetch_all()

    def login(self, userid, password):
        row = self.dao.login(userid, password)
        if row is None:
            view = 'intro.html'
        else:
            view = 'index.html'
        return view