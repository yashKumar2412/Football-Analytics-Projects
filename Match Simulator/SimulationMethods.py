import random

def is_goal(xg):
    
    num = random.randrange(1000)
    
    if num < xg:
        return 1
    else:
        return 0

def preprocess_data(xg_home, xga_home, xg_away, xga_away):
    
    calc_xg_home = round((xg_home * xga_away) / 90, 3) * 1000
    calc_xg_away = round((xg_away * xga_home) / 90, 3) * 1000
    
    return calc_xg_home, calc_xg_away

def match_sim(sample_size, xg_home, xga_home, xg_away, xga_away):
    
    xg_home_input, xg_away_input = preprocess_data(xg_home, xga_home, xg_away, xga_away)
    
    c = 0
    total_goals_home = 0
    total_goals_away = 0
    home_wins = 0
    away_wins = 0
    draws = 0
    
    while c < sample_size:
        goal_home = 0
        goal_away = 0

        for min in range(90):
            goal_home = goal_home + is_goal(xg_home_input)
            goal_away = goal_away + is_goal(xg_away_input)
        
        if goal_home > goal_away:
            home_wins = home_wins + 1
        elif goal_home < goal_away:
            away_wins = away_wins + 1
        else:
            draws = draws + 1
        
        total_goals_home = total_goals_home + goal_home
        total_goals_away = total_goals_away + goal_away
        
        c = c + 1
    
    total_goals_home_p90 = round(total_goals_home / sample_size, 2)
    total_goals_away_p90 = round(total_goals_away / sample_size, 2)
    
    result_set = [home_wins, draws, away_wins]

    return total_goals_home_p90, total_goals_away_p90, result_set