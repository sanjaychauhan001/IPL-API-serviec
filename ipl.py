import pandas as pd
import  numpy as np

ipl_matches = pd.read_csv("C:\\Users\\sanja\\OneDrive\\Pictures\\excel\\ipl-matches.csv")
df = pd.read_csv("C:\\Users\\sanja\\OneDrive\\Pictures\\excel\\IPL.csv")

def teamsAPI():
    teams = list(set(list(ipl_matches['Team1']) + list(ipl_matches['Team2'])))
    team_dict = {
        "Teams":teams
    }
    return team_dict


def teamVteamAPI(team1, team2):
    valid_teams = list(set(list(ipl_matches['Team1']) + list(ipl_matches['Team2'])))

    if team1 and team2 in valid_teams:
        temp_df = ipl_matches[(ipl_matches['Team1'] == team1) & (ipl_matches['Team2'] == team2) | (ipl_matches['Team1'] == team2) & (ipl_matches['Team2'] == team1)]
        total_matches = temp_df.shape[0]
        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]

        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
            'total_matches':str(total_matches),
            team1:str(matches_won_team1),
            team2:str(matches_won_team2),
            'draws':str(draws)
        }
        return response
    else:
        return {"message":"invalid team name"}

def teamAPI(team):

  total_teams = list(set(list(ipl_matches['Team1']) + list(ipl_matches['Team2'])))
  team_stats_dict = {}

  filtered_team = ipl_matches[(ipl_matches['Team1'] == team) | (ipl_matches['Team2'] == team)]
  total_matches_played = filtered_team.shape[0]
  total_matches_won = filtered_team[filtered_team['WinningTeam'] == team].shape[0]
  total_matches_lost = total_matches_played-total_matches_won
  no_result = total_matches_played - (total_matches_won + total_matches_lost)
  super_over_team = filtered_team[filtered_team['SuperOver'] == "Y"]
  total_super_over_match = super_over_team.shape[0]
  super_over_won = super_over_team[super_over_team['WinningTeam'] == team].shape[0]
  super_over_lost = total_super_over_match - super_over_won

  team_stats_dict[team] = {"total_matches":total_matches_played,
              "won":total_matches_won,
              "lost":total_matches_lost,
              "noResult":no_result,
              "Total_super_over":total_super_over_match,
              "SuperOverwon":super_over_won,
              "SuperOverlost":super_over_lost}

  for i in total_teams:
    if(i != team):

      team1 = filtered_team[(filtered_team['Team1'] == i) | (filtered_team['Team2'] == i)]
      total = filtered_team[(filtered_team['Team1'] == i) | (filtered_team['Team2'] == i)].shape[0]
      won = team1[team1['WinningTeam'] == team].shape[0]
      lost = total-won
      draws = total - (won+lost)


      team_stats_dict[i] = {"matchesPlayed":total,
                    "won":won,
                    "lost":lost,
                    "noresult":draws}
  return team_stats_dict

def batterAPI(batsman):
    out = df[df['player_out'] == batsman].shape[0]
    temp_df = df[df['batter'] == batsman]


    total_run = temp_df.groupby('batter')['batsman_run'].sum().iloc[0]
    fours = temp_df[temp_df['batsman_run'] == 4].shape[0]
    sixs = temp_df[temp_df['batsman_run'] == 6].shape[0]
    total_ball = temp_df.shape[0]
    strike_rate = (total_run/total_ball)*100
    avg = total_run/out

    temp2_df = temp_df.groupby('ID')['batsman_run'].sum().sort_values(ascending=False).reset_index()
    total_innings = temp2_df.shape[0]
    not_out = total_innings - out
    height_score = temp_df.groupby('ID')['batsman_run'].sum().sort_values(ascending=False).iloc[0]
    hundreds = temp2_df[temp2_df['batsman_run'] >= 100].shape[0]
    fifties =  temp2_df[(temp2_df['batsman_run'] >= 50) & (temp2_df['batsman_run'] < 100)].shape[0]

    response = {batsman:{'Innings':str(total_innings),
                         "runs":str(total_run),
                         "fours":str(fours),
                         "sixs":str(sixs),
                         "avg":str(avg),
                         "strikeRate":str(strike_rate),
                         "hundreds":str(hundreds),
                         "fifties":str(fifties),
                         "heightScore":str(height_score),
                         "NotOut":str(not_out)}}
    return response
