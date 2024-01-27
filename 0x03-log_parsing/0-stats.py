#!/usr/bin/python3
'''Log Parsing'''
import re


def extract_input(input_line):
    '''Get the input'''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<statusCode>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'statusCode': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        statusCode = resp_match.group('statusCode')
        file_size = int(resp_match.group('file_size'))
        info['statusCode'] = statusCode
        info['file_size'] = file_size
    return info


def print_statistics(totalFileSize, statusCodesStats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('File size: {:d}'.format(totalFileSize), flush=True)
    for statusCode in sorted(statusCodesStats.keys()):
        num = statusCodesStats.get(statusCode, 0)
        if num > 0:
            print('{:s}: {:d}'.format(statusCode, num), flush=True)


def update_metrics(line, totalFileSize, statusCodesStats):
    '''Update metrices'''
    line_info = extract_input(line)
    statusCode = line_info.get('statusCode', '0')
    if statusCode in statusCodesStats.keys():
        statusCodesStats[statusCode] += 1
    return totalFileSize + line_info['file_size']


def run():
    '''run the log parser'''
    lineNum = 0
    totalFileSize = 0
    statusCodesStats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            totalFileSize = update_metrics(
                line,
                totalFileSize,
                statusCodesStats,
            )
            lineNum += 1
            if lineNum % 10 == 0:
                print_statistics(totalFileSize, statusCodesStats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(totalFileSize, statusCodesStats)


if __name__ == "__main__":
    run()
