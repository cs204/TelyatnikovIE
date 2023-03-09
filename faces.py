def main():
    s = input()
    def convert(s):
        s1 = s.replace(":)", "🙂")
        s2 = s1.replace(":(", "🙁")
        return(s2)
    print(convert(s))
main()