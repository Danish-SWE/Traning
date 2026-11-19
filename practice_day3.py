# inheritance in python
class Research:
    def __init__(self, title, method):
        self.title = title
        self.method = method

    def show_research_info(self):
        print("Research Title :", self.title)
        print("Research Method :", self.method)


class SurveyResearch(Research):
    def __init__(self, title, duration, sample_size):
        super().__init__(title, method="Survey")
        self.duration = duration
        self.sample_size = sample_size

    def show_details(self):
        self.show_research_info()
        print("Duration :", self.duration)
        print("Sample Size :", self.sample_size)


project = SurveyResearch("Review to Backlog", "Two months", 120)
project.show_details()