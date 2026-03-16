subject = 0
grade_all = 0
grade = 0
point = [4.5, 3.5, 2.5, 1.5, 4.0, 3.0, 2.0, 1.0]
    
for b in range(20):
    name, num, point_now  = input().split()
    
    if len(point_now) == 2:
        subject += float(num)
        if point_now[1] == "+":
            P_n = ord(point_now[0]) - 65
            grade_all += float(num) * point[P_n]
        else:
            P_n = ord(point_now[0]) - 65 + 4
            grade_all += float(num) * point[P_n]
    elif point_now == "F":
        subject += float(num)
        
if subject != 0.0:
    grade = grade_all / subject

print(round(grade, 6))
