import subprocess

# for this program to work their needs to be a file in the same directory that when executed
# will ask for a password and a password list must be given if using your
# own have it in the same directory and change "password_list.txt" on line 28 to your .txt file
# use your own or use and call it password_list.txt:
# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/Ashley-Madison.txt

# ignore if not doing picoCTF challenge PW Crack 4
pos_pw_list = ["158f", "1655", "d21e", "4966", "ed69", "1010", "dded", "844c", "40ab", "a948", "156c", "ab7f", "4a5f",
               "e38c", "ba12", "f7fd", "d780", "4f4d", "5ba1", "96c5", "55b9", "8a67", "d32b", "aa7a", "514b", "e4e1",
               "1230", "cd19", "d6dd", "b01f", "fd2f", "7587", "86c2", "d7b8", "55a2", "b77c", "7ffe", "4420", "e0ee",
               "d8fb", "d748", "b0fe", "2a37", "a638", "52db", "51b7", "5526", "40ed", "5356", "6ad4", "2ddd", "177d",
               "84ae", "cf88", "97a3", "17ad", "7124", "eff2", "e373", "c974", "7689", "b8b2", "e899", "d042", "47d9",
               "cca9", "ab2a", "de77", "4654", "9ecb", "ab6e", "bb8e", "b76b", "d661", "63f8", "7095", "567e", "b837",
               "2b80", "ad4f", "c514", "ffa4", "fc37", "7254", "b48b", "d38b", "a02b", "ec6c", "eacc", "8b70", "b03e",
               "1b36", "81ff", "77e4", "dbe6", "59d9", "fd6a", "5653", "8b95", "d0e5"]


# where level4.py put the file you want to crack on line 23
# if you want to use a different file format change python on line 23
def pass_crack(x):
    process = subprocess.Popen(["python", "level4.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    output, _ = process.communicate(input=x)
    print(f"output for password {x}: {output.strip()}")


file = open("password_list.txt", "r")
# put this: print(line[x]) inside str() on line 37 if you want to use a password list
# if doing picoCTF challenge PW Crack 4 change the bit inside str() on line 37 to pos_pw_list[x]
line = file.readlines()


# if the program stops with an error, and it is because x is out of bounds of the password list this is fine
def loop():
    for x in range(0, 1000000000000000000000000000000000000000000000):
        pass_crack(str(pos_pw_list[x]))


loop()

# if the program finishes with the error IndexError: list index out of range
# don't worry as this does not matter as the program should've still ran successfully 
# if the program finishes check back through to see if the correct password was put in if not try a different wordlist
