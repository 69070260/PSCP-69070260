"""โปรแกรมคำนวน Elo"""

RA = int(input())
RB = int(input())
c = input()

if c == "A":
    EA = 1/(1+10**((RB-RA)/400))
    print(f"{EA:.2f}")
elif c == "B":
    EB = 1/(1+10**((RA-RB)/400))
    print(f"{EB:.2f}")
