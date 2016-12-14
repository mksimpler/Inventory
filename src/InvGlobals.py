runner = None

def sign_off():
    task = runner.findTask('taskMain')
    if task is not None:
        from voice import globalwords
        globalwords.words['sign off'].enabled = False
        task.sign_off()