# Simple Chatbot

![Python](https://img.shields.io/badge/Python-3.8%2B-1f6feb?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Type-CLI-111827?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-2ea043?style=for-the-badge)

A minimal command-line chatbot that replies to a small set of predefined inputs. Built to practice control flow, input handling, and simple intent matching.

**Highlights**

- Interactive terminal loop with instant responses
- Deterministic intent matching for known phrases
- Clean exit with the `bye` command

**Tech**

- Python 3.8+

**How It Works**

The script reads user input, normalizes it to lowercase, and checks it against known phrases. If no match is found, it returns a default response.

**Run**

```bash
python chatbot.py
```

**Sample Session**

```text
Basic Chatbot
type 'bye' to exit.
You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: bye
Bot: Goodbye!
```

**Project Structure**

- `chatbot.py` - Main chatbot script
