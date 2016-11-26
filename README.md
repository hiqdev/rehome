ReHome
======

**Script to deploy home easily**

[![GitHub version](https://badge.fury.io/gh/hiqdev%2Frehome.svg)](https://badge.fury.io/gh/hiqdev%2Frehome)
[![Scrutinizer Code Coverage](https://img.shields.io/scrutinizer/coverage/g/hiqdev/rehome.svg)](https://scrutinizer-ci.com/g/hiqdev/rehome/)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/hiqdev/rehome.svg)](https://scrutinizer-ci.com/g/hiqdev/rehome/)

- keep all your home in repository
- define config: shell and dependencies in `.rehome.json`
- `wget https://raw.githubusercontent.com/hiqdev/rehome/master/rehome ; python rehome init git://my.repo/me/home`
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

- `shell` - given shell will be set with `chsh`
- `checks` - checks that given commands run without error
- `repos` - given repos will be installed/updated to given paths
- `installs` - given scripts will be run to install paths if they don't exist
- `updates` - given scripts will be run to update paths

## License

This project is released under the terms of the BSD-3-Clause [license](LICENSE).
Read more [here](http://choosealicense.com/licenses/bsd-3-clause).

Copyright © 2016, HiQDev (http://hiqdev.com/)
