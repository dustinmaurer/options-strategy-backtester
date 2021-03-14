"""The Option oobject stores (or solves for) all attributes of an option"""
from datetime import date

class Option():
    def __init__(self, kind, strike, expiration):
        if kind.lower() not in ["put","call"]:
            raise TypeError("The option must be either a put or a call.")
        self.kind = 1 if kind.lower() == "put" else -1

        if strike <= 0:
            raise TypeError("The option strike must be positive.")
        self.strike = strike

        if type(expiration) is not date:   
            try:
                expiration = date.fromisoformat(expiration)
            except:
                raise TypeError("Expiration must be a date.")
        self.expiration = expiration