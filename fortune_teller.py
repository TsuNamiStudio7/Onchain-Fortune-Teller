from web3 import Web3
import os
import random

# Connect to Ethereum (Infura or other RPC provider)
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check connection
if not w3.isConnected():
    print("🔌 Failed to connect to Ethereum network.")
    exit()

# Example fortune messages
FORTUNES = [
    "🤑 Riches are coming your way.",
    "🚀 You will ape into a gem… or a rug.",
    "🤔 Be cautious with that next transaction.",
    "💖 Love awaits you… in the metaverse.",
    "🦉 Owls are watching, make wise choices.",
    "🧪 A DAO will invite you soon.",
    "💼 Big deal on-chain. Don't miss it.",
    "🥷 Trust no one. Especially not anonymous devs.",
    "🌌 You’re about to discover a forgotten wallet.",
    "🧠 Your next idea will go viral on Farcaster."
]

def get_latest_block_hash():
    latest_block = w3.eth.get_block('latest')
    return latest_block.hash.hex()

def generate_fortune():
    block_hash = get_latest_block_hash()
    random.seed(block_hash)
    fortune = random.choice(FORTUNES)
    return block_hash, fortune

def main():
    print("🔮 Welcome to the Onchain Fortune Teller 🔮")
    input("Press Enter to reveal your fortune from the Ethereum gods...\n")
    block_hash, fortune = generate_fortune()
    print(f"🌐 Based on block hash: {block_hash}")
    print(f"💬 Your onchain prophecy: {fortune}")

if __name__ == "__main__":
    main()
