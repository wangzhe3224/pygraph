import datetime


class StopWatch(object):
    """ A simple stop watch to log processing time

    Examples
    --------
    >>> import time
    >>> sw = StopWatch()
    >>> time.sleep(1)
    >>> sw.click('first done')
    """

    def __init__(self):
        """"""
        self.start_time = self.now
        self.__clicks = []

    def click(self, tag: str):
        """ Click the stop watch, will keep a record in log

        :param tag:
        :return:
        """
        self.__clicks.append((tag, self.now))

    @property
    def now(self):
        return datetime.datetime.now()

    def report(self):
        """ report """
        return [
            {
                'tag': tag,
                'start': start,
                'end': stop,
                'time': self.calc_time_ms(start, stop)
            }
            for (tag, stop), (_, start) in
            zip(
                self.__clicks,
                [(None, self.start_time)] + self.__clicks[:-1]
            )
        ]

    @staticmethod
    def calc_time_ms(start: datetime.datetime, end: datetime.datetime):
        """ calculate time difference in ms """
        return int((end-start).total_seconds()*1000)

