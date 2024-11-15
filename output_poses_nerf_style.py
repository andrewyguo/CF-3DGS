import os
import json
import torch
import numpy as np
import argparse

def load_camera_intrinsics(cameras_path):
    """Load camera intrinsics from a cameras.txt file."""
    with open(cameras_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith('#') or line.strip() == '' or line.startswith('Number of cameras:'):
            continue

        # Parse the intrinsics from the line
        parts = line.split()
        if len(parts) > 4:
            width = int(parts[2])
            height = int(parts[3])
            fx = float(parts[4])
            fy = float(parts[5])
            cx = float(parts[6])
            cy = float(parts[7])
            k1 = float(parts[8])
            k2 = float(parts[9])
            p1 = float(parts[10])
            p2 = float(parts[11])

            return {
                'w': width,
                'h': height,
                'fl_x': fx,
                'fl_y': fy,
                'cx': cx,
                'cy': cy,
                'k1': k1,
                'k2': k2,
                'p1': p1,
                'p2': p2
            }

    raise ValueError("No valid camera intrinsics found in the file.")

def save_poses_to_json(result_path, cameras_path, output_path):
    """Save poses and camera intrinsics to a NeRF-style transforms.json file."""
    # Load poses
    pose_path = os.path.join(result_path, 'ep00_init.pth')
    poses = torch.load(pose_path)
    import IPython; IPython.embed(); exit(1)

    poses_pred = poses['poses_pred'].inverse().cpu().numpy()

    # Load camera intrinsics
    intrinsics = load_camera_intrinsics(cameras_path)

    # Create the NeRF-style JSON structure
    transforms = intrinsics
    transforms["frames"] = []

    for idx, pose in enumerate(poses_pred):
        transform_matrix = pose.tolist()
        frame = {
            "file_path": f"images/{idx:06d}.png",  # Placeholder for image file paths
            "transform_matrix": transform_matrix
        }
        transforms["frames"].append(frame)

    # Save to JSON
    with open(output_path, 'w') as f:
        json.dump(transforms, f, indent=4)

    print(f"Transforms.json saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save poses and camera intrinsics to a NeRF-style transforms.json file.")
    parser.add_argument("-r", "--result_path", required=True, help="Path to the result directory containing ep00_init.pth")
    parser.add_argument("-c", "--cameras_path", required=True, help="Path to the cameras.txt file")
    parser.add_argument("-o", "--output_path", required=True, help="Path to save the output transforms.json file")

    args = parser.parse_args()

    save_poses_to_json(args.result_path, args.cameras_path, args.output_path)