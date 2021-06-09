def demo(filename):
    with open(filename,"r") as f:
        ans = f.readlines(14301702)
        with open("password.txt","w") as g:
            g.writelines(ans)

# demo("rockyou.txt")