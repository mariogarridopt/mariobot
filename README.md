![MarioBot](img/mario-banner.jpg)

# MarioBot (Discord Bot) ![latest tag)](https://img.shields.io/github/v/tag/mariogarridopt/mariobot) [![Python Unit Test](https://github.com/mariogarridopt/mariobot/actions/workflows/unittest.yml/badge.svg)](https://github.com/mariogarridopt/mariobot/actions/workflows/unittest.yml)
> MarioBot is a mutipurpose Discord Bot built with [discord.py](https://github.com/Rapptz/discord.py)

## 📑 Requirements

1. Docker
2. A Discord Bot Token [Guide](https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot)

## 🚀 Getting Started

```sh
git clone https://github.com/mariogarridopt/mariobot.git
cd mariobot
```

Set up discord token
```sh
cp .env.example .env
# edit .env file
```

Start the bot
```sh
docker compose up -d
```

Before submiting code please run the test suit:
```sh
    docker exec -it mario-bot "make test"
```

## ⚙️ Configuration

⚠️ Please keep in mind that you should never commit or publicly distribute your token or API keys.⚠️

We have the file `.env` and all the configs should be there and never pushed.
**If you dont want to activate features that use this keys, you can leave them blank.**
```sh
BOT_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXX
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
AWS_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXX
AWS_ACCESS_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXX
AWS_REGION=eu-west-3
AWS_MC_INSTANCE_ID=i-00000000000000000
AWS_MC_SERVER_IP=55.555.555.555
```

## 🗨 Features & Commands

Rolls (commands)
- [X] **`roll`**
- [X] **`valorantroll`**
- [X] **`leagueroll`**

Roles (feature)
- [X] **`add role on react to message`**
- [X] **`remove role on react to message`**

Time (feature)
- [X] **`display current time on discord`**

AI (feature)
- [X] **`chat with the bot on bot channel`**
- [X] **`Command /ai`**

AWS Commands (feature)
- [X] **`start minecraft server on request`**
- [X] **`Command /start-minecraft-server`**

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to be learn, 
inspire, and create. Any contributions you make are **greatly appreciated**.

1. [Fork the repository](https://github.com/mariogarridopt/mariobot/fork)
2. Clone your fork `git clone https://github.com/<youruser>/mariobot.git`
3. Create your feature branch `git checkout -b AmazingFeature`
4. Stage changes `git add .`
5. Commit your changes `git commit -m 'Added some AmazingFeature'`
6. Push to the branch `git push origin AmazingFeature`
7. Submit a pull request
