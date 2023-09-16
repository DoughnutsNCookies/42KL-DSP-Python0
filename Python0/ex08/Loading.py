import time


def ft_tqdm(iterable):
    """
        A tqdm-like function.
        Only accepts iterables.
    """
    total = len(iterable)
    progress = 1
    start_time = time.time()

    # Prints the initial message
    print(f"0%|{' ' * 100}| 0/{total} [00:00<?, ?it/s]", end="\r")
    for item in iterable:
        yield item
        # Prints the percentage complete
        percentage_complete = (progress / total) * 100
        message = f"{percentage_complete:.0f}%|"

        # Prints the progress bar
        message += f"{int(percentage_complete) * '█'}"
        message += f"{(100 - int(percentage_complete)) * ' '}|"
        message += f" {progress}/{total}"

        # Prints the elapsed time
        # If the elapsed time is greater than 1 hour
        # It prints the elapsed time in hours, minutes and seconds
        elapsed_time = time.time() - start_time
        min_elapsed, sec_elapsed = divmod(elapsed_time, 60)
        if min_elapsed > 60:
            hours_elapsed, min_elapsed = divmod(min_elapsed, 60)
            message += f" [{round(hours_elapsed):02d}:"
            message += f"{round(min_elapsed):02d}:"
            message += f"{round(sec_elapsed):02d}<"
        else:
            message += f" [{round(min_elapsed):02d}:"
            message += f"{round(sec_elapsed):02d}<"

        # Prints the remaining time
        # If the remaining time is greater than 1 hour
        # It prints the remaining time in hours, minutes and seconds
        time_remaining = (elapsed_time / progress) * (total - progress)
        min_remaining, sec_remaining = divmod(time_remaining, 60)
        if min_remaining > 60:
            hours_remaining, min_remaining = divmod(min_remaining, 60)
            message += f"{round(hours_remaining):02d}:"
            message += f"{round(min_remaining):02d}:"
            message += f"{round(sec_remaining):02d},"
        else:
            message += f"{round(min_remaining):02d}:"
            message += f"{round(sec_remaining):02d},"

        # Prints the iterations per second
        iterations_per_second = progress / elapsed_time
        message += f" {iterations_per_second:.2f}it/s]"

        # Prints the message and carriage return
        # Then increments the progress
        print(message, end="\r")
        progress += 1
    print()
