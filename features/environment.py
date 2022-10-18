from yaml import full_load
import features.steps.json_responses as json_responses


def before_all(context):
    context.settings = full_load(open('features/conf.yaml').read())
    context.base_url = ""
    context.headers = {}
    context.verify_ssl = True
    context.user_agent = context.settings['user_agent']
    context.json_responses = json_responses
