
def p_p(z:list)->type:
    return list(map(lambda x: type(x),z))

y=map(int,(input().split()))
print(p_p(y))

#func print


