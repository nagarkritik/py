import os

l = os.listdir(r"C:\Users\kritik nagar\Desktop\Boolean-Ranked-Retrieval-System-master\Data")
c = 1
for name in l:
    final = str(c) + '.txt'
    initial = r"C:\Users\kritik nagar\Desktop\Boolean-Ranked-Retrieval-System-master\Data\\" + name
    final = r"C:\Users\kritik nagar\Desktop\Boolean-Ranked-Retrieval-System-master\Data\\" + final

    os.rename(initial,final)
    c+=1