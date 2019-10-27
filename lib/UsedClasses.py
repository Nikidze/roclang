class UsedClasses:
    classes = {
        "DBL": "lib/Classes/Types/DBL.CPP",
        "INT": "lib/Classes/Types/INT.CPP",
        "STR": "lib/Classes/Types/STR.CPP",
        "INT_ARR": "lib/Classes/Arrs/INT_ARR.CPP",
    }
    used = {
        "DBL": False,
        "INT": False,
        "STR": False,
        "INT_ARR": False,
    }

    def add(self, cls):
        self.used[cls] = True

    def get(self):
        classes = ""
        for i in self.used:
            if i:
                classes += open(self.classes[i]).read()
        return classes


UC = UsedClasses()
