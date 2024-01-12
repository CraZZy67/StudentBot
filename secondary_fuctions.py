from settings import DELIMITER


def formatting_text(sheet: dict):
    if len(sheet) > 0 and sheet != "empty":
        text_list = str()
        count_lines = 1

        for line in sheet.values():
            text_list += f"{count_lines}. {line[0]} | {line[1]} | {line[2]}\nДаты: {line[3]}\n{DELIMITER}\n"
            count_lines += 1

        return text_list
    else:
        return "Записей еще нет!"
