import random
import tkinter as tk
from team import *
from player import *
from league import *


def createTeams():
    tOp1 = Player(70, 80, 35, 70, "Todd Simmions")
    tOp2 = Player(80, 60, 40, 85, "Joaquin Bolívar")
    tOp3 = Player(50, 85, 80, 75, "Winthrop Cavalcante")
    tOP4 = Player(40, 90, 80, 45, "Dwain Hubert")
    tOp5 = Player(35, 95, 95, 30, "Colson Pocock")
    teamOne = [tOp1, tOp2, tOp3, tOP4, tOp5]

    tTp1 = Player(70, 80, 35, 70, "Herminio Carmona")
    tTp2 = Player(80, 60, 40, 85, "Saint Ward")
    tTp3 = Player(50, 85, 80, 75, "Lindy Fermi")
    tTP4 = Player(40, 90, 80, 45, "Boubacar Readdie")
    tTp5 = Player(35, 95, 95, 30, "Jonás Arreola")
    teamTwo = [tTp1, tTp2, tTp3, tTP4, tTp5]

    tThp1 = Player(70, 80, 35, 70, "Alberto Palmer")
    tThp2 = Player(80, 60, 40, 85, "Christopher Howard")
    tThp3 = Player(50, 85, 80, 75, "Bernard Garrett")
    tThP4 = Player(40, 90, 80, 45, "Tim Davis")
    tThp5 = Player(35, 95, 95, 30, "Myron Soto")
    teamThree = [tThp1, tThp2, tThp3, tThP4, tThp5]

    tFp1 = Player(70, 80, 35, 70, "Alberto Palmer")
    tFp2 = Player(80, 60, 40, 85, "Christopher Howard")
    tFp3 = Player(50, 85, 80, 75, "Bernard Garrett")
    tFP4 = Player(40, 90, 80, 45, "Tim Davis")
    tFp5 = Player(35, 95, 95, 30, "Myron Soto")
    teamFour = [tFp1, tFp2, tFp3, tFP4, tFp5]

    return teamOne, teamTwo, teamThree, teamFour


def play(t):
    score = 0
    for p in t.getPlayer():
        p.setGameStat(0)
        for x in range(25):
            playType = random.randrange(1, 4)
            shotSuccess = random.randrange(1, 10)
            if playType == 1:
                overall = p.getThree()
                if overall >= 90:
                    if shotSuccess <= 5:
                        score = score + 3
                        p.setGameStat(p.getGameStat() + 3)

                elif (overall <= 89) & (overall > 70):
                    if shotSuccess <= 4:
                        score = score + 3
                        p.setGameStat(p.getGameStat() + 3)
                elif (overall <= 79) & (overall > 60):
                    if shotSuccess <= 3:
                        score = score + 3
                        p.setGameStat(p.getGameStat() + 3)
                else:
                    if shotSuccess == 1:
                        score = score + 3
                        p.setGameStat(p.getGameStat() + 3)

            elif playType == 2:
                overall = p.getLayup()
                if overall >= 90:
                    if shotSuccess <= 5:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
                elif (overall <= 89) & (overall > 70):
                    if shotSuccess <= 4:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
                elif (overall <= 79) & (overall > 60):
                    if shotSuccess <= 3:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
                else:
                    if shotSuccess == 1:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
            elif playType == 3:
                overall = p.getDunk()
                if overall >= 90:
                    if shotSuccess <= 5:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
                elif (overall <= 89) & (overall > 70):
                    if shotSuccess <= 4:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
                elif (overall <= 79) & (overall > 60):
                    if shotSuccess <= 3:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
                else:
                    if shotSuccess == 1:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
            elif playType == 4:
                overall = p.getMid()
                if overall >= 90:
                    if shotSuccess <= 5:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
                elif (overall <= 89) & (overall > 70):
                    if shotSuccess <= 4:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
                elif (overall <= 79) & (overall > 60):
                    if shotSuccess <= 3:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
                else:
                    if shotSuccess == 1:
                        score = score + 2
                        p.setGameStat(p.getGameStat() + 2)
        p.setSeasonStat(p.getGameStat())
    return score


def match(homeTeam, awayTeam):
    homeScore = play(homeTeam)
    awayScore = play(awayTeam)

    if homeScore > awayScore:
        homeTeam.updateWins()
        awayTeam.updateLoss()
    else:
        awayTeam.updateWins()
        homeTeam.updateLoss()

    print(homeTeam.getName(), "(", homeTeam.getWins(), "-", homeTeam.getLoss(), ")", homeScore, "      ",
          awayTeam.getName(),  "(", awayTeam.getWins(), "-", awayTeam.getLoss(), ")", awayScore, "\n")
    teamStats(homeTeam, homeTeam.getName())
    print("\n")
    teamStats(awayTeam, awayTeam.getName())


def teamStats(team, teamName):
    print(teamName, " Game Stats:")
    for p in team.players:
        print(p.getName(), "Points: ", p.getGameStat())


window = tk.Tk()
frame = tk.Frame(master=window, width=600, height=600, bg="#687FA1")
frame.pack()
title = tk.Label(master=frame, text="Basketball Simulator", bg="#687FA1", fg="white", font=("Modern", 30))
title.place(x=165, y=0)


def playButtonTask():

    teamName_A = tk.Label(master=frame, text="Team 1", bg="#687FA1", fg="white", font=("Modern", 20))
    teamName_A.place(x=80, y=100)
    teamName_B = tk.Label(master=frame, text="Team 2", bg="#687FA1", fg="white", font=("Modern", 20))
    teamName_B.place(x=420, y=100)
    teamOne, teamTwo = createTeams()
    tOScoreLabel = play(teamOne)
    tTScoreLabel = play(teamTwo)
    tOScoreLabel = str(tOScoreLabel)
    tTScoreLabel = str(tTScoreLabel)
    teamScore_A = tk.Label(master=frame, text=tOScoreLabel, bg="#687FA1", fg="white", font=("Modern", 20))
    teamScore_A.place(x=100, y=130)
    teamScore_B = tk.Label(master=frame, text=tTScoreLabel, bg="#687FA1", fg="white", font=("Modern", 20))
    teamScore_B.place(x=440, y=130)


playButton = tk.Button(master=frame, text="Play", width=15, height=3, bg="white", fg="black", font=("Modern", 20),
                       command=lambda: [playButtonTask(), playButton.destroy()])
playButton.place(x=200, y=250)


def main():
    teamOne, teamTwo, teamThree, teamFour = createTeams()
    ccj = Team("Cruz City Jewels", teamOne)
    dcs = Team("Dayton City Speedsters", teamTwo)
    nyb = Team("New York Badgers", teamThree)
    sdm = Team("San Diego Mythics", teamFour)

    league1 = League("League 1", [ccj, dcs, nyb, sdm])

    match(ccj, dcs)
    print("\n")
    match(nyb, sdm)
    print("\n")
    match(ccj, nyb)
    print("\n")
    match(dcs, sdm)
    print("\n")
    match(sdm, ccj)
    print("\n")
    match(dcs, nyb)
    print("\n")

    print("Season Stats: ")
    for t in league1.getTeams():
        print(t.getName(), "(", t.getWins(), "-", t.getLoss(), ")\n")




main()
#window.mainloop()
