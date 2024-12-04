def is_save ( list_of_leves: list) -> bool:
    if len(list_of_leves)<2:
        return True
    
    first_diff = list_of_leves[1] - list_of_leves[0]

    for index in range (len(list_of_leves)-1):
        diff = list_of_leves[index+1]-list_of_leves[index]

        if ( diff * first_diff < 0 ):
            return False
        if ( abs(diff)<1 or abs(diff)>3):
            return False

    return True


def count_save_reports ( list_of_reports: list) -> int:
    save_reports = list(filter(is_save, list_of_reports))
    return len ( save_reports)