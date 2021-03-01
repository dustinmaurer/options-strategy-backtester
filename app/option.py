"""The Option oobject stores (or solves for) all attributes of an option"""

class Option():
    def __init__(self, kind):
        if kind.lower() not in ["put","call"]:
            raise TypeError("The option must be either a put or a call.")
        self.kind = 1 if kind.lower() == "put" else -1