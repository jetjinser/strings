from nonebot import CommandSession, on_command
from nonebot import on_natural_language, NLPSession, IntentCommand

import re
from random import randint


@on_command('roll_num')
async def roll_num(session: CommandSession):
    roll_1 = session.get("roll_1")
    roll_2 = session.get("roll_2")

    n_list = []

    for i in range(int(roll_1)):
        n_list.append(randint(1, int(roll_2)))

    m_list = map(str, n_list)
    print(m_list)
    print(n_list)

    if len(n_list) >= 2:
        await session.send(' , '.join(m_list))
    else:
        await session.send(''.join(m_list))


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    msg = session.ctx.get('message')
    msg = str(msg)

    pattern = re.compile(r'^(\d*)d(\d*)$')

    roll = pattern.match(msg)

    if roll:
        if roll.group(1) and roll.group(2):
            roll_1 = roll.group(1)
            roll_2 = roll.group(2)

            return IntentCommand(90, 'roll_num', args={'roll_1': roll_1, 'roll_2': roll_2})

        elif roll.group(2):
            roll_1 = 1
            roll_2 = roll.group(2)

            return IntentCommand(90, 'roll_num', args={'roll_1': roll_1, 'roll_2': roll_2})
