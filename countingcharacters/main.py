#Sawyer Wood, skillpractice counting characters.

list1 = list(input("What is the grid you want to count?: "))

def count_now(list1 = [

['A', 'B', 'C', 'A', 'D'],

['C', 'A', 'B', 'D', 'E'],

['A', 'D', 'C', 'E', 'A'],

['B', 'A', 'C', 'A', 'D'],

['D', 'C', 'B', 'E', 'A'] ]):

    ACount = 0
    BCount = 0
    CCount = 0
    DCount = 0
    ECount = 0
    FCount = 0
    GCount = 0
    HCount = 0
    ICount = 0
    JCount = 0
    KCount = 0
    LCount = 0
    MCount = 0
    NCount = 0
    OCount = 0
    PCount = 0
    QCount = 0
    RCount = 0
    SCount = 0
    TCount = 0
    UCount = 0
    VCount = 0
    WCount = 0
    XCount = 0
    YCount = 0
    ZCount = 0

    for x in list1:

        for i in x:

            if i == 'A':
                ACount += 1
            
            elif i == 'B':
                BCount += 1

            elif i == 'C':
                CCount += 1
            
            elif i == 'D':
                DCount += 1

            elif i == 'E':
                ECount += 1
            
            elif i == 'F':
                FCount += 1
            
            elif i == 'G':
                GCount += 1

            elif i == 'H':
                HCount += 1

            elif i == 'I':
                ICount += 1

            elif i == 'J':
                JCount += 1

            elif i == 'K':
                KCount += 1

            elif i == 'L':
                LCount += 1

            elif i == 'M':
                MCount += 1

            elif i == 'N':
                NCount += 1

            elif i == 'O':
                OCount += 1

            elif i == 'P':
                PCount += 1
            
            elif i == 'Q':
                QCount += 1

            elif i == 'R':
                RCount += 1

            elif i == 'S':
                SCount += 1

            elif i == 'T':
                TCount += 1

            elif i == 'U':
                UCount += 1

            elif i == 'V':
                VCount += 1

            elif i == 'W':
                WCount += 1

            elif i == 'X':
                XCount += 1

            elif i == 'Y':
                YCount += 1

            elif i == 'Z':
                ZCount += 1

    else:
        print(f"A: {ACount}\nB: {BCount}\nC: {CCount}\nD: {DCount}\nE: {ECount}\nF: {FCount}\nG: {GCount}\nH: {HCount}\nI: {ICount}\nJ: {JCount}\nK: {KCount}\nL: {LCount}\nM: {MCount}\nN: {NCount}\nO: {OCount}\nP: {PCount}\nQ: {QCount}\nR: {RCount}\nS: {SCount}\nT: {TCount}\nU: {UCount}\nV: {VCount}\nW: {WCount}\nX: {XCount}\nY: {YCount}\nZ: {ZCount}")
if list1 == []:
    count_now()
else:
    count_now(list1)