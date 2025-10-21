import requests
import os
from urllib.parse import urlparse
import sys

def fetch_image():
    print("🌍 Welcome to the Ubuntu Image Fetcher!")

    # Prompt the user for a URL
    image_url = input("Enter the URL of the image to download: ").strip()

    # Create directory for fetched images
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        # Send HTTP GET request to fetch image
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Extract filename from URL
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)

        # If URL doesn't contain a valid filename, create one
        if not filename:
            filename = "downloaded_image.jpg"

        # Create full path
        filepath = os.path.join(folder_name, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully downloaded and saved as '{filepath}'")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please ensure it starts with http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("🚫 Connection Error: Unable to reach the server.")
    except requests.exceptions.Timeout:
        print("⏰ Request timed out. Please try again later.")
    except Exception as e:
        print(f"⚡ Unexpected error: {e}")
    finally:
        print("\n🙏 Program ended gracefully. Thank you for using Ubuntu Image Fetcher!")


# Run the program
if __name__ == "__main__":
    fetch_image()
