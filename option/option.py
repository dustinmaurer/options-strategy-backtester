"""The Option oobject stores (or solves for) all attributes of an option"""
import scipy.stats as sps
import numpy as np
from datetime import date, timedelta

class Option:
    def __init__(self, underlying, kind, strike, expiration, iv=.2, value=None, delta=None):
        """
        A class used to represent a European style Option contract

        ...

        Attributes
        ----------
        underlying : str
            the name of the underyling security for the option
        kind : str
            either 'put' or 'call'
        kind_val : int
            puts are represented by 1 calls by -1 since usually we deal with short options
        strike : float
            the price at which the option would be executed
        expiration : date
            the date that the option expires
        iv : float
            the implied volatility of the option
        value : float
            the current theoretic value of the option
        delta : int
            the current theoretic delta of the option

        Functions
        -------
        getValue(underlyingPrice, date, iv)
            Calculates the value of the option
        """

        if type(underlying) is not str:
          raise TypeError("The underlying must be a string.")
        self.underlying = underlying

        if kind.lower() not in ["put","call"]:
          raise TypeError("The option must be either a put or a call.")
        self.kind = kind.lower()
        self.kind_value = 1 if self.kind == "put" else -1

        if strike <= 0:
          raise TypeError("The option strike must be positive.")
        self.strike = strike

        if type(expiration) is not date:   
          try:
            expiration = date.fromisoformat(expiration)
          except:
            raise TypeError("Expiration must be a date.")
        self.expiration = expiration

        self.iv = iv
        self.value = value
        self.delta = delta
        self.interest_rate = 0




    def getValue(self, price, eval_date):
      """
      Calculates the value of the option
      """
      if type(eval_date) is not date:   
        try:
          eval_date = date.fromisoformat(eval_date)
        except:
          raise TypeError("Expiration must be a date.")

      time_delta = self.expiration - eval_date + timedelta(days = 1)
      if time_delta.days <= 0:
        if self.kind == "put":
          if self.strike <= price:
            return 0
          else:
            return price - self.strike
        else:
          if self.strike >= price:
            return 0
          else:
            return self.strike - price

      time = time_delta.days / 365.0

      d1 = (np.log(price / self.strike) + .5 * self.iv ** 2 * time) / self.iv / np.sqrt(time)
      d2 = d1 - self.iv * np.sqrt(time)
      value = self.kind_value * price * sps.norm.cdf( self.kind_value * d1 ) - self.kind_value * self.strike * sps.norm.cdf( self.kind_value * d2 )

      return value




