def main():
    from sorting import random_numbers
    results = StudentsGrades(random_numbers(30, 0, 100))
    print(results.count())
    for i in range(results.count()):
        print(f'Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}')
    print(results.find(100))
    print(results.get_sorted())
    print(results.average())
    print(results.best())
    print(results.worst())
    print(results.pass_rate())
    print(results)

class StudentsGrades :
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        x = self.get_by_index(index)
        if x >= 90:
            return f'A'
        elif x >= 80:
            return f'B'
        elif x >= 70:
            return f'C'
        elif x >= 60:
            return f'D'
        elif x >= 50:
            return f'E'
        else:
            return f'F'

    def find(self, points):
        scores = self.scores
        students = []
        for i in range(len(scores)):
            if scores[i]==points:
                students.append(i)
        return students

    def get_sorted(self):
        scores = self.scores.copy()
        for j in range(len(scores) - 1):
            status = 0
            for i in range(len(scores) - 1 - j):
                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]
                    status += 1
            if status == 0:
                break
        return scores

    def average(self):
        return sum(self.scores)/self.count()

    def best(self):
        return max(self.scores)

    def worst(self):
        return min(self.scores)

    def pass_rate(self):
        pas = 0
        for i in self.scores:
            if i>=50:
                pas+=1
        return pas/self.count()

    def __str__(self):
        return f"StudentsGrades: {self.count()} studentů, průměr {self.average():.1f}"

main()