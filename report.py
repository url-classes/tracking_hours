import abc


class Report(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_report(self, filename: str):
        raise NotImplementedError
