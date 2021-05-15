import configparser


class ReadConf:

    def getBaseURL(self):
        config = configparser.RawConfigParser()
        file_path = ".\\Configuration\\config.ini"
        print(file_path)
        config.read(file_path)
        url = config.get("configuration", "base_url")
        return url
