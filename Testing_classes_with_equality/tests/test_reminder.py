from lib.reminder import *

def test_remind_the_user_to_do_a_task():
    reminder = Reminder('Kat')
    reminder.remind_me_to('Feed cats')
    result = reminder.remind()
    assert result == 'Feed cats, Kat!'