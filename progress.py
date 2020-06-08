# TODO: implement time estimation function decorator
def timer(function, total):
    old_time = np.zeros(total)
    for i in range(total):
        yield i
        new_time = time.time()


def print_progressbar(iteration, total, prefix ='', suffix ='', decimals = 1, length = 100, fill ='█', printEnd ="\r"):
    """Call in a loop to create terminal progress bar

    Parameters
    -------
     iteration   - Required  : current iteration (Int)
     total       - Required  : total iterations (Int)
     prefix      - Optional  : prefix string (Str)
     suffix      - Optional  : suffix string (Str)
     decimals    - Optional  : positive number of decimals in percent complete (Int)
     length      - Optional  : character length of bar (Int)
     fill        - Optional  : bar fill character (Str)
     printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    Source: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
