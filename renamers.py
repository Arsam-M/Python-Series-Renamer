import os
import re

def rename_all(folder_path, series_name, num_seasons, episodes_per_season, all_files):
    print(f"\nFound {len(all_files)} files.Starting FULL renaming process...\n")
    
    file_index = 0
    for season_num in range(1, num_seasons + 1):
        ep_count = episodes_per_season[season_num - 1] if season_num <= len(episodes_per_season) else 0
        
        season_folder_name = f"S{season_num:02d}"
        season_folder_path = os.path.join(folder_path, season_folder_name)
                
        if  not os.path.exists(season_folder_path):
            os.mkdir(season_folder_path)
                    
        for ep_num in range(1, ep_count + 1):
            if file_index >= len(all_files):
                print("Warning: Ran out of files to rename")
                return
            
            file_path = all_files[file_index]
            filename = os.path.basename(file_path)
            name, ext = os.path.splitext(filename)
            
            new_name = f"{series_name} S{season_num:02d}E{ep_num:02d}{ext}"
            new_path = os.path.join(season_folder_path, new_name)
            
            if os.path.exists(new_path):
                print(f'Skipped {filename} (Target "{new_name}" already exists)')
            else:
                try:
                    os.rename(file_path, new_path)
                    print(f"✅ {filename} -> {new_name}")
                except Exception as e:
                    print(f"Error moving:{e}")
            file_index += 1
        
        
def rename_range(folder_path, series_name, episodes_per_season, all_files, start_s, start_e, end_s, end_e):
    print(f"\nFound {len(all_files)} files.Starting RANGE renaming process...\n")
    season_ep_pattern = re.compile(r'[Ss](\d+)[Ee](\d+)')
    double_ep_pattern = re.compile(r'[Ss]\d+[Ee](\d+)(?:[Ee\-\&])(\d+)')
    
    count_renamed = 0

    for file_path in all_files:
        if not os.path.exists(file_path):
            continue
        
        filename = os.path.basename(file_path)
        match = season_ep_pattern.search(filename)
        
        if match:
            season_num = int(match.group(1))
            ep_num = int(match.group(2))
            
            is_after_start = (season_num > start_s) or (season_num == start_s and ep_num >= start_e)
            is_before_end = (season_num < end_s) or (season_num == end_s and ep_num <= end_e)
            
            if is_after_start and is_before_end:
                name, ext = os.path.splitext(filename)
                season_folder_name = f"S{season_num:02d}"
                season_folder_path = os.path.join(folder_path, season_folder_name) 
                
                if  not os.path.exists(season_folder_path):
                    os.mkdir(season_folder_path)
                
                is_double = False
                double_match = double_ep_pattern.search(filename)
                
                if double_match:
                    if int(double_match.group(1)) == ep_num:
                        is_double = True
                if is_double:
                    new_name = f"{series_name} S{season_num:02d}E{ep_num:02d}-E{ep_num+1:02d}{ext}"
                else:
                    new_name = f"{series_name} S{season_num:02d}E{ep_num:02d}{ext}"
                
                new_path = os.path.join(season_folder_path, new_name)
                
                if os.path.exists(new_path):
                    print(f'Skipped {filename} (Target "{new_name}" already exists!)')
                else:
                    try:
                        os.rename(file_path, new_path)
                        print(f"✅ {filename} -> {new_name}")
                        count_renamed += 1
                    except Exception as e:
                        print(f"Error moving {filename}:{e}")
    if count_renamed == 0:
        print("No files were found matching the folowing description")
    else:
        print(f"\nsuccessfully renamed {count_renamed} files.")
