# If this script does not work then most likely you need to change line 7 so that it finds your download folder or line 10 so that the target folder is found.

import os
import shutil
from pathlib import Path

# Find Downloads folder automatically
downloads = Path.home() / "Downloads"

# Project folder (where this script is saved)
project = Path(__file__).resolve().parent.parent

moved = 0

for filename in os.listdir(downloads):

    # Only process Sen1Floods11 files
    if not filename.startswith("v1.1_data_flood_events_HandLabeled_"):
        continue

    if not filename.endswith(".tif"):
        continue

    # Decide which folder the file belongs to
    if "_LabelHand_" in filename:
        data_type = "LabelHand"
    elif "_S1Hand_" in filename:
        data_type = "S1Hand"
    else:
        continue

    # Remove the long prefix
    prefix = f"v1.1_data_flood_events_HandLabeled_{data_type}_"
    new_name = filename.removeprefix(prefix)

    # Move file to the correct folder
    destination_folder = project / "data" / data_type
    destination_folder.mkdir(parents=True, exist_ok=True)

    old_path = downloads / filename
    new_path = destination_folder / new_name

    if not new_path.exists():
        shutil.move(old_path, new_path)
        moved += 1
        print(filename, "->", new_name)
    else:
        print("Already exists, skipped:", new_name)

print("Finished! Moved files:", moved)