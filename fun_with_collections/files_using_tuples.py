file_name = 'student_info.txt'


def write_to_file(tuple):
    try:
        file = open(file_name, "a")
        try:
            file.write(tuple)
            file.write('\n')
        finally:
            file.close()
    except IOError:
        print("Cannot create file on file system!")


def get_student_info(student_name):
    scores = []
    print('Please enter your available scores. Enter -999 to continue after entering your scores.')
    while True:
        score = int(input("Enter score:"))
        if score == -999:
            break
        scores.append(score)
    write_to_file(str((student_name, scores)))


def read_from_file():
    file = open(file_name)
    for line in file.readlines():
        print(line)
    file.close()


if __name__ == '__main__':
    get_student_info('Paul')
    get_student_info('Trevor')
    get_student_info('Amy')
    get_student_info('Shane')

    read_from_file()
