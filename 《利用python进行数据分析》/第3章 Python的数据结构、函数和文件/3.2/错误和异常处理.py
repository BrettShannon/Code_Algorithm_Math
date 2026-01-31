def attempt_float(x):
    try:
        print(float(x)) # 
    except:
        print(x)
    
    
attempt_float('fjfdl')

attempt_float('88448.84848')

# TypeError, ValueError 错误的处理:
def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x
    
#
f = open(path, 'w')

try:
    write_to_file(f)
finally:
    f.close()

#
f = open(path, 'w')

try:
    write_to_file(f)
except:
    print('Succeeded')
finally:
    f.close()

    