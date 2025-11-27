 # Luma Lanterns — Defold minimal project
 
 This workspace contains a minimal Defold project structure for a simple vertical, mobile-friendly tap game.

 What is included
 - `game.project` — basic project config for 720x1280 portrait
 - `main/main.collection` — minimal placeholder collection
 - `main/main.go` — placeholder describing required factory + script components
 - `main/main.script` — main game logic: spawns lanterns, handles taps, energy, lives
 - `main/lantern.go` — placeholder for lantern prototype
 - `main/lantern.script` — lantern movement + destroy logic
 - `main/luma.go` & `main/luma.script` — Luma object and energy state logic
 - `main/background.go` — background placeholder
 - `gui/hud.gui` & `gui/hud.gui_script` — HUD and logic (energy bar, hearts, target color, state text)
 - `gui/pause.gui` & `gui/pause.gui_script` — pause menu placeholder
 - `atlases/game.atlas` — atlas placeholder (generate PNGs then create atlas in editor)
 - `input/game.input_binding` — minimal input binding for touch
 - `tools/generate_placeholders.py` & `scripts/generate_assets.sh` — generate solid PNG placeholders

 Quick setup
 1. Open Defold and `Project -> Open` this folder.
 2. Generate placeholder PNGs (optional, helpful to avoid manual image creation):

 ```bash
 ./scripts/generate_assets.sh
 ```

 3. In Defold Editor: create an Atlas `game.atlas` and add the generated PNGs from `assets/images/`.
	 Name atlas sprites as: `lantern_red`, `lantern_blue`, `lantern_yellow`, `luma_idle`, `heart`, `background`.
 4. In the `main` collection create a game object (or use `main/main.go` placeholder):
	 - Add a Factory component called `lantern_factory` that references `/main/lantern.go`.
	 - Add a Script component referencing `/main/main.script` on the same GO.
	 - Add GUI for HUD (attach `gui/hud.gui_script`, ensure GUI id is `hud`) and a GUI for pause if desired.
	 - Add Luma and Background instances referencing `/main/luma.go` and `/main/background.go`.

 How Level 1 works
 - Lanterns spawn from the bottom and float upward.
 - The HUD shows a target color (initially red) and an energy bar.
 - Tapping the correct color increases energy; incorrect taps reduce lives.
 - Reaching max energy triggers `Level Complete`, zero lives triggers `Game Over`.

 Notes
 - The project is intentionally minimal: many `.go` and `.gui` files are placeholders that require you to add components and sprites in the Defold Editor.
 - Use `./scripts/generate_assets.sh` to create the PNG placeholders automatically.