# 2.3.2 

file = 'traffic_log_for_dataivy'
fn = open(file, 'r') # 打开要读区的日志文件 'r'表示只读模式,'w'表示写入模式,'r+'表示读写模式.
content = fn.readline() # 读取一行
print(content[:2]) # 打印前两个字符
fn.close() # 关闭文件
