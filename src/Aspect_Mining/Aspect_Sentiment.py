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
            result = 'Among those reviews that mentioned the ' + aspect + ' of ' + sql_results[0][0] + ', ' +pos_per_str + ' of them are positive.\nNot bad.'
        else:
            result = 'Among those reviews that mentioned the ' + aspect + ' of ' + sql_results[0][0] + ', ' + pos_per_str + ' of them are positive.\nPretty good.'
    else:
        neg_per = num_neg / (num_pos + num_neg)
        neg_per_str = '{:.0%}'.format(neg_per)
        if float(neg_per) > 0.5 and neg_per <= 0.7:
            result = 'Among those reviews that mentioned the ' + aspect + ' of ' + sql_results[0][0] + ', ' + neg_per_str + ' of them are negative.\nNot so good.'
        else:
            result = 'Among those reviews that mentioned the ' + aspect + ' of ' + sql_results[0][0] + ', ' + neg_per_str + ' of them are positive.\nPretty bad.'


    return result








