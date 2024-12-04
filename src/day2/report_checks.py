def is_save ( list_of_levels: list) -> bool:
    if len(list_of_levels)<2:
        return True
    
    first_diff = list_of_levels[1] - list_of_levels[0]

    for index in range (len(list_of_levels)-1):
        if ( not is_current_diff_save ( first_diff, list_of_levels[index+1]-list_of_levels[index])):
            return False

    return True

def is_current_diff_save ( first_diff: int, current_diff: int) -> bool:
    return (first_diff * current_diff > 0 ) and abs(current_diff)>=1 and abs(current_diff)<=3
        

def count_save_reports ( list_of_reports: list) -> int:
    save_reports = list(filter(is_save, list_of_reports))
    return len ( save_reports)

def is_save_with_dampener (list_of_levels: list) -> bool:
    if len(list_of_levels)<2:
        return True
    
    first_diff = list_of_levels[1] - list_of_levels[0]

    for index in range (len(list_of_levels)-1):
        if ( not is_current_diff_save ( first_diff, list_of_levels[index+1]-list_of_levels[index])):
            return is_save ( list_of_levels[:index] + list_of_levels[index+1:])

    return True