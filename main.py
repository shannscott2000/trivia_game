import requests
import json
from re import search

score = 0
# make a request from api
def request_api_data():
    url = 'http://jservice.io/api/random'
    res = requests.get(url)
    json_response = json.loads(res.text)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the API and try again!')
    return json_response

# get a random clue from the API and store the question, answer, category and value
def get_random_clue():
    response = request_api_data()
    dictionary = (response[0])
    question = dictionary['question']
    answer = dictionary['answer']
    category = dictionary['category']['title']
    value = dictionary['value']
    if value == None:
        value = 100
    # return the values
    return (question, answer, category, value)

# pose the question and take the answer form input
def ask_for_answer(question, category, value):
    user_answer = input(
        f'This question is worth {value}. The category is {category} \n{question}: ')
    return user_answer

# check user answer against the answer returned from the API
def check_answer(answer, returned_answer, value):
    global score
    if answer != '' and search(answer.lower(), returned_answer.lower()):
        print(f'{returned_answer} is correct!')
        score = score + value
        print(score)
        return score

    else:
        print(f'Incorrect!. The answer is {returned_answer}')
        score = score - value
        print(score)
        return score


def main():
    # make the API call and store the returned values
    returned_question, returned_answer, returned_category, value = get_random_clue()
    # ask for answer and check answer using the returned values
    check_answer(ask_for_answer(returned_question,
                                returned_category, value), returned_answer, value)
    return 'done'


# call the main function x number of times
for i in range(10):
    main()


# if ('what' or 'who') not in answer.lower():
    #     print(f'Ooo. I\'m sorry. Your answer was not in the form of a question. The correct answer is {returned_answer}.')
    #     # score = score - value
    #     # print(score)
    #     return False
