import yaml
import pandas as pd
import numpy as np

value = 0
for num in range(211028,211029):
    try:
        with open('D:\\STUDY\\3.2\\Project 300\\T20_male\\'+str(num)+'.yaml') as fileName:
            data = yaml.load(fileName)
            fileName.close()

            # print(data)
            # for i in data['innings'][0]['1st innings']['deliveries']: print(i)
            umpires = data['info']['umpires']
            dates = data['info']['dates']
            venue = data['info']['venue']

            retrieveData = 0

            try:
                result = data['info']['outcome']['winner']
                result_margin = data['info']['outcome']['by']
                retrieveData = 1
            except:
                result = data['info']['outcome']['result']
                try:
                    result_margin = data['info']['outcome']['bowl_out']
                    retrieveData = 1
                except:
                    retrieveData = 0

            if retrieveData == 1:

                # player_of_match = data['info']['player_of_match'][0]
                # city = data['info']['city']
                teams = ' vs '.join(data['info']['teams'])
                team_one = data['info']['teams'][0]
                team_two = data['info']['teams'][1]
                match_type = data['info']['match_type']
                toss = data['info']['toss']['winner']
                decision = data['info']['toss']['decision']
                gender = data['info']['gender']
                overs = data['info']['overs']

                # print(umpires, dates, venue, result, teams, toss)
                # print(data['innings'][0]['1st innings']['deliveries'])

                firstInningsDeliveryData = data['innings'][0]['1st innings']['deliveries']
                secondInningsDeliveryData = data['innings'][1]['2nd innings']['deliveries']

                ''' This part for forming data for 1st Innings of a match
                    require ball, team, batsman, bowler, runs, team run,
                '''
                ball_list, batsman_run_list, team_total_list, total_run_list, batsman_list, bowler_list, \
                innings_list, wicket_list, player_out_list, ballfaced_striker_list, strike_rate_list  = [
                    [], [], [], [], [], [], [], [], [], [], []]

                player_name, ball_faced, run_taken = [[], [], []]

                team_one_total = 0
                wicket = 0
                ballfaced_striker = 0
                ballfaced_non_striker = 0
                striker = ''
                non_striker = ''
                striker_run = 0
                non_striker_run = 0

                for k in firstInningsDeliveryData:

                    # print(list(k.keys())[0])
                    ball = list(k.keys())[0]
                    # print(k[ball])
                    batsman_run = k[ball]['runs']['batsman']
                    total_run = k[ball]['runs']['total']
                    batsman_name = k[ball]['batsman']

                    non_striker_name = k[ball]['non_striker']

                    bowler_name = k[ball]['bowler']

                    flag = 0
                    i = 0
                    print(i, len(player_name))
                    for i in player_name:
                        print(batsman_name,i,player_name[i])
                        if batsman_name == player_name[i]:
                            try:
                                wide = k[ball]['extras']['wides']
                            except:
                                ball_faced[i] = ball_faced[i] + 1
                        ballfaced_striker = ball_faced[i]
                        run_taken[i] = run_taken[i] + batsman_run
                        striker_run = run_taken[i]
                        flag = 1

                    if flag == 0:
                        #length = len(player_name)
                        #print(length)
                        player_name.append(batsman_name)
                        ball_faced.append(0)
                        run_taken.append(0)
                        ballfaced_striker = 0
                        striker_run = 0
                        print(player_name[i], ball_faced[i], run_taken)

                    #print(striker, non_striker, ballfaced_striker, ballfaced_non_striker, striker_run, non_striker_run)
                    #if batsman_name != striker :
                        #if batsman_name == non_striker:
                            #striker, non_striker = non_striker, striker
                            #ballfaced_striker, ballfaced_non_striker = ballfaced_non_striker, ballfaced_striker
                            #striker_run, non_striker_run = non_striker_run, striker_run
                        #else:
                            #striker = batsman_name
                            #non_striker = non_striker_name
                            #ballfaced_striker = 0
                            #striker_run = 0

                   #ballfaced_striker = ballfaced_striker + 1
                    #striker_run = striker_run + batsman_run





                    try:
                        player_out = k[ball]['wicket']['player_out']
                        wicket = wicket + 1

                        # if player_out == striker:
                        # striker_run = 0
                        # ballfaced_striker = 0
                        # else:
                        # non_striker_run = 0
                        # ballfaced_non_striker = 0
                    except:
                        player_out = ''

                    # print(batsman_run, " ", total_run)
                    team_one_total += total_run
                    # Construct List for pandas Series
                    innings_list.append('1st')
                    ball_list.append(ball)
                    batsman_list.append(batsman_name)
                    batsman_run_list.append(batsman_run)
                    bowler_list.append(bowler_name)
                    team_total_list.append(team_one_total)
                    total_run_list.append(total_run)
                    player_out_list.append(player_out)
                    wicket_list.append(wicket)
                    ballfaced_striker_list.append(ballfaced_striker)
                    try:
                        ballfaced_striker != 0
                        strike_rate_list.append(striker_run/ballfaced_striker * 100)
                    except:
                        strike_rate_list.append(0)

                team_two_total = 0
                wicket = 0
                ballfaced_striker = 0
                ballfaced_non_striker = 0
                striker = ''
                non_striker = ''
                striker_run = 0
                non_striker_run = 0

                for k in secondInningsDeliveryData:
                    # print(list(k.keys())[0])
                    ball = list(k.keys())[0]
                    # print(k[ball])
                    batsman_run = k[ball]['runs']['batsman']
                    total_run = k[ball]['runs']['total']
                    batsman_name = k[ball]['batsman']
                    bowler_name = k[ball]['bowler']

                    flag = 0
                    i = 0
                    for i in player_name:
                        if batsman_name == player_name[i]:
                            try:
                                wide = k[ball]['extras']['wides']
                            except:
                                ball_faced[i] = ball_faced[i] + 1
                        ballfaced_striker = ball_faced[i]
                        run_taken[i] = run_taken[i] + batsman_run
                        striker_run = run_taken[i]
                        flag = 1

                        # if flag == 0:
                        # length = len(player_name)
                        # print(length)
                        # player_name[i] = batsman_name
                        # ball_faced[i] = 0
                        # run_taken = 0
                        # ballfaced_striker = 0
                        # striker_run = 0

                        # print(striker, non_striker, ballfaced_striker, ballfaced_non_striker, striker_run, non_striker_run)
                        # if batsman_name != striker :
                        # if batsman_name == non_striker:
                        # striker, non_striker = non_striker, striker
                        # ballfaced_striker, ballfaced_non_striker = ballfaced_non_striker, ballfaced_striker
                        # striker_run, non_striker_run = non_striker_run, striker_run
                        # else:
                        # striker = batsman_name
                        # non_striker = non_striker_name
                        # ballfaced_striker = 0
                        # striker_run = 0

                        # ballfaced_striker = ballfaced_striker + 1
                        # striker_run = striker_run + batsman_run


                    try:
                        player_out = k[ball]['wicket']['player_out']
                        wicket = wicket + 1

                        #if player_out == striker:
                            #striker_run = 0
                            #ballfaced_striker = 0
                        #else:
                            #non_striker_run = 0
                            #ballfaced_non_striker = 0
                    except:
                        player_out = ''

                    team_two_total += total_run
                    # Construct List for pandas Series
                    innings_list.append('2nd')
                    ball_list.append(ball)
                    batsman_list.append(batsman_name)
                    batsman_run_list.append(batsman_run)
                    bowler_list.append(bowler_name)
                    team_total_list.append(team_two_total)
                    total_run_list.append(total_run)
                    player_out_list.append(player_out)
                    wicket_list.append(wicket)
                    ballfaced_striker_list.append(ballfaced_striker)
                    try:
                        ballfaced_striker != 0
                        strike_rate_list.append(striker_run / ballfaced_striker * 100)
                    except:
                        strike_rate_list.append(0)

                # print(dates, team_one, team_two, toss, venue, umpires)


                # Construction of a DataFrame
                data_set = pd.DataFrame({
                    'Team 1': team_one,
                    'Team 2': team_two,
                    'Toss': toss,
                    'Ball': ball_list,
                    'Venue': venue,
                    'Innings': pd.Series(innings_list),
                    'Batsman': pd.Series(batsman_list),
                    'Bowler': pd.Series(bowler_list),
                    'Batsman Run': pd.Series(batsman_run_list),
                    'Team Total': pd.Series(team_total_list),
                    'Wicket': pd.Series(wicket_list),
                    'Player Out': pd.Series(player_out_list),
                    'Ball Faced By Striker': pd.Series(ballfaced_striker_list),
                    'Strike Rate': pd.Series(strike_rate_list)
                })

        value = value+1
        #print(data_set)
        folder = 'D:\\STUDY\\3.2\\Project 300\\T20_male_csv\\'
        #file_name = folder + teams + '.csv'
        file_name = folder + str(value) + '.csv'
        data_set.to_csv(file_name,encoding='utf-8')
    except OSError as e:
        print(e.errno)