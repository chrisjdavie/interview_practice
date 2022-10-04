from invoke import task


@task
def backlight(c):
    # okay, I know the command I need to run (at the moment) but I also need to lower the permissions
    # of the file (cos I'd rather not do this under sudo) but the instructions for that are here, and
    # need to mess about with udev, so I'll punt that down the road
    # https://unix.stackexchange.com/questions/20125/how-can-i-change-the-permissions-in-sys-to-alter-the-state-of-a-led-light-using
    # damn linux, all I want to do is turn my keyboard backlight on
    pass
