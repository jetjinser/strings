from sql_exe import *
from typing import Union, List, Dict

off_dict: Dict[int, bool] = {}


def enable_group() -> Union[List[set], None]:
    sql_check = (
        'SELECT group_id FROM setting WHERE bool=?;'
    )
    enable_group_list = sql_exe(sql_check, (0,))
    if enable_group_list:
        return enable_group_list
    else:
        return


on_off_list = enable_group()
if on_off_list:
    off_dict = {}
    for i in on_off_list:
        group_id = i[0]
        if not off_dict.get(group_id):
            off_dict[group_id] = False
