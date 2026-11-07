import os
from utils import get_valid_int, get_valid_path, get_all_files
from renamers import rename_all, rename_range

def main():
    print("=== Ultimate Series Sorter ===")
    
    folder_path = get_valid_path("Enter the absolute path of the main folder: ")
    video_ext = ('.mp4', '.mkv', '.mov', '.avi')
    all_files = get_all_files(folder_path, video_ext)
    
    if not all_files:
        print("No Videos Found in selected Directory or subdirectories!")
        return
    
    print(f'Found {len(all_files)} video files in total (including subfolders).')
    
    print('''
Select a mode:
1. Rename ALL files (Based on season/episode count)
2. Rename a SPECIFIC RANGE (Start to End)''')
    
    mode = get_valid_int("Enter your choice: ")
    
    series_name = input("Enter the series name (e.g., 'Breaking Bad'): ").strip()
    
    if mode == 1:
        num_seasons = get_valid_int("How many Seasons in Total? ")
        episodes_per_season = []
        for s in range (1, num_seasons + 1):
            eps = get_valid_int(f"Enter the number of Episodes for Season {s}: ")
            episodes_per_season.append(eps)
            
        rename_all(folder_path, series_name, num_seasons, episodes_per_season, all_files)
    
    elif mode == 2:
        num_seasons = get_valid_int("How many Seasons in Total? ")
        episodes_per_season = []
        for s in range (1, num_seasons + 1):
            eps = get_valid_int(f"Enter the number of Episodes for Season {s}: ")
            episodes_per_season.append(eps)
            
        print("\n--- Select Range ---")
        start_s = get_valid_int("Start from Season :")
        start_e = get_valid_int("Start from Episode :")
        end_s = get_valid_int("End at Season :")
        end_e = get_valid_int("end at Episode :")
        
        rename_range(folder_path, series_name, episodes_per_season, all_files, start_s, start_e, end_s, end_e)
        
    else:
        print("Invalid Choice. Exitting.")
        
    print("\n All done! Your series are now perfectly organized.")

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to run again? (Y/N)").strip().lower()
        if again !="y":
            print("Goodbye")
            break