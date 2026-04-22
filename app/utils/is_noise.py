IGNORE_KEYWORDS = [
    "login",
    "signup",
    "menu",
    "navigation",
    "search",
    "filter",
    "tools",
    "features",
    "api access",
    "privacy",
    "cookie",
    "terms",
]

def is_noise(text: str):
    text = text.lower()
    return any(keyword in text for keyword in IGNORE_KEYWORDS)