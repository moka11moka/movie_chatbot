from datetime import datetime, date


class ServiceDictionary:

    DICTIONARY = {
        "今天几号": "今天是公历%s年%s月%s日",
        "现在几点": "现在是%s时%s分%s秒",
        "haha": "ha ni mei"
    }

    NOT_FOUND = "啊呀！ 找不到相关信息呢！"

    @classmethod
    def get_item(cls, key, default=NOT_FOUND):
        if key not in cls.DICTIONARY:
            return default

        item = cls.DICTIONARY.get(key)

        if key == "今天几号":
            return item % (date.today().year, date.today().month, date.today().day)
        elif key == "现在几点":
            return item % (datetime.now().hour, datetime.now().minute, datetime.now().second)
        else:
            return item
