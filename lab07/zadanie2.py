def czy_zakonczyc():
    isEnd = input('Czy chcesz zakończyć program? (t/n)')
    czy_t(isEnd)


def czy_t(isEnd):
    if isEnd == 't':
        exit(0)
    else:
        czy_zakonczyc()


czy_zakonczyc()
