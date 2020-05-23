from vk_api import vk_api
from datetime import datetime
from time import sleep
import random

token_dict = {
    'Victor': '883af3386ebd9f77473891bc08a2b28c2ca9a402846427a79bbed84e5dfcba96b25531898bf78fbe82db0',
}

temperature_list = [
    "Привеет, {} сегодня",
    "Привет, всё хорошо с температурой",
    "Привет, {} на градуснике",
    "Добрый день, температура {}",
    "Привет, {} температура)",
]


class User:
    def __init__(self, name, token):
        self.name = name
        self.api = vk_api.VkApi(token=token).get_api()
        self.is_sent = False
        self.next_hour = random.randint(5, 7)
        self.next_minute = random.randint(0, 60)

    def send_temperature(self):
        self.api.messages.send(
            peer_id=204254792,
            message=get_phrase(),
            random_id=random.randint(0, 9999999999)
        )
        self.is_sent = True
        self.next_hour = random.randint(5, 6)
        self.next_minute = random.randint(0, 60)

    def __str__(self):
        string = f"name: {self.name}\n" \
                 f"next_time: {self.next_hour}:{self.next_minute}\n" \
                 f"is_sent: {self.is_sent}"
        return string


users_list = [User(name, token) for name, token in token_dict.items()]


def get_phrase():
    t = 36.1 + 0.1 * float(random.randint(0, 8))
    phrase = random.choice(temperature_list)
    return phrase.format(t)


while True:
    time = datetime.now()
    print(time)
    for user in users_list:
        print(user)
        if time.hour == user.next_hour and time.minute == user.next_minute:
            try:
                user.send_temperature()
            except Exception as exception:
                print(exception)

    if time.hour == 0 and time.minute == 0:
        for user in users_list:
            user.is_sent = False
    sleep(10)
