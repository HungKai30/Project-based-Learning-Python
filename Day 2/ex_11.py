students_scores = {
    "Alice": {"class": "Math", "score": 85},
    "Bob": {"class": "Science", "score": 90},
    "Charlie": {"class": "Math", "score": 95},
    "David": {"class": "History", "score": 80},
    "Eva": {"class": "Science", "score": 95},
    "Frank": {"class": "Math", "score": 70},
    "Grace": {"class": "History", "score": 85},
    "Hung": {"class": "Science", "score": 90}
}
highest_score = 0
top_students = []

for student, details in students_scores.items():
    if details["score"] > highest_score:
        highest_score = details["score"]
        top_students = [student]
    elif details["score"] == highest_score:
        top_students.append(student)

print("Top students with the highest score:", top_students)