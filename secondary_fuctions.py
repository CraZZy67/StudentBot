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


def add_exam_value(count_str: str):
    count_list = count_str.split("/")
    add = int(count_list[0]) + 1

    if add != int(count_list[1]):
        result_string = f"{add}/{count_list[1]}"
        return result_string

    else:
        return "finish"


def shuffle(sheet: dict):
    if len(sheet) > 0 and sheet != "empty":
        shuffle_sheet = {}
        count = 0

        for v in sheet.values():
            shuffle_sheet[f"{count}"] = v
            count += 1
        return shuffle_sheet
    else:
        return "empty"
