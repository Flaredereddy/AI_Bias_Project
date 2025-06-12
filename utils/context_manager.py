
class ContextManager:
    def __init__(self):
        self.context = {
            "dataset": None,
            "target": None,
            "demographic": None,
            "model": None
        }
    def update_context(self, key, value):
        self.context[key] = value
    def get_context(self):
        return self.context
