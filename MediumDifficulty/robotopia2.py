cases = int(input())

for i in range(cases):
    # Organize input
    tmp = list(map(int, input().split()))
    legs_one = tmp[0]
    arms_one = tmp[1]
    legs_two = tmp[2]
    arms_two = tmp[3]
    legs_total = tmp[4]
    arms_total = tmp[5]
    
    answer = ''
    solutions = 0
    # Upper limit on amount of legs or arms
    limit = max({legs_total, arms_total})
    
    # j is possible solution for type one
    for j in range(1, limit):
        legs_remaining = legs_total - (j * legs_one)
        arms_remaining = arms_total - (j * arms_one)
        
        # Check remaining legs and arms, checking modulos sequentially to reduce runtime
        if (legs_remaining > 0) & (arms_remaining > 0):
            if arms_remaining % arms_two == 0:
                if legs_remaining % legs_two == 0:

                    # if arms_remaining/arms_two == legs_remaining/legs_two
                    # calculating type 2, checking that the both arms and legs requirement is met
                    if arms_remaining * legs_two == legs_remaining * arms_two:
                        solutions += 1
                        answer = "{} {:g}".format(j, arms_remaining / arms_two)

    if solutions == 1:
        print(answer)
    else:
        # if there are none or multiple solutions
        print("?")
