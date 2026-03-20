from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Result:
    def __init__(self, score, total):
        self.score = score
        self.total = total
        self.time_submitted = datetime.now()

    def get_result(self):
        return f"Score: {self.score}/{self.total} at {self.time_submitted.strftime('%H:%M:%S')}"