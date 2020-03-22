def aspect_score(aspect,sql_results):
    print(sql_results[0])
    result = 'Sorry, I don\'t have the information for now.'
    sql_dict = {'acting_pos':sql_results[0][1],'acting_neg':sql_results[0][2],
                      'direction_pos':sql_results[0][3],'direction_neg':sql_results[0][4],
                      'screenplay_pos':sql_results[0][5],'screenplay_neg':sql_results[0][6],
                      'sound_pos':sql_results[0][7],'sound_neg':sql_results[0][8],
                      'story_pos':sql_results[0][9], 'story_neg':sql_results[0][10],
                      'visual_pos':sql_results[0][11],'visual_neg':sql_results[0][12]}

    num_pos = sql_dict[aspect+'_pos']
    num_neg = sql_dict[aspect+'_neg']

    if aspect == 'acting':
        aspect = 'actors'
    if aspect == 'visual':
        aspect = 'visual effects'
    if aspect == 'sound':
        aspect = 'sound effects and music'

    if num_pos == num_neg == 0:
        result = 'Sorry, there are no reviews about the ' + aspect + 'of ' + sql_results[0][0] + ' yet.'
    if num_pos == num_neg:
        result = 'The reviewers\' attitude towards the ' + aspect + ' of this movie is neutral.'
    elif num_pos > num_neg:
        pos_per = num_pos/(num_pos+num_neg)
        pos_per_str = '{:.0%}'.format(pos_per)
        if pos_per > 0.5 and pos_per <= 0.7:
            result = pos_per_str + ' of the reviewers liked the ' + aspect + ' of ' + sql_results[0][0] + '.\n' \
                                                                                              'Not bad.'
        else:
            result = pos_per_str + ' of the reviewers liked the ' + aspect + ' of ' + sql_results[0][0] + '.\n' \
                                                                                                        'Pretty good.'
    else:
        neg_per = num_neg / (num_pos + num_neg)
        neg_per_str = '{:.0%}'.format(neg_per)
        if float(neg_per) > 0.5 and neg_per <= 0.7:
            result = neg_per_str + ' of the reviewers didn\'t like the ' + aspect + ' of ' + sql_results[0][0] + '.\n' \
                                                                                              'Not good.'
        else:
            result = neg_per_str + ' of the reviewers liked the ' + aspect + ' of ' + sql_results[0][0] + '.\n' \
                                                                                                        'Seems bad.'


    return result








