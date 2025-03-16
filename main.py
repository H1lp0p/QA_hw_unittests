class History:
    def __init__(self):
        self.logs = []

    def store(self, a, b, result):
        self.logs.append({'a': a, 'b': b, 'result': result})

    def logError(self, message):
        self.logs.append({"type": "error", "message": message})

    def __str__(self):
        return "\n".join(
            [f'> {i["a"]} + {i["b"]} = {i["result"]}' if i.get("a") is not None
             else f'!> {i["type"]}: {i["message"]}'
             for i in self.logs]
        )


class Calculator:
    def __init__(self):
        self.logs = History()

    def sum(self, a, b):
        try:
            float_a = float(a)
            float_b = float(b)

            result = float_a + float_b
            if (result - int(result) == 0):
                result = int(result)

            self.logs.store(a,b, result)

            return result

        except ValueError:
            msg = "value can not be parsed to float"
            self.logs.logError(msg)
            raise ValueError(msg)