import math

staff_stats = [9,8,6]
fist_stats = [8,6,5]
AC = input("Input AC: ")

try:
    AC = int(AC)
except:
    print("Enter a valid number. For now, byeee")
    quit()

def correction(P):
    if P < 1/20:
        P = 1/20
    if P > 1:
        P = 1
    return P

P_staff_miss = correction((AC-staff_stats[0])/20)
P_fist_miss = correction((AC-fist_stats[0])/20)

P_staff_hit = 1-P_staff_miss - 1/20
P_fist_hit = 1-P_fist_miss - 1/20

def expected():
    def staff_damage():
        damage = 0
        for i in range(1, staff_stats[1]+1):
            damage += i/staff_stats[1]
        return damage + staff_stats[2]

    def fist_damage():
        damage = 0
        for i in range(1, fist_stats[1]+1):
            damage += i/fist_stats[1]
        return damage + fist_stats[2]

    expected_no_ki = (P_staff_hit * staff_damage() + 1/20 * (staff_damage() + staff_stats[1]+staff_stats[2]))*2 + P_fist_hit * fist_damage() + 1/20 * (fist_damage() + fist_stats[1]+fist_stats[2])
    expected_ki = expected_no_ki + P_fist_hit * fist_damage() + 1/20 * (fist_damage() + fist_stats[1]+fist_stats[2])

    return (expected_no_ki, expected_ki)
    
staff_chances = [P_staff_miss, P_staff_hit, 1/20]
fist_chances = [P_fist_miss, P_fist_hit, 1/20]

print(expected())