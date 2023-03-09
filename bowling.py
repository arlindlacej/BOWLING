def main():
    scores_dic = dict()
    strikes_dic = dict()
    misses_dic = dict()
    with open("bowling.txt") as file_in:
        for line in file_in:
            line = line.rstrip()
            elements = line.split(";")
            name = elements[0] + " " + elements[1]
            score = 0
            misses_dic[name] = 0
            strikes_dic[name] = 0
            for i in range(2, len(elements)):
                score = int(score) + int(elements[i])
                if int(elements[i]) == 10:
                    strikes_dic[name] = strikes_dic[name] + 1
                if int(elements[i]) == 0:
                    misses_dic[name] = misses_dic[name] + 1
            scores_dic[score] = name
    reverse_misses_dic = {value: key for (key, value) in misses_dic.items()}
    reverse_strikes_dic = {value: key for (key, value) in strikes_dic.items()}
    misses = []
    strikes = []
    for key in reverse_strikes_dic.keys():
        strikes.append(key)
    strikes.sort(reverse=True)
    for key in reverse_misses_dic:
        misses.append(key)
    misses.sort(reverse=True)
    score_lst = []
    for key in scores_dic.keys():
        score_lst.append(key)
    score_lst.sort(reverse=True)
    for element in score_lst:
        print(f"{scores_dic[element]:10} {element}")
    if strikes[0]>strikes[1]:
        print(f"{reverse_strikes_dic[strikes[0]]}has knocked down all the pins {strikes[0]} times")
    if misses[0]>misses[1]:
        print(f"{reverse_misses_dic[misses[0]]}has missed all the pins {misses[0]} time (s)")


if __name__ == '__main__':
    main()
