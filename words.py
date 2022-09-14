class Words():

    filename = open('book.txt')
    counts = dict()
    for line in filename:
        words = line.split()
        for word in words:
            wrd = word.lower()
            counts[wrd] = counts.get(wrd, 0) + 1

    fine = list()
    for kie, vaal in counts.items():
        newtup = (vaal, kie)
        fine.append(newtup)

    fine.sort(reverse=True)
    print(fine[:10])







