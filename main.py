class Team:
    def _init_(self, name, captain, players,score):
        self.name = name
        self.captain = captain
        self.players = players
        self.score=score

    def update(self, name=None, captain=None, players=None,score=None):
        if name:
            self.name = name
        if captain:
            self.captain = captain
        if players:
            self.players = players
        if score:
            self.score=score    


class League:
    def _init_(self):
        self.teams = []

    def add_team(self):
        name = input("Enter team name: ")
        captain = input("Enter the captain name: ")
        score=input("Enter the score:")
        while True:
            try:
                players = int(input("Enter number of players: "))
                break
            except ValueError:
                print("Please enter a valid number for players:")
        new_team = Team(name, captain, players,score)
        self.teams.append(new_team)
        print(f"Team {name} added successfully!\n")

    def display_teams(self):
        if not self.teams:
            print("No teams in the league yet.")
            return
        print("\nTeams in the League:")
        for i, team in enumerate(self.teams):
            print(f"Team {i + 1}: {team.name}, Captain: {team.captain}, Players: {team.players},score:{team.score}")

    def update_team(self):
        self.display_teams()
        try:
            team_index = int(input("\nEnter the number of the team you want to update: ")) - 1
            if 0 <= team_index < len(self.teams):
                team = self.teams[team_index]
                name = input(f"Enter new name for {team.name}:")
                captain = input(f"Enter new captain for {name}:")
                score=input(f"Enter the new score for{name}:")
                while True:
                    players = input(f"Enter new number of players for {name} : ")
                    if players:
                        try:
                            players = int(players)
                            break
                        except ValueError:
                            print("Please enter a valid number for players.")
                    else:
                        players = team.players
                        break
                team.update(name,captain, players,score)
                print(f"Team {team.name} updated successfully!\n")
            else:
                print("Invalid team number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def delete_team(self):
        self.display_teams()
        try:
            team_index = int(input("\nEnter the number of the team you want to delete: ")) - 1
            if 0 <= team_index < len(self.teams):
                team = self.teams.pop(team_index)
                print(f"Team {team.name} deleted successfully!\n")
            else:
                print("Invalid team number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def menu():
    league = League()
    while True:
        print("\nSports League Management System")
        print("1. Add Team")
        print("2. Display Teams")
        print("3. Update Team")
        print("4. Delete Team")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            league.add_team()
        elif choice == '2':
            league.display_teams()
        elif choice == '3':
            league.update_team()
        elif choice == '4':
            league.delete_team()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    menu()
