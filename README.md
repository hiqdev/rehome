ReHome
======

**Script to deploy and maintain home easily**
The goal is to setup all environment with a single command

[![GitHub version](https://badge.fury.io/gh/hiqdev%2Frehome.svg)](https://badge.fury.io/gh/hiqdev%2Frehome)
[![Scrutinizer Code Coverage](https://img.shields.io/scrutinizer/coverage/g/hiqdev/rehome.svg)](https://scrutinizer-ci.com/g/hiqdev/rehome/)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/hiqdev/rehome.svg)](https://scrutinizer-ci.com/g/hiqdev/rehome/)

- keep your dotfiles in repository
- define home config (shell and dependencies) in `.rehome.json`
- `wget https://raw.githubusercontent.com/hiqdev/rehome/master/rehome ; python rehome init me/dotfiles`
- Congrats! You're done with setuping all your environment to a new desktop or server.

## Configuration

The main config file is `.rehome.json`

Here is example config:

```json
{
    "dotfiles": "hiqsol/dotfiles",
    "shell": "zsh",
    "installs": {
        "zsh": "system",
        "tmux": "system",
        "composer": [
            "wget https://getcomposer.org/installer -O composer-setup.php",
            "php composer-setup.php --install-dir=bin --filename=composer"
        ]
    },
    "updates": {
        "bin/composer": [
            "bin/composer self-update",
            "bin/composer global update"
        ],
        "prj/hiqdev/hidev/vendor": [
            "cd prj/hiqdev/hidev ; composer update"
        ]
    }
}
```

Looks quite clear:

1. `dotfiles` - generally accessable dotfiles repository
2. `shell`    - shell to be set with `chsh`
3. `installs` - array of path => commands to be run if path doesn't exist
4. `updates`  - array of path => commands to be run on update

## License

This project is released under the terms of the BSD-3-Clause [license](LICENSE).
Read more [here](http://choosealicense.com/licenses/bsd-3-clause).

Copyright © 2016-2017, HiQDev (http://hiqdev.com/)
