def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")
def feet2meter(v):
    import re
    s = v
    s1 = re.sub("ft", "", s)
    f = float (s1) / (3.28084)
    return(f)
main()