import numpy as np

import tkinter as tk

# Fenster und Eingabefelder
window = tk.Tk()
window.title("Beachvolleyball-Strategie")
window.geometry('400x300')

team_a_label = tk.Label(window, text="Spielstärke Team A (0-10): ")
team_a_label.pack()
team_a_input = tk.Entry(window)
team_a_input.pack()

team_b_label = tk.Label(window, text="Spielstärke Team B (0-10): ")
team_b_label.pack()
team_b_input = tk.Entry(window)
team_b_input.pack()

play_button = tk.Button(window, text="Simulation starten", command=lambda: simulate_game(int(team_a_input.get()), int(team_b_input.get())))
play_button.pack()

result_label = tk.Label(window)
result_label.pack()

# Simulation
def simulate_game(team_a_strength, team_b_strength):
    team_a_risk = 5
    team_b_risk = 5
    team_a_score = 0
    team_b_score = 0

    while abs(team_a_score - team_b_score) < 2 or (team_a_score < 21 and team_b_score < 21):
        # Simuliere einen Ballwechsel
        team_a_win_chance = np.random.normal(loc=team_a_strength, scale=10-team_a_risk)
        team_b_win_chance = np.random.normal(loc=team_b_strength, scale=10-team_b_risk)
        if team_a_win_chance > team_b_win_chance:
            team_a_score += 1
        else:
            team_b_score += 1

        # Entscheide, ob die Teams ihr Risiko ändern
        if team_a_score == team_b_score:
            team_a_risk = np.clip(team_a_risk + np.random.randint(-1, 2), 0, 10)
            team_b_risk = np.clip(team_b_risk + np.random.randint(-1, 2), 0, 10)
        elif team_a_score > team_b_score:
            team_a_risk = np.clip(team_a_risk + np.random.randint(-1, 1), 0, 10)
            team_b_risk = np.clip(team_b_risk + np.random.randint(-2, 1), 0, 10)
        else:
            team_a_risk = np.clip(team_a_risk + np.random.randint(-2, 1), 0, 10)
            team_b_risk = np.clip(team_b_risk + np.random.randint(-1, 1), 0, 10)

    if team_a_score > team_b_score:
        result_label.config(text="Team A hat gewonnen!")
    else:
        result_label.config(text="Team B hat gewonnen!")

# Starte das Fenster
window.mainloop()
