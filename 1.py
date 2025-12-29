# 查找这整个文件夹内的所有文件，找出包含“署名”关键字的文件、
# 并打印出这些文件的文件名和行号。
# 1.使用os.walk()函数遍历文件夹内的所有文件
# 2.使用open()函数打开文件
# 3.使用readlines()函数读取文件内容
# 4.使用enumerate()函数获取行号
# 5.使用in关键字判断是否包含“署名”关键字
# 6.使用print()函数打印文件名和行号
import os

# 定义一个函数来查找包含关键字的文件和行号
def find_files_with_keyword(directory, keyword):
    # 使用os.walk遍历文件夹
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 拼接文件路径
            file_path = os.path.join(root, file)
            try:
                # 以UTF-8编码打开文件
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for line_no, line in enumerate(lines, start=1):
                        # 判断是否包含关键字
                        if keyword in line:
                            print(f'文件名: {file_path}, 行号: {line_no}')
            except UnicodeDecodeError:
                # 如果文件不是UTF-8编码，就跳过
                continue

# 调用函数，查找包含“署名”关键字的文件
find_files_with_keyword('.', '署名')
