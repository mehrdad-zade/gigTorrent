# pip install libtorrent
# pip install tqdm

import libtorrent as lt
import time
import logging
import sys
from tqdm import tqdm

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_torrent(magnet_link, download_path, timeout=3600):
    """
    Download a torrent using a magnet link.

    :param magnet_link: str, the magnet link of the torrent
    :param download_path: str, the path where the torrent will be downloaded
    :param timeout: int, the time in seconds to wait for the download to complete
    """
    try:
        # Create a session
        ses = lt.session()

        # Add settings to the session
        settings = {
            'listen_interfaces': '0.0.0.0:6881',
        }
        ses.apply_settings(settings)

        # Parse magnet link and add torrent
        params = lt.parse_magnet_uri(magnet_link)
        params.save_path = download_path
        handle = ses.add_torrent(params)

        # Logging and waiting for the download to start
        logging.info("Downloading metadata...")
        while not handle.has_metadata():
            time.sleep(1)
        logging.info("Got metadata, starting torrent download...")

        # Setup progress bar
        torrent_info = handle.get_torrent_info()
        total_size = torrent_info.total_size()
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading")

        # Downloading the torrent
        start_time = time.time()
        while (handle.status().state != lt.torrent_status.seeding):
            if time.time() - start_time > timeout:
                raise TimeoutError("Timeout reached, download incomplete.")
            
            downloaded = handle.status().total_done
            progress_bar.update(downloaded - progress_bar.n)  # Update progress bar
            time.sleep(1)

        progress_bar.close()
        logging.info("Download completed.")

    except Exception as e:
        progress_bar.close()
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <magnet_link>")
        sys.exit(1)

    magnet_link = sys.argv[1]
    download_path = "<DOWNLOAD_PATH>"
    download_torrent(magnet_link, download_path)


