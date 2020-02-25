from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.trainers import ListTrainer

from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

strings_bot = ChatBot(
    'strings',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': '我不知道该说什么',
            'maximum_similarity_threshold': 0.90
        },
    ],
    response_selection_method=get_most_frequent_response
)


@on_command('chatterbot', aliases=['>'])
async def chat_chatterbot(session: CommandSession):
    msg = session.get('msg', prompt='什么')
    response = strings_bot.get_response(msg)
    await session.send(str(response))


@chat_chatterbot.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['msg'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('你要说什么')

    session.state[session.current_key] = stripped_arg

conversation = []


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    msg = session.msg_text
    if msg:
        if 'https://' in msg:
            return
        conversation.append(session.msg_text)
        if len(conversation) > 10:
            return IntentCommand(60, 'trainer', args={'conversation_train': conversation})


@on_command('trainer')
async def chat_trainer(session: CommandSession):
    conversation_train = session.get('conversation_train')
    trainer = ListTrainer(strings_bot)
    trainer.train(conversation_train)

    global conversation
    conversation = []
