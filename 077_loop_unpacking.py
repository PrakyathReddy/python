from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    listt=[]
    for x,y in scores:
        listt.append(y)
    listt.sort(reverse=True)
    highest_score=listt[0]
    for a,b in scores:
        if b==highest_score:
            return a


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
