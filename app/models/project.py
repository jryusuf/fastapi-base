class Project:
    def __init__(self, name: str, status: str = 'Not Started'):
        self.name = name
        self.sources = []
        self.status = status

    def add_source(self, source):
        self.sources.append(source)

    def update_status(self, new_status: str):
        self.status = new_status
