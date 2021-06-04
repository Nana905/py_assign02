
import time,functools

def show_time(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        time.sleep(0.5)
        result=func(*args,**kwargs)
        t2=time.time()
        print(f'运行{func.__name__}函数的时间为：%.6f'%(t2-t1-0.5))
        return result
    return wrapper


@show_time
def add(a,b):
    return a+b

@show_time
def is_prime(i):
    for j in range(1,int(i**0.5)):
        if i%j==0:
            return '%d不是素数'%i
    return '%d是素数'%i


re=is_prime(15)
print(re)

# print(is_prime.__name__)

add_result=add(5555,9999)
