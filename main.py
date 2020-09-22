from block import Block
from transactions import Transaction


def main():

    genesis_transaction = Transaction("Logan", "Dorian", 3)

    # initialize genesis
    genesis_block = Block("wow you're cool if you find this message...", genesis_transaction)

    second_transaction = Transaction("Terry", "Bob", 42)
    second_block = Block(genesis_block.hash, second_transaction)

    print(genesis_block.hash)
    print(second_block.hash)


# by default run main method
if __name__ == "__main__":
    main()
