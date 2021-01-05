def create_fail(f):
    file = open(f,'r', encoding = "utf-8-sig")
    mas = []
    for line in file:
        mas.append(line.strip())
    file.close()
    return mas
def save_file(f,line):
    file = open(f, 'a', encoding = "utf-8-sig")
    file.write(line+'\n')
    file.close()
def rewrite_file (f,line):
    rus_new = create_fail(f)
    new_line = input("Введите правильный перевод\n:")
    ndx = rus_new.index(line)
    rus_new[ndx] = new_line
    new_file = open(f, "w+", encoding = "utf-8-sig")
    for i in range(len(rus_new)):
        new_file.write(rus_new[i] + "\n")
    new_file.close()
