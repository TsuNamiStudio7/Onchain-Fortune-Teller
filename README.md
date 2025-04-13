# 🔮 Onchain Fortune Teller

A fun and creative Python app that gives you a random "onchain fortune" based on the latest Ethereum block hash. It’s deterministic, decentralized, and delightfully weird.

## 🧙‍♂️ What it does

Every time you run it, the script fetches the latest block hash from Ethereum Mainnet, seeds a random generator with that hash, and returns a "prophecy" chosen from a list of fortunes.

## 📦 Requirements

- Python 3.x
- `web3.py`

Install dependencies:

```bash
pip install web3
