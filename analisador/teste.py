from textblob import TextBlob

texts = [
    "I love sunny days",
    "I hate rain",
    "This is just a normal day"
]

for text in texts:
    blob = TextBlob(text)
    print(f"Texto: '{text}'\nPolaridade: {blob.sentiment.polarity}\n")
