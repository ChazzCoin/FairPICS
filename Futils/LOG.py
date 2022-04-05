from Futils import DATE, DICT
import os


ERROR = 0  # -> Show ERROR only
INFO = 1  # -> Show ERROR and INFO
DEBUG = 2  # -> Show ERROR, INFO and DEBUG
VERBOSE = 3  # -> Show ERROR, INFO, DEBUG AND VERBOSE
LOG_LEVEL = DEBUG

class LogColors:
    HEADER = '\033[95m'
    DEBUG_BLUE = '\033[94m'  # ->
    VERBOSE_CYAN = '\033[96m'  # ->
    SUCCESS_GREEN = '\033[92m'  # -> INFO
    WARNING_YELLOW = '\033[93m'
    ERROR_FAIL = '\033[91m'  # -> ERROR
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Log:
    log_level = 1
    ERROR_color = LogColors.ERROR_FAIL
    WARNING_color = LogColors.WARNING_YELLOW
    INFO_color = "\33[0m"
    DEBUG_color = LogColors.DEBUG_BLUE
    VERBOSE_color = LogColors.VERBOSE_CYAN
    SUCCESS_color = LogColors.SUCCESS_GREEN
    log_color = INFO_color
    log_name = "TiffanyBot"
    title = "Tiffany-Bot"
    # log_path = config.MASTER_PATH + "/Data/Export/Logs"
    className = ""
    timeIn = 0
    timeOut = 0
    totalTime = 0

    def __init__(self, className, log_level=LOG_LEVEL, log_name="TiffanyBot"):
        # self.timeIn = process_time()
        # self.i("--> Run time has begun <--")
        self.log_level = log_level
        self.className = className
        self.log_name += f"{log_name}-{log_level}-{DATE.to_db_date()}"

    def notify(self, text):
        self.v("Creating MAC Push Notification: ", text)
        os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(text, self.title))

    def i(self, *messages, d: str = None, v: str = None):
        """ INFO Logging """
        if d:
            self.d(self.create_message(messages, d))
        if v:
            self.v(self.create_message(messages, v))
        if self.log_level == INFO:
            level = "INFO"
            self.write_log(level, self.create_message(messages))
        elif self.log_level > INFO and not d and not v:
            level = "INFO"
            self.write_log(level, self.create_message(messages))

    def e(self, *messages, error=""):
        """ ERROR Logging """
        log = f"{self.create_message(messages)}: {error}"
        level = "ERROR"
        self.write_log(level, log)

    def w(self, *messages, warning=""):
        """ WARNING Logging """
        log = f"{self.create_message(messages)}: {warning}"
        level = "WARNING"
        self.write_log(level, log)

    def d(self, *messages, v: str = None):
        """ DEBUG Logging """
        if v:
            self.v(self.create_message(messages, v))
        if self.log_level == DEBUG:
            level = "DEBUG"
            self.write_log(level, self.create_message(messages))
        elif self.log_level > DEBUG and not v:
            level = "DEBUG"
            self.write_log(level, self.create_message(messages))

    def v(self, *messages):
        """ VERBOSE Logging """
        if self.log_level >= VERBOSE:
            log = f"{self.create_message(messages)}"
            level = "VERBOSE"
            self.write_log(level, log)

    def s(self, *messages):
        """ SUCCESS Logging """
        log = f"{self.create_message(messages)}"
        level = "SUCCESS"
        self.write_log(level, log)

    def p(self, *messages):
        """ Only Prints Log to Terminal/Console """
        if self.log_level >= DEBUG:
            # -> Add "p" to debug mode.
            self.d(messages)
        else:
            print(self.className, self.create_message(messages))

    def p_by_line(self, *messages):
        """ Only Prints Log to Terminal/Console """
        for message in messages:
            print(self.className, message)

    def print_hookups(self, hookups):
        for item in hookups:
            self.print_hookup(item)

    def print_hookup(self, hookup):
        self.p("-- -- -- --")
        self.p(f"Title:", str(DICT.get("title", hookup)))
        self.p(f"Rank:", str(DICT.get("rank", hookup)))
        self.p(f"URL:", str(DICT.get("url", hookup)))
        self.p("-- -- -- --")

    def create_message(self, *messages):
        temp_message = ""
        for m in messages:
            temp_message = temp_message + " " + str(m)
        return temp_message

    def write_log(self, level, message):
        date = DATE.get_log_date_time()
        log = f"{date}: {level}: {self.className} -> {message}"
        color = self.get_log_color(log_level=level)
        print(color + log)
        # self.write_log_file(log)

    # def write_log_file(self, log):
    #     log_file = self.open_log_file()
    #     log_file.write(log)
    #     log_file.write("\n")
    #     log_file.close()

    # def open_log_file(self):
    #     log_file = open(f'{self.log_path}/{self.log_name}.log', 'a')
    #     return log_file

    @staticmethod
    def get_log_color(log_level):
        if log_level == "ERROR":
            return Log.ERROR_color
        elif log_level == "WARNING":
            return Log.WARNING_color
        elif log_level == "INFO":
            return Log.INFO_color
        elif log_level == "DEBUG":
            return Log.DEBUG_color
        elif log_level == "VERBOSE":
            return Log.VERBOSE_color
        elif log_level == "SUCCESS":
            return Log.SUCCESS_color

