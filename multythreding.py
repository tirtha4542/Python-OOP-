import threading
def print_name(name,*args):
    print(name,*args)
name ="Tirtha"
thred1 = threading.Thread(target=print_name,args=(name,10))
thred2 = threading.Thread(target=print_name,args =(name,20,10))

thred1.start()
thred2.start()

thred1.join()
thred2.join()
