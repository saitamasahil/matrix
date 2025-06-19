# matrix

A simple digital rain effect in pure Bash.  
Just run it. No dependencies, no setup—just vibes.  
<img src="matrix.gif" alt="matrix rain preview">

---

## Preview Instantly

Run it straight from your terminal, no installation needed:

```bash
bash <(curl -s https://raw.githubusercontent.com/saitamasahil/matrix2/main/matrix)
```

This runs the default theme with random colors.

To use a specific color theme, pass a flag like this:

```bash
bash <(curl -s https://raw.githubusercontent.com/saitamasahil/matrix2/main/matrix) --red
```

> Check more flags below in the [🎨 Available Themes](#-available-themes) section.

Tip: Use a dark or black terminal background to get the best visual effect.

---

## Download and Install

Clone the repository:

```bash
git clone https://github.com/saitamasahil/matrix2
cd matrix
```

(Optional) Install it globally so you can run `matrix` from anywhere:

```bash
sudo cp matrix /usr/local/bin
```

---

## How to Use

Once installed, just type:

```bash
matrix             # Default: random color rain
matrix --green     # Classic Matrix green
matrix --red       # Red theme
matrix --low-power # Slower animation, uses less CPU
```

If you're running it directly:

```bash
./matrix
```

---

## Available Themes

| Flag         | Description              |
| ------------ | ------------------------ |
| `--green`    | Classic Matrix green     |
| `--orange`   | Orange rain              |
| `--blue`     | Blue rain                |
| `--red`      | Red rain                 |
| `--cyan`     | Cyan rain                |
| `--purple`   | Purple rain              |
| `--sky`      | Sky blue rain            |
| `--amber`    | Amber/orange-yellow rain |
| `--pink`     | Pink rain                |
| `--sakura`   | Cherry blossom pink rain |
| `--ice`      | Icy light blue rain      |
| `--mint`     | Fresh mint rain          |
| `--peach`    | Peach rain               |
| `--lavender` | Light lavender rain      |
| `--gold`     | Golden yellow rain       |
| `--silver`   | Silver rain              |
| `--rgb`      | Red, green, blue rain    |
| _(default)_  | Random color rain        |

---

## Other Flags

| Flag          | Description                    |
| ------------- | ------------------------------ |
| `--help`      | Show the help panel            |
| `--low-power` | Enables low FPS, uses less CPU |

Example:

```bash
matrix --green --low-power
```

---

## Requirements

- Bash 3.2+
- UTF-8 capable terminal (GNOME Terminal, iTerm2, Alacritty, etc.)
- Truecolor (24-bit) terminal support
- Terminal must support ANSI escape sequences
- Works on Linux, macOS, and WSL
- No external dependencies

---

## Uninstall

If you installed with `cp`, remove it like so:

```bash
sudo rm /usr/local/bin/matrix
```

---

## Inspired By

Originally inspired by the [matrix project by wick3dr0se](https://github.com/wick3dr0se/matrix) and, of course, the legendary visuals from _The Matrix_.

"I can only show you the door. You're the one that has to walk through it." — Morpheus
