class QuizResultSearcher:
    def __init__(self, scores_dict):
        self.scores_dict = scores_dict
        self.scores_list = list(scores_dict.items())

    def direct_access(self, student_name):
        return self.scores_dict.get(student_name, "Student not found")

    def linear_search(self, target_score):
        for student, score in self.scores_list:
            if score == target_score:
                return student
        return "Score not found"

    def find_duplicate_scores(self):
        duplicates = []
        n = len(self.scores_list)
        for i in range(n):
            for j in range(i + 1, n):
                student1, score1 = self.scores_list[i]
                student2, score2 = self.scores_list[j]
                if score1 == score2:
                    duplicates.append((student1, student2, score1))
        return duplicates

if __name__ == "__main__":
    quiz_data = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 92,
        "Ethan": 88
    }

    searcher = QuizResultSearcher(quiz_data)

    print(searcher.direct_access('Bob'))
    print(searcher.linear_search(78))
    print(searcher.find_duplicate_scores())