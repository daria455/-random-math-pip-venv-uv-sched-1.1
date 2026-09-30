PI = 3.14159265358979
VERSION = "1.0.0"
_secret = "это скрытая константа"

def circle_area(r): return PI * r ** 2
def circle_len(r):  return 2 * PI * r
def helper():       return PI / 2

if __name__== "__main__":
    print(f"[{VERSION}] Самопроверка my module:")
    print(" S(r=2) =", circle_area(2))
    print(" L(r=2) =", circle_len(2))




import mymodule
from mymodule import circle_area, VERSION
from mymodule import circle_len as perimeter
import mymodule as mm


print("1) mymodule.circle_area(5) =", mymodule.