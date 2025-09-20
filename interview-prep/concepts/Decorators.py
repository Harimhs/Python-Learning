def novelreader(funcn):
    def novel():
        print("Read the novel")
        val = funcn()
        print("novel name")
        return val
    return novel

@novelreader
def novels():
    print("novel bro")

novels()