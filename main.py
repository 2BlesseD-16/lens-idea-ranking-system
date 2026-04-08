class Idea:
    def __init__(self, name, creativity, trend, ease, engagement):
        self.name = name
        self.creativity = creativity
        self.trend = trend
        self.ease = ease
        self.engagement = engagement
        self.score = 0

    def calculate_score(self):
        import random

        trend_boost = random.randint(0, 2)

        self.score = (
            self.creativity * 2 +
            (self.trend + trend_boost) * 3 +
            self.ease * 1 +
            self.engagement * 4
        )

    def explain_score(self):
        reasons = []

        if self.engagement >= 8:
            reasons.append("high engagement")

        if self.trend >= 8:
            reasons.append("strong trend relevance")

        if self.creativity >= 8:
            reasons.append("very creative")

        if self.ease >= 8:
            reasons.append("easy to build")

        return ", ".join(reasons)

    def __str__(self):
        return f"Idea: {self.name}, Score: {self.score}"
    
    def generate_insight(self):
        if self.score >= 80:
            return "High potential viral lens"
        elif self.score >= 70:
            return "Strong candidate for development"
        elif self.score >= 60:
            return "Moderate potential"
        else:
            return "Low priority idea"

def create_idea():
    name = input("Enter idea name: ")
    creativity = int(input("Creativity (1-10): "))
    trend = int(input("Trend relevance (1-10): "))
    ease = int(input("Ease of build (1-10): "))
    engagement = int(input("Engagement potential (1-10): "))

    return Idea(name, creativity, trend, ease, engagement)

def search_idea(ideas):
    query = input("Search for an idea: ").lower()

    found = False

    for idea in ideas:
        if query in idea.name.lower():
            print(f"Found: {idea} → {idea.explain_score()}")
            found = True

    if not found:
        print("No matching ideas found.")

def filter_high_score(ideas):
    print("\nHigh Scoring Ideas:")

    found = False

    for idea in ideas:
        if idea.score >= 75:
            print(f"{idea} → {idea.explain_score()}")
            found = True

    if not found:
        print("No high scoring ideas found.")

def menu():
    print("\n=== Lens Idea System ===")
    print("1. Add Ideas")
    print("2. View Ranked Ideas")
    print("3. Search Ideas")
    print("4. Filter High Score Ideas")   
    print("5. Exit")

# Main program strats here
ideas = []

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            idea = create_idea()
            ideas.append(idea)

            cont = input("Add another idea? (yes/no): ")
            if cont.lower() != "yes":
                break

    elif choice == "2":
        for idea in ideas:
            idea.calculate_score()

        ideas.sort(key=lambda idea: idea.score, reverse=True)

        print("\nRanked Ideas:")
        for idea in ideas:
            print(f"{idea} → {idea.explain_score()} | Insight: {idea.generate_insight()}")

    elif choice == "3":
        search_idea(ideas)

    elif choice == "4":
        filter_high_score(ideas)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Try again.")