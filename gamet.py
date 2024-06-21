import random
import matplotlib.pyplot as plt

# Define payoffs
PAYOFFS = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1)
}

class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.history = []

    def make_choice(self, opponent_history):
        if self.strategy == 'tit_for_tat':
            return 'C' if not opponent_history or opponent_history[-1] == 'C' else 'D'
        elif self.strategy == 'always_cooperate':
            return 'C'
        elif self.strategy == 'always_defect':
            return 'D'
        elif self.strategy == 'random':
            return random.choice(['C', 'D'])
        elif self.strategy == 'grim_trigger':
            return 'D' if 'D' in opponent_history else 'C'
        else:
            raise ValueError("Unknown strategy")

def play_round(player1, player2):
    choice1 = player1.make_choice(player2.history)
    choice2 = player2.make_choice(player1.history)
    player1.history.append(choice1)
    player2.history.append(choice2)
    return PAYOFFS[(choice1, choice2)]

def simulate_game(strategy1, strategy2, rounds=10):
    player1 = Player(strategy1)
    player2 = Player(strategy2)
    scores = [0, 0]
    for _ in range(rounds):
        score1, score2 = play_round(player1, player2)
        scores[0] += score1
        scores[1] += score2
    return scores

# Test different strategy pairings
strategies = ['tit_for_tat', 'always_cooperate', 'always_defect', 'random', 'grim_trigger']
results = {}

for strat1 in strategies:
    for strat2 in strategies:
        result = simulate_game(strat1, strat2, 100)
        results[(strat1, strat2)] = result

# Display the results
for (strat1, strat2), scores in results.items():
    print(f"{strat1} vs {strat2}: {scores}")

# Prepare data for plotting
labels = []
player1_scores = []
player2_scores = []

for (strat1, strat2), scores in results.items():
    labels.append(f"{strat1} vs {strat2}")
    player1_scores.append(scores[0])
    player2_scores.append(scores[1])

y = range(len(labels))

# Plot the results
fig, ax = plt.subplots()
bar_width = 0.35

bar1 = ax.barh(y, player1_scores, bar_width, label='Player 1')
bar2 = ax.barh([i + bar_width for i in y], player2_scores, bar_width, label='Player 2')

ax.set_ylabel('Strategy Pairings')
ax.set_xlabel('Scores')
ax.set_title('Prisoner\'s Dilemma Strategy Outcomes')
ax.set_yticks([i + bar_width / 2 for i in y])
ax.set_yticklabels(labels)
ax.legend()

plt.tight_layout()
plt.show()
