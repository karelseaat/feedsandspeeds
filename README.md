# feedsandspeeds

A no-frills Python tool to calculate feed rates and chip loads from spindle speed, flute count, and material. I built this after getting tired of flipping through machining handbooks and spreadsheet templates.

Three files in the repo:
- `feedsandspeeds.py` — the actual calculator
- `ncursestest.py` — a quick curses demo (just prints a message)
- `pyscreentest.py` — a tiny PySCREEN demo showing form rendering

## Usage

```bash
python3 feedsandspeeds.py
```

Enter flute count and spindle RPM (e.g., `4` flutes, `12000` RPM). Output is feed rate (in/min) and chip load (mm/tooth or thou/tooth) for:
- Aluminum 6061
- Mild steel
- Stainless 304
- Polycarbonate
- Oak

Values come from common Machinist’s Handbook formulas—no magic numbers.

## Files Overview

### `feedsandspeeds.py`

Main script. Parses inputs, applies:

```
Feed Rate = RPM × N_flutes × Chip Load
Chip Load = K × D_tool / N_flutes   (simplified, K is material-specific)
```

Stashes material constants in a dict at the top. Easy to tweak.

### `ncursestest.py`

Just enough curses to show an interactive prompt. Useful for sanity-checking terminal behavior before building something bigger.

### `pyscreentest.py`

 Demonstrates PySCREEN’s form API with a title, dropdown, and text field. Not production-ready—just a template.

## Contributing

Pull requests welcome for:
- New materials (just add K and chip load ranges to the constants dict)
- Edge cases (e.g., input validation for RPM < 100)
- Cleanups (if you spot redundant code)

No style docs—just follow what’s there. Run `black` before pushing if you care about formatting.

## License

MIT — see [LICENSE](LICENSE).