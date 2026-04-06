# gradebook.py

import datetime

s = []  # students
c = []  # courses  
g = []  # grades

def ns(fn, ln, yr, em):
    for i in range(len(s)):
        if s[i][2] == em:
            print("exists")
            return
    id = len(s) + 1
    s.append([id, fn + " " + ln, em, yr, [], 0])
    print("added " + str(id))

def nc(name, cr, max_g):
    for i in range(len(c)):
        if c[i][0] == name:
            print("exists")
            return
    c.append([name, cr, max_g, []])
    print("ok")

def ag(sid, cname, score, t):
    sf = -1
    cf = -1
    for i in range(len(s)):
        if s[i][0] == sid:
            sf = i
    for i in range(len(c)):
        if c[i][0] == cname:
            cf = i
    if sf == -1:
        print("no student")
        return
    if cf == -1:
        print("no course")
        return
    if score < 0 or score > c[cf][2]:
        print("bad score")
        return
    if t != "exam" and t != "hw" and t != "lab" and t != "test":
        print("bad type")
        return
    for i in range(len(g)):
        if g[i][0] == sid and g[i][1] == cname and g[i][3] == t and g[i][4] == "active":
            print("already has this type")
            return
    dt = datetime.datetime.now()
    gid = len(g) + 1
    g.append([sid, cname, score, t, "active", dt, gid])
    p = score / c[cf][2] * 100
    if p >= 90:
        gr = "A"
    if p >= 75 and p < 90:
        gr = "B"
    if p >= 60 and p < 75:
        gr = "C"
    if p >= 50 and p < 60:
        gr = "D"
    if p < 50:
        gr = "F"
    g[-1].append(gr)
    s[sf][4].append(gid)
    s[sf][5] = s[sf][5] + score
    c[cf][3].append(gid)
    print("grade added: " + gr)

def sg(sid):
    sf = -1
    for i in range(len(s)):
        if s[i][0] == sid:
            sf = i
    if sf == -1:
        print("no student")
        return
    print("=== " + s[sf][1] + " grades ===")
    total = 0
    cnt = 0
    for i in range(len(g)):
        if g[i][0] == sid and g[i][4] == "active":
            print(g[i][1] + " | " + g[i][3] + " | " + str(g[i][2]) + " | " + g[i][7])
            total = total + g[i][2]
            cnt = cnt + 1
    if cnt == 0:
        print("no grades")
        return
    avg = total / cnt
    if avg >= 90:
        overall = "A"
    if avg >= 75 and avg < 90:
        overall = "B"
    if avg >= 60 and avg < 75:
        overall = "C"
    if avg >= 50 and avg < 60:
        overall = "D"
    if avg < 50:
        overall = "F"
    print("avg: " + str(round(avg, 1)) + " overall: " + overall)

def cc(cname):
    cf = -1
    for i in range(len(c)):
        if c[i][0] == cname:
            cf = i
    if cf == -1:
        print("no course")
        return
    print("=== " + cname + " ===")
    grades_list = []
    for i in range(len(g)):
        if g[i][1] == cname and g[i][4] == "active":
            grades_list.append(g[i][2])
    if len(grades_list) == 0:
        print("no grades yet")
        return
    mn = grades_list[0]
    mx = grades_list[0]
    sm = 0
    for i in range(len(grades_list)):
        sm = sm + grades_list[i]
        if grades_list[i] < mn:
            mn = grades_list[i]
        if grades_list[i] > mx:
            mx = grades_list[i]
    print("count: " + str(len(grades_list)))
    print("avg: " + str(round(sm / len(grades_list), 1)))
    print("min: " + str(mn) + " max: " + str(mx))

def dg(gid):
    for i in range(len(g)):
        if g[i][6] == gid:
            if g[i][4] == "active":
                g[i][4] = "deleted"
                print("deleted")
                return
            if g[i][4] == "deleted":
                print("already deleted")
                return
    print("not found")

def top(n):
    tmp = []
    for i in range(len(s)):
        total = 0
        cnt = 0
        for j in range(len(g)):
            if g[j][0] == s[i][0] and g[j][4] == "active":
                total = total + g[j][2]
                cnt = cnt + 1
        if cnt > 0:
            tmp.append([s[i][1], total / cnt])
    for i in range(len(tmp)):
        for j in range(len(tmp) - 1):
            if tmp[j][1] < tmp[j+1][1]:
                x = tmp[j]
                tmp[j] = tmp[j+1]
                tmp[j+1] = x
    print("=== top " + str(n) + " ===")
    for i in range(n):
        if i < len(tmp):
            print(str(i+1) + ". " + tmp[i][0] + " - " + str(round(tmp[i][1], 1)))

def rep(sid, cname):
    sf = -1
    cf = -1
    for i in range(len(s)):
        if s[i][0] == sid:
            sf = i
    for i in range(len(c)):
        if c[i][0] == cname:
            cf = i
    if sf == -1 or cf == -1:
        print("not found")
        return
    have = []
    need = ["exam", "hw", "lab", "test"]
    for i in range(len(g)):
        if g[i][0] == sid and g[i][1] == cname and g[i][4] == "active":
            have.append(g[i][3])
    missing = []
    for i in range(len(need)):
        if need[i] not in have:
            missing.append(need[i])
    print("student: " + s[sf][1])
    print("course: " + cname + " (" + str(c[cf][1]) + " credits)")
    print("completed: " + str(len(have)) + "/4")
    if len(missing) > 0:
        print("missing: " + str(missing))
    else:
        print("all done")


# usage
nc("Math", 5, 100)
nc("Physics", 4, 100)
nc("Programming", 6, 100)
nc("History", 3, 50)

ns("Anna", "Kovalenko", 2, "anna@uni.edu")
ns("Ivan", "Petrenko", 1, "ivan@uni.edu")
ns("Maria", "Bondar", 3, "maria@uni.edu")
ns("Oleg", "Shevchenko", 2, "oleg@uni.edu")

ag(1, "Math", 88, "exam")
ag(1, "Math", 45, "hw")
ag(1, "Programming", 95, "exam")
ag(1, "Programming", 90, "lab")
ag(2, "Math", 60, "exam")
ag(2, "Physics", 72, "exam")
ag(2, "Physics", 55, "lab")
ag(3, "Programming", 78, "exam")
ag(3, "History", 40, "test")
ag(4, "Math", 91, "exam")
ag(4, "Physics", 85, "exam")

sg(1)
sg(2)
cc("Math")
cc("Physics")
top(3)
rep(1, "Math")
