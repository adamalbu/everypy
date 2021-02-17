

print('Hi.')
print('Welcome to everypy where you can do lots of things.')
print('Type help when you need some help.')
cmd = ""
while cmd != "shutdown":
    cmd = input("P:/>")
    splitcmd = cmd.split()
    if splitcmd[0] == "help":
        print('cd')
        print('help')
        print('shutdown')
    
