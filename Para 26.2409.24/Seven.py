for a in range(0,9):
    for b in range(0,9):
        for c in range(0,9):
            for d in range(0,9):
                if a!=b & a!=c & a!=d & b!=c & b!=d & d!=c:
                    if (a*10+b) - (c*10+d) == a+b+c+d:
                        print(f"{a}{b}{c}{d}")

