import time


def start_breathing(cycles=5):

    print("\nStarting guided breathing protocol\n")

    for i in range(cycles):

        print("Inhale")
        time.sleep(3)

        print("Hold")
        time.sleep(3)

        print("Exhale")
        time.sleep(3)

    print("\nBreathing session complete\n")