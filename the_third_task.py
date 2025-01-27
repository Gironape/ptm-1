import datetime
import csv


def week_csv(w_file, week_start, week_end) -> None:
    """
    Принимает на вход данные за неделю и создает csv файл с этими данными
    :param w_file: Входные данные.
    :param week_start: Начальная дата.
    :param week_end: Конечная дата.
    """
    start = datetime.datetime.strftime(week_start, '%Y%m%d')
    end = datetime.datetime.strftime(week_end, '%Y%m%d')
    with open((start + '_' + end) + ".csv", "w", encoding='utf-8') as w_file_week:
        file_writer_week = csv.writer(w_file_week, delimiter=",", lineterminator="\r")
        file_writer_week.writerow(["Дата", "Курс Доллара"])
        reader = csv.DictReader(w_file)
        w_file.seek(0)
        for row in reader:
            if row['Дата'] >= week_end.strftime('%Y-%m-%d'):
                if row['Дата'] <= week_start.strftime('%Y-%m-%d'):
                    file_writer_week.writerow([row['Дата'], row['Курс Доллара']])
