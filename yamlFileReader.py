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
                umpires = data['info']['umpires']
                dates = data['info']['dates'][0]
                venue = data['info']['venue']
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
                ball_list, batsman_run_list, team_total_list, total_run_list,player_out_list, wicket_list, striker_list, non_striker_list, bowler_list, innings_list, striker_run_list, \
                non_striker_run_list = [[], [], [], [], [], [], [], [], [], [], [], []]

                team_one_total = 0
                wicket = 0

                for k in firstInningsDeliveryData:

                    # print(list(k.keys())[0])
                    ball = list(k.keys())[0]
                    # print(k[ball])
                    batsman_run = k[ball]['runs']['batsman']
                    total_run = k[ball]['runs']['total']
                    batsman_name = k[ball]['batsman']
                    non_striker = k[ball]['non_striker']

                    striker_run = 0
                    non_striker_run = 0
                    for old_k in firstInningsDeliveryData:
                        old_ball = list(old_k.keys())[0]
                        if old_k[old_ball]['batsman'] == batsman_name:
                            striker_run = striker_run + old_k[old_ball]['runs']['batsman']
                        elif old_k[old_ball]['batsman'] == non_striker:
                            non_striker_run = non_striker_run + old_k[old_ball]['runs']['batsman']
                        if ball == old_ball:
                            break

                    try:
                        player_out = k[ball]['wicket']['player_out']
                        wicket = wicket + 1

                    except:
                        player_out = ''

                    bowler_name = k[ball]['bowler']
                    # print(batsman_run, " ", total_run)
                    team_one_total += total_run
                    # Construct List for pandas Series
                    innings_list.append('1st')
                    ball_list.append(ball)
                    striker_list.append(batsman_name)
                    non_striker_list.append(non_striker)  # new
                    batsman_run_list.append(batsman_run)
                    bowler_list.append(bowler_name)
                    team_total_list.append(team_one_total)
                    total_run_list.append(total_run)
                    striker_run_list.append(striker_run)  # new
                    non_striker_run_list.append(non_striker_run)  # new
                    player_out_list.append(player_out)
                    wicket_list.append(wicket)



                team_two_total = 0
                wicket = 0

                for k in secondInningsDeliveryData:
                    # print(list(k.keys())[0])
                    ball = list(k.keys())[0]
                    # print(k[ball])
                    batsman_run = k[ball]['runs']['batsman']
                    total_run = k[ball]['runs']['total']
                    batsman_name = k[ball]['batsman']

                    non_striker = k[ball]['non_striker']  # new

                    striker_run = 0
                    non_striker_run = 0
                    for old_k in firstInningsDeliveryData:
                        old_ball = list(old_k.keys())[0]
                        if old_k[old_ball]['batsman'] == batsman_name:
                            striker_run = striker_run + old_k[old_ball]['runs']['batsman']
                        elif old_k[old_ball]['batsman'] == non_striker:
                            non_striker_run = non_striker_run + old_k[old_ball]['runs']['batsman']
                        if ball == old_ball:
                            break

                    bowler_name = k[ball]['bowler']

                    try:
                        player_out = k[ball]['wicket']['player_out']
                        wicket = wicket + 1

                    except:
                        player_out = ''

                    bowler_name = k[ball]['bowler']
                    team_two_total += total_run
                    # Construct List for pandas Series
                    innings_list.append('2nd')
                    ball_list.append(ball)
                    striker_list.append(batsman_name)
                    non_striker_list.append(non_striker)  # new
                    batsman_run_list.append(batsman_run)
                    bowler_list.append(bowler_name)
                    team_total_list.append(team_two_total)
                    total_run_list.append(total_run)
                    striker_run_list.append(striker_run)  # new
                    non_striker_run_list.append(non_striker_run)  # new
                    # print(dates, team_one, team_two, toss, venue, umpires)
                    wicket_list.append(wicket)


                # print(dates, team_one, team_two, toss, venue, umpires)

                # Construction of a DataFrame
                data_set = pd.DataFrame({
                    'Team 1': team_one,
                    'Team 2': team_two,
                    'Winner/Result': result, #new
                    'Date': str(dates), #new
                    'Toss': toss,
                    'Ball': ball_list,
                    'Venue': venue,
                    'Innings': pd.Series(innings_list),
                    'Striker': pd.Series(striker_list),
                    'Non Striker': pd.Series(non_striker_list), #new
                    'Striker Run': pd.Series(striker_run_list), #new
                    'Non Striker Run': pd.Series(non_striker_run_list), #new
                    'Bowler': pd.Series(bowler_list),
                    'Batsman Run': pd.Series(batsman_run_list),
                    'Team Total': pd.Series(team_total_list),
                    'Wicket': pd.Series(wicket_list),
                    'Player Out': pd.Series(player_out_list),

                })

        value = value+1
        #print(data_set)
        folder = 'D:\\STUDY\\3.2\\Project 300\\T20_male_csv\\'
        #file_name = folder + teams + '.csv'
        file_name = folder + str(value) + '.csv'
        data_set.to_csv(file_name,encoding='utf-8')
    except OSError as e:
        print(e.errno)