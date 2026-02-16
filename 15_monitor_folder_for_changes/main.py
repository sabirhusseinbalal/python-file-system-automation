from pathlib import Path
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

BASE_DIR = Path(__file__).resolve().parent

class FolderEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"[CREATED] {event.src_path}")

    def on_deleted(self, event):
        print(f"[DELETED] {event.src_path}")

    def on_modified(self, event):
        # Avoid printing directory metadata changes repeatedly
        if not event.is_directory:
            print(f"[MODIFIED] {event.src_path}")

    def on_moved(self, event):
        print(f"[MOVED] from {event.src_path} to {event.dest_path}")

def monitor_folder(path_to_watch):
    """Monitors the given folder for changes."""
    try:
        event_handler = FolderEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path=path_to_watch, recursive=True)
        observer.start()
        print(f"Monitoring started on: {path_to_watch}")
        print("Press Ctrl+C to stop.")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping monitoring...")
        observer.stop()
    except FileNotFoundError:
        print(f"Error: The folder '{path_to_watch}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    observer.join()

    

while True:
    print()
    user_path = input("Enter full folder path (or 'q' to quit): ").strip()
    print()

    default_folder = BASE_DIR / "input"

    if user_path.lower() == 'q':
        print("Exiting...")
        break

    if not user_path:
        path = default_folder
        if path.is_dir():
            print(f"No path provided — using default folder: {path}")
        else:
            print("Default folder is missing.")
            continue
    else:
        path = Path(user_path)
    
    if path.is_dir():
        try:
            print(f"Folder exists: {path}")
            monitor_folder(path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Folder not found. Please enter a valid folder path.")
