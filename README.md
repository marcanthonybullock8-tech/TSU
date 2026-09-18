# TSU — The Social Universe

An MCU-style franchise bible dramatizing the real founding myths of the social internet (fictionalized, PG-13, 100% owned) through a Black core cast of former child stars turned platform founders.

## Structure

- **`canon/`** — the locked/living bible documents. Source of truth for every script.
  - `TSU_Core_Cast.md` — the founding seven's bios
  - `TSU_Family_Bible.md` — family units for all seven
  - `TSU_Extended_Ensemble.md` — supporting/recurring cast
  - `TSU_Platform_Roster.md` — real platform -> fictional 1:1 counterparts, organized by Phase
  - `TSU_Continuity_Bible.md` — master canon: serialization model, house style, fixed timeline anchors, character status tracker
  - `TSU_Historical_Context.md` — the soft-alternate-history world these characters exist in

- **`scripts/`** — full screenplays, one per film, named after their platform (e.g. `THE_ROSTER.md`). Each includes the pitch, logline, synopsis, antagonists, format specs, full scene-by-scene breakdown, and sample pages in standard screenplay format.

- **`tools/md2pdf.py`** — converts every `.md` file to a matching `.pdf`. Every file in `canon/` and `scripts/` is tracked as both: the `.md` is the editable source of truth, the `.pdf` is the deliverable. Re-run this after any edit to keep them in sync (see the script's own header for setup/usage).

If canon docs ever conflict, `TSU_Continuity_Bible.md` wins until a change is logged in its §8 Change Log.
