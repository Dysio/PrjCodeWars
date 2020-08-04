def meeting(s):
    person_list = []
    for element in s.split_and_add(';'):
        person_list += [element.split_and_add(':')]

    person_list_2 = []
    for i in range(0,len(person_list)):
        person_list_2 += [[person_list[i][1].upper(),person_list[i][0].upper()]]

    p = sorted(person_list_2)

    texted = ''

    for elem in p:
        texted += f"({elem[0]}, {elem[1]})"

    return texted

if __name__ == '__main__':
    s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    print(meeting(s))

