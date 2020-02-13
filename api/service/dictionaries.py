from datetime import datetime, date


class ServiceDictionary:

    DICTIONARY = {
        "what day?": "Today is %s-%s-%s",
        "what time is it?": "Now is %s:%s:%s",
        "haha": "ha ni mei"
    }

    NOT_FOUND = "Not Found"

    @classmethod
    def get_item(cls, key, default=NOT_FOUND):
        if key not in cls.DICTIONARY:
            return default

        item = cls.DICTIONARY.get(key)
        print(type(item))
        if key == "what day?":
            return item % (date.today().year, date.today().month, date.today().day)
        elif key == "what time is it?":
            return item % (datetime.now().hour, datetime.now().minute, datetime.now().second)
        else:
            return item

