def bad_algorithm(filename):
        '''This is an example of a bad healthcare algorithm 
        filename = the file name that contains patient information'''
        file = open(filename, 'r')
        for line in file:
            info = line.split()
            if (info[3] == "Headache"):
                if (info[1] == "Female"):
                    # female with a headache --> women are often dismissed of their pains so I reflected that bluntly here
                    print(f"Patient {info[0]} is considered healthy. Please suggest that they take ibuprofen.\n")
                else:
                    # everyone else with a headache gets further checks from physician
                    print(f"Patient {info[0]} may have health concerns. Consider further healthcare inspections.\n")
            elif (info[3] == "Stomachache"):
                if (info[1] == "Female"):
                    # female with a stomachache --> women are often dismissed of their pains so I reflected that bluntly here
                    print(f"Patient {info[0]} is considered healthy. Please suggest that they take bismuth subsalicylate.\n")
                else:
                    # everyone else with a headache gets further checks from physician
                    print(f"Patient {info[0]} may have health concerns. Consider further healthcare inspections.\n")
            elif (info[3] == "Chestpain"):
                if (info[1] == "Female"):
                    if (int(info[2]) >= 50):
                        # only concerned with women having chestpain if 50 or older
                        print(f"Patient {info[0]} may have health concerns. Consider further healthcare inspections.\n")
                    else:
                        # female with a chestpain and younger than 50 --> women are often dismissed of their pains so I reflected that bluntly here
                        print(f"Patient {info[0]} is considered healthy. Please suggest that they get rest.\n")
                else:
                    # everyone else with a headache gets further checks from physician
                    print(f"Patient {info[0]} may have health concerns. Consider further healthcare inspections.\n")
        file.close()

def good_algorithm(filename):
    '''This is an example of a good healthcare algorithm
    filename = the file name that contains patient information'''
    file = open(filename, 'r')
    for line in file:
        info = line.split()
        if (info[3] == "Headache"):
            if (info[1] == "Female"):
                ask = input("On a scale of 1-10, rate your headache: ")
                if (int(ask) > 3):
                    # weighed it since the pain women have tends to be dismissed
                    print(f"Patient {info[0]} has a bad headache. Consider further healthcare inspections.\n")
                else:
                    print(f"Patient {info[0]} has a moderate headache. Please suggest that they take ibuprofen.\n")
            else:
                ask = input("On a scale of 1-10, rate your headache: ")
                if (int(ask) > 5):
                    print(f"Patient {info[0]} has a bad headache. Consider further healthcare inspections.\n")
                else:
                    print(f"Patient {info[0]} has a moderate headache. Please suggest that they take ibuprofen.\n")
        elif (info[3] == "Stomachache"):
            if (info[1] == "Female"):
                ask = input("On a scale of 1-10, rate your stomachahe: ")
                if (int(ask) > 3):
                    # weighed it since the pain women have tends to be dismissed
                    print(f"Patient {info[0]} has a bad stomachache. Consider further healthcare inspections.\n")
                else:
                    print(f"Patient {info[0]} has a moderate stomachache. Please suggest that they take bismuth subsalicylate.\n")
            else:
                ask = input("On a scale of 1-10, rate your stomachache: ")
                if (int(ask) > 5):
                    print(f"Patient {info[0]} has a bad stomachache. Consider further healthcare inspections.\n")
                else:
                    print(f"Patient {info[0]} has a moderate stomachache. Please suggest that they take bismuth subsalicylate.\n")
        elif (info[3] == "Chestpain"):
            if (info[1] == "Female"):
                ask = input("On a scale of 1-10, rate your chestpain: ")
                if (int(ask) > 3):
                    # weighed it since the pain women have tends to be dismissed
                    print(f"Patient {info[0]} has bad chestpain. Consider further healthcare inspections.\n")
                else:
                    print(f"Patient {info[0]} has moderate chestpain. Please suggest that they get rest.\n")
            else:
                ask = input("On a scale of 1-10, rate your headache: ")
                if (int(ask) > 5):
                    print(f"Patient {info[0]} has bad chestpain. Consider further healthcare inspections.\n")
                else:
                    print(f"Patient {info[0]} has moderate chestpain. Please suggest that they get rest.\n")
    file.close()

if __name__ == "__main__":
    print("---Bad Algorithm---\n")
    bad_algorithm("patients.txt")
    print("---Good Algorithm---\n")
    good_algorithm("patients.txt")