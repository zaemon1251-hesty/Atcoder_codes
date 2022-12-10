def main():
    s = input()
    tgday = "Saturday"
    week = f"Monday,Tuesday,Wednesday,Thursday,Friday,{tgday}".split(",")
    print(week.index(tgday) - week.index(s))


if __name__ == '__main__':
    main()
