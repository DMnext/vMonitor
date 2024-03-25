import time


class timer:
    
    def start_timer(self):
        # %y.%m.%d_%H:%M:
        self.start_time_sec = time.strftime('%S')
        self.start_time_min = time.strftime('%M')
        self.start_time_hour = time.strftime('%H')
        self.start_time_day = time.strftime('%d')
        self.start_time_month = time.strftime('%m')
        self.start_time_year = time.strftime('%y')

    def end_timer(self):
        # %y.%m.%d_%H:%M:
        self.end_time_sec = time.strftime('%S')
        self.end_time_min = time.strftime('%M')
        self.end_time_hour = time.strftime('%H')
        self.end_time_day = time.strftime('%d')
        self.end_time_month = time.strftime('%m')
        self.end_time_year = time.strftime('%y')

    def get_time(self):
        self.start_time_sec - self.end_time_sec

