import os
import shutil

from colorama import init, Fore, Style


class TerminalCLI:
    def __init__(self):
        # Terminal
        self.update_terminal_size()

        # Colorama
        init()

        # Colors
        self.fore = Fore
        self.style = Style

        self.green = Fore.GREEN
        self.red = Fore.RED
        self.yellow = Fore.YELLOW
        self.blue = Fore.BLUE
        self.cyan = Fore.CYAN
        self.magenta = Fore.MAGENTA

        self.reset = Style.RESET_ALL

        # Box styles
        self.box_styles = {
            "normal": {
                "horizontal": "─",
                "vertical": "│",
                "top_left": "┌",
                "top_right": "┐",
                "bottom_left": "└",
                "bottom_right": "┘",
            },

            "double": {
                "horizontal": "═",
                "vertical": "║",
                "top_left": "╔",
                "top_right": "╗",
                "bottom_left": "╚",
                "bottom_right": "╝",
            },

            "ascii": {
                "horizontal": "-",
                "vertical": "|",
                "top_left": "+",
                "top_right": "+",
                "bottom_left": "+",
                "bottom_right": "+",
            },

            "simple": {
                "horizontal": "-",
                "vertical": "|",
                "top_left": ".",
                "top_right": ".",
                "bottom_left": "'",
                "bottom_right": "'",
            }
        }

    def update_terminal_size(self):
        self.terminal_size = shutil.get_terminal_size(
            fallback=(80, 24)
        )

        self.terminal_width = self.terminal_size.columns
        self.terminal_height = self.terminal_size.lines

    def clear_terminal(self):
        os.system(
            "cls" if os.name == "nt" else "clear"
        )

    def draw_line(self, char="─", color=None):
        self.update_terminal_size()

        line = char * self.terminal_width

        if color:
            line = color + line + self.reset

        print(line)

    def header(self, text, color=None, char="─", space=1):
        self.update_terminal_size()

        text = f'{" " * space}{text}{" " * space}'

        if len(text) >= self.terminal_width:
            text = text[:self.terminal_width - 4] + "..."

        total_padding = self.terminal_width - len(text)

        left = total_padding // 2
        right = total_padding - left

        header_line = (
            f"{char * left}"
            f"{text}"
            f"{char * right}"
        )

        if color:
            header_line = color + header_line + self.reset

        print(header_line)

    def draw_cool_line(self, color=None):
        self.header(
            "|||",
            color=color,
            char="─",
            space=1
        )

    def box(
        self,
        text="",
        style="normal",
        color=None,

        # Custom chars
        horizontal=None,
        vertical=None,
        top_left=None,
        top_right=None,
        bottom_left=None,
        bottom_right=None
    ):
        lines = text.strip().splitlines()

        max_length = max(len(line) for line in lines)

        selected_style = self.box_styles.get(
            style,
            self.box_styles["normal"]
        )

        horizontal = horizontal or selected_style["horizontal"]
        vertical = vertical or selected_style["vertical"]

        top_left = top_left or selected_style["top_left"]
        top_right = top_right or selected_style["top_right"]

        bottom_left = (
            bottom_left or
            selected_style["bottom_left"]
        )

        bottom_right = (
            bottom_right or
            selected_style["bottom_right"]
        )

        top = (
            top_left +
            horizontal * (max_length + 2) +
            top_right
        )

        bottom = (
            bottom_left +
            horizontal * (max_length + 2) +
            bottom_right
        )

        if color:
            top = color + top + self.reset
            bottom = color + bottom + self.reset

        print(top)

        for line in lines:
            content = (
                f"{vertical} "
                f"{line.ljust(max_length)} "
                f"{vertical}"
            )

            if color:
                content = color + content + self.reset

            print(content)

        print(bottom)