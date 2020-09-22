import hashlib as h


class Transaction:
    def __init__(self, sender, recipient, amount):

        self.sender = sender
        self.recipient = recipient
        self.amount = amount

        string_to_encode = self.sender+self.recipient+str(self.amount)

        self.string = h.sha256(string_to_encode.encode()).hexdigest()
