import hashlib as h


class Block:
    def __init__(self, prev_hash, transaction):

        self.prev_hash = prev_hash
        self.transactions = transaction

        self.hash_string = transaction.string + prev_hash
        self.hash = h.sha256(self.hash_string.encode()).hexdigest()
