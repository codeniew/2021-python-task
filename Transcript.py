import csv
import webbrowser

with open('gradeLaber.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    print(list_of_rows)

    for list_of_row in list_of_rows:
        GEN_HTML = "grade_"+list_of_row[0]+"_"+list_of_row[1]+".html" #命名生成的html
        f = open(GEN_HTML,'w')
        message = """
        <html>
        <head></head>
        <body>
        <h1 align="center">期末考试成绩单</h1>
        <p align="center">姓名：%s</p>
        <p align="center">学号：%s</p>
        <p align="center">高等数学：%s</p>
        <p align="center">英语：%s</p>
        <p align="center">Python:%s</p>
        <p align="center">总分：%s</p>
        </body>
        </html>"""%(list_of_row[1],list_of_row[0],list_of_row[2],list_of_row[3],list_of_row[4],list_of_row[5])

        f.write(message)
        f.close()

        webbrowser.open(GEN_HTML)



