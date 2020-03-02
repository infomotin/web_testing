list_m = [1,1,12,35,2,4]

print(list(map(lambda item: item*2,list_m)))


# finds duplicates 
a = '''1: Note the hyphen (or the minus sign) in "thirty-four" above. Technically, it's correct to hyphenate all compound numbers from twenty-one (21) through ninety-nine (99).
2: In American English, when writing out natural numbers of three or more digits, the word "and" is not used after "hundred" or "thousand". So it is "one hundred twenty-three" and not "one hundred and twenty-three", though you may hear a lot of people using the last, informally.
In British English, the word "and" is used after "hundred" or "thousand" in numbers of three or more digits.
3. Do not use commas when writing out numbers above 999: so it is "one thousand two hundred thirty-four" and not "one thousand, two hundred thirty-four".
4. For clarity, use commas when writing figures of four or more digits: 1,234, 43,290,120, etc. In other countries a point is used to group digits by 3 and a comma to separate the decimals, ex: 1.234,55, 43.290.120,84. In some other countries a space is used to group digits by 3, ex: 1 234, 43 290 120.'''
my_list =[]
for i in a:
    my_list.append(i)
    print(i)


dupli_list =[]

for v in my_list:
    if my_list.count(v) >1:
        if v not in dupli_list:
            dupli_list.append(v)
print(dupli_list.sort)
