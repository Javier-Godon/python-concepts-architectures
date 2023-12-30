from datetime import datetime

unix_epoch: int = 1703757783


def format_time(epoch: int) -> str:
    return datetime.fromtimestamp(epoch).strftime('%Y_%m_%d')


print(format_time(unix_epoch))
