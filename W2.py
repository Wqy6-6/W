import winsound
import time
z=0
x=0
y=0
while True:
    time.sleep(1)
    x+=1
    if x==60:
        x=0
        y+=1
        if y==60:
            y=0
            z+=1
    if z==0 and y==1 and x==0:
                break


    print(f'{z}:{y}:{x}')

end_time = time.time() + 60
while time.time() < end_time:
    winsound.Beep(1000, 500) # 每次响 0.5 秒
    time.sleep(0.5)

































