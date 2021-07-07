import mysql.connector as mysql
import xlsxwriter
import datetime


def connect_to_db(db):
    HOST = "172.17.38.68"
    DATABASE = db
    USER = "test"
    PASSWORD = "1qaz@WSX"

    return mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)


def pass_test(company):
    if company == "hc":
        context = connect_to_db("moodle")
    if company == "kvrz":
        context = connect_to_db("moodle_kvrz")
    if company == "kvrp":
        context = connect_to_db("moodle_kvrp")
    if company == "bvrp":
        context = connect_to_db("moodle_bvrp")
    if company == "vrp":
        context = connect_to_db("moodle_vrp")
    query = """ 
    SELECT
                    user2.lastname AS 'Фамилия',
                    user2.firstname AS 'Имя',
                    user2.email AS 'E-mail',
                    user2.institution AS 'Компания',
                    course.fullname AS 'Название курса',
                    gg.rawgrade AS 'Количество баллов',
                    ROUND(gg.finalgrade / gg.rawgrademax * 100 ,2) AS 'Процент',
                    IF (ROUND(gg.finalgrade / gg.rawgrademax * 100 ,2) > 84.99,'Тест пройден' , 'Обучение не пройдено') AS 'Курс пройден',
                    FROM_UNIXTIME(gg.timemodified) AS 'Время'

                    FROM grade_grades AS gg 
                    JOIN grade_items AS gi ON gg.itemid = gi.id
                    JOIN user AS user2 ON gg.usermodified = user2.id
                    JOIN course AS course ON gi.courseid = course.id 
    """
    cur = context.cursor()
    cur.execute(query)
    result = cur.fetchall()
    return result


def user_enroll(company):
    if company == "hc":
        context = connect_to_db("moodle")
    if company == "kvrz":
        context = connect_to_db("moodle_kvrz")
    if company == "kvrp":
        context = connect_to_db("moodle_kvrp")
    if company == "bvrp":
        context = connect_to_db("moodle_bvrp")
    if company == "vrp":
        context = connect_to_db("moodle_vrp")

    query = """ 
    SELECT
            user2.lastname AS Lastname,
            user2.firstname AS Firstname,
            user2.email AS Email,
            user2.institution AS 'Компания',
            course.fullname AS Course
            ,(SELECT name FROM role WHERE id=en.roleid) AS RoleName

            FROM course AS course 
            JOIN enrol AS en ON en.courseid = course.id
            JOIN user_enrolments AS ue ON ue.enrolid = en.id
            JOIN user AS user2 ON ue.userid = user2.id
    """
    cur = context.cursor()
    cur.execute(query)
    result = cur.fetchall()
    return result


def join_tables(user_enroll, user_pass):
    all_passing = []

    for row in user_pass:
        key = []
        key.append(row[0])
        key.append(row[1])
        key.append(row[4])
        all_passing.append(key)

    count = 0

    for row in user_enroll:
        key = []
        key.append(row[0])
        key.append(row[1])
        key.append(row[4])
        try:
            index_value = all_passing.index(key)
        except ValueError:
            index_value = -1
        if index_value != -1:
            user_enroll_row = list(user_enroll[count])
            user_pass_row = list(user_pass[index_value])
            user_enroll_row[5] = user_pass_row[5]
            user_enroll_row.append(user_pass_row[6])
            user_enroll_row.append(user_pass_row[7])
            user_enroll_row.append(user_pass_row[8])
            user_enroll[count] = tuple(user_enroll_row)
        count = count + 1
    return user_enroll


def write_file(result, company):
    current_date = datetime.datetime.now()
    today = datetime.date.today()
    today = today.strftime("%d-%m-%Y")
    if company == "hc":
        name_file = 'Отчет по обучению ЦА на ' + str(today) + '.xlsx'
    if company == "kvrz":
        name_file = 'Отчет по обучению КВРЗ на ' + str(today) + '.xlsx'
    if company == "kvrp":
        name_file = 'Отчет по обучению КВРП на ' + str(today) + '.xlsx'
    if company == "bvrp":
        name_file = 'Отчет по обучению БВРП на ' + str(today) + '.xlsx'
    if company == "vrp":
        name_file = 'Отчет по обучению ВРП на ' + str(today) + '.xlsx'
    file_path= "N:\УК\УКБ\Курсы Moodle\Отчеты\Временная папка для программы\\" + name_file
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet('Обучение')
    r = 0
    c = 0
    col_name = (
    'Фамилия', 'Имя', 'Email', 'Компания', 'Название курса', 'Количество баллов', 'Процент', 'Курс пройден', 'Время')
    first_row_format = workbook.add_format()
    first_row_format.set_bg_color('#C5D9F1')
    first_row_format.set_bold()
    first_row_format.set_font_size(11)
    first_row_format.set_text_wrap()
    first_row_format.set_font_name('Calibri')
    worksheet.write_row(r, c, col_name, first_row_format)
    r = r + 1
    worksheet.set_column(8, 500)
    for row in result:
        user_novotrans=list(row)
        if str(user_novotrans[0]) != 'Новотранс':
            worksheet.write_row(r, c, tuple(row))
        else:
             r=r-1
        if len(row)-1 == 8:
            dateformat = workbook.add_format({'num_format': 'dd-mm-yyyy hh:mm'})
            number_format = workbook.add_format({'num_format': '0.00'})
            worksheet.set_column('I:I', 20, dateformat)
            worksheet.set_column('A:B', 18)
            worksheet.set_column('C:C', 22)
            worksheet.set_column('D:D', 24)
            worksheet.set_column('F:G', 18)
            worksheet.set_column('F:F', cell_format=number_format)
            worksheet.set_column('H:H', 22)
            worksheet.set_column('E:E', 50)

        r = r + 1
    workbook.close()


def get_report(company):
    write_file(join_tables(user_enroll(company), pass_test(company)), company)