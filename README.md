<div align="center">

# matrix

**A stupid simple digital rain effect implemented in pure Bash**  
Just run and vibe. No dependencies. No nonsense.  
<img src="matrix.gif" alt="matrix rain preview">

<p>
  <img src="https://shields.io/badge/made-with%20%20bash-green?style=flat-square&color=d5c4a1&labelColor=1d2021&logo=gnu-bash">
  <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg">
  <a href="https://discord.gg/W4mQqNnfSq">
    <img src="https://discordapp.com/api/guilds/913584348937207839/widget.png?style=shield"/>
  </a>
</p>

</div>

---

## ⚡ Preview It Instantly

Run directly in your terminal with no install:

```bash
bash <(curl -s https://raw.githubusercontent.com/saitamasahil/matrix2/main/matrix)
```

> This is the default theme & it uses random colors.

Use any color theme by passing a flag:

```bash
bash <(curl -s https://raw.githubusercontent.com/saitamasahil/matrix2/main/matrix) --red
```

> This command runs the digital rain in the red color theme.

> Check more flags below in the [🎨 Available Themes](#-available-themes) section.

---

## 📦 Download & Install

Clone the repo:

```bash
git clone https://github.com/saitamasahil/matrix2
cd matrix
```

Optional: install globally

```bash
sudo cp matrix /usr/local/bin
```

---

## 🕹️ Usage

You can now run the digital rain like so:

```bash
matrix             # Default: random color mode
matrix --green     # Classic green rain
matrix --red       # Red rain
matrix --low-power # Low power mode (slower animation)
```

If not installed, run directly via:

```bash
./matrix
```

---

## 🎨 Available Themes

| Flag         | Description           |
| ------------ | --------------------- |
| `--green`    | Classic Matrix green  |
| `--orange`   | Orange rain           |
| `--blue`     | Blue rain             |
| `--red`      | Red rain              |
| `--cyan`     | Cyan rain             |
| `--purple`   | Purple rain           |
| `--sky`      | Sky blue rain         |
| `--amber`    | Amber/orange-yellow   |
| `--pink`     | Bright pink rain      |
| `--sakura`   | Sakura soft pink rain |
| `--ice`      | Icy blue rain         |
| `--mint`     | Fresh mint rain       |
| `--peach`    | Peach tone rain       |
| `--lavender` | Light lavender rain   |
| `--gold`     | Golden yellow rain    |
| `--silver`   | Silver rain           |
| `--rgb`      | Red, green, blue rain |
| _(default)_  | Random color mode     |

> Run `matrix` with no flag for a random-colored experience

---

## ⚙️ Optional mode

| `--low-power` | Enables low FPS, uses less CPU |

Example:

```bash
matrix --green --low-power
```

This runs the green theme with low power usage (slower drops, less CPU load).

## ✅ Requirements

- Bash 3.2+
- UTF-8 capable terminal (GNOME Terminal, iTerm2, Alacritty, etc.)
- Truecolor (24-bit) terminal support (most modern terminals support this)
- Terminal must support ANSI escape sequences
- Works on **Linux**, **macOS**, and **WSL**
- No external dependencies

---

## ❌ Uninstall

If you installed with `cp`, remove it like so:

```bash
sudo rm /usr/local/bin/matrix
```

---

## 🧠 Inspired By

Originally inspired by the [matrix project by wick3dr0se](https://github.com/wick3dr0se/matrix) and, of course, the legendary visuals from _The Matrix_.

> “I can only show you the door. You’re the one that has to walk through it.” — Morpheus
