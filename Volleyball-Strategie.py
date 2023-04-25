import random

def simulate_game(team_a_strength, team_b_strength, team_a_risk, team_b_risk):
    """
    Simuliert ein Spiel zwischen zwei Mannschaften mit gegebenen Spielstärken und Risikostrategien.
    Gibt den Gewinner des Spiels zurück (1 für Mannschaft A, 2 für Mannschaft B).
    """
    score_a = 0
    score_b = 0
    while abs(score_a - score_b) < 2 or max(score_a, score_b) < 21:
        risk_a = random.uniform(-team_a_risk, team_a_risk)
        risk_b = random.uniform(-team_b_risk, team_b_risk)
        if random.random() < (team_a_strength + risk_a) / (team_a_strength + team_b_strength + risk_a + risk_b):
            score_a += 1
        else:
            score_b += 1
    return 1 if score_a > score_b else 2

def find_optimal_risk(team_a_strength, team_b_strength):
    """
    Findet die optimale Risikostrategie für Mannschaft A gegen Mannschaft B.
    Gibt das optimale Risiko für Mannschaft A zurück.
    """
    best_risk = 0
    best_wins = 0
    for risk in range(11):
        wins = 0
        for _ in range(1000):
            if simulate_game(team_a_strength, team_b_strength, risk, 5) == 1:
                wins += 1
        if wins > best_wins:
            best_wins = wins
            best_risk = risk
    return best_risk

# Beispiel: Mannschaft A hat Spielstärke 6, Mannschaft B hat Spielstärke 8
team_a_strength = 6
team_b_strength = 8

# Berechne die optimale Risikostrategie für Mannschaft A
optimal_risk = find_optimal_risk(team_a_strength, team_b_strength)

print(f"Die optimale Risikostrategie für Mannschaft A ist: {optimal_risk}")
