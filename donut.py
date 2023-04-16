import math
import os
import sys

# Define the dimensions of the terminal window
WIDTH = 80
HEIGHT = 22

# Define the characters to use for rendering the 3D wireframe image
ASCII_CHARS = ".,-~:;=!*#$@"


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def render_frame(A, B):
    """Render a single frame of the 3D wireframe image."""
    # Create an empty list to store the rendered characters
    frame = [" "] * (WIDTH * HEIGHT)

    # Calculate the x and y coordinates for each point on the surface of the sphere
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            sini = math.sin(i / 100)
            cosj = math.cos(j / 100)
            sinA = math.sin(A)
            sinj = math.sin(j / 100)
            cosA = math.cos(A)
            cosj2 = cosj + 2
            mess = 1 / (sini * cosj2 * sinA + sinj * cosA + 5)
            cosi = math.cos(i / 100)
            cosB = math.cos(B)
            sinB = math.sin(B)
            t = sini * cosj2 * cosA - sinj * sinA
            x = int(40 + 30 * mess * (cosi * cosj2 * cosB - t * sinB))
            y = int(11 + 15 * mess * (cosi * cosj2 * sinB + t * cosB))
            o = x + WIDTH * y
            N = int(
                8
                * (
                    (sinj * sinA - sini * cosj * cosA) * cosB
                    - sini * cosj * sinA
                    - sinj * cosA
                    - cosi * cosj * sinB
                )
            )
            if 0 <= x < WIDTH and 0 <= y < HEIGHT and mess > frame[o]:
                frame[o] = ASCII_CHARS[N if N > 0 else 0]

    # Return the rendered frame as a single string
    return "".join(frame[i : i + WIDTH] + "\n" for i in range(0, WIDTH * HEIGHT, WIDTH))


def main():
    """Main program loop."""
    A = 0.0
    B = 0.0
    while True:
        clear_screen()
        frame = render_frame(A, B)
        sys.stdout.write(frame)
        A += 0.04
        B += 0.02


if __name__ == "__main__":
    main()
