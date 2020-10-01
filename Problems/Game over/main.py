scores = input().split()    # list of each element in input
count_i = scores.count('I')
count_c = scores.count('C')

while 15 <= len(scores) <= 50:
    if count_i > 2:
        i_index = [i for i, s in enumerate(scores) if s == 'I']     # get the index for all I
        split_i_index = i_index[:3]     # split after 3 I
        get_position = split_i_index[2]     # get the position to the last I
        split_scores = scores[:get_position + 1]
        c_count = split_scores.count('C')
        print(f'Game over\n{c_count}')
        break
    else:
        print(f'You won\n{count_c}')
        break
