def get_summ(one, two, delimiter='&'):
    one=one.capitalize()
    two=two.capitalize()
    return f'{one} {delimiter} {two}'
print(get_summ("learn","python","_"))