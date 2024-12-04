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
    return len (save_reports)

def count_save_reports_with_dampener ( list_of_reports: list) -> int:
    save_reports = list(filter(is_save_with_dampener, list_of_reports))
    return len (save_reports)

def is_save_with_dampener (list_of_levels: list) -> bool:
    if len(list_of_levels)<2:
        return True
    
    first_diff = list_of_levels[1] - list_of_levels[0]

    for index in range (len(list_of_levels)-1):
        if ( not is_current_diff_save ( first_diff, list_of_levels[index+1]-list_of_levels[index])):            
            # either current element is the problem, or the next one, or the first element gives a wrong "direction"
            result = is_save ( list_of_levels[:index] + list_of_levels[index+1:]) \
                or is_save ( list_of_levels[:index+1] + list_of_levels[index+2:]) \
                or is_save ( list_of_levels[1:])
            return result

    return True