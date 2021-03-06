# -*- coding:utf-8 -*-

import logging

AptPPA = [
    "add-apt-repository ppa:zeal-developers/ppa",
    "curl https://build.opensuse.org/projects/home:manuelschneid3r/public_key | sudo apt-key add -",
    "sudo sh -c \"echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /' > /etc/apt/sources.list.d/home:manuelschneid3r.list\"",
    "apt update",  # 始终放在最后
]

APT = {
    "app": [
        "zssh",
        "sshfs",
        "tmux",
        "curl",
        "zeal",
        "git",
        "bash-completion",
        "shutter",
        "shadowsocks-libev",
        "proxychains4",
        "albert",
        "alacarte",
        "aria2",
        "chromium-browser",
        "okular",
        "smplayer",
        "silversearcher-ag",
        "emacs",
    ],
    "cxx": [
        "cppcheck",
        "clang",
        "clang-format",
        "cmake",
        "build-essential",
        "automake",
        "autoconf",
        "libtool",
        "gcc",
    ],
    "lua": ["lua", "luarocks"],
    "python": ["python3", "python3-pip"],
    "golang": ["golang"],
    "js": ["npm", "node"],
    "markdown": ["markdown"],
}

YUM = {
    "app": [],
    "cxx": [],
    "lua": [],
    "python": [],
    "golang": [],
    "js": [],
}

Brew = {
    "app": [
        "zssh",
        "tmux",
        "the_silver_searcher",
        "proxychains-ng",
        "sshfs",
        "markdown",
    ],
    "cxx": [],
    "lua": ["lua", "luarocks"],
    "python": ["python3"],
    "golang": ["golang"],
    "js": ["npm", "node"],
}

BrewCask = [
    "dash",
    "shadowsocksx-ng",
    "chromium",
    "iina",
    "emacs",
]


NPM = [
    "livedown",
    "bash-language-server",
    "lua-fmt",
]

LuaRocks = [
    "luacheck",
    "lanes",
    "checks",
    "Formatter",
    "ldoc",
    "lua-discount",
    "lunamark",
    "lua-cjson",
    "penlight",
]


Pip = ["pipenv", "ipython", "yapf", "pylint", "black"]

GO = ["GO111MODULE=on go get golang.org/x/tools/gopls@latest"]


def main():
    logging.basicConfig(level=logging.DEBUG)

    for s in AptPPA:
        logging.debug(s)

    for (k, v) in APT.items():
        if v:
            logging.debug("apt install -y {}".format(" ".join(v)))

    for (k, v) in YUM.items():
        if v:
            logging.debug("yum install -y {}".format(" ".join(v)))

    for (k, v) in Brew.items():
        if v:
            logging.debug("brew install {}".format(" ".join(v)))

    if BrewCask:
        logging.debug("brew cask install {}".format(" ".join(BrewCask)))

    if NPM:
        logging.debug(
            "npm --registry https://registry.npm.taobao.org  install -g {}".format(
                " ".join(NPM)
            )
        )

    if LuaRocks:
        logging.debug("luarocks install {}".format(" ".join(LuaRocks)))

    if Pip:
        logging.debug("pip3 install {}".format(" ".join(Pip)))

    if GO:
        logging.debug("go get {}".format(" ".join(GO)))


if __name__ == "__main__":
    main()
