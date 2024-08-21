import matplotlib.pyplot as plt
import random

class Player:
    def __init__(self, name, age, role):
        # Initialize player attributes
        self.name = name
        self.age = age
        self.role = role
        self.matches_played = 0
        self.runs = 0
        self.wickets = 0
        self.catches = 0
        self.stumpings = 0
        self.run_outs = 0
        self.fielding_position = None

    def update_fielding_position(self, position):
        # Update fielding position
        self.fielding_position = position

    def add_match_stats(self, runs=0, wickets=0, catches=0, stumpings=0, run_outs=0):
        # Add stats for a match
        self.matches_played += 1
        self.runs += runs
        self.wickets += wickets
        self.catches += catches
        self.stumpings += stumpings
        self.run_outs += run_outs

    def display_player_stats(self):
        # Display player stats
        print(f"Player Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Role: {self.role}")
        print(f"Matches Played: {self.matches_played}")
        print(f"Runs: {self.runs}")
        print(f"Wickets: {self.wickets}")
        print(f"Catches: {self.catches}")
        print(f"Stumpings: {self.stumpings}")
        print(f"Run Outs: {self.run_outs}")
        print(f"Fielding Position: {self.fielding_position}")
        print("-" * 40)

# Example Usage
player1 = Player("Kishan Kumar", 30, "Batsman")
player1.update_fielding_position("Slip")
player1.add_match_stats(runs=50, catches=1)
player1.display_player_stats()

class Batsman(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="Batsman")
        self.strike_rate = 0.0
        self.batting_average = 0.0

    def calculate_strike_rate(self, runs_scored, balls_faced):
        # Calculate strike rate
        self.strike_rate = (runs_scored / balls_faced) * 100

    def calculate_batting_average(self, total_runs, dismissals):
        # Calculate batting average
        self.batting_average = total_runs / dismissals if dismissals > 0 else total_runs

    def display_player_stats(self):
        # Display batsman stats
        super().display_player_stats()
        print(f"Strike Rate: {self.strike_rate}")
        print(f"Batting Average: {self.batting_average}")
        print("=" * 40)

# Example Usage
batsman1 = Batsman("Demo Batsman", 25)
batsman1.add_match_stats(runs=200)
batsman1.calculate_strike_rate(200, 150)
batsman1.calculate_batting_average(200, 4)
batsman1.display_player_stats()

class Bowler(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="Bowler")
        self.economy_rate = 0.0
        self.bowling_average = 0.0
        self.wickets_against_positions = {}

    def calculate_economy_rate(self, runs_conceded, overs_bowled):
        # Calculate economy rate
        self.economy_rate = runs_conceded / overs_bowled

    def calculate_bowling_average(self, runs_conceded, wickets_taken):
        # Calculate bowling average
        self.bowling_average = runs_conceded / wickets_taken if wickets_taken > 0 else 0.0

    def add_wicket_against_position(self, batting_position):
        # Add a wicket against a specific batting position
        if batting_position in self.wickets_against_positions:
            self.wickets_against_positions[batting_position] += 1
        else:
            self.wickets_against_positions[batting_position] = 1

    def display_player_stats(self):
        # Display bowler stats
        super().display_player_stats()
        print(f"Economy Rate: {self.economy_rate}")
        print(f"Bowling Average: {self.bowling_average}")
        print("=" * 40)

# Example Usage
bowler1 = Bowler("Demo Bowler", 28)
bowler1.add_match_stats(wickets=5)
bowler1.calculate_economy_rate(120, 10)
bowler1.calculate_bowling_average(120, 5)
bowler1.add_wicket_against_position(1)  # Wicket against top-order batsman
bowler1.display_player_stats()

class AllRounder(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="All-Rounder")
        # Initialize both Batsman and Bowler attributes
        self.strike_rate = 0.0
        self.batting_average = 0.0
        self.economy_rate = 0.0
        self.bowling_average = 0.0

    def calculate_strike_rate(self, runs_scored, balls_faced):
        # Calculate strike rate
        self.strike_rate = (runs_scored / balls_faced) * 100

    def calculate_batting_average(self, total_runs, dismissals):
        # Calculate batting average
        self.batting_average = total_runs / dismissals if dismissals > 0 else total_runs

    def calculate_economy_rate(self, runs_conceded, overs_bowled):
        # Calculate economy rate
        self.economy_rate = runs_conceded / overs_bowled

    def calculate_bowling_average(self, runs_conceded, wickets_taken):
        # Calculate bowling average
        self.bowling_average = runs_conceded / wickets_taken if wickets_taken > 0 else 0.0

    def display_player_stats(self):
        # Display all-rounder stats
        super().display_player_stats()
        print(f"Strike Rate: {self.strike_rate}")
        print(f"Batting Average: {self.batting_average}")
        print(f"Economy Rate: {self.economy_rate}")
        print(f"Bowling Average: {self.bowling_average}")
        print("=" * 40)

# Example Usage
allrounder1 = AllRounder("Demo All Rounder", 27)
allrounder1.add_match_stats(runs=100, wickets=3)
allrounder1.calculate_strike_rate(100, 80)
allrounder1.calculate_batting_average(100, 2)
allrounder1.calculate_economy_rate(80, 10)
allrounder1.calculate_bowling_average(80, 3)
allrounder1.display_player_stats()

class WicketKeeper(Batsman):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.role = "Wicket-Keeper"
        self.stumpings = 0

    def add_stumping(self):
        # Add a stumping
        self.stumpings += 1

# Example Usage
keeper1 = WicketKeeper("Demo Wicketkeeper", 24)
keeper1.add_match_stats(runs=70, stumpings=2)
keeper1.add_stumping()
keeper1.calculate_strike_rate(70, 50)
keeper1.calculate_batting_average(70, 3)
keeper1.display_player_stats()

class ScoringSystem:
    def __init__(self):
        self.total_runs = 0
        self.wickets = 0
        self.extras = 0
        self.over_details = []

    def add_runs(self, runs, shot_type="normal"):
        # Add runs with different shot types
        if shot_type == "normal":
            self.total_runs += runs
        elif shot_type in ["bye", "leg_bye", "overthrow"]:
            self.extras += runs
            self.total_runs += runs

    def add_extras(self, extra_type, runs=1):
        # Add extras (wide, no-ball)
        if extra_type in ["wide", "no-ball"]:
            self.extras += runs
            self.total_runs += runs

    def simulate_over(self, over_number, runs_scored, wickets_lost, is_powerplay=False, is_death_over=False):
        # Simulate an over with optional powerplay and death over bonuses
        if is_powerplay:
            runs_scored += int(runs_scored * 0.2)  # 20% boost
        elif is_death_over:
            runs_scored += int(runs_scored * 0.3)  # 30% boost

        self.total_runs += runs_scored
        self.wickets += wickets_lost
        self.over_details.append((over_number, runs_scored, wickets_lost))

    def calculate_net_run_rate(self, overs_bowled):
        # Calculate net run rate
        return self.total_runs / overs_bowled if overs_bowled > 0 else 0.0

# Example Usage
scoring = ScoringSystem()
scoring.add_runs(10)
scoring.add_extras("wide", 5)
scoring.simulate_over(1, 30, 1, is_powerplay=True)
print("Total Runs:", scoring.total_runs)
print("Extras:", scoring.extras)
print("Net Run Rate:", scoring.calculate_net_run_rate(1))

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        # Add a player to the team
        if isinstance(player, Player):
            self.players.append(player)

    def calculate_team_average_strike_rate(self):
        # Calculate average strike rate for batsmen
        total_strike_rate = sum(p.strike_rate for p in self.players if isinstance(p, Batsman))
        total_batsmen = len([p for p in self.players if isinstance(p, Batsman)])
        return total_strike_rate / total_batsmen if total_batsmen > 0 else 0.0

    def calculate_team_bowling_economy(self):
        # Calculate average economy rate for bowlers
        total_economy = sum(p.economy_rate for p in self.players if isinstance(p, Bowler))
        total_bowlers = len([p for p in self.players if isinstance(p, Bowler)])
        return total_economy / total_bowlers if total_bowlers > 0 else 0.0

# Example Usage
team = Team("Warriors")
team.add_player(batsman1)
team.add_player(bowler1)
print("Team Average Strike Rate:", team.calculate_team_average_strike_rate())
print("Team Bowling Economy Rate:", team.calculate_team_bowling_economy())

class PlayerComparison:
    @staticmethod
    def compare_batsmen(batsman1, batsman2):
        # Compare two batsmen
        print(f"Comparing {batsman1.name} and {batsman2.name}:")
        print(f"{batsman1.name} - Strike Rate: {batsman1.strike_rate}, Batting Average: {batsman1.batting_average}")
        print(f"{batsman2.name} - Strike Rate: {batsman2.strike_rate}, Batting Average: {batsman2.batting_average}")

    @staticmethod
    def compare_bowlers(bowler1, bowler2):
        # Compare two bowlers
        print(f"Comparing {bowler1.name} and {bowler2.name}:")
        print(f"{bowler1.name} - Economy Rate: {bowler1.economy_rate}, Bowling Average: {bowler1.bowling_average}")
        print(f"{bowler2.name} - Economy Rate: {bowler2.economy_rate}, Bowling Average: {bowler2.bowling_average}")

# Example Usage
PlayerComparison.compare_batsmen(batsman1, Batsman("Eve White", 26))
PlayerComparison.compare_bowlers(bowler1, Bowler("Frank Black", 32))

class MatchSimulator:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_score = ScoringSystem()
        self.team2_score = ScoringSystem()

    def simulate_match(self):
        # Simulate match between two teams
        print(f"Simulating match between {self.team1.team_name} and {self.team2.team_name}...")
        self.simulate_innings(self.team1, self.team1_score)
        self.simulate_innings(self.team2, self.team2_score)

        print(f"Final Scores:\n{self.team1.team_name}: {self.team1_score.total_runs}/{self.team1_score.wickets}")
        print(f"{self.team2.team_name}: {self.team2_score.total_runs}/{self.team2_score.wickets}")

        if self.team1_score.total_runs > self.team2_score.total_runs:
            print(f"{self.team1.team_name} wins!")
        else:
            print(f"{self.team2.team_name} wins!")

    def simulate_innings(self, team, scoring_system):
        # Simulate innings with 20 overs
        for over in range(1, 21):
            runs = random.randint(20, 50)  # Random runs for the over
            wickets = random.randint(0, 2)  # Random wickets lost
            is_powerplay = over <= 6
            is_death_over = over >= 16
            scoring_system.simulate_over(over, runs, wickets, is_powerplay, is_death_over)

# Example Usage
team1 = Team("Team A")
team2 = Team("Team B")
team1.add_player(batsman1)
team1.add_player(bowler1)
team2.add_player(AllRounder("George White", 29))
match_simulator = MatchSimulator(team1, team2)
match_simulator.simulate_match()

class DataVisualization:
    @staticmethod
    def plot_player_performance(players):
        # Plot player performance in terms of runs and wickets
        names = [player.name for player in players]
        runs = [player.runs for player in players]
        wickets = [player.wickets for player in players]

        fig, ax = plt.subplots(2, 1, figsize=(10, 8))

        ax[0].bar(names, runs, color='blue')
        ax[0].set_title('Player Runs')
        ax[0].set_ylabel('Runs')

        ax[1].bar(names, wickets, color='red')
        ax[1].set_title('Player Wickets')
        ax[1].set_ylabel('Wickets')

        plt.tight_layout()
        plt.show()

# Example Usage
players = [batsman1, bowler1, allrounder1]
DataVisualization.plot_player_performance(players)


