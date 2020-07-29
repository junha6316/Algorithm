



def solution(skill, skill_trees):
    answer =len(skill_trees)
    temp=[]
    checks = [[] for _ in skill_trees]

    for idx, skill_tree in enumerate(skill_trees):
        for c in skill_tree:
            if c in skill:
                checks[idx].append(skill.index(c))

    for check in checks:
       for idx,c in enumerate(check):
           if idx != c:
               answer -= 1
               break

    return answer


skill="CBDLKOE"
skill_trees=["BACDEJP", "CBADFQWE", "AECBETR", "BDATUY"]
print(solution(skill, skill_trees))
