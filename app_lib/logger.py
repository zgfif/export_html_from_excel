import logging
import os


class Logger:
    def __init__(self, filepath: str = 'logs/app.log', loglevel = logging.DEBUG) -> None:
        """
        Initialize logger with path for logfile and loglevel.

        Args:
            filepath (str): path to logfile
            loglevel - 
        """
        self._filepath = filepath
        self._loglevel = loglevel



    def setup(self):
        logging.basicConfig(
            level=logging.DEBUG,
            filename=self._filepath,
            encoding="utf-8",
            filemode="a",
            format=self._format(),
            style="{",
            datefmt=self._date_format(),
        )
    
        return logging
    

    
    def _format(self) -> str:
        """
        Return format of log record.
        """
        return "{asctime} - {levelname} - {message}"
    


    def _date_format(self) -> str:
        """
        Return format of date.
        """
        return "%Y-%m-%d %H:%M"
    

