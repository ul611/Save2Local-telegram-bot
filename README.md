# Save2Local Telegram Bot

Save2Local-telegram-bot is a Telegram bot that saves files from Telegram to your local machine. This repository contains all the code you need to set up your own instance of the bot.


## Installation

To get started, follow these steps:

### Clone the repository

Clone this repository to your local machine using the following command:

```sh
git clone https://github.com/ul611/Save2Local-telegram-bot.git
```

### Create a virtual environment

It is recommended to create a virtual environment to install the dependencies for this bot. To create a virtual environment, run the following command in the root directory of the repository:

```sh
python -m venv env
```

This will create a virtual environment in a folder called _env_.

### Install the dependencies

Activate the virtual environment by running the following command:

```sh
source env/bin/activate
```

Then, install the required packages by running the following command:

```sh
pip install -r requirements.txt
```

This will install all the required dependencies for the bot.

## Creating your own Telegram bot

To create your own Telegram bot, follow these steps:

### Write to BotFather

Open the Telegram app and search for [`@BotFather`](https://telegram.me/BotFather). Start a chat with BotFather and type `/newbot`. Follow the instructions to create a new bot and receive a token.

![bot_father](https://user-images.githubusercontent.com/62026468/221434793-aa1c8aaa-c477-4317-94e9-93f8fa32576b.jpg)

### Copy the token to config.py

Copy the token that you received from BotFather and paste it into the [config.py](https://github.com/ul611/Save2Local-telegram-bot/blob/main/config.py) file in the repository.


### Run the bot

To run the bot, activate the virtual environment by running the following command:

```sh
source env/bin/activate
```

Then, run the bot using the following command:

```sh
python bot.py
```

## Send or forward files from Telegram

To save files from Telegram to your local machine using the bot, simply send or forward a file to your bot. The bot will save the file in the directory with the name of the sender. You can access the saved files in the same directory where you cloned the repository.

Good luck!
