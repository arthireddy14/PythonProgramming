# notes 1,2,5,10,20,50,100,200,500,2000
def count_notes(amt):
    if(amt==1 or amt==2 or amt==5 or amt==10 or amt==20 or amt==50 or amt==100 or amt==200 or amt==500 or amt==2000):
        return 1
    elif(amt>1 and amt<2):
        return 1
    elif(amt>2 and amt<5):
        return (amt/2)
    elif(amt>5 and amt<10):
        return (amt/5)+((amt%5)/2)+((amt%2)/1)
    elif(amt>10 and amt<20):
        return (amt/10)+((amt%10)/5)+(amt/5)+((amt%5)/2)+((amt%2)/1)
    elif(amt>20 and amt<50):
        if(amt%20==0):
            return amt/20
        else:
            return ((amt/20)) 
    elif(amt>50 and amt<100):
        return 

