import random

def gambler_stimulate(goal,trial,stake):
    win = 0
    total_bets = 0
    
    for _ in range(trial):
        cash = stake
        while 0 < cash < goal:# either has no cash or reached goal
            total_bets +=1
            if random.random() < 0.5:# 50-50% chage of either lossing or winning
                cash += 1
            else:
                cash -= 1
        if cash == goal:
            win += 1
    win_percent=(win/trial) * 100
    loss_percent=100 - win_percent
    
    print(f"Total Wins : {win}")
    print(f"Total Bets Made: {total_bets}")
    print(f"Win Percentage : {win_percent:.2f}%")
    print(f"Loss Percentage: {loss_percent:.2f}%")

gambler_stimulate(20,100,10)
