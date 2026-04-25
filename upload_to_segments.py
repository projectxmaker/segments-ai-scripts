from segments import SegmentsClient
import os
import argparse

# API KEY
API_KEY = "3bf7a27d2fb773a8c2999c0ca904db2b2ec0ebb5"

def upload_sequence(folder, dataset_name, sample_name):
    client = SegmentsClient(API_KEY)

    if not os.path.exists(folder):
        print(f"Error: Folder {folder} does not exist.")
        return

    files = sorted([f for f in os.listdir(folder) if f.endswith(('.jpg', '.png'))])
    print(f"Uploading {len(files)} frames from folder '{folder}' to dataset '{dataset_name}'...")

    frames_list = []

    for filename in files:
        file_path = os.path.join(folder, filename)
        with open(file_path, 'rb') as f:
            uploaded_file = client.upload_asset(f, filename)
            actual_url = uploaded_file.url

            frame_entry = {
                "name": filename,
                "image": {
                    "url": actual_url
                }
            }
            frames_list.append(frame_entry)
            print(f"Uploaded: {filename}")

    attributes = {"frames": frames_list}

    try:
        client.add_sample(dataset_name, name=sample_name, attributes=attributes)
        print("-" * 30)
        print(f"FINISHED! Sample '{sample_name}' is ready.")
    except Exception as e:
        print(f"Error at add_sample: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload image sequence to Segments.ai")
    parser.add_argument("--folder", required=True, help="Image folder")
    parser.add_argument("--dataset", required=True, help="Dataset name (exp: Ohayou/Hand_Action_Labeling)")
    parser.add_argument("--name", required=True, help="Sample name (exp: video_case_2)")

    args = parser.parse_args()
    upload_sequence(args.folder, args.dataset, args.name)
