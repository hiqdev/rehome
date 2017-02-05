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
    "dotfiles": "hiqsol/dotfiles",
    "shadows": {
        "prj/sol/shadow-home": "ssh://git.solex.me:222/git/sol/shadow-home"
    },
    "shell": "zsh",
    "repos": {
        ".vim/bundle/Vundle.vim": "VundleVim/Vundle.vim",
        "prj/hiqsol/quotes": "hiqsol/quotes",
        "prj/hiqdev/rehome": "hiqdev/rehome"
    },
    "installs": {
        "bin/zsh": "which zsh || echo apt-get install zsh",
        "bin/vim": "which vim || echo apt-get install vim",
        "bin/tmux": "which tmux || echo apt-get install tmux",
        "bin/composer": [
            "wget https://getcomposer.org/installer -O composer-setup.php",
            "php composer-setup.php --install-dir=bin --filename=composer",
            "rm composer-setup.php",
            "bin/composer global install"
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
2. `shadows`  - protected (shadow) repositories with files to be simlinked into home
3. `shell`    - shell to be set with `chsh`
4. `repos`    - array of path => repo to be installed/updated to given paths
5. `installs` - array of path => commands to be run if path doesn't exist
6. `updates`  - array of path => commands to be run on update

If you want run commands unconditionally just put them into `installs` or `update`
section with unexistent path.
See zsh, vim and tmux in example which check these commands availability.

## License

This project is released under the terms of the BSD-3-Clause [license](LICENSE).
Read more [here](http://choosealicense.com/licenses/bsd-3-clause).

Copyright © 2016-2017, HiQDev (http://hiqdev.com/)
