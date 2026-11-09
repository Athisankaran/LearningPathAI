import math

def dot(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    return sum(x * y for x, y in zip(a, b))

def magnitude(v: list[float]) -> float:
    return math.sqrt(dot(v, v))

def cosine_similarity(a: list[float], b: list[float]) -> float:
    return dot(a, b) / (magnitude(a) * magnitude(b))

vectors = {
    "cat":    [0.9, 0.8, 0.1, 0.0],
    "kitten": [0.85, 0.75, 0.15, 0.05],
    "car":    [0.0, 0.1, 0.9, 0.8],
    "truck":  [0.05, 0.2, 0.85, 0.9],
}

pairs = [("cat", "kitten"), ("cat", "car"), ("car", "truck"), ("kitten", "truck")]

for a, b in pairs:
    score = cosine_similarity(vectors[a], vectors[b])
    print(f"{a} vs {b}: {score:.3f}")

query = "dog"
query_vector = [0.88, 0.7, 0.2, 0.1]  # hand-made, pretend this is "dog"

ranked = []

for word, vec in vectors.items():
    score = cosine_similarity(query_vector, vec)
    ranked.append((word, score))

for word, score in ranked:
    print(f"{word}: {score:.3f}")