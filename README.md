ReHome
======

**Script to deploy and maintain home easily**

[![GitHub version](https://badge.fury.io/gh/hiqdev%2Frehome.svg)](https://badge.fury.io/gh/hiqdev%2Frehome)
[![Scrutinizer Code Coverage](https://img.shields.io/scrutinizer/coverage/g/hiqdev/rehome.svg)](https://scrutinizer-ci.com/g/hiqdev/rehome/)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/hiqdev/rehome.svg)](https://scrutinizer-ci.com/g/hiqdev/rehome/)

- keep your dotfiles in repository
- define config: shell and dependencies in `.rehome.json`
- `wget https://raw.githubusercontent.com/hiqdev/rehome/master/rehome ; python rehome init me/dotfiles`
- Congrats! You're done with moving your home to new server.

## Configuration

The main config file is `.rehome.json`

Here is example config:

```json
{
    "shell": "zsh",
    "checks": {
        "which zsh": "apt-get install zsh",
        "which vim": "apt-get install vim",
        "which tmux": "apt-get install tmux"
    },
    "repos": {
        ".vim/bundle/Vundle.vim": "VundleVim/Vundle.vim",
        "src/quotes": "git@github.com:hiqsol/quotes"
    },
    "installs": {
        "bin/composer": [
            "wget https://getcomposer.org/installer -O composer-setup.php",
            "php composer-setup.php --install-dir=bin --filename=composer",
            "rm composer-setup.php"
        ]
    },
    "updates": {
        "bin/composer": [
            "bin/composer self-update"
        ],
        "prj/hiqdev/hidev/vendor": [
            "cd prj/hiqdev/hidev/vendor ; composer update"
        ]
    }
}
```

Looks quite clear:

1. `dotfiles` - dotfiles repository
2. `shadows`  - repositories with files to be simlinked into home
3. `shell`    - shell to be set with `chsh`
4. `repos`    - repositories to be installed/updated to given paths
5. `commands` - commands to be run unconditionally
6. `installs` - scripts to be run if path doesn't exist
7. `updates`  - scripts to be run on update

## License

This project is released under the terms of the BSD-3-Clause [license](LICENSE).
Read more [here](http://choosealicense.com/licenses/bsd-3-clause).

Copyright © 2016-2017, HiQDev (http://hiqdev.com/)
