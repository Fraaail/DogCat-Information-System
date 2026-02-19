# DogCat-Information-System

---

## Overview
A simple Tkinter GUI for browsing short, consistent information about dog and cat breeds. The app uses `Main.py` as the launcher and stores breed entries in `Dogs.py` and `Cats.py` (entries should be short phrases so they fit the Tkinter textboxes).

## Quick start ✅
1. Requirements: Python 3.x and Tkinter (Linux: `sudo apt install python3-tk`).
2. Run the app:

   `python3 Main.py`

3. If images don't appear or the app fails to start, see **Fix paths** below.

## Fix paths / Cross-platform note ⚠️
The project currently contains absolute Windows paths inside `Main.py`. To run on Linux (or any other system), change those to relative paths.

- Replace the Windows asset path with a relative path:

  From:

  ```python
  ASSETS_PATH = OUTPUT_PATH / Path(r"D:\\School\\College\\Codes\\DogCat Information System\\assets\\frame2")
  ```

  To:

  ```python
  ASSETS_PATH = OUTPUT_PATH / Path("assets/frame2")
  ```

- Replace absolute subprocess calls with relative references (or use `OUTPUT_PATH`):

  From:

  ```python
  subprocess.run([sys.executable, r"D:\\School\\College\\Codes\\DogCat Information System\\Dogs.py"])
  ```

  To:

  ```python
  subprocess.run([sys.executable, str(OUTPUT_PATH / "Dogs.py")])
  ```

After updating, run `python3 Main.py` from the repository root.

### Example 1 — Exercise needs
Prompt:
Exercise needs of these dog breeds. Answer only in one phrase
Afghan Hound
Akita
Australian Shepherd
Beagle
Boxer
Bulldog
Chihuahua
Cocker Spaniel
Collie
Dachshund
Doberman Pinscher


ChatGPT:
Afghan Hound: High exercise needs
Akita: Moderate exercise needs
Australian Shepherd: High exercise needs
Beagle: Moderate exercise needs
Boxer: High exercise needs
Bulldog: Low exercise needs
Chihuahua: Moderate exercise needs
Cocker Spaniel: Moderate exercise needs
Collie: High exercise needs
Dachshund: Moderate exercise needs
Doberman Pinscher: High exercise needs



### Example 2 — Colors
Prompt:
Colors of these dog breeds. Answer only in one word or phrase
Afghan Hound
Akita
Australian Shepherd
Beagle
Boxer
Bulldog
Chihuahua
Cocker Spaniel
Collie
Dachshund
Doberman Pinsche

ChatGPT:
Afghan Hound: Various colors
Akita: Multiple colors
Australian Shepherd: Varied coat colors
Beagle: Tri-color or bi-color
Boxer: Fawn or brindle
Bulldog: Various colors
Chihuahua: Various colors
Cocker Spaniel: Various solid colors
Collie: Sable and white, tri-color, or blue merle
Dachshund: Various colors and patterns
Doberman Pinscher: Black and tan, red, blue, or fawn



## Dog Page — data format 🐶
- Use the `Cats.py` entries as the canonical format for consistency.
- Keep each field to **one short phrase** so it fits the textbox.
- Use ChatGPT (or similar) to generate concise values, then paste them into `Dogs.py`.

> Tip: keep answers short — each entry should be a single phrase to fit the GUI textbox.

## Assets / Images 📁
- Use relative paths such as `assets/frame0`, `assets/frame1`, `assets/frame2`.
- Avoid Windows-style backslashes (`\\assets\\frame#`) in code; use forward slashes or `pathlib`.

## Project structure
- `Main.py` — launcher / GUI
- `Dogs.py` — dog breed data
- `Cats.py` — cat breed data
- `Cats_Backup.py` — backup data
- `assets/` — image frames (`frame0`, `frame1`, `frame2`)

## Contributing ✨
- Follow the existing data format in `Cats.py` when adding breeds to `Dogs.py`.
- Open a PR or edit files directly if you are working locally.

## License
No license specified.

---