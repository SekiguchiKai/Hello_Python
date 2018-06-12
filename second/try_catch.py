class MinusError(Exception):
    pass

def div(a,b):
    try:
        if(a < 0):
            raise MinusError
        print(a/b)
    except ZeroDivisionError:
        print("0で割っちゃだめ")
    except MinusError:
        print("割られる数がマイナスはだめえええ")
    else:
        print("例外じゃない")
    finally:
        print("終了")


div(5,0)
div(10,2)
div(-10,2)