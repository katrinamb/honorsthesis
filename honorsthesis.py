def bad_algorithm(filename):
        '''This is an example of a bad healthcare algorithm 
        filename = the file name that contains patient information'''
        file = open(filename, 'r')
        for line in file:
            info = line.split()
            if (info[3] == "Headache"):
                if (info[1] == "Female"):
                    print(f"Patient {info[0]} is considered healthy. Please suggest that they take ibuprofen.\n")
                else:
                    print(f"Patient {info[0]} may have health concerns. Please check their heart rate.\n")
            elif (info[3] == "Stomachache"):
                if (info[1] == "Female"):
                    print(f"Patient {info[0]} is considered healthy. Please suggest that they take bismuth subsalicylate.\n")
                else:
                    print(f"Patient {info[0]} may have health concerns. Please check their heart rate.\n")
            elif (info[3] == "Chestpains"):
                if (info[1] == "Female"):
                    if (int(info[2]) >= 50):
                        print(f"Patient {info[0]} may have health concerns. Please check their heart rate.\n")
                    else:
                        print(f"Patient {info[0]} is considered healthy. Please suggest that they cut down on caffiene.\n")
                else:
                    print(f"Patient {info[0]} may have health concerns. Please check their heart rate.\n")
        file.close()

def good_algorithm(filename):
    '''This is an example of a good healthcare algorithm
    filename = the file name that contains patient information'''
    file = open(filename, 'r')
    for line in file:
        # do something with the line
        print(line)
    file.close()

if __name__ == "__main__":
    bad_algorithm("patients.txt")
    good_algorithm("patients.txt")