def count_chars(txt):
    rs = 0
    for char in txt:
        rs+=1
    return rs
input_txt = input("Enter your string:")
print("length: ", count_chars(input_txt))