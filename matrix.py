import os
import sys
import time
import random
import threading
from shutil import get_terminal_size


class TerminalManager:
    """Handles terminal initialization, cleanup, and resizing."""
    def __init__(self):
        self.original_settings = None

    def init_term(self):
        """Initialize terminal settings."""
        self.original_settings = os.system("stty -echo")  # Disable key echo
        print("\033[?1049h", end="")  # Switch to alternate screen buffer
        print("\033[?25l", end="")   # Hide cursor

    def deinit_term(self):
        """Restore terminal settings."""
        if self.original_settings is not None:
            os.system("stty echo")  # Re-enable key echo
        print("\033[?1049l", end="")  # Restore original screen buffer
        print("\033[?25h", end="")   # Show cursor

    def get_terminal_size(self):
        """Get current terminal dimensions."""
        return get_terminal_size()


class RainDrop:
    """Represents a single rain drop."""
    def __init__(self, term_manager, color_mode, sleep_time):
        self.term_manager = term_manager
        self.color_mode = color_mode
        self.sleep_time = sleep_time
        self.rows, self.cols = self.term_manager.get_terminal_size()
        self.cols *= 5
        self.col = random.randint(1, self.cols - 1)
        self.length = random.randint(8, self.rows // 3 + 8)
        self.speed = random.randint(3, 10)/10
        self.r, self.g, self.b = self._get_color()

    def _get_color(self):
        """Determine the RGB color based on the color mode."""
        if self.color_mode == "random":
            return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        elif self.color_mode == "rgb-only":
            return [(255, 0, 0), (0, 255, 0), (0, 0, 255)][random.randint(0, 2)]
        else:
            return map(int, self.color_mode.split())

    def draw_char_rgb(self, row, col, char, r, g, b):
        """Draw a character at a specific position with RGB color."""
        print(f"\033[{row};{col}H\033[38;2;{r};{g};{b}m{char}\033[0m", end="", flush=True)

    def run(self):
        """Simulate the falling rain drop."""
        for i in range(1, self.rows + self.length + 1):
            char = random.choice(SYMBOLS)
            self.draw_char_rgb(i, self.col, char, self.r, self.g, self.b)

            # Draw fading trail
            for offset in range(1, 7):
                fade_r, fade_g, fade_b = self.r // (offset + 1), self.g // (offset + 1), self.b // (offset + 1)
                trail_row = i - offset
                if trail_row > 0:
                    self.draw_char_rgb(trail_row, self.col, random.choice(SYMBOLS), fade_r, fade_g, fade_b)

            # Clear characters out of view
            if i > self.length and i - self.length <= self.rows:
                print(f"\033[{i - self.length};{self.col}H ", end="", flush=True)

            time.sleep(self.sleep_time / self.speed)


class MatrixRain:
    """Manages the overall Matrix rain animation."""
    def __init__(self):
        self.term_manager = TerminalManager()
        self.color_mode = "random"  # Default to random colors
        self.sleep_time = 0.05      # Default sleep time between spawns

    def parse_args(self):
        """Parse command-line arguments."""
        for arg in sys.argv[1:]:
            if arg == "--green":
                self.color_mode = "0 255 0"
            elif arg == "--blue":
                self.color_mode = "0 120 255"
            elif arg == "--red":
                self.color_mode = "255 0 0"
            elif arg == "--orange":
                self.color_mode = "255 179 71"
            elif arg == "--cyan":
                self.color_mode = "0 255 255"
            elif arg == "--purple":
                self.color_mode = "180 0 255"
            elif arg == "--sky":
                self.color_mode = "135 206 235"
            elif arg == "--amber":
                self.color_mode = "255 191 0"
            elif arg == "--pink":
                self.color_mode = "255 105 180"
            elif arg == "--sakura":
                self.color_mode = "255 182 193"
            elif arg == "--ice":
                self.color_mode = "173 216 230"
            elif arg == "--mint":
                self.color_mode = "152 255 152"
            elif arg == "--peach":
                self.color_mode = "255 203 164"
            elif arg == "--lavender":
                self.color_mode = "200 150 230"
            elif arg == "--gold":
                self.color_mode = "255 215 0"
            elif arg == "--silver":
                self.color_mode = "220 220 220"
            elif arg == "--rgb":
                self.color_mode = "rgb-only"
            elif arg == "--low-power":
                self.sleep_time = 0.1  # Lower CPU usage
            elif arg == "--help":
                self.print_help()
                sys.exit(0)
            else:
                print(f"Unknown option: {arg}", file=sys.stderr)
                sys.exit(1)

    def print_help(self):
        """Display help menu."""
        print("""
Matrix Rain CLI Options:
  matrix               → Random color rain
  matrix --green       → Classic Matrix green
  matrix --blue        → Blue rain
  matrix --red         → Red rain
  matrix --orange      → Orange rain
  matrix --cyan        → Cyan rain
  matrix --purple      → Purple rain
  matrix --sky         → Sky blue rain
  matrix --amber       → Amber/orange-yellow rain
  matrix --pink        → Pink rain
  matrix --sakura      → Cherry blossom pink rain
  matrix --ice         → Icy light blue rain
  matrix --mint        → Fresh mint rain
  matrix --peach       → Peach rain
  matrix --lavender    → Light lavender rain
  matrix --gold        → Golden yellow rain
  matrix --silver      → Silver rain
  matrix --rgb         → Red, green, blue rain
  matrix --low-power   → Enables low FPS, uses less CPU
  matrix --help        → Show this help panel

Example: matrix --blue --low-power
Press Ctrl+C anytime to exit the Matrix Rain.
""")

    def main(self):
        
        self.term_manager.init_term()
        try:
            while True:
                # Limit number of active threads to avoid overloading CPU
                if len(threading.enumerate()) < self.term_manager.get_terminal_size().columns * 4:
                    threading.Thread(target=RainDrop(self.term_manager, self.color_mode, self.sleep_time).run, daemon=True).start()
                time.sleep(self.sleep_time / 2)
        except KeyboardInterrupt:
            pass
        finally:
            self.term_manager.deinit_term()


if __name__ == "__main__":
    SYMBOLS = 'ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=<>?/|[]{}□△▽※¤☆♪♫∆∇∞§'
    app = MatrixRain()
    app.parse_args()
    app.main()