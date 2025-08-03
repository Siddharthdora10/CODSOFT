

books = [
    {"title": "Python Basics", "tags": ["python", "beginner", "programming"]},
    {"title": "Data Science", "tags": ["data", "pandas", "python", "analytics"]},
    {"title": "Machine Learning", "tags": ["ml", "algorithms", "data"]},
    {"title": "Web Development", "tags": ["html", "css", "web", "javascript"]},
    {"title": "Flask Guide", "tags": ["flask", "python", "web"]}
]

def recommend(user_input):
    input_keywords = user_input.lower().split()
    scores = []

    for book in books:
        match_count = 0
        for tag in book["tags"]:
            if tag.lower() in input_keywords:
                match_count += 1
        scores.append((match_count, book["title"]))

    scores.sort(reverse=True)
    best_match = scores[0]

    if best_match[0] == 0:
        return "Sorry, no suitable book found."
    else:
        return f"You might like: {best_match[1]}"

# Example usage
query = input("What kind of book are you interested in?\n> ")
result = recommend(query)
print(result)

