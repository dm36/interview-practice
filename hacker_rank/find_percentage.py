if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    # use query name as key in student_marks map to grab the scores
    # sum all scores and divide by the # of scores

    student_scores = student_marks[query_name]
    student_score = float(sum(student_scores)/len(student_scores))
    print '{:.2f}'.format(student_score)
